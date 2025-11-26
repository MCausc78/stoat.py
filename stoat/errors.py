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

if typing.TYPE_CHECKING:
    from .adapter import HTTPResponse


# Thanks Rapptz/discord.py for docs


class StoatException(Exception):
    """Base exception class for stoat.py

    Ideally speaking, this could be caught to handle any exceptions raised from this library.

    .. versionchanged:: 1.2

        Renamed from ``PyvoltException`` to ``StoatException``.

    .. deprecated:: 1.2

        The ``PyvoltException`` alias is a deprecated alias.
    """

    __slots__ = ()


PyvoltException = StoatException


class HTTPException(StoatException):
    """Exception that's raised when a HTTP request operation fails.

    This inherits from :class:`StoatException`.

    Attributes
    ----------
    response: :class:`.HTTPResponse`
        The response of the failed HTTP request.
    data: Union[Dict[:class:`str`, Any], Any]
        The data of the error. Could be an empty string.
    status: :class:`int`
        The status code of the HTTP request.
    type: :class:`str`
        The Stoat specific error type for the failure.
    retry_after: Optional[:class:`float`]
        The duration in seconds to wait until ratelimit expires.
    error: Optional[:class:`str`]
        The validation error details.
        Only applicable when :attr:`~.type` is ``'FailedValidation'``.
    max: Optional[:class:`int`]
        The maximum count of entities.
        Only applicable when :attr:`~.type` one of following values:

        - ``'FileTooLarge'``
        - ``'GroupTooLarge'``
        - ``'TooManyAttachments'``
        - ``'TooManyChannels'``
        - ``'TooManyEmbeds'``
        - ``'TooManyEmoji'``
        - ``'TooManyPendingFriendRequests'``
        - ``'TooManyReplies'``
        - ``'TooManyRoles'``
        - ``'TooManyServers'``
    permission: Optional[:class:`str`]
        The permission required to perform request.
        Only applicable when :attr:`~.type` one of following values:

        - ``'MissingPermission'``
        - ``'MissingUserPermission'``
    operation: Optional[:class:`str`]
        The database operation that failed.
        Only applicable when :attr:`~.type` is ``'DatabaseError'``.
    collection: Optional[:class:`str`]
        The collection's name the operation was on.
        Not always available when :attr:`~.type` is ``'DatabaseError'``.
    location: Optional[:class:`str`]
        The path to Rust location where error occured.
    with_: Optional[:class:`str`]
        The collection's name the operation was on.
        Only applicable when :attr:`~.type` one of following values:
        - ``'IncorrectData'``

        Not always available when :attr:`~.type` is ``'DatabaseError'``.
    feature: Optional[:class:`str`]
        The feature that was disabled.
        Only applicable when :attr:`~.type` is ``'FeatureDisabled'``.

        Possible values:

        - ``'features.mass_mentions_enabled'``
    """

    # response: HTTPResponse
    # type: str
    # retry_after: typing.Optional[float]
    # error: typing.Optional[str]
    # max: typing.Optional[int]
    # permission: typing.Optional[str]
    # operation: typing.Optional[str]
    # collection: typing.Optional[str]
    # location: typing.Optional[str]
    # with_: typing.Optional[str]

    __slots__ = (
        'response',
        'data',
        'type',
        'retry_after',
        'error',
        'max',
        'permission',
        'operation',
        'collection',
        'location',
        'with_',
        'feature',
    )

    def __init__(
        self,
        response: HTTPResponse,
        data: typing.Union[dict[str, typing.Any], str],
        /,
    ) -> None:
        self.response: HTTPResponse = response
        self.data: typing.Union[dict[str, typing.Any], str] = data
        self.status: int = response.status

        if isinstance(data, str):
            self.type: str = ''
            self.retry_after: typing.Optional[float] = None
            self.error: typing.Optional[str] = data
            self.max: typing.Optional[int] = None
            self.permission: typing.Optional[str] = None
            self.operation: typing.Optional[str] = None
            self.collection: typing.Optional[str] = None
            self.location: typing.Optional[str] = None
            self.with_: typing.Optional[str] = None
            self.feature: typing.Optional[str] = None
        else:
            self.type = data.get('type', 'Unknown')

            self.retry_after = data.get('retry_after', 0)
            self.error = data.get('error')
            self.max = data.get('max')
            self.permission = data.get('permission')
            self.operation = data.get('operation')
            self.collection = data.get('collection')
            self.location = data.get('location')
            self.with_ = data.get('with')
            self.feature = data.get('feature')

        super().__init__(f'{self.type} (raw={data})')


class NoEffect(StoatException):
    """HTTP exception that corresponds to HTTP 200 status code.

    This exists because Stoat API returns 200 with error body for some reason.

    This inherits from :class:`.StoatException`.
    """

    __slots__ = ('data',)

    def __init__(
        self,
        data: dict[str, typing.Any],
        /,
    ) -> None:
        self.data: dict[str, typing.Any] = data


class Unauthorized(HTTPException):
    """HTTP exception that corresponds to HTTP 401 status code.

    This inherits from :class:`.HTTPException`.
    """

    __slots__ = ()


class Forbidden(HTTPException):
    """HTTP exception that corresponds to HTTP 403 status code.

    This inherits from :class:`.HTTPException`.
    """

    __slots__ = ()


class NotFound(HTTPException):
    """HTTP exception that corresponds to HTTP 404 status code.

    This inherits from :class:`.HTTPException`.
    """

    __slots__ = ()


class Conflict(HTTPException):
    """HTTP exception that corresponds to HTTP 409 status code.

    This inherits from :class:`.HTTPException`.
    """

    __slots__ = ()


class Ratelimited(HTTPException):
    """HTTP exception that corresponds to HTTP 429 status code.

    This inherits from :class:`.HTTPException`.
    """

    __slots__ = ()


class InternalServerError(HTTPException):
    """HTTP exception that corresponds to HTTP 5xx status code.

    This inherits from :class:`.HTTPException`.
    """

    __slots__ = ()


class BadGateway(HTTPException):
    """HTTP exception that corresponds to HTTP 502 status code.

    This inherits from :class:`.HTTPException`.
    """

    __slots__ = ()


class ShardError(StoatException):
    """Exception that's raised when any shard-related
    error happens.

    This inherits from :class:`StoatException`.
    """

    __slots__ = ()


class ShardClosedError(ShardError):
    """Exception that's raised when shard
    was already closed.

    This inherits from :class:`ShardError`.
    """

    __slots__ = ()


class AuthenticationError(ShardError):
    """Exception that's raised when WebSocket
    authentication fails.

    This inherits from :class:`ShardError`.

    Attributes
    ----------
    payload: Optional[Dict[:class:`str`, Any]]
        The WebSocket payload.
    """

    __slots__ = ()

    def __init__(self, payload: dict[str, typing.Any], /) -> None:
        self.payload: dict[str, typing.Any] = payload
        super().__init__(f'Failed to connect shard: {payload}')


class ConnectError(ShardError):
    """Exception that's raised when the library fails
    to connect to Stoat WebSocket.

    This inherits from :class:`ShardError`.

    Attributes
    ----------
    errors: List[:exc:`Exception`]
        The errors.
    """

    __slots__ = ('errors',)

    def __init__(self, tries: int, errors: list[Exception], /) -> None:
        self.errors: list[Exception] = errors
        super().__init__(f'Giving up, after {tries} tries, last 3 errors: {errors[-3:]}')


class DiscoverError(StoatException):
    """Exception that's raised when a HTTP request operation fails.

    This inherits from :class:`StoatException`.

    Attributes
    ----------
    response: :class:`.HTTPResponse`
        The response of the failed HTTP request.
    data: Union[Dict[:class:`str`, Any], Any]
        The data of the error. Could be an empty string.
    status: :class:`int`
        The status code of the HTTP request.
    """

    __slots__ = ('response', 'status', 'data')

    def __init__(
        self,
        response: HTTPResponse,
        status: int,
        data: str,
        /,
    ) -> None:
        self.response: HTTPResponse = response
        self.status: int = status
        self.data: str = data
        super().__init__(status, data)


class InvalidData(StoatException):
    """Exception that's raised when the library encounters unknown
    or invalid data from Stoat.

    This inherits from :class:`StoatException`.
    """

    __slots__ = ('reason',)

    def __init__(self, reason: str, /) -> None:
        self.reason: str = reason
        super().__init__(reason)


class NoData(StoatException):
    """Exception that's raised when the library did not found
    data requested from cache.

    This is different from :exc:`NotFound`, and inherits from :class:`StoatException`.
    """

    __slots__ = ('what', 'type')

    def __init__(self, what: str, type: str) -> None:
        self.what = what
        self.type = type
        super().__init__(f'Unable to find {type} {what} in cache')


__all__ = (
    'StoatException',
    'PyvoltException',
    'HTTPException',
    'NoEffect',
    'Unauthorized',
    'Forbidden',
    'NotFound',
    'Conflict',
    'Ratelimited',
    'InternalServerError',
    'BadGateway',
    'ShardError',
    'ShardClosedError',
    'AuthenticationError',
    'ConnectError',
    'DiscoverError',
    'InvalidData',
    'NoData',
)
