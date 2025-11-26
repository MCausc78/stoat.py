from __future__ import annotations

import typing

import stoat

client = stoat.Client(token='token', bot=False)


def sort_private_channel(channel: typing.Union[stoat.DMChannel, stoat.GroupChannel]) -> str:
    return channel.last_message_id or '0'


@client.on(stoat.ReadyEvent)
async def on_ready(event: stoat.ReadyEvent) -> None:
    event.process()
    event.cancel()

    for channel in client.ordered_private_channels:
        if isinstance(channel, stoat.DMChannel):
            target = channel.recipient or await client.fetch_user(channel.recipient_id)
            if channel.active:
                print('DM with', target.display_name or target.name)
            else:
                print('Inactive DM with', target.display_name or target.name)
        elif isinstance(channel, stoat.GroupChannel):
            print('Group', channel.name, 'with', len(channel.recipient_ids), 'recipients')


client.run()
