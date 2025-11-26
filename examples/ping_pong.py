from __future__ import annotations

import stoat


# Whether the example should be ran as a user account or not
self_bot = False

client = stoat.Client(token='token', bot=not self_bot)


@client.on(stoat.ReadyEvent)
async def on_ready(_, /) -> None:
    print('Logged on as', client.me)


@client.on(stoat.MessageCreateEvent)
async def on_message(event: stoat.MessageCreateEvent) -> None:
    message = event.message

    # Don't respond to ourselves/others
    if (message.author.relationship is stoat.RelationshipStatus.user) ^ self_bot:
        return

    if message.content == 'ping':
        await message.channel.send('pong')


client.run()
