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
from aiohttp.helpers import reify

if typing.TYPE_CHECKING:
    from multidict import CIMultiDict, CIMultiDictProxy

    from .utils import MaybeAwaitable, MaybeAwaitableFunc


@typing.runtime_checkable
class HTTPResponse(typing.Protocol):
    status: int

    @reify
    def headers(self) -> CIMultiDictProxy[str]:
        """CIMultiDictProxy[:class:`str`]: The response headers."""
        ...

    def close(self) -> MaybeAwaitable[None]:
        """Release request resources."""
        ...

    async def read(self) -> bytes:
        """:class:`bytes`: Read the response body."""
        ...

    async def text(self, *, encoding: typing.Optional[str] = None, errors: str = 'strict') -> str:
        """:class:`str`: Read the response body as string."""
        ...


class HTTPAdapter(ABC):
    """Represents a HTTP adapter."""

    __slots__ = ()

    async def request(
        self,
        method: str,
        url: str,
        *,
        headers: CIMultiDict[typing.Any],
        **kwargs,
    ) -> HTTPResponse:
        """Perform an actual HTTP request.

        .. note::
            You should not perform Revolt API error and ratelimit handling in this method if you're overriding it.

        Parameters
        ----------
        method: :class:`str`
            The HTTP method.
        url: :class:`str`
            The URL to send HTTP request to.
        headers: CIMultiDict[Any]
            The HTTP headers.
        \\*\\*kwargs
            The keyword arguments to pass to requester function.

            Usually these are passed:

            - ``json``
            - ``params``
            - ``proxy``
            - ``proxy_auth``

        Returns
        -------
        :class:`.HTTPResponse`
            The response.
        """
        ...


# horrible name please PR a better name
class AIOHTTPAdapter(HTTPAdapter):
    """Represents a HTTP adapter using :doc:`aiohtpt`."""

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

    async def request(
        self,
        method: str,
        url: str,
        *,
        headers: CIMultiDict[typing.Any],
        **kwargs,
    ) -> HTTPResponse:
        """Perform an actual HTTP request.

        .. note::
            You should not perform Revolt API error and ratelimit handling in this method if you're overriding it.

        Parameters
        ----------
        method: :class:`str`
            The HTTP method.
        url: :class:`str`
            The URL to send HTTP request to.
        headers: CIMultiDict[Any]
            The HTTP headers.
        \\*\\*kwargs
            The keyword arguments to pass to :meth:`aiohttp.ClientSession.request`.

        Returns
        -------
        :class:`aiohttp.ClientResponse`
            The response.
        """
        session = await self.get_session()

        return await session.request(
            method,
            url,
            headers=headers,
            **kwargs,
        )


__all__ = (
    'HTTPAdapter',
    'AIOHTTPAdapter',
)
