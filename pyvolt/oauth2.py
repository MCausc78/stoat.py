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
    from .bot import PublicBot
    from .user import User


@define(slots=True)
class OAuth2ScopeReasoning:
    """Represents reasoning why a certain OAuth2 scope is being requested."""

    allow: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: ..."""

    deny: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: ..."""


@define(slots=True)
class PossibleOAuth2Authorization:
    """Represents a possible OAuth2 authorization."""

    bot: PublicBot = field(repr=True, kw_only=True, eq=True)
    """:class:`PublicBot`: The bot."""

    user: User = field(repr=True, kw_only=True, eq=True)
    """:class:`User`: The bot user."""

    allowed_scopes: dict[str, OAuth2ScopeReasoning] = field(repr=True, kw_only=True, eq=True)
    """Dict[:class:`str`]: A mapping of OAuth2 scopes to reasoning why would it be requested."""


__all__ = (
    'OAuth2ScopeReasoning',
    'PossibleOAuth2Authorization',
)
