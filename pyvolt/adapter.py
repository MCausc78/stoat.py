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

from abc import ABC
from inspect import isawaitable
import typing

import aiohttp

if typing.TYPE_CHECKING:
    from .utils import MaybeAwaitableFunc


class HTTPAdapter(ABC):
    __slots__ = ()


# horrible name please PR a better name
class AIOHTTPAdapter(HTTPAdapter):
    __slots__ = ('_session',)

    _session: typing.Optional[
        typing.Union[aiohttp.ClientSession, MaybeAwaitableFunc[[AIOHTTPAdapter], aiohttp.ClientSession]]
    ]

    def __init__(
        self,
        *,
        session: typing.Optional[
            typing.Union[aiohttp.ClientSession, MaybeAwaitableFunc[[AIOHTTPAdapter], aiohttp.ClientSession]]
        ],
    ) -> None:
        self._session: typing.Optional[
            typing.Union[aiohttp.ClientSession, MaybeAwaitableFunc[[AIOHTTPAdapter], aiohttp.ClientSession]]
        ] = session

    async def get_session(self) -> aiohttp.ClientSession:
        """:class:`aiohttp.ClientSession`: The HTTP session."""
        if self._session is None:
            self._session = aiohttp.ClientSession()
            return self._session

        # Just in case if self._session suddenly becomes callable
        if callable(self._session) and not isinstance(self._session, aiohttp.ClientSession):
            ret = self._session(self)
            if isawaitable(ret):
                ret = await ret
            self._session = ret

        return self._session


__all__ = (
    'HTTPAdapter',
    'AIOHTTPAdapter',
)
