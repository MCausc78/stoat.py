import asyncio
import base64
import stoat


async def main():
    voice_channel_id = '01...P1'

    print('Creating client...', flush=True)
    client = stoat.Client(
        token='vA...VS',
        bot=True,
        http_base='https://api.exampledomain.xyz',
        websocket_base='wss://events.exampledomain.xyz',
    )

    ready = asyncio.Event()

    @client.on(stoat.ReadyEvent)
    async def on_ready(event: stoat.ReadyEvent):
        print(f'Connected as {client.me}', flush=True)
        ready.set()

    print('Starting client...', flush=True)

    async def start_client():
        await client.start()

    start_task = asyncio.create_task(start_client())

    try:
        await asyncio.wait_for(ready.wait(), timeout=10)
        print('Client is ready!', flush=True)
    except asyncio.TimeoutError:
        print('Timeout waiting for ready event', flush=True)
        start_task.cancel()
        await client.close()
        return

    await asyncio.sleep(1)

    # Query instance to get voice nodes
    print('Querying instance for voice nodes...', flush=True)
    instance = await client.http.query_node()

    if instance.features.voice.is_livekit():
        nodes = instance.features.voice.nodes
        print(f'Using node: {nodes[0].name}', flush=True)
        node_name = nodes[0].name
    else:
        print('Instance uses Voso, not LiveKit', flush=True)
        await client.close()
        return

    # Get channel
    print('Fetching channel...', flush=True)
    channel = await client.http.get_channel(voice_channel_id)
    print(f'Channel: {channel.name}', flush=True)

    # First just call join_call to see what token we get
    print('Getting join call token...', flush=True)
    token, url = await client.http.join_call(channel, node=node_name)
    print(f'Token: {token[:100]}...', flush=True)
    print(f'URL: {url}', flush=True)

    # Decode the token to see what's in it
    parts = token.split('.')
    if len(parts) >= 2:
        payload = parts[1]
        # Add padding if needed
        payload += '=' * (4 - len(payload) % 4)
        decoded = base64.b64decode(payload)
        print(f'Token payload: {decoded}', flush=True)

    try:
        voice_client = await channel.connect(node=node_name)
        print(f'VoiceClient: {voice_client}', flush=True)
        print(f'Room: {voice_client.room}', flush=True)
        print(f'Connection state: {voice_client.room.connection_state}', flush=True)

        sample_audio = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
        print(f'Playing: {sample_audio}', flush=True)

        try:
            audio = await voice_client.play(sample_audio, 'test')
            print(f'Audio playing!', flush=True)
            await asyncio.sleep(5)
            print('Stopping...', flush=True)
            await voice_client.stop('test')
        except Exception as e:
            print(f'Play error: {e}', flush=True)
            import traceback

            traceback.print_exc()

        print('Disconnecting...', flush=True)
        await voice_client.disconnect()
        print('Disconnected!', flush=True)

    except Exception as e:
        print(f'Error during connect: {e}', flush=True)
        import traceback

        traceback.print_exc()

    print('Closing client...', flush=True)
    await client.close()
    print('Done!', flush=True)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Interrupted', flush=True)
    except Exception as e:
        print(f'Error: {e}', flush=True)
        import traceback

        traceback.print_exc()
