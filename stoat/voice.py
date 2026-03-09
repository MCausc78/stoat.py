from __future__ import annotations

import asyncio
import logging
import subprocess
import typing
from abc import ABC, abstractmethod

import livekit.rtc as rtc

if typing.TYPE_CHECKING:
    from livekit.rtc import Room

logger = logging.getLogger(__name__)

DEFAULT_SAMPLE_RATE = 48000
DEFAULT_NUM_CHANNELS = 1


class AudioSourceBase(ABC):
    @abstractmethod
    async def create_track(self) -> rtc.LocalAudioTrack:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass


AudioSource = AudioSourceBase


class FFmpegAudio(AudioSourceBase):
    def __init__(
        self,
        source: str,
        sample_rate: int = DEFAULT_SAMPLE_RATE,
        num_channels: int = DEFAULT_NUM_CHANNELS,
    ) -> None:
        self._source = source
        self._sample_rate = sample_rate
        self._num_channels = num_channels
        self._audio_source: typing.Optional[rtc.AudioSource] = None
        self._track: typing.Optional[rtc.LocalAudioTrack] = None
        self._process: typing.Optional[subprocess.Popen] = None
        self._task: typing.Optional[asyncio.Task] = None
        self._closed = False
        self._started = False

    async def create_track(self) -> rtc.LocalAudioTrack:
        self._audio_source = rtc.AudioSource(self._sample_rate, self._num_channels)
        self._track = rtc.LocalAudioTrack.create_audio_track(f'audio-{id(self)}', self._audio_source)
        return self._track

    async def start(self) -> None:
        if self._closed:
            raise RuntimeError('FFmpegAudio already closed')

        if self._started:
            return
        self._started = True

        ffmpeg_cmd = [
            'ffmpeg',
            '-i',
            self._source,
            '-ac',
            str(self._num_channels),
            '-ar',
            str(self._sample_rate),
            '-f',
            's16le',
            '-',
        ]

        logger.info(f'Starting FFmpeg: {" ".join(ffmpeg_cmd)}')

        self._process = subprocess.Popen(
            ffmpeg_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        self._task = asyncio.create_task(self._read_loop())

    async def _read_loop(self) -> None:
        if self._process is None or self._audio_source is None:
            return

        bytes_per_sample = 2 * self._num_channels
        frame_size = self._sample_rate // 100 * bytes_per_sample
        logger.info(f'FFmpeg read loop started, frame_size={frame_size}')

        try:
            while True:
                if self._closed:
                    break

                data = self._process.stdout.read(frame_size)
                if not data:
                    logger.info('FFmpeg output ended')
                    break

                if len(data) != frame_size:
                    logger.warning(f'FFmpeg read incomplete: {len(data)}/{frame_size}')
                    continue

                frame = rtc.AudioFrame(
                    data=data,
                    sample_rate=self._sample_rate,
                    num_channels=self._num_channels,
                    samples_per_channel=self._sample_rate // 100,
                )
                logger.info(f'Pushing frame to audio_source: {type(self._audio_source)}')
                await self._audio_source.capture_frame(frame)
        except Exception as e:
            logger.error(f'Error reading from FFmpeg: {e}')
        finally:
            await self.stop()

    async def stop(self) -> None:
        if self._process:
            self._process.terminate()
            try:
                self._process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self._process.kill()
                self._process.wait()
            stderr = self._process.stderr.read() if self._process.stderr else ''
            if stderr:
                logger.warning(f'FFmpeg stderr: {stderr.decode()[:500]}')
            self._process = None

    async def close(self) -> None:
        self._closed = True
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None
        await self.stop()
        self._audio_source = None
        self._track = None


class VoiceClient:
    def __init__(self, room: Room) -> None:
        self._room = room
        self._audio_sources: dict[str, FFmpegAudio] = {}
        self._published_tracks: set[str] = set()

        @room.on('track_published')
        def on_track_published(publication, participant):
            logger.info(f'Track published: {publication.sid}, is local: {participant.is_local()}')
            if participant.is_local():
                self._published_tracks.add(publication.sid)

        @room.on('track_subscription_failed')
        def on_track_sub_failed(track_sid, participant, error):
            logger.error(f'Track subscription failed: track_sid={track_sid}, participant={participant}, error={error}')

        @room.on('connection_state_changed')
        def on_connection_state_changed(state):
            logger.info(f'Connection state changed: {state}')

    @property
    def room(self) -> Room:
        return self._room

    async def play(self, source: str, name: str = 'audio') -> FFmpegAudio:
        if name in self._audio_sources:
            await self._audio_sources[name].close()

        audio = FFmpegAudio(source)
        track = await audio.create_track()

        logger.info(f'Publishing track: {track.sid}')

        # Wait for publication with timeout - try specifying source as microphone
        try:
            opts = rtc.TrackPublishOptions(source=rtc.TrackSource.SOURCE_MICROPHONE)
            publication = await asyncio.wait_for(self._room.local_participant.publish_track(track, opts), timeout=30.0)
            logger.info(f'Track published successfully: {publication.sid}')

            # Now start FFmpeg to push audio frames
            await audio.start()

        except Exception as e:
            logger.error(f'Failed to publish track: {e}, type: {type(e)}')
            import traceback

            traceback.print_exc()
            await audio.close()
            raise

        self._audio_sources[name] = audio
        return audio

    async def stop(self, name: str = 'audio') -> None:
        if name in self._audio_sources:
            audio = self._audio_sources.pop(name)
            track = audio._track

            if track:
                try:
                    await self._room.local_participant.unpublish_track(track)
                except Exception as e:
                    logger.warning(f'Error unpublishing track: {e}')

            await audio.close()

    async def stop_all(self) -> None:
        names = list(self._audio_sources.keys())
        for name in names:
            await self.stop(name)

    async def disconnect(self) -> None:
        await self.stop_all()
        await self._room.disconnect()
