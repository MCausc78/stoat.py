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

import typing

from attrs import define, field

if typing.TYPE_CHECKING:
    from datetime import datetime

    from . import raw
    from .bot import PublicBot
    from .http import HTTPOverrideOptions
    from .state import State
    from .user import User


class OAuth2ScopeReasoning:
    """Represents reasoning why a certain OAuth2 scope is being requested.

    .. versionadded:: 1.2

    Attributes
    ----------
    allow: :class:`str`
        ...
    deny: :class:`str`
        ...

    Parameters
    ----------
    allow: :class:`str`
        ...
    deny: :class:`str`
        ...
    """

    __slots__ = (
        'allow',
        'deny',
    )

    def __init__(self, *, allow: str, deny: str) -> None:
        self.allow: str = allow
        self.deny: str = deny

    def __eq__(self, other: object, /) -> bool:
        return self is other or (
            isinstance(other, OAuth2ScopeReasoning) and other.allow == self.allow and other.deny == self.deny
        )

    def __repr__(self) -> str:
        return f'<OAuth2ScopeReasoning allow={self.allow!r} deny={self.deny!r}>'

    def to_dict(self) -> raw.OAuth2ScopeReasoning:
        return {
            'allow': self.allow,
            'deny': self.deny,
        }


@define(slots=True)
class PossibleOAuth2Authorization:
    """Represents a possible OAuth2 authorization.

    .. versionadded:: 1.2
    """

    bot: PublicBot = field(repr=True, kw_only=True, eq=True)
    """:class:`PublicBot`: The bot."""

    user: User = field(repr=True, kw_only=True, eq=True)
    """:class:`User`: The bot user."""

    allowed_scopes: dict[str, OAuth2ScopeReasoning] = field(repr=True, kw_only=True, eq=True)
    """Dict[:class:`str`, :class:`OAuth2ScopeReasoning`]: A mapping of OAuth2 scopes to reasoning why would it be requested."""


@define(slots=True)
class OAuth2AccessToken:
    """Represents result of exchanging OAuth2 code, or refreshing token.

    .. versionadded:: 1.2
    """

    state: State = field(repr=False, kw_only=True)
    """:class:`State`: State that controls this OAuth2 authorization."""

    access_token: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The OAuth2 token."""

    refresh_token: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The refresh token, used to retrieve new access tokens."""

    token_type: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The type of OAuth2 token."""

    scopes: list[str] = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The scopes that the OAuth2 token has."""

    async def revoke(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> OAuth2Authorization:
        """|coro|

        Revokes the OAuth2 token.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+--------------------------------+
            | Value                | Reason                         |
            +----------------------+--------------------------------+
            | ``InvalidOperation`` | The token was already revoked. |
            +----------------------+--------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+------------------------+
            | Value                | Reason                 |
            +----------------------+------------------------+
            | ``NotAuthenticated`` | The token was invalid. |
            +----------------------+------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------------------+
            | Value        | Reason                                |
            +--------------+---------------------------------------+
            | ``NotFound`` | The OAuth2 authorization was deleted. |
            +--------------+---------------------------------------+

        Returns
        -------
        :class:`OAuth2Authorization`
            The revoked OAuth2 authorization.
        """
        return await self.state.http.revoke_oauth2_token(self.access_token, http_overrides=http_overrides)


@define(slots=True)
class OAuth2Authorization:
    """Represents OAuth2 bot authorization.

    .. versionadded:: 1.2
    """

    state: State = field(repr=False, kw_only=True)
    """:class:`State`: State that controls this OAuth2 authorization."""

    bot_id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The bot's ID this OAuth2 authorization is for."""

    bot: typing.Optional[PublicBot] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`PublicBot`]: The bot."""

    user_id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The user's ID who has this OAuth2 authorization."""

    created_at: datetime = field(repr=True, kw_only=True)
    """:class:`~datetime.datetime`: When the OAuth2 authorization was created."""

    deauthorized_at: typing.Optional[datetime] = field(repr=True, kw_only=True)
    """Optional[:class:`~datetime.datetime`]: When the OAuth2 authorization was deleted."""

    scopes: list[str] = field(repr=True, kw_only=True)
    """List[:class:`str`]: The scopes this OAuth2 authorization grants."""

    async def revoke(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> OAuth2Authorization:
        """|coro|

        Revokes the OAuth2 authorization.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+--------------------------------+
            | Value                | Reason                         |
            +----------------------+--------------------------------+
            | ``InvalidOperation`` | The token was already revoked. |
            +----------------------+--------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------------------+
            | Value        | Reason                                |
            +--------------+---------------------------------------+
            | ``NotFound`` | The OAuth2 authorization was deleted. |
            +--------------+---------------------------------------+

        Returns
        -------
        :class:`OAuth2Authorization`
            The revoked OAuth2 authorization.
        """

        return await self.state.http.revoke_oauth2_authorization(self.bot_id, http_overrides=http_overrides)


__all__ = (
    'OAuth2ScopeReasoning',
    'PossibleOAuth2Authorization',
    'OAuth2AccessToken',
    'OAuth2Authorization',
)
