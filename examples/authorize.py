from __future__ import annotations

from base64 import urlsafe_b64encode
from hashlib import sha256
from os import urandom

import stoat
import yarl

client = stoat.Client(token='token', bot=False)

client_id = '01JNEQ9R0YZAQKT8JJTKMCJ8H3'
redirect_uri = 'http://127.0.0.1:5000/oauth2/complete'


@client.on(stoat.ReadyEvent)
async def on_ready(event: stoat.ReadyEvent) -> None:
    event.process()
    event.cancel()

    await authorize_non_public_client()
    await authorize_public_client()


async def authorize_non_public_client() -> None:
    raw_url = await client.http.authorize(
        client_id,
        scopes=[stoat.OAuth2Scope.identify],
        redirect_uri=redirect_uri,
        response_type=stoat.OAuth2ResponseType.token,
    )
    url = yarl.URL(raw_url)
    token = url.query['code']

    print(f'Authorized bot (ID: {client_id}, non public client) and received a token: {token}')
    await client.http.get_me(http_overrides=stoat.HTTPOverrideOptions(bot=False, oauth2=True, token=token))


async def authorize_public_client() -> None:
    code_verifier = urlsafe_b64encode(urandom(32)).rstrip(b'=').decode('utf-8')
    code_challenge = urlsafe_b64encode(sha256(code_verifier.encode('utf-8')).digest()).decode('utf-8').rstrip('=')

    raw_url = await client.http.authorize(
        client_id,
        scopes=[stoat.OAuth2Scope.identify],
        redirect_uri=redirect_uri,
        response_type=stoat.OAuth2ResponseType.code,
        code_challenge=code_challenge,
        code_challenge_method=stoat.OAuth2CodeChallengeMethod.s256,
    )
    url = yarl.URL(raw_url)
    code = url.query['code']
    result = await client.http.exchange_token(
        code=code,
        client=client_id,
        grant_type=stoat.OAuth2GrantType.authorization_code,
        code_verifier=code_verifier,
    )
    token = result.access_token

    print(f'Authorized bot (ID: {client_id}, public client) and received a token: {token}')
    await client.http.get_me(http_overrides=stoat.HTTPOverrideOptions(bot=False, oauth2=True, token=token))


client.run()
