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

from attrs import define, field
import typing

from .cache import (
    CacheContextType,
    ChannelThroughReadStateChannelCacheContext,
    _CHANNEL_THROUGH_READ_STATE_CHANNEL,
)
from .core import (
    UNDEFINED,
    UndefinedOr,
    ULIDOr,
    resolve_id,
    ZID,
)
from .errors import NoData

if typing.TYPE_CHECKING:
    from . import raw
    from .channel import Channel
    from .http import HTTPOverrideParameters
    from .message import BaseMessage
    from .state import State


@define(slots=True)
class ReadState:
    """Represents the read state of a channel.

    .. note::
        An entity currently refers to message here. However this might change in future.
    """

    state: State = field(repr=False, kw_only=True)

    channel_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The channel's ID the read state for."""

    user_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID the read state belongs to."""

    last_acked_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The last acknowledged entity's ID. It *may* not point to an existing or valid entity."""

    mentioned_in: list[str] = field(repr=True, kw_only=True)
    """List[:class:`str`]: The message's IDs that mention the user."""

    def get_channel(self) -> typing.Optional[Channel]:
        """Optional[:class:`.Channel`]: The channel the read state belongs to."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelThroughReadStateChannelCacheContext(
                type=CacheContextType.channel_through_read_state_channel,
                read_state=self,
            )
            if state.provide_cache_context('ReadState.channel')
            else _CHANNEL_THROUGH_READ_STATE_CHANNEL
        )

        return cache.get_channel(self.channel_id, ctx)

    def __hash__(self) -> int:
        return hash((self.channel_id, self.user_id))

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, ReadState)
            and self.channel_id == other.channel_id
            and self.user_id == self.user_id
        )

    @property
    def channel(self) -> Channel:
        """:class:`.Channel`: The channel the read state belongs to."""
        channel = self.get_channel()
        if channel is None:
            raise NoData(what=self.channel_id, type='ReadState.channel')
        return channel

    async def edit(
        self,
        *,
        last_acked_id: UndefinedOr[typing.Optional[ULIDOr[BaseMessage]]] = UNDEFINED,
        http_overrides: typing.Optional[HTTPOverrideParameters] = None,
    ) -> ReadState:
        """|coro|

        Edits the read state.

        You must have :attr:`~Permissions.view_channel` to do this.

        Fires :class:`.MessageAckEvent` for the current user.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        last_acked_id: UndefinedOr[Optional[ULIDOr[:class:`.BaseMessage`]]]
            The new last acknowledged entity's ID.
        http_overrides: Optional[:class:`.HTTPOverrideParameters`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +-----------+-------------------------------------------+
            | Value     | Reason                                    |
            +-----------+-------------------------------------------+
            | ``IsBot`` | The current token belongs to bot account. |
            +-----------+-------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+-------------------------------------------------------------+
            | Value                 | Reason                                                      |
            +-----------------------+-------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to view the message. |
            +-----------------------+-------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+

        Returns
        -------
        :class:`.ReadState`
            The newly updated read state.
        """

        if last_acked_id is UNDEFINED:
            return self

        if last_acked_id is None:
            last_acked_id = ZID
        else:
            last_acked_id = resolve_id(last_acked_id)

        await self.state.http.acknowledge_message(self.channel_id, last_acked_id, http_overrides=http_overrides)
        read_state = ReadState(
            state=self.state,
            channel_id=self.channel_id,
            user_id=self.user_id,
            last_acked_id=None if last_acked_id == ZID else last_acked_id,
            mentioned_in=[m for m in self.mentioned_in if m >= last_acked_id],
        )
        return read_state

    def to_dict(self) -> raw.ChannelUnread:
        """:class:`dict`: Convert read state to raw data."""
        payload: raw.ChannelUnread = {
            '_id': {
                'channel': self.channel_id,
                'user': self.user_id,
            },
        }
        if self.last_acked_id is not None:
            payload['last_id'] = self.last_acked_id
        if len(self.mentioned_in):
            payload['mentions'] = self.mentioned_in
        return payload


__all__ = ('ReadState',)
