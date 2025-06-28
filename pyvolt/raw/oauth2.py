from __future__ import annotations

import typing
import typing_extensions

from .bots import PublicBot
from .users import User


class OAuth2AuthorizeAuthResponse(typing.TypedDict):
    redirect_uri: str


class OAuth2ScopeReasoning(typing.TypedDict):
    allow: str
    deny: str


class OAuth2AuthorizeInfoResponse(typing.TypedDict):
    bot: PublicBot
    user: User
    allowed_scopes: dict[OAuth2Scope, OAuth2ScopeReasoning]


OAuth2ResponseType = typing.Literal[
    'code',
    'token',
]
OAuth2GrantType = typing.Literal[
    'authorization_code',
    'implicit',
]
OAuth2CodeChallengeMethod = typing.Literal[
    'plain',
    'S256',
]


class OAuth2AuthorizationForm(typing.TypedDict):
    client_id: str
    scope: str
    redirect_uri: str
    response_type: OAuth2ResponseType
    state: typing_extensions.NotRequired[str]
    code_challenge: typing_extensions.NotRequired[str]
    code_challenge_method: typing_extensions.NotRequired[OAuth2CodeChallengeMethod]


class OAuth2TokenExchangeForm(typing.TypedDict):
    grant_type: OAuth2GrantType
    client_id: str
    client_secret: typing_extensions.NotRequired[str]
    code: str
    code_verifier: typing_extensions.NotRequired[str]


class OAuth2TokenExchangeResponse(typing.TypedDict):
    access_token: str
    token_type: str
    scope: str


OAuth2Scope = typing.Literal[
    'identify',
    'full',
]
