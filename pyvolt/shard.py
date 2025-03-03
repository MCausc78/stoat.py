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
import asyncio
from inspect import isawaitable
import logging
import typing

from multidict import CIMultiDict

from . import __version__, utils
from .adapter import WebSocketConnectionFailure, HTTPWebSocket, HTTPAdapter, AIOHTTPAdapter
from .core import ULIDOr, resolve_id
from .enums import ShardFormat
from .errors import PyvoltException, ShardClosedError, AuthenticationError, ConnectError

if typing.TYPE_CHECKING:
    from datetime import datetime

    from . import raw
    from .channel import TextableChannel
    from .message import BaseMessage
    from .server import BaseServer
    from .state import State

try:
    import msgpack  # type: ignore
except ImportError:
    _HAS_MSGPACK = False
else:
    _HAS_MSGPACK = True

_L = logging.getLogger(__name__)


class Close(Exception):
    __slots__ = ()


class Reconnect(Exception):
    __slots__ = ()


class EventHandler(ABC):
    """A handler for shard events."""

    __slots__ = ()

    @abstractmethod
    def handle_raw(self, shard: Shard, payload: raw.ClientEvent, /) -> utils.MaybeAwaitable[None]:
        """Handles dispatched event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard that received the event.
        payload: Dict[:class:`str`, Any]
            The received event payload.
        """
        ...

    def before_connect(self, shard: Shard, /) -> utils.MaybeAwaitable[None]:
        """Called before connecting to Revolt."""
        ...

    def after_connect(self, shard: Shard, socket: HTTPWebSocket, /) -> utils.MaybeAwaitable[None]:
        """Called when successfully connected to Revolt WebSocket.

        Parameters
        ----------
        socket: :class:`.HTTPWebSocket`
            The connected WebSocket.
        """
        ...


DEFAULT_SHARD_USER_AGENT = f'pyvolt (https://github.com/MCausc78/pyvolt, {__version__})'


class Shard(ABC):
    __slots__ = ('send',)

    state: State

    @abstractmethod
    def is_closed(self) -> bool:
        """:class:`bool`: Whether the connection is closed."""
        ...

    @property
    @abstractmethod
    def base_url(self) -> str:
        """:class:`str`: The base WebSocket URL."""
        ...

    @property
    @abstractmethod
    def bot(self) -> bool:
        """:class:`bool`: Whether the token belongs to bot account."""
        ...

    @property
    @abstractmethod
    def format(self) -> ShardFormat:
        """:class:`.ShardFormat`: The message format to use when communicating with Revolt WebSocket."""
        ...

    @property
    @abstractmethod
    def handler(self) -> typing.Optional[EventHandler]:
        """Optional[:class:`.EventHandler`]: The handler that receives events. Defaults to ``None`` if not provided."""
        ...

    @property
    @abstractmethod
    def last_ping_at(self) -> typing.Optional[datetime]:
        """Optional[:class:`~datetime.datetime`]: When the shard sent ping."""
        ...

    @property
    @abstractmethod
    def last_pong_at(self) -> typing.Optional[datetime]:
        """Optional[:class:`~datetime.datetime`]: When the shard received response to ping."""
        ...

    @property
    @abstractmethod
    def logged_out(self) -> bool:
        """:class:`bool`: Whether the shard got logged out."""
        ...

    @property
    @abstractmethod
    def token(self) -> str:
        """:class:`str`: The shard token. May be empty if not started."""

    @abstractmethod
    async def cleanup(self) -> None:
        """Closes the aiohttp session."""
        ...

    @abstractmethod
    async def close(self) -> None:
        """Closes the connection to Revolt."""
        ...

    @property
    @abstractmethod
    def socket(self) -> HTTPWebSocket:
        """:class:`.HTTPWebSocket`: The current WebSocket connection."""
        ...

    @abstractmethod
    def with_credentials(self, token: str, *, bot: bool = True) -> None:
        """Modifies HTTP request credentials.

        Parameters
        ----------
        token: :class:`str`
            The authentication token.
        bot: :class:`bool`
            Whether the token belongs to bot account or not.
        """
        ...

    @abstractmethod
    async def authenticate(self) -> None:
        """|coro|

        Authenticates the currently connected WebSocket. This is called right after successful WebSocket handshake.
        """
        ...

    @abstractmethod
    async def ping(self) -> None:
        """|coro|

        Pings the WebSocket.
        """
        ...

    @abstractmethod
    async def begin_typing(self, channel: ULIDOr[TextableChannel], /) -> None:
        """|coro|

        Begins typing in a channel.

        Parameters
        ----------
        channel: ULIDOr[:class:`TextableChannel`]
            The channel to begin typing in.
        """
        ...

    @abstractmethod
    async def end_typing(self, channel: ULIDOr[TextableChannel], /) -> None:
        """|coro|

        Ends typing in a channel.

        Parameters
        ----------
        channel: ULIDOr[:class:`.TextableChannel`]
            The channel to end typing in.
        """
        ...

    @abstractmethod
    async def subscribe_to(self, server: ULIDOr[BaseServer], /) -> None:
        """|coro|

        Subscribes user to a server. After calling this method, you will begin
        receiving :class:`.UserUpdateEvent`'s for members of the subscribed server.

        .. note::

            Calling this method has no effect on bot tokens. Additionally:
            - Server subscriptions automatically expire within 15 minutes.
            - You may have up only to 5 active subscriptions.
            - This command should only be sent if application/client is in focus.
            - You should aim to call this method at most every 10 minutes per server.

        Parameters
        ----------
        server: ULIDOr[:class:`.BaseServer`]
            The server to subscribe to.
        """
        ...

    @abstractmethod
    async def begin_editing(self, channel: ULIDOr[TextableChannel], message: ULIDOr[BaseMessage]) -> None:
        """|coro|

        Begins editing a message.

        Parameters
        ----------
        channel: ULIDOr[:class:`.TextableChannel`]
            The channel the message was sent in.
        message: ULIDOr[:class:`.BaseMessage`]
            The message to begin editing.
        """
        ...

    @abstractmethod
    async def stop_editing(self, channel: ULIDOr[TextableChannel], message: ULIDOr[BaseMessage]) -> None:
        """|coro|

        Stops editing a message.

        Parameters
        ----------
        channel: ULIDOr[:class:`.TextableChannel`]
            The channel the message was sent in.
        message: ULIDOr[:class:`.BaseMessage`]
            The message to stop editing.
        """
        ...

    @abstractmethod
    async def connect(self) -> None:
        """Starts the WebSocket lifecycle."""


class ShardImpl(Shard):
    """Implements Revolt WebSocket client.

    Attributes
    ----------
    base_url: :class:`str`
        The base WebSocket URL.
    bot: :class:`bool`
        Whether the token belongs to bot account. Defaults to ``True``.
    connect_delay: Optional[:class:`float`]
        The duration in seconds to sleep when reconnecting to WebSocket due to aiohttp errors. Defaults to 2.
    format: :class:`ShardFormat`
        The message format to use when communicating with Revolt WebSocket.
    handler: Optional[:class:`.EventHandler`]
        The handler that receives events. Defaults to ``None`` if not provided.
    last_ping_at: Optional[:class:`~datetime.datetime`]
        When the shard sent ping.
    last_pong_at: Optional[:class:`~datetime.datetime`]
        When the shard received response to ping.
    logged_out: :class:`bool`
        Whether the shard got logged out.
    reconnect_on_timeout: :class:`bool`
        Whether to reconnect when received pong nonce is not equal to current ping nonce. Defaults to ``True``.
    request_user_settings: Optional[List[:class:`str`]]
        The list of user setting keys to request.
    state: :class:`State`
        The state.
    token: :class:`str`
        The shard token. May be empty if not started.
    user_agent: :class:`str`
        The HTTP user agent used when connecting to WebSocket.
    """

    __slots__ = (
        '_adapter',
        '_base_url',
        '_bot',
        '_closed',
        '_format',
        '_handler',
        '_heartbeat_sequence',
        '_last_close_code',
        '_last_ping_at',
        '_last_pong_at',
        '_logged_out',
        '_sequence',
        '_socket',
        '_token',
        'connect_delay',
        'reconnect_on_timeout',
        'request_user_settings',
        'retries',
        'state',
        'user_agent',
        'recv',
        'send',
    )

    def __init__(
        self,
        token: str,
        *,
        adapter: typing.Optional[typing.Union[utils.MaybeAwaitableFunc[[Shard], HTTPAdapter], HTTPAdapter]] = None,
        base_url: typing.Optional[str] = None,
        bot: bool = True,
        connect_delay: typing.Optional[float] = 2,
        format: ShardFormat = ShardFormat.json,
        handler: typing.Optional[EventHandler] = None,
        reconnect_on_timeout: bool = True,
        request_user_settings: typing.Optional[list[str]] = None,
        retries: typing.Optional[int] = None,
        # session: typing.Union[utils.MaybeAwaitableFunc[[Shard], aiohttp.ClientSession], aiohttp.ClientSession],
        state: State,
        user_agent: typing.Optional[str] = None,
    ) -> None:
        if format is ShardFormat.msgpack and not _HAS_MSGPACK:
            raise TypeError('Cannot use msgpack format without dependency')

        self._adapter: typing.Optional[typing.Union[utils.MaybeAwaitableFunc[[Shard], HTTPAdapter], HTTPAdapter]] = (
            adapter
        )
        self._base_url: str = base_url or 'wss://ws.revolt.chat/'
        self._bot: bool = bot
        self._closed: bool = False
        self._format: ShardFormat = format
        self._handler: typing.Optional[EventHandler] = handler
        self._heartbeat_sequence: int = 1
        self._last_close_code: typing.Optional[int] = None
        self._last_ping_at: typing.Optional[datetime] = None
        self._last_pong_at: typing.Optional[datetime] = None
        self._logged_out: bool = False
        self._sequence: int = 0
        self._socket: typing.Optional[HTTPWebSocket] = None
        self._token: str = token

        self.connect_delay: typing.Optional[float] = connect_delay
        self.reconnect_on_timeout: bool = reconnect_on_timeout
        self.request_user_settings = request_user_settings
        self.retries: int = retries or 150
        self.state: State = state
        self.user_agent: str = user_agent or DEFAULT_SHARD_USER_AGENT

        self.recv = self._recv_json if format is ShardFormat.json else self._recv_msgpack
        self.send = self._send_json if format is ShardFormat.json else self._send_msgpack

    def is_closed(self) -> bool:
        return self._closed and not self._socket

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def bot(self) -> bool:
        return self._bot

    @property
    def format(self) -> ShardFormat:
        return self._format

    @property
    def handler(self) -> typing.Optional[EventHandler]:
        return self._handler

    @property
    def last_ping_at(self) -> typing.Optional[datetime]:
        return self._last_ping_at

    @property
    def last_pong_at(self) -> typing.Optional[datetime]:
        return self._last_pong_at

    @property
    def logged_out(self) -> bool:
        return self._logged_out

    @property
    def token(self) -> str:
        return self._token

    async def get_adapter(self) -> HTTPAdapter:
        if self._adapter is None:
            adapter = AIOHTTPAdapter()
            self._adapter = adapter
            return adapter

        if callable(self._adapter):
            ret = self._adapter(self)
            if isawaitable(ret):
                ret = await ret
            self._adapter = ret
            return ret
        return self._adapter

    def maybe_get_adapter(self) -> typing.Optional[HTTPAdapter]:
        if self._adapter is None or not isinstance(self._adapter, HTTPAdapter):
            return None
        return self._adapter

    @property
    def adapter(self) -> HTTPAdapter:
        if self._adapter is None or (callable(self._adapter) and not isinstance(self._adapter, HTTPAdapter)):
            raise TypeError('No adapter is available')
        return self._adapter

    async def cleanup(self) -> None:
        """|coro|

        Closes the aiohttp session.
        """
        adapter = self.maybe_get_adapter()
        if adapter is not None:
            await adapter.close()

    async def close(self) -> None:
        """|coro|

        Closes the connection to Revolt.
        """
        if self._socket is not None:
            if self._closed:
                raise ShardClosedError('Already closed')
            self._closed = True
            await self._socket.close(code=1000)

    @property
    def socket(self) -> HTTPWebSocket:
        if self._socket is None:
            raise TypeError('No websocket')
        return self._socket

    def with_credentials(self, token: str, *, bot: bool = True) -> None:
        self._token = token
        self._bot = bot

    async def authenticate(self) -> None:
        payload: raw.ServerAuthenticateEvent = {
            'type': 'Authenticate',
            'token': self.token,
        }
        await self.send(payload)

    async def ping(self) -> None:
        self._heartbeat_sequence += 1
        payload: raw.ServerPingEvent = {
            'type': 'Ping',
            'data': self._heartbeat_sequence,
        }
        await self.send(payload)
        self._last_ping_at = utils.utcnow()

    async def begin_typing(self, channel: ULIDOr[TextableChannel], /) -> None:
        payload: raw.ServerBeginTypingEvent = {'type': 'BeginTyping', 'channel': resolve_id(channel)}
        await self.send(payload)

    async def end_typing(self, channel: ULIDOr[TextableChannel], /) -> None:
        payload: raw.ServerEndTypingEvent = {'type': 'EndTyping', 'channel': resolve_id(channel)}
        await self.send(payload)

    async def subscribe_to(self, server: ULIDOr[BaseServer], /) -> None:
        payload: raw.ServerSubscribeEvent = {'type': 'Subscribe', 'server_id': resolve_id(server)}
        await self.send(payload)

    async def begin_editing(self, channel: ULIDOr[TextableChannel], message: ULIDOr[BaseMessage]) -> None:
        payload: raw.ServerBeginEditingEvent = {
            'type': 'BeginEditing',
            'channel': resolve_id(channel),
            'message': resolve_id(message),
        }
        await self.send(payload)

    async def stop_editing(self, channel: ULIDOr[TextableChannel], message: ULIDOr[BaseMessage]) -> None:
        payload: raw.ServerStopEditingEvent = {
            'type': 'StopEditing',
            'channel': resolve_id(channel),
            'message': resolve_id(message),
        }
        await self.send(payload)

    async def _send_json(self, d: raw.ServerEvent, /) -> None:
        _L.debug('Sending %s', d)
        await self.socket.send_str(utils.to_json(d))

    async def _send_msgpack(self, d: raw.ServerEvent, /) -> None:
        _L.debug('Sending %s', d)

        # Will never none according to stubs: https://github.com/sbdchd/msgpack-types/blob/a9ab1c861933fa11aff706b21c303ee52a2ee359/msgpack-stubs/__init__.pyi#L40-L49
        payload: bytes = msgpack.packb(d)  # type: ignore
        await self.socket.send_bytes(payload)

    async def _recv_json(self) -> raw.ClientEvent:
        try:
            frame = await self.socket.receive()
        except (KeyboardInterrupt, asyncio.CancelledError):
            raise Close

        adapter = self.adapter

        if adapter.is_close_frame(frame):
            self._last_close_code = data = self.socket.close_code
            _L.debug('WebSocket closed with %s (closed: %s)', data, self._closed)
            if self._closed:
                raise Close
            await asyncio.sleep(0.25)
            raise Reconnect

        if adapter.is_error_frame(frame):
            _L.debug('Received invalid WebSocket payload. Reconnecting.')
            raise Reconnect

        if not adapter.is_text_frame(frame):
            _L.debug(
                'Received unknown frame type: %s (expected TEXT). Reconnecting.',
                frame,
            )
            raise Reconnect

        k = utils.from_json(adapter.payload_from_frame(frame))
        if k['type'] != 'Ready':
            _L.debug('Received %s', k)
        return k

    async def _recv_msgpack(self) -> raw.ClientEvent:
        try:
            frame = await self.socket.receive()
        except (KeyboardInterrupt, asyncio.CancelledError):
            raise Close

        adapter = self.adapter

        if adapter.is_close_frame(frame):
            self._last_close_code = data = self.socket.close_code
            _L.debug('WebSocket closed with %s (closed: %s)', data, self._closed)
            if self._closed:
                raise Close
            await asyncio.sleep(0.25)
            raise Reconnect

        if adapter.is_error_frame(frame):
            _L.debug('Received invalid WebSocket payload. Reconnecting.')
            raise Reconnect

        if not adapter.is_binary_frame(frame):
            _L.debug(
                'Received unknown frame type: %s (expected BINARY). Reconnecting.',
                frame,
            )
            raise Reconnect

        # `msgpack` wont be unbound here
        k: raw.ClientEvent = msgpack.unpackb(adapter.payload_from_frame(frame), use_list=True)  # type: ignore
        if k['type'] != 'Ready':
            _L.debug('Received %s', k)
        return k

    def get_headers(self) -> dict[str, str]:
        """Dict[:class:`str`, :class:`str`]: The headers to use when connecting to WebSocket."""
        return {'User-Agent': self.user_agent}

    async def _heartbeat(self) -> None:
        while True:
            await asyncio.sleep(30.0)
            await self.ping()

    async def _socket_connect(self) -> HTTPWebSocket[typing.Any]:
        adapter = await self.get_adapter()

        params: raw.BonfireConnectionParameters = {
            'version': '1',
            'format': self.format.value,
        }
        if self.request_user_settings is not None:
            params['__user_settings_keys'] = ','.join(self.request_user_settings)

        errors = []

        i = 0
        _L.debug('Connecting to %s, format=%s', self.base_url, self.format)

        headers: dict[str, str] = self.get_headers()
        while True:
            if i >= self.retries:
                break
            try:
                return await adapter.websocket(
                    self.base_url,
                    headers=CIMultiDict(headers),
                    params=params,  # type: ignore # Not true
                )
            except OSError as exc:
                if i == 0:
                    _L.warning('Connection failed (code: %i)', exc.errno)
                if exc.errno == 11001:
                    await asyncio.sleep(1)
                i += 1
            except WebSocketConnectionFailure as exc:
                _L.debug('Server replied with %i', exc.status)
                if exc.status in (502, 525):
                    await asyncio.sleep(1.5)
                    continue
                raise exc from None
            except Exception as exc:
                i += 1
                errors.append(exc)
                _L.exception('Connection failed on %i attempt', i)
                if self.connect_delay is not None:
                    await asyncio.sleep(self.connect_delay)
        raise ConnectError(self.retries, errors)

    async def connect(self) -> None:
        if self._socket is not None:
            raise PyvoltException('The connection is already open.')

        while not self._closed:
            if self.handler:
                r = self.handler.before_connect(self)
                if isawaitable(r):
                    await r

            socket = await self._socket_connect()
            if self.handler:
                r = self.handler.after_connect(self, socket)
                if isawaitable(r):
                    await r

            self._closed = False
            self._last_close_code = None

            self._socket = socket
            heartbeat_task = asyncio.create_task(self._heartbeat())

            try:
                await self.authenticate()

                message = await self.recv()
                if message['type'] != 'Authenticated':
                    raise AuthenticationError(message)  # type: ignore

                self._logged_out = False
                await self._handle(message)
                message = None
            except:
                heartbeat_task.cancel()
                raise
            else:
                heartbeat_task.cancel()
                heartbeat_task = asyncio.create_task(self._heartbeat())

            exc: typing.Optional[BaseException] = None
            while not self._closed:
                try:
                    if exc:
                        tmp = exc
                        exc = None
                        raise tmp
                    try:
                        message = await self.recv()
                    except (asyncio.CancelledError, KeyboardInterrupt):
                        raise Close
                except Close:
                    heartbeat_task.cancel()
                    await socket.close()
                    return
                except Reconnect:
                    await asyncio.sleep(1)
                    heartbeat_task.cancel()
                    _socket = self.socket
                    self._socket = None
                    try:
                        await _socket.close()
                    except Exception:
                        pass
                    break
                else:
                    r = self._handle(message)
                    if isawaitable(r):
                        r = await r
                    if not r:
                        if self.logged_out:
                            try:
                                await socket.close()
                            except Exception:  # Ignore close error
                                pass
                            return
                        exc = Reconnect()

            if not socket.closed:
                try:
                    await socket.close()
                except Exception as exc:
                    _L.warning('Failed to close websocket', exc_info=exc)
        self._last_close_code = None

    async def _handle(self, payload: raw.ClientEvent, /) -> bool:
        authenticated = True
        if payload['type'] == 'Pong':
            nonce = payload['data']
            if nonce != self._heartbeat_sequence:
                extra = ''
                if isinstance(nonce, int) and nonce < self._heartbeat_sequence:
                    extra = f'nonce is behind of {self._heartbeat_sequence - nonce} beats'
                if self.reconnect_on_timeout:
                    _L.error(
                        'Missed Pong, expected %s, got %s (%s)',
                        self._heartbeat_sequence,
                        nonce,
                        extra,
                    )
                else:
                    _L.warning(
                        'Missed Pong, expected %s, got %s (%s)',
                        self._heartbeat_sequence,
                        nonce,
                        extra,
                    )
                return not self.reconnect_on_timeout
            self._last_pong_at = utils.utcnow()
        elif payload['type'] == 'Logout':
            authenticated = False

        if self.handler is not None:
            r = self.handler.handle_raw(self, payload)
            if isawaitable(r):
                await r
            self._sequence += 1
        return authenticated


__all__ = (
    'Close',
    'Reconnect',
    'EventHandler',
    'DEFAULT_SHARD_USER_AGENT',
    'Shard',
    'ShardImpl',
)
