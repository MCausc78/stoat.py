from __future__ import annotations

import typing
import typing_extensions

from .oauth2 import OAuth2ScopeReasoning, OAuth2Scope
from .users import User


class Bot(typing.TypedDict):
    _id: str
    owner: str
    token: str
    public: bool
    analytics: typing_extensions.NotRequired[bool]
    discoverable: typing_extensions.NotRequired[bool]
    interactions_url: typing_extensions.NotRequired[str]
    terms_of_service_url: typing_extensions.NotRequired[str]
    privacy_policy_url: typing_extensions.NotRequired[str]
    oauth2: typing_extensions.NotRequired[BotOauth2]
    flags: typing_extensions.NotRequired[int]


FieldsBot = typing.Literal['Token', 'InteractionsURL', 'Oauth2', 'Oauth2Secret']


class PublicBot(typing.TypedDict):
    _id: str
    username: str
    avatar: typing_extensions.NotRequired[str]
    description: typing_extensions.NotRequired[str]


class FetchBotResponse(typing.TypedDict):
    bot: Bot
    user: User


class DataCreateBot(typing.TypedDict):
    name: str


class DataEditBot(typing.TypedDict):
    name: typing_extensions.NotRequired[str]
    public: typing_extensions.NotRequired[bool]
    analytics: typing_extensions.NotRequired[bool]
    interactions_url: typing_extensions.NotRequired[str]
    oauth2: typing_extensions.NotRequired[DataEditBotOauth2]
    remove: typing_extensions.NotRequired[list[FieldsBot]]


class DataEditBotOauth2(typing.TypedDict):
    # All of them don't have skip_serializing_if on backend and are marked as Option<T> :(
    public: typing_extensions.NotRequired[typing.Optional[bool]]
    redirects: typing_extensions.NotRequired[typing.Optional[list[str]]]  # 1-10 items
    allowed_scopes: typing_extensions.NotRequired[typing.Optional[dict[OAuth2Scope, OAuth2ScopeReasoning]]]


class ServerInviteBotDestination(typing.TypedDict):
    server: str


class GroupInviteBotDestination(typing.TypedDict):
    group: str


InviteBotDestination = typing.Union[ServerInviteBotDestination, GroupInviteBotDestination]


class OwnedBotsResponse(typing.TypedDict):
    bots: list[Bot]
    users: list[User]


class BotWithUserResponse(Bot):
    user: User


class BotOauth2(typing.TypedDict):
    public: bool
    secret: typing.Optional[str]
    redirects: list[str]
    allowed_scopes: dict[OAuth2Scope, OAuth2ScopeReasoning]
