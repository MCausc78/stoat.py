from __future__ import annotations

import json

import pyotp
import stoat

bot = stoat.Client()

token = 'token'
password = 'password'


@bot.on(stoat.MessageCreateEvent)
async def on_message(event: stoat.MessageCreateEvent) -> None:
    message = event.message

    if message.author.relationship is not stoat.RelationshipStatus.user:
        return

    if message.content == 'disable mfa':
        ticket = await bot.http.create_password_ticket(password)
        await bot.http.disable_totp_mfa(mfa_ticket=ticket.token)
        await message.reply('Turned off MFA.')
    elif message.content == 'enable mfa':
        await message.reply('Enabling on MFA.')
        ticket = await bot.http.create_password_ticket(password)

        codes = await bot.http.generate_recovery_codes(mfa_ticket=ticket.token)

        with open('./local_codes.json', 'w') as fp:
            json.dump(codes, fp, indent=4)

        ticket = await bot.http.create_password_ticket(password)

        secret = await bot.http.generate_totp_secret(mfa_ticket=ticket.token)
        totp = pyotp.TOTP(secret)
        await message.reply(f'MFA secret: {secret}')
        code = totp.now()
        await bot.http.enable_totp_mfa(stoat.ByTOTP(code))
        await message.reply('Turned on MFA.')


# This is also possible
bot.run(token, bot=False)
