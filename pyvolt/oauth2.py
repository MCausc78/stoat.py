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
    from . import raw
    from .bot import PublicBot
    from .user import User


class OAuth2ScopeReasoning:
    """Represents reasoning why a certain OAuth2 scope is being requested.

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
    """Represents a possible OAuth2 authorization."""

    bot: PublicBot = field(repr=True, kw_only=True, eq=True)
    """:class:`PublicBot`: The bot."""

    user: User = field(repr=True, kw_only=True, eq=True)
    """:class:`User`: The bot user."""

    allowed_scopes: dict[str, OAuth2ScopeReasoning] = field(repr=True, kw_only=True, eq=True)
    """Dict[:class:`str`, :class:`OAuth2ScopeReasoning`]: A mapping of OAuth2 scopes to reasoning why would it be requested."""


@define(slots=True)
class OAuth2AccessToken:
    """Represents result of exchanging OAuth2 code."""

    access_token: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The OAuth2 token."""

    token_type: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The token type of OAuth2 token."""

    scopes: list[str] = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The scopes that the OAuth2 token has."""


__all__ = (
    'OAuth2ScopeReasoning',
    'PossibleOAuth2Authorization',
    'OAuth2AccessToken',
)
