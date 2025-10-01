from __future__ import annotations

import typing

from .bots import PublicBot

class AuthorizedBotId(typing.TypedDict):
    user: str
    bot: str


class AuthorizedBot(typing.TypedDict):
    _id: AuthorizedBotId
    created_at: str
    deauthorized_at: typing.Optional[str]
    scope: str

class AuthorizedBotsResponse(typing.TypedDict):
    public_bot: PublicBot
    authorized_bot: AuthorizedBot