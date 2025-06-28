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

from abc import ABC, abstractmethod
from inspect import isawaitable
import typing

import aiohttp

if typing.TYPE_CHECKING:
    from typing_extensions import Self

    from multidict import MultiMapping, CIMultiDict
    from yarl import URL

    from .utils import MaybeAwaitable, MaybeAwaitableFunc

F = typing.TypeVar('F')


class WebSocketConnectionFailure(Exception):
    """Signal that WebSocket endpoint did not return "101 Switching Protocols" status code."""

    __slots__ = ('status',)

    def __init__(self, *, status: int) -> None:
        self.status: int = status
        super().__init__(f'WebSocket endpoint returned {status} status code')


@typing.runtime_checkable
class HTTPResponse(typing.Protocol):
    """A HTTP response."""

    @property
    def method(self) -> str:
        """:class:`str`: The HTTP request method."""
        ...

    @property
    def status(self) -> int:
        """:class:`int`: The HTTP response status code."""
        ...

    @property
    def headers(self) -> MultiMapping[str]:
        """MultiMapping[:class:`str`]: The response headers."""
        ...

    @property
    def closed(self) -> bool:
        """:class:`bool`: Whether the request resources were released."""
        ...

    @property
    def url(self) -> URL:
        """:class:`yarl.URL`: The request URL."""
        ...

    def close(self) -> MaybeAwaitable[None]:
        """Release request resources."""
        ...

    async def read(self) -> bytes:
        """:class:`bytes`: Read the response body."""
        ...

    async def text(self, encoding: typing.Optional[str] = None, errors: str = 'strict') -> str:
        """:class:`str`: Read the response body as string."""
        ...


class AIOHTTPResponseWrapper:
    """A wrapper around :class:`aiohttp.ClientResponse`."""

    __slots__ = ('underlying',)

    def __init__(self, underlying: aiohttp.ClientResponse, /) -> None:
        self.underlying: aiohttp.ClientResponse = underlying

    @property
    def method(self) -> str:
        """:class:`str`: The HTTP request method."""
        return self.underlying.method

    @property
    def status(self) -> int:
        """:class:`int`: The HTTP response status code."""
        return self.underlying.status

    @property
    def headers(self) -> MultiMapping[str]:
        """MultiMapping[:class:`str`]: The response headers."""
        return self.underlying.headers

    @property
    def closed(self) -> bool:
        """:class:`bool`: Whether the request resources were released."""
        return self.underlying.closed

    @property
    def url(self) -> URL:
        """:class:`yarl.URL`: The request URL."""
        return self.underlying.url

    def close(self) -> MaybeAwaitable[None]:
        """Release request resources."""
        return self.underlying.close()

    async def read(self) -> bytes:
        """:class:`bytes`: Read the response body."""
        return await self.underlying.read()

    async def text(self, encoding: typing.Optional[str] = None, errors: str = 'strict') -> str:
        """:class:`str`: Read the response body as string."""
        return await self.underlying.text(encoding=encoding, errors=errors)


@typing.runtime_checkable
class HTTPWebSocket(typing.Generic[F], typing.Protocol):  # type: ignore
    """A HTTP WebSocket connection."""

    @property
    def close_code(self) -> typing.Optional[int]: ...

    @property
    def closed(self) -> bool: ...

    async def close(self, *, code: int = 1000, message: bytes = b'') -> bool: ...

    async def receive(self, timeout: typing.Optional[float] = None) -> F: ...

    async def send_bytes(self, data: bytes, compress: typing.Optional[int] = None) -> None: ...

    async def send_str(self, data: str, compress: typing.Optional[int] = None) -> None: ...


class HTTPForm:
    """Represents a form.

    This is constructed by the library and meant
    to be converted to form consumable by underlying HTTP backend.
    """

    __slots__ = (
        'fields',
        'charset',
        'quote_fields',
    )

    def __init__(
        self,
        fields: typing.Optional[list[dict[str, typing.Any]]] = None,
        *,
        charset: typing.Optional[str] = None,
        quote_fields: bool = True,
    ) -> None:
        if fields is None:
            fields = []

        self.fields: list[dict[str, typing.Any]] = fields
        self.charset: typing.Optional[str] = charset
        self.quote_fields: bool = quote_fields

    def add_field(
        self,
        name: str,
        value: typing.Any,
        *,
        content_type: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
    ) -> Self:
        """Adds a field."""

        self.fields.append(
            {
                'name': name,
                'value': value,
                'content_type': content_type,
                'filename': filename,
            }
        )
        return self


class HTTPAdapter(ABC, typing.Generic[F]):
    """Represents a HTTP adapter."""

    __slots__ = ()

    async def startup(self) -> None:
        """Sets up adapter."""

    async def close(self) -> None:
        """Release all underlying resources."""

    @abstractmethod
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

            - ``form``
            - ``json``
            - ``params``
            - ``proxy``
            - ``proxy_auth``

        Returns
        -------
        :class:`HTTPResponse`
            The response.
        """
        ...

    @abstractmethod
    async def websocket(
        self,
        url: str,
        *,
        headers: CIMultiDict[typing.Any],
        **kwargs,
    ) -> HTTPWebSocket[F]:
        """Creates a WebSocket connection.

        .. note::
            You **should** perform basic WebSocket handshake validation in this method if you're overriding it.

            However you **should not** validate frames sent by Revolt itself.

        Parameters
        ----------
        url: :class:`str`
            The URL to create WebSocket connection to.
        headers: CIMultiDict[Any]
            The HTTP headers.
        \\*\\*kwargs
            The keyword arguments to pass to requester function.

            Usually these are passed:

            - ``proxy``
            - ``proxy_auth``

        Returns
        -------
        :class:`.HTTPWebSocket`
            The response.
        """
        ...

    @abstractmethod
    def is_close_frame(self, frame: F, /) -> bool:
        """:class:`bool`: Returns whether the provided frame is a CLOSE/CLOSED/CLOSING frame."""
        ...

    @abstractmethod
    def is_error_frame(self, frame: F, /) -> bool:
        """:class:`bool`: Returns whether the provided frame is an ERROR pseudo-frame."""
        ...

    @abstractmethod
    def is_binary_frame(self, frame: F, /) -> bool:
        """:class:`bool`: Returns whether the provided frame is a BINARY frame."""
        ...

    @abstractmethod
    def is_text_frame(self, frame: F, /) -> bool:
        """:class:`bool`: Returns whether the provided frame is a TEXT frame."""
        ...

    @abstractmethod
    def payload_from_frame(self, frame: F, /) -> typing.Any:
        """Any: Returns frame payload."""


class AIOHTTPAdapter(HTTPAdapter[aiohttp.WSMessage]):
    """Represents a HTTP adapter using :class:`aiohttp.ClientSession`.

    This inherits from :class:`.HTTPAdapter`.
    """

    __slots__ = ('_session',)

    _session: typing.Optional[
        typing.Union[aiohttp.ClientSession, MaybeAwaitableFunc[[AIOHTTPAdapter], aiohttp.ClientSession]]
    ]

    def __init__(
        self,
        *,
        session: typing.Optional[
            typing.Union[aiohttp.ClientSession, MaybeAwaitableFunc[[AIOHTTPAdapter], aiohttp.ClientSession]]
        ] = None,
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

    def maybe_get_session(self) -> typing.Optional[aiohttp.ClientSession]:
        if self._session is None or not isinstance(self._session, aiohttp.ClientSession):
            return None
        return self._session

    async def close(self) -> None:
        """Release all underlying resources."""
        session = self.maybe_get_session()
        if session is not None:
            await session.close()

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
        :class:`.AIOHTTPResponseWrapper`
            The response.
        """

        if 'form' in kwargs:
            form = kwargs.pop('form')
            if form is None:
                modified_kwargs = {}
            else:
                modified_kwargs = kwargs | {'data': self.convert_form(form)}
        else:
            modified_kwargs = kwargs

        session = await self.get_session()

        response = await session.request(
            method,
            url,
            headers=headers,
            **modified_kwargs,
        )
        return AIOHTTPResponseWrapper(response)

    async def websocket(
        self,
        url: str,
        *,
        headers: CIMultiDict[typing.Any],
        **kwargs,
    ) -> HTTPWebSocket:
        """Creates a WebSocket connection.

        .. note::
            You **should** perform basic WebSocket handshake validation in this method if you're overriding it.

            However you **should not** validate frames sent by Revolt itself.

        Parameters
        ----------
        url: :class:`str`
            The URL to create WebSocket connection to.
        headers: CIMultiDict[Any]
            The HTTP headers.
        \\*\\*kwargs
            The keyword arguments to pass to requester function.

            Usually these are passed:

            - ``proxy``
            - ``proxy_auth``

        Returns
        -------
        :class:`.HTTPWebSocket`
            The response.
        """
        session = await self.get_session()

        try:
            connection = await session.ws_connect(url, headers=headers, **kwargs)
        except aiohttp.WSServerHandshakeError as exc:
            raise WebSocketConnectionFailure(status=exc.status) from exc

        return connection

    def is_close_frame(self, frame: aiohttp.WSMessage, /) -> bool:
        """:class:`bool`: Returns whether the provided frame is a close frame."""
        return frame.type in (
            aiohttp.WSMsgType.CLOSE,
            aiohttp.WSMsgType.CLOSED,
            aiohttp.WSMsgType.CLOSING,
        )

    def is_error_frame(self, frame: aiohttp.WSMessage, /) -> bool:
        """:class:`bool`: Returns whether the provided frame is an ERROR pseudo-frame."""
        return frame.type is aiohttp.WSMsgType.ERROR

    def is_binary_frame(self, frame: aiohttp.WSMessage, /) -> bool:
        """:class:`bool`: Returns whether the provided frame is a BINARY frame."""
        return frame.type is aiohttp.WSMsgType.BINARY

    def is_text_frame(self, frame: aiohttp.WSMessage, /) -> bool:
        """:class:`bool`: Returns whether the provided frame is a TEXT frame."""
        return frame.type is aiohttp.WSMsgType.TEXT

    def payload_from_frame(self, frame: aiohttp.WSMessage, /) -> typing.Any:
        """Any: Returns frame payload."""
        return frame.data

    def convert_form(self, form: HTTPForm, /) -> aiohttp.FormData:
        """Converts agnostic :class:`HTTPForm` to :class:`aiohttp.FormData`."""
        res = aiohttp.FormData(
            form.fields,
            quote_fields=form.quote_fields,
            charset=form.charset,
        )
        return res


__all__ = (
    'WebSocketConnectionFailure',
    'HTTPResponse',
    'AIOHTTPResponseWrapper',
    'HTTPWebSocket',
    'HTTPForm',
    'HTTPAdapter',
    'AIOHTTPAdapter',
)
