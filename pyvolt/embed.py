"""
The MIT License (MIT)

Copyright (c) 2024-present MCausc78

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
import typing

from attrs import define, field

if typing.TYPE_CHECKING:
    from . import raw
    from .cdn import StatelessAsset, Asset
    from .enums import LightspeedContentType, TwitchContentType, BandcampContentType, ImageSize
    from .state import State


class BaseEmbed(ABC):
    """Base class for message embeds."""

    __slots__ = ()

    @abstractmethod
    def attach_state(self, state: State, /) -> Embed:
        """:class:`Embed`: Attach a state to embed.

        Parameters
        ----------
        state: :class:`State`
            The state to attach.
        """
        ...


@define(slots=True)
class BaseEmbedSpecial:
    """Information about special remote content."""


@define(slots=True)
class NoneEmbedSpecial(BaseEmbedSpecial):
    """No remote content.

    This inherits from :class:`BaseEmbedSpecial`.
    """

    def to_dict(self) -> raw.NoneSpecial:
        """:class:`dict`: Convert embed special to raw data."""
        return {
            'type': 'None',
        }


_NONE_EMBED_SPECIAL = NoneEmbedSpecial()


@define(slots=True)
class GIFEmbedSpecial(BaseEmbedSpecial):
    """A content hint that embed contains a GIF. Metadata should be used to find video or image to play.

    This inherits from :class:`BaseEmbedSpecial`.
    """

    def to_dict(self) -> raw.GIFSpecial:
        """:class:`dict`: Convert embed special to raw data."""
        return {
            'type': 'GIF',
        }


_GIF_EMBED_SPECIAL = GIFEmbedSpecial()


@define(slots=True)
class YouTubeEmbedSpecial(BaseEmbedSpecial):
    """Represents information about Youtube video.

    This inherits from :class:`BaseEmbedSpecial`.
    """

    id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The video ID."""

    timestamp: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The video timestamp."""

    def to_dict(self) -> raw.YouTubeSpecial:
        """:class:`dict`: Convert embed special to raw data."""
        payload: raw.YouTubeSpecial = {
            'type': 'YouTube',
            'id': self.id,
        }
        if self.timestamp is not None:
            payload['timestamp'] = self.timestamp
        return payload


@define(slots=True)
class LightspeedEmbedSpecial(BaseEmbedSpecial):
    """Represents information about Lightspeed.tv stream.

    This inherits from :class:`BaseEmbedSpecial`.
    """

    content_type: LightspeedContentType = field(repr=True, kw_only=True, eq=True)
    """:class:`LightspeedContentType`: The Lightspeed.tv content type."""

    id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The Lightspeed.tv stream ID."""

    def to_dict(self) -> raw.LightspeedSpecial:
        """:class:`dict`: Convert embed special to raw data."""
        return {
            'type': 'Lightspeed',
            'content_type': self.content_type.value,
            'id': self.id,
        }


@define(slots=True)
class TwitchEmbedSpecial(BaseEmbedSpecial):
    """Represents information about Twitch stream or clip.

    This inherits from :class:`BaseEmbedSpecial`.
    """

    content_type: TwitchContentType = field(repr=True, kw_only=True, eq=True)
    """:class:`TwitchContentType`: The Twitch content type."""

    id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The Twitch content ID."""

    def to_dict(self) -> raw.TwitchSpecial:
        """:class:`dict`: Convert embed special to raw data."""
        return {
            'type': 'Twitch',
            'content_type': self.content_type.value,
            'id': self.id,
        }


@define(slots=True)
class SpotifyEmbedSpecial(BaseEmbedSpecial):
    """Represents information about Spotify track.

    This inherits from :class:`BaseEmbedSpecial`.
    """

    content_type: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The Spotify content type."""

    id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The Spotify content ID."""

    def to_dict(self) -> raw.SpotifySpecial:
        """:class:`dict`: Convert embed special to raw data."""
        return {
            'type': 'Spotify',
            'content_type': self.content_type,
            'id': self.id,
        }


@define(slots=True)
class SoundcloudEmbedSpecial(BaseEmbedSpecial):
    """Represents information about Soundcloud track.

    This inherits from :class:`BaseEmbedSpecial`.
    """

    def to_dict(self) -> raw.SoundcloudSpecial:
        """:class:`dict`: Convert embed special to raw data."""
        return {
            'type': 'Soundcloud',
        }


_SOUNDCLOUD_EMBED_SPECIAL = SoundcloudEmbedSpecial()


@define(slots=True)
class BandcampEmbedSpecial(BaseEmbedSpecial):
    """Represents information about Bandcamp track.

    This inherits from :class:`BaseEmbedSpecial`.
    """

    content_type: BandcampContentType = field(repr=True, kw_only=True, eq=True)
    """:class:`BandcampContentType`: The Bandcamp content type."""

    id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The Bandcamp content ID."""

    def to_dict(self) -> raw.BandcampSpecial:
        """:class:`dict`: Convert embed special to raw data."""
        return {
            'type': 'Bandcamp',
            'content_type': self.content_type.value,
            'id': self.id,
        }


@define(slots=True)
class AppleMusicEmbedSpecial(BaseEmbedSpecial):
    """Represents information about Apple Music track.

    This inherits from :class:`BaseEmbedSpecial`.
    """

    album_id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The Apple Music album ID."""

    track_id: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The Apple Music track ID."""

    def to_dict(self) -> raw.AppleMusicSpecial:
        """:class:`dict`: Convert embed special to raw data."""
        payload: raw.AppleMusicSpecial = {
            'type': 'AppleMusic',
            'album_id': self.album_id,
        }
        if self.track_id is not None:
            payload['track_id'] = self.track_id
        return payload


@define(slots=True)
class StreamableEmbedSpecial(BaseEmbedSpecial):
    """Represents information about Streamable video.

    This inherits from :class:`BaseEmbedSpecial`.
    """

    id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The video ID."""

    def to_dict(self) -> raw.StreamableSpecial:
        """:class:`dict`: Convert embed special to raw data."""
        return {
            'type': 'Streamable',
            'id': self.id,
        }


@define(slots=True)
class ImageEmbed(BaseEmbed):
    """Represents an image in an embed.

    This inherits from :class:`BaseEmbed`.
    """

    url: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The URL to the original image."""

    width: int = field(repr=True, kw_only=True, eq=True)
    """:class:`int`: The width of the image."""

    height: int = field(repr=True, kw_only=True, eq=True)
    """:class:`int`: The height of the image."""

    size: ImageSize = field(repr=True, kw_only=True, eq=True)
    """:class:`ImageSize`: The positioning and size of the image."""

    def attach_state(self, state: State, /) -> Embed:
        return self

    @typing.overload
    def to_dict(self, *, as_embed: typing.Literal[False]) -> raw.Image: ...

    @typing.overload
    def to_dict(self, *, as_embed: typing.Literal[True] = ...) -> raw.ImageEmbed: ...

    def to_dict(self, *, as_embed: bool = True) -> typing.Union[raw.Image, raw.ImageEmbed]:
        """:class:`dict`: Convert embed to raw data.

        Parameters
        ----------
        as_embed: :class:`bool`
            Whether to serialize image as embed. If set to ``False``, this means removal of ``type`` key in root object. Defaults to ``True``.
        """
        if as_embed:
            return {
                'type': 'Image',
                'url': self.url,
                'width': self.width,
                'height': self.height,
                'size': self.size.value,
            }
        return {
            'url': self.url,
            'width': self.width,
            'height': self.height,
            'size': self.size.value,
        }


@define(slots=True)
class VideoEmbed(BaseEmbed):
    """Represents a video in an embed.

    This inherits from :class:`BaseEmbed`.
    """

    url: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The URL to the original video."""

    width: int = field(repr=True, kw_only=True, eq=True)
    """:class:`int`: The width of the video."""

    height: int = field(repr=True, kw_only=True, eq=True)
    """:class:`int`: The height of the video."""

    def attach_state(self, state: State, /) -> Embed:
        return self

    @typing.overload
    def to_dict(self, *, as_embed: typing.Literal[False]) -> raw.Video: ...

    @typing.overload
    def to_dict(self, *, as_embed: typing.Literal[True] = ...) -> raw.VideoEmbed: ...

    def to_dict(self, *, as_embed: bool = True) -> typing.Union[raw.Video, raw.VideoEmbed]:
        """:class:`dict`: Convert embed to raw data.

        Parameters
        ----------
        as_embed: :class:`bool`
            Whether to serialize video as embed. If set to ``False``, this means removal of ``type`` key in root object. Defaults to ``True``.
        """
        if as_embed:
            return {
                'type': 'Video',
                'url': self.url,
                'width': self.width,
                'height': self.height,
            }
        return {
            'url': self.url,
            'width': self.width,
            'height': self.height,
        }


@define(slots=True)
class WebsiteEmbed(BaseEmbed):
    """Represents website embed within Revolt message.

    This inherits from :class:`BaseEmbed`.
    """

    url: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The direct URL to web page."""

    original_url: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The original direct URL."""

    special: typing.Optional[EmbedSpecial] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`EmbedSpecial`]: The remote content."""

    title: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The title of website."""

    description: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The description of website."""

    image: typing.Optional[ImageEmbed] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`ImageEmbed`]: The embedded image."""

    video: typing.Optional[VideoEmbed] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`VideoEmbed`]: The embedded video."""

    site_name: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The site name."""

    icon_url: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The URL to site icon."""

    color: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The embed's CSS color."""

    def attach_state(self, state: State, /) -> Embed:
        return self

    @typing.overload
    def to_dict(self, *, as_embed: typing.Literal[False]) -> raw.WebsiteMetadata: ...

    @typing.overload
    def to_dict(self, *, as_embed: typing.Literal[True] = ...) -> raw.WebsiteEmbed: ...

    def to_dict(self, *, as_embed: bool = True) -> typing.Union[raw.WebsiteMetadata, raw.WebsiteEmbed]:
        """:class:`dict`: Convert embed to raw data.

        Parameters
        ----------
        as_embed: :class:`bool`
            Whether to serialize website metadata as embed. If set to ``False``, this means removal of ``type`` key in root object. Defaults to ``True``.
        """
        if as_embed:
            payload: raw.WebsiteEmbed = {
                'type': 'Website',
            }
            if self.url is not None:
                payload['url'] = self.url
            if self.original_url is not None:
                payload['original_url'] = self.original_url
            if self.special is not None:
                payload['special'] = self.special.to_dict()
            if self.title is not None:
                payload['title'] = self.title
            if self.description is not None:
                payload['description'] = self.description
            if self.image is not None:
                payload['image'] = self.image.to_dict(as_embed=False)
            if self.video is not None:
                payload['video'] = self.video.to_dict(as_embed=False)
            if self.icon_url is not None:
                payload['icon_url'] = self.icon_url
            if self.color is not None:
                payload['colour'] = self.color
            return payload
        metadata: raw.WebsiteMetadata = {}
        if self.url is not None:
            metadata['url'] = self.url
        if self.original_url is not None:
            metadata['original_url'] = self.original_url
        if self.special is not None:
            metadata['special'] = self.special.to_dict()
        if self.title is not None:
            metadata['title'] = self.title
        if self.description is not None:
            metadata['description'] = self.description
        if self.image is not None:
            metadata['image'] = self.image.to_dict(as_embed=False)
        if self.video is not None:
            metadata['video'] = self.video.to_dict(as_embed=False)
        if self.icon_url is not None:
            metadata['icon_url'] = self.icon_url
        if self.color is not None:
            metadata['colour'] = self.color
        return metadata


@define(slots=True)
class StatelessTextEmbed(BaseEmbed):
    """Represents stateless text embed within Revolt message.

    This inherits from :class:`BaseEmbed`.
    """

    icon_url: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The URL to site icon."""

    url: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The direct URL to web page."""

    title: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The embed's title."""

    description: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The embed's description."""

    internal_media: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`StatelessAsset`]: The stateless embed media."""

    color: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The embed's CSS color."""

    def attach_state(self, state: State, /) -> Embed:
        return TextEmbed(
            icon_url=self.icon_url,
            url=self.url,
            title=self.title,
            description=self.description,
            internal_media=self.internal_media,
            color=self.color,
            state=state,
        )

    @typing.overload
    def to_dict(self, *, as_embed: typing.Literal[False]) -> raw.Text: ...

    @typing.overload
    def to_dict(self, *, as_embed: typing.Literal[True] = ...) -> raw.TextEmbed: ...

    def to_dict(self, *, as_embed: bool = True) -> typing.Union[raw.Text, raw.TextEmbed]:
        """:class:`dict`: Convert embed to raw data.

        Parameters
        ----------
        as_embed: :class:`bool`
            Whether to serialize text metadata as embed. If set to ``False``, this means removal of ``type`` key in root object. Defaults to ``True``.
        """
        if as_embed:
            payload: raw.TextEmbed = {
                'type': 'Text',
            }
            if self.icon_url is not None:
                payload['icon_url'] = self.icon_url
            if self.url is not None:
                payload['url'] = self.url
            if self.title is not None:
                payload['title'] = self.title
            if self.description is not None:
                payload['description'] = self.description
            if self.internal_media is not None:
                payload['media'] = self.internal_media.to_dict('attachments')
            if self.color is not None:
                payload['colour'] = self.color
            return payload
        else:
            metadata: raw.Text = {}
            if self.icon_url is not None:
                metadata['icon_url'] = self.icon_url
            if self.url is not None:
                metadata['url'] = self.url
            if self.title is not None:
                metadata['title'] = self.title
            if self.description is not None:
                metadata['description'] = self.description
            if self.internal_media is not None:
                metadata['media'] = self.internal_media.to_dict('attachments')
            if self.color is not None:
                metadata['colour'] = self.color
            return metadata


@define(slots=True)
class TextEmbed(StatelessTextEmbed):
    """Represents a text embed within Revolt message.

    This is a stateful version of :class:`StatelessTextEmbed`, and inherits from it.
    """

    state: State = field(repr=False, hash=False, kw_only=True, eq=False)

    @property
    def media(self) -> typing.Optional[Asset]:
        """Optional[:class:`Asset`]: The embed media."""
        return self.internal_media.attach_state(self.state, 'attachments') if self.internal_media else None


class NoneEmbed(BaseEmbed):
    """Embed that holds nothing.

    This inherits from :class:`BaseEmbed`.
    """

    def attach_state(self, state: State, /) -> Embed:
        return self

    def to_dict(
        self,
    ) -> raw.NoneEmbed:
        """:class:`dict`: Convert embed to raw data."""
        return {
            'type': 'None',
        }


_NONE_EMBED: typing.Final[NoneEmbed] = NoneEmbed()

EmbedSpecial = typing.Union[
    NoneEmbedSpecial,
    GIFEmbedSpecial,
    YouTubeEmbedSpecial,
    LightspeedEmbedSpecial,
    TwitchEmbedSpecial,
    SpotifyEmbedSpecial,
    SoundcloudEmbedSpecial,
    BandcampEmbedSpecial,
    AppleMusicEmbedSpecial,
    StreamableEmbedSpecial,
]
StatelessEmbed = typing.Union[WebsiteEmbed, ImageEmbed, VideoEmbed, StatelessTextEmbed, NoneEmbed]
Embed = typing.Union[WebsiteEmbed, ImageEmbed, VideoEmbed, TextEmbed, NoneEmbed]

__all__ = (
    'BaseEmbed',
    'BaseEmbedSpecial',
    'NoneEmbedSpecial',
    '_NONE_EMBED_SPECIAL',
    'GIFEmbedSpecial',
    '_GIF_EMBED_SPECIAL',
    'YouTubeEmbedSpecial',
    'LightspeedEmbedSpecial',
    'TwitchEmbedSpecial',
    'SpotifyEmbedSpecial',
    'SoundcloudEmbedSpecial',
    '_SOUNDCLOUD_EMBED_SPECIAL',
    'BandcampEmbedSpecial',
    'AppleMusicEmbedSpecial',
    'StreamableEmbedSpecial',
    'ImageEmbed',
    'VideoEmbed',
    'WebsiteEmbed',
    'StatelessTextEmbed',
    'TextEmbed',
    'NoneEmbed',
    '_NONE_EMBED',
    'EmbedSpecial',
    'StatelessEmbed',
    'Embed',
)
