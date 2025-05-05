from __future__ import annotations

import asyncio

import pyvolt


async def main() -> None:
    channel_id = '01F92C5ZXBQWQ8KY7J8KY917NM'
    token = 'token'

    state = pyvolt.State()
    async with pyvolt.HTTPClient(token=token, state=state).attach() as http:
        # Sending a message in Revolt > Lounge
        message = await http.send_message(channel_id, 'Hello world')
        print('Message was sent in Revolt > Lounge, with ID', message.id)

        # Editing a message
        await message.edit(content='Hello, world!')
        print('Message was successfully edited')

        # Deleting it afterwards (you can do "await http.delete_message(channel_id, message.id)" instead if you do not have a BaseMessage object)
        await message.delete()
        print('And message was successfully deleted')

        my_id = message.author_id

        channel = await http.get_channel(channel_id)

        if isinstance(channel, pyvolt.BaseServerChannel):
            print(
                f'{channel.type.name.capitalize()} channel {channel.id} named "{channel.name}" is in server with ID {channel.server_id}'
            )
        elif isinstance(channel, pyvolt.SavedMessagesChannel):
            print('This channel is your personal "Saved Notes" channel')
        elif isinstance(channel, pyvolt.DMChannel):
            recipient_id = [user_id for user_id in channel.recipient_ids if user_id != my_id][0]
            recipient = await http.get_user(recipient_id)
            print(f'This channel is your private channel with {recipient.tag}')
        elif isinstance(channel, pyvolt.GroupChannel):
            print(f'Group "{channel.name}" has {len(channel.recipient_ids)}')


asyncio.run(main())
