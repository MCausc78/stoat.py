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

from datetime import datetime
import typing

from attrs import define, field

from .base import Base
from .cache import (
    CacheContextType,
    UserThroughUserAddedSystemEventUserCacheContext,
    UserThroughUserAddedSystemEventAuthorCacheContext,
    UserThroughUserRemovedSystemEventUserCacheContext,
    UserThroughUserRemovedSystemEventAuthorCacheContext,
    MemberOrUserThroughUserJoinedSystemEventUserCacheContext,
    MemberThroughUserJoinedSystemEventUserCacheContext,
    UserThroughUserJoinedSystemEventUserCacheContext,
    MemberOrUserThroughUserLeftSystemEventUserCacheContext,
    MemberThroughUserLeftSystemEventUserCacheContext,
    UserThroughUserLeftSystemEventUserCacheContext,
    MemberOrUserThroughUserKickedSystemEventUserCacheContext,
    MemberThroughUserKickedSystemEventUserCacheContext,
    UserThroughUserKickedSystemEventUserCacheContext,
    MemberOrUserThroughUserBannedSystemEventUserCacheContext,
    MemberThroughUserBannedSystemEventUserCacheContext,
    UserThroughUserBannedSystemEventUserCacheContext,
    UserThroughChannelRenamedSystemEventAuthorCacheContext,
    UserThroughChannelDescriptionChangedSystemEventAuthorCacheContext,
    UserThroughChannelIconChangedSystemEventAuthorCacheContext,
    UserThroughChannelOwnershipChangedSystemEventFromCacheContext,
    UserThroughChannelOwnershipChangedSystemEventToCacheContext,
    MessageThroughMessagePinnedSystemEventPinnedMessageCacheContext,
    MemberOrUserThroughMessagePinnedSystemEventAuthorCacheContext,
    MemberThroughMessagePinnedSystemEventAuthorCacheContext,
    UserThroughMessagePinnedSystemEventAuthorCacheContext,
    MessageThroughMessageUnpinnedSystemEventUnpinnedMessageCacheContext,
    MemberOrUserThroughMessageUnpinnedSystemEventAuthorCacheContext,
    MemberThroughMessageUnpinnedSystemEventAuthorCacheContext,
    UserThroughMessageUnpinnedSystemEventAuthorCacheContext,
    UserThroughCallStartedSystemEventAuthorCacheContext,
    ChannelThroughMessageChannelCacheContext,
    ServerThroughMessageServerCacheContext,
    MemberOrUserThroughMessageAuthorCacheContext,
    MemberThroughMessageAuthorCacheContext,
    UserThroughMessageAuthorCacheContext,
    MemberOrUsersThroughMessageMentionsCacheContext,
    MembersThroughMessageMentionsCacheContext,
    UsersThroughMessageMentionsCacheContext,
    RoleThroughMessageRoleMentionsCacheContext,
    _USER_THROUGH_USER_ADDED_SYSTEM_EVENT_USER,
    _USER_THROUGH_USER_ADDED_SYSTEM_EVENT_BY,
    _USER_THROUGH_USER_REMOVED_SYSTEM_EVENT_USER,
    _USER_THROUGH_USER_REMOVED_SYSTEM_EVENT_BY,
    _MEMBER_OR_USER_THROUGH_USER_JOINED_SYSTEM_EVENT_USER,
    _MEMBER_THROUGH_USER_JOINED_SYSTEM_EVENT_USER,
    _USER_THROUGH_USER_JOINED_SYSTEM_EVENT_USER,
    _MEMBER_OR_USER_THROUGH_USER_LEFT_SYSTEM_EVENT_USER,
    _MEMBER_THROUGH_USER_LEFT_SYSTEM_EVENT_USER,
    _USER_THROUGH_USER_LEFT_SYSTEM_EVENT_USER,
    _MEMBER_OR_USER_THROUGH_USER_KICKED_SYSTEM_EVENT_USER,
    _MEMBER_THROUGH_USER_KICKED_SYSTEM_EVENT_USER,
    _USER_THROUGH_USER_KICKED_SYSTEM_EVENT_USER,
    _MEMBER_OR_USER_THROUGH_USER_BANNED_SYSTEM_EVENT_USER,
    _MEMBER_THROUGH_USER_BANNED_SYSTEM_EVENT_USER,
    _USER_THROUGH_USER_BANNED_SYSTEM_EVENT_USER,
    _USER_THROUGH_CHANNEL_RENAMED_SYSTEM_EVENT_BY,
    _USER_THROUGH_CHANNEL_DESCRIPTION_CHANGED_SYSTEM_EVENT_BY,
    _USER_THROUGH_CHANNEL_ICON_CHANGED_SYSTEM_EVENT_BY,
    _USER_THROUGH_CHANNEL_OWNERSHIP_CHANGED_SYSTEM_EVENT_FROM,
    _USER_THROUGH_CHANNEL_OWNERSHIP_CHANGED_SYSTEM_EVENT_TO,
    _MESSAGE_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_PINNED_MESSAGE,
    _MEMBER_OR_USER_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_BY,
    _MEMBER_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_BY,
    _USER_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_BY,
    _MESSAGE_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_UNPINNED_MESSAGE,
    _MEMBER_OR_USER_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_BY,
    _MEMBER_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_BY,
    _USER_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_BY,
    _USER_THROUGH_CALL_STARTED_SYSTEM_EVENT_BY,
    _CHANNEL_THROUGH_MESSAGE_CHANNEL,
    _SERVER_THROUGH_MESSAGE_SERVER,
    _MEMBER_OR_USER_THROUGH_MESSAGE_AUTHOR,
    _MEMBER_THROUGH_MESSAGE_AUTHOR,
    _USER_THROUGH_MESSAGE_AUTHOR,
    _MEMBER_OR_USERS_THROUGH_MESSAGE_MENTIONS,
    _MEMBERS_THROUGH_MESSAGE_MENTIONS,
    _USERS_THROUGH_MESSAGE_MENTIONS,
    _ROLE_THROUGH_MESSAGE_ROLE_MENTIONS,
)
from .channel import BaseServerChannel, TextableChannel, PartialMessageable
from .cdn import AssetMetadata, StatelessAsset, Asset, ResolvableResource, resolve_resource
from .context_managers import Editing
from .core import (
    UNDEFINED,
    UndefinedOr,
    ULIDOr,
    resolve_id,
    ZID,
)
from .emoji import ResolvableEmoji
from .enums import AssetMetadataType, ContentReportReason, RelationshipStatus
from .errors import NoData
from .flags import MessageFlags
from .server import Member
from .user import BaseUser, User

if typing.TYPE_CHECKING:
    from . import raw
    from .embed import StatelessEmbed, Embed
    from .http import HTTPOverrideOptions
    from .server import Role, Server
    from .state import State

_new_message_flags = MessageFlags.__new__


class Reply:
    """Represents a message reply.

    Attributes
    ----------
    id: :class:`str`
        The ID of the message that being replied to.
    mention: :class:`bool`
        Whether to mention author of referenced message or not.
    fail_if_not_exists: Optional[:class:`bool`]
        Whether the HTTP request should fail with an error, if message does not exist. Defaults to ``True``.
    """

    __slots__ = (
        'id',
        'mention',
        'fail_if_not_exists',
    )

    def __init__(
        self, id: ULIDOr[BaseMessage], mention: bool = False, *, fail_if_not_exists: typing.Optional[bool] = None
    ) -> None:
        self.id: str = resolve_id(id)
        self.mention: bool = mention
        self.fail_if_not_exists: typing.Optional[bool] = fail_if_not_exists

    def to_dict(self) -> raw.ReplyIntent:
        """:class:`dict`: Convert reply to raw data."""
        payload: raw.ReplyIntent = {
            'id': self.id,
            'mention': self.mention,
        }
        if self.fail_if_not_exists is not None:
            payload['fail_if_not_exists'] = self.fail_if_not_exists
        return payload


class MessageInteractions:
    """Represents information how to guide interactions on the message.

    Attributes
    ----------
    reactions: List[:class:`str`]
        The reactions which should always appear and be distinct. Must be either emoji ID, or an unicode emoji.
    restrict_reactions: :class:`bool`
        Whether reactions should be restricted to the given list.

        Can only be set to ``True`` if :attr:`.reactions` has at least 1 emoji. Defaults to ``False``.
    """

    __slots__ = ('reactions', 'restrict_reactions')

    def __init__(self, reactions: list[str], restrict_reactions: bool = False) -> None:
        self.reactions: list[str] = reactions
        self.restrict_reactions: bool = restrict_reactions

    def to_dict(self) -> raw.Interactions:
        """:class:`dict`: Convert interactions information to raw data."""
        return {
            'reactions': self.reactions,
            'restrict_reactions': self.restrict_reactions,
        }


class MessageMasquerade:
    """Represents overrides of name and/or avatar on message.

    Attributes
    ----------
    name: Optional[:class:`str`]
        The name to replace the display name on message with. Must be between 1 and 32 characters long.
    avatar: Optional[:class:`str`]
        The image URL to replace the displayed avatar on message with.
    color: Optional[:class:`str`]
        The CSS color to replace display role color shown on message.
        This must be valid `CSS color <https://developer.mozilla.org/en-US/docs/Web/CSS/color_value>`_.

        You (or webhook) must have :attr:`~Permissions.manage_roles` permission to set this attribute.
    """

    __slots__ = ('name', 'avatar', 'color')

    def __init__(
        self,
        name: typing.Optional[str] = None,
        avatar: typing.Optional[str] = None,
        *,
        color: typing.Optional[str] = None,
    ) -> None:
        self.name: typing.Optional[str] = name
        self.avatar: typing.Optional[str] = avatar
        self.color: typing.Optional[str] = color

    def to_dict(self) -> raw.Masquerade:
        """:class:`dict`: Convert masquerade to raw data."""
        payload: raw.Masquerade = {}
        if self.name is not None:
            payload['name'] = self.name
        if self.avatar is not None:
            payload['avatar'] = self.avatar
        if self.color is not None:
            payload['colour'] = self.color
        return payload


class SendableEmbed:
    """Represents a text embed before it is sent.

    Attributes
    ----------
    icon_url: Optional[:class:`str`]
        The embed icon URL.
    url: Optional[:class:`str`]
        The embed URL.
    title: Optional[:class:`str`]
        The embed's title.
    description: Optional[:class:`str`]
        The embed's description.
    media: Optional[:class:`ResolvableResource`]
        The file inside the embed.
    color: Optional[:class:`str`]
        The embed color. This must be valid `CSS color <https://developer.mozilla.org/en-US/docs/Web/CSS/color_value>`_.
    """

    __slots__ = ('icon_url', 'url', 'title', 'description', 'media', 'color')

    def __init__(
        self,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        *,
        icon_url: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        media: typing.Optional[ResolvableResource] = None,
        color: typing.Optional[str] = None,
    ) -> None:
        self.icon_url: typing.Optional[str] = icon_url
        self.url: typing.Optional[str] = url
        self.title: typing.Optional[str] = title
        self.description: typing.Optional[str] = description
        self.media: typing.Optional[ResolvableResource] = media
        self.color: typing.Optional[str] = color

    async def to_dict(self, state: State, /) -> raw.SendableEmbed:
        """Convert sendable embed to raw data.

        Parameters
        ----------
        state: :class:`State`
            The state. Required to resolve :attr:`~.media` attribute into file ID.

        Returns
        -------
        :class:`dict`
            The raw data.
        """
        payload: raw.SendableEmbed = {}
        if self.icon_url is not None:
            payload['icon_url'] = self.icon_url
        if self.url is not None:
            payload['url'] = self.url
        if self.title is not None:
            payload['title'] = self.title
        if self.description is not None:
            payload['description'] = self.description
        if self.media is not None:
            payload['media'] = await resolve_resource(state, self.media, tag='attachments')
        if self.color is not None:
            payload['colour'] = self.color
        return payload


@define(slots=True)
class MessageWebhook:
    """Specifies information about the webhook bundled with :class:`~stoat.Message`."""

    name: str = field(repr=True, kw_only=True)
    """:class:`str`: The webhook's name. Can be between 1 to 32 characters."""

    avatar: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The webhook avatar's ID, if any."""

    def to_dict(self) -> raw.MessageWebhook:
        """:class:`dict`: Convert message webhook to raw data."""
        return {
            'name': self.name,
            'avatar': self.avatar,
        }


@define(slots=True)
class BaseMessage(Base):
    """Represents a message in channel on Stoat.

    This inherits from :class:`Base`.
    """

    channel_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The channel's ID this message was sent in."""

    def get_channel(self) -> typing.Optional[TextableChannel]:
        """Optional[:class:`TextableChannel`]: The channel this message was sent in."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelThroughMessageChannelCacheContext(
                type=CacheContextType.channel_through_message_channel,
                message=self,
            )
            if state.provide_cache_context('Message.channel')
            else _CHANNEL_THROUGH_MESSAGE_CHANNEL
        )

        channel = cache.get_channel(self.channel_id, ctx)
        if channel is None:
            return None

        assert isinstance(channel, TextableChannel)
        return channel

    def get_server(self) -> tuple[typing.Optional[Server], str]:
        """Returns the server this message was sent in.

        Returns
        -------
        Tuple[Optional[:class:`Server`], :class:`str`]
            The server and server ID (may be empty).
        """
        state = self.state
        cache = state.cache

        if cache is None:
            return (None, '')

        ctx = (
            ServerThroughMessageServerCacheContext(
                type=CacheContextType.server_through_message_server,
                message=self,
            )
            if state.provide_cache_context('Message.server')
            else _SERVER_THROUGH_MESSAGE_SERVER
        )

        channel = cache.get_channel(self.channel_id, ctx)
        if channel is None:
            return (None, '')

        if isinstance(channel, BaseServerChannel):
            server_id = channel.server_id

            return cache.get_server(server_id, ctx), server_id

        return (None, '')

    def __hash__(self) -> int:
        return hash((self.channel_id, self.id))

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, BaseMessage)
            and self.channel_id == other.channel_id
            and self.id == other.id
        )

    @property
    def channel(self) -> typing.Union[TextableChannel, PartialMessageable]:
        """Union[:class:`TextableChannel`, :class:`PartialMessageable`]: The channel this message was sent in."""
        channel = self.get_channel()

        if channel is None:
            return PartialMessageable(state=self.state, id=self.channel_id)

        return channel

    @property
    def server(self) -> typing.Optional[Server]:
        """Optional[:class:`Server`]: The server this message was sent in."""
        server, server_id = self.get_server()
        if server is None and len(server_id):
            raise NoData(
                what=server_id,
                type='Message.server',
            )
        return server

    async def ack(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Marks this message as read.

        This is an alias for :meth:`~.acknowledge`.

        You must have :attr:`~Permissions.view_channel` to do this.

        Fires :class:`MessageAckEvent` for the current user.

        .. note::
            This can only be used by non-bot accounts.

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
        """
        return await self.acknowledge(http_overrides=http_overrides)

    async def acknowledge(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Marks this message as read.

        You must have :attr:`~Permissions.view_channel` to do this.

        There is an alias for this called :meth:`~.ack`.

        Fires :class:`MessageAckEvent` for the current user.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
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
        """
        return await self.state.http.acknowledge_message(self.channel_id, self.id, http_overrides=http_overrides)

    async def clear_reactions(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Removes all the reactions from the message.

        You must have :attr:`~Permissions.manage_messages` to do this.

        Fires :class:`MessageUpdateEvent` with empty :attr:`~PartialMessage.reactions` for all users who can see target channel.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+---------------------------------------------------------------------+
            | Value                 | Reason                                                              |
            +-----------------------+---------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to remove all the reactions. |
            +-----------------------+---------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------------------+
            | Value        | Reason                                |
            +--------------+---------------------------------------+
            | ``NotFound`` | The channel or message was not found. |
            +--------------+---------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """
        return await self.state.http.clear_reactions(self.channel_id, self.id, http_overrides=http_overrides)

    async def delete(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Deletes the message in a channel.

        You must have :attr:`~Permissions.manage_messages` to do this if message is not yours.

        Fires :class:`MessageDeleteEvent` for all users who can see target channel.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+---------------------------------------------------------------+
            | Value                 | Reason                                                        |
            +-----------------------+---------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to delete the message. |
            +-----------------------+---------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------------------+
            | Value        | Reason                                |
            +--------------+---------------------------------------+
            | ``NotFound`` | The channel or message was not found. |
            +--------------+---------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """
        return await self.state.http.delete_message(self.channel_id, self.id, http_overrides=http_overrides)

    async def edit(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        content: UndefinedOr[str] = UNDEFINED,
        embeds: UndefinedOr[list[SendableEmbed]] = UNDEFINED,
    ) -> Message:
        """|coro|

        Edits the message.

        Fires :class:`MessageUpdateEvent` and optionally :class:`MessageAppendEvent`, both for all users who can see target channel.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        content: UndefinedOr[:class:`str`]
            The new content to replace the message with. Must be between 1 and 2000 characters long.
        embeds: UndefinedOr[List[:class:`SendableEmbed`]]
            The new embeds to replace the original with. Must be a maximum of 10. To remove all embeds ``[]`` should be passed.

            You must have :attr:`~Permissions.send_embeds` to provide this.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+----------------------------+
            | Value                  | Reason                     |
            +------------------------+----------------------------+
            | ``FailedValidation``   | The payload was invalid.   |
            +------------------------+----------------------------+
            | ``PayloadTooLarge``    | The message was too large. |
            +------------------------+----------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+----------------------------------------------------------+
            | Value                 | Reason                                                   |
            +-----------------------+----------------------------------------------------------+
            | ``CannotEditMessage`` | The message you tried to edit isn't yours.               |
            +-----------------------+----------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to send messages. |
            +-----------------------+----------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-----------------------------------------+
            | Value        | Reason                                  |
            +--------------+-----------------------------------------+
            | ``NotFound`` | The channel/message/file was not found. |
            +--------------+-----------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Message`
            The newly edited message.
        """

        return await self.state.http.edit_message(
            self.channel_id, self.id, http_overrides=http_overrides, content=content, embeds=embeds
        )

    def editing(self) -> Editing:
        """:class:`Editing`: Returns an asynchronous context manager that allows you to send an editing indicator for a message in channel for an indefinite period of time."""

        return Editing(
            channel_id=self.channel_id,
            message_id=self.id,
            shard=self.state.shard,
        )

    async def fetch(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> Message:
        """|coro|

        Retrieves the message.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+-------------------------------------------------------------+
            | Value                 | Reason                                                      |
            +-----------------------+-------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to view the channel. |
            +-----------------------+-------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+------------------------------------+
            | Value        | Reason                             |
            +--------------+------------------------------------+
            | ``NotFound`` | The channel/message was not found. |
            +--------------+------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Message`
            The retrieved message.
        """
        return await self.state.http.get_message(self.channel_id, self.id, http_overrides=http_overrides)

    async def pin(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Pins the message.

        You must have :attr:`~Permissions.manage_messages` to do this, unless the channel is :class:`DMChannel`.

        Fires :class:`MessageUpdateEvent` and :class:`MessageCreateEvent`, both for all users who can see target channel.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+---------------------------------+
            | Value             | Reason                          |
            +-------------------+---------------------------------+
            | ``AlreadyPinned`` | The message was already pinned. |
            +-------------------+---------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+------------------------------------------------------------+
            | Value                 | Reason                                                     |
            +-----------------------+------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to pin the message. |
            +-----------------------+------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+------------------------------------+
            | Value        | Reason                             |
            +--------------+------------------------------------+
            | ``NotFound`` | The channel/message was not found. |
            +--------------+------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """
        return await self.state.http.pin_message(self.channel_id, self.id, http_overrides=http_overrides)

    async def react(
        self,
        emoji: ResolvableEmoji,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> None:
        """|coro|

        React to this message.

        You must have :attr:`~Permissions.react` to do this.

        Fires :class:`MessageReactEvent` for all users who can see target channel.

        Parameters
        ----------
        emoji: :class:`ResolvableEmoji`
            The emoji to react with.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+---------------------------------------------------------------------------------------------------------------+
            | Value                | Reason                                                                                                        |
            +----------------------+---------------------------------------------------------------------------------------------------------------+
            | ``InvalidOperation`` | One of these:                                                                                                 |
            |                      |                                                                                                               |
            |                      | - The message has too many reactions.                                                                         |
            |                      | - If :attr:`MessageInteractions.restrict_reactions` is ``True``, then the emoji provided was not whitelisted. |
            |                      | - The provided emoji was invalid.                                                                             |
            +----------------------+---------------------------------------------------------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+--------------------------------------------------+
            | Value                 | Reason                                           |
            +-----------------------+--------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to react. |
            +-----------------------+--------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------------------------------+
            | Value        | Reason                                          |
            +--------------+-------------------------------------------------+
            | ``NotFound`` | The channel/message/custom emoji was not found. |
            +--------------+-------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.add_reaction_to_message(
            self.channel_id, self.id, emoji, http_overrides=http_overrides
        )

    async def reply(
        self,
        content: typing.Optional[str] = None,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        nonce: typing.Optional[str] = None,
        attachments: typing.Optional[list[ResolvableResource]] = None,
        embeds: typing.Optional[list[SendableEmbed]] = None,
        masquerade: typing.Optional[MessageMasquerade] = None,
        interactions: typing.Optional[MessageInteractions] = None,
        silent: typing.Optional[bool] = None,
        mention_everyone: typing.Optional[bool] = None,
        mention_online: typing.Optional[bool] = None,
        mention: bool = True,
    ) -> Message:
        """|coro|

        Replies to this message.

        You must have :attr:`~Permissions.send_messages` to do this.

        If message mentions "\\@everyone" or "\\@online", you must have :attr:`~Permissions.mention_everyone` to do that.

        If message mentions any roles, you must :attr:`~Permission.mention_roles` to do that.

        Fires :class:`MessageCreateEvent` and optionally :class:`MessageAppendEvent`, both for all users who can see target channel.

        Parameters
        ----------
        content: Optional[:class:`str`]
            The message content.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        nonce: Optional[:class:`str`]
            The message nonce.
        attachments: Optional[List[:class:`ResolvableResource`]]
            The attachments to send the message with.

            You must have :attr:`~Permissions.upload_files` to provide this.
        replies: Optional[List[Union[:class:`Reply`, ULIDOr[:class:`BaseMessage`]]]]
            The message replies.
        embeds: Optional[List[:class:`SendableEmbed`]]
            The embeds to send the message with.

            You must have :attr:`~Permissions.send_embeds` to provide this.
        masquearde: Optional[:class:`MessageMasquerade`]
            The message masquerade.

            You must have :attr:`~Permissions.use_masquerade` to provide this.

            If :attr:`.MessageMasquerade.color` is provided, :attr:`~Permissions.manage_roles` is also required.
        interactions: Optional[:class:`MessageInteractions`]
            The message interactions.

            If :attr:`.MessageInteractions.reactions` is provided, :attr:`~Permissions.react` is required.
        silent: Optional[:class:`bool`]
            Whether to suppress notifications or not.
        mention_everyone: Optional[:class:`bool`]
            Whether to mention all users who can see the channel. This cannot be mixed with ``mention_online`` parameter.

            .. note::

                User accounts cannot set this to ``True``.
        mention_online: Optional[:class:`bool`]
            Whether to mention all users who are online and can see the channel. This cannot be mixed with ``mention_everyone`` parameter.

            .. note::

                User accounts cannot set this to ``True``.
        mention: :class:`bool`
            Whether to mention author of message you're replying to.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | Value                  | Reason                                                                                                             |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``EmptyMessage``       | The message was empty.                                                                                             |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``FailedValidation``   | The payload was invalid.                                                                                           |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``InvalidFlagValue``   | Both ``mention_everyone`` and ``mention_online`` were ``True``.                                                    |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``InvalidOperation``   | The passed nonce was already used. One of :attr:`.MessageInteractions.reactions` elements was invalid.             |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``InvalidProperty``    | :attr:`.MessageInteractions.restrict_reactions` was ``True`` but :attr:`.MessageInteractions.reactions` was empty. |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``IsBot``              | The current token belongs to bot account.                                                                          |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``IsNotBot``           | The current token belongs to user account.                                                                         |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``PayloadTooLarge``    | The message was too large.                                                                                         |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``TooManyAttachments`` | You provided more attachments than allowed on this instance.                                                       |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``TooManyEmbeds``      | You provided more embeds than allowed on this instance.                                                            |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
            | ``TooManyReplies``     | You were replying to more messages than was allowed on this instance.                                              |
            +------------------------+--------------------------------------------------------------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+----------------------------------------------------------+
            | Value                 | Reason                                                   |
            +-----------------------+----------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to send messages. |
            +-----------------------+----------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------------------+
            | Value        | Reason                                |
            +--------------+---------------------------------------+
            | ``NotFound`` | The channel/file/reply was not found. |
            +--------------+---------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+-------------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                                | Populated attributes                                                |
            +-------------------+-------------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database.        | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+-------------------------------------------------------+---------------------------------------------------------------------+
            | ``InternalError`` | Somehow something went wrong during message creation. |                                                                     |
            +-------------------+-------------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Message`
            The message that was sent.
        """
        return await self.state.http.send_message(
            self.channel_id,
            content=content,
            http_overrides=http_overrides,
            nonce=nonce,
            attachments=attachments,
            replies=[Reply(self.id, mention=mention)],
            embeds=embeds,
            masquerade=masquerade,
            interactions=interactions,
            silent=silent,
            mention_everyone=mention_everyone,
            mention_online=mention_online,
        )

    async def report(
        self,
        reason: ContentReportReason,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        additional_context: typing.Optional[str] = None,
    ) -> None:
        """|coro|

        Report the message to the instance moderation team.

        Fires :class:`ReportCreateEvent` internally (but not fired over WebSocket).

        Internally, 15 messages around provided message will be snapshotted for context. All attachments of provided message are snapshotted as well.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        reason: :class:`ContentReportReason`
            The reason for reporting.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        additional_context: Optional[:class:`str`]
            The additional context for moderation team. Can be only up to 1000 characters.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------------+---------------------------------------+
            | Value                    | Reason                                |
            +--------------------------+---------------------------------------+
            | ``CannotReportYourself`` | You tried to report your own message. |
            +--------------------------+---------------------------------------+
            | ``FailedValidation``     | The payload was invalid.              |
            +--------------------------+---------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The message was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.report_message(
            self.id, reason, http_overrides=http_overrides, additional_context=additional_context
        )

    async def unpin(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Unpins the message.

        You must have :attr:`~Permissions.manage_messages` to do this, unless the channel is :class:`DMChannel`.

        Fires :class:`MessageUpdateEvent` and :class:`MessageCreateEvent`, both for all users who can see target channel.

        Parameters
        ----------
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +---------------+-----------------------------+
            | Value         | Reason                      |
            +---------------+-----------------------------+
            | ``NotPinned`` | The message was not pinned. |
            +---------------+-----------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+--------------------------------------------------------------+
            | Value                 | Reason                                                       |
            +-----------------------+--------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to unpin the message. |
            +-----------------------+--------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+------------------------------------+
            | Value        | Reason                             |
            +--------------+------------------------------------+
            | ``NotFound`` | The channel/message was not found. |
            +--------------+------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.unpin_message(self.channel_id, self.id, http_overrides=http_overrides)

    async def unreact(
        self,
        emoji: ResolvableEmoji,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        user: typing.Optional[ULIDOr[BaseUser]] = None,
        remove_all: typing.Optional[bool] = None,
    ) -> None:
        """|coro|

        Remove your own, someone else's or all of a given reaction.

        You must have :attr:`~Permissions.react` to do this.

        Fires :class:`MessageClearReactionEvent` if ``remove_all`` is ``True`` or :class:`MessageUnreactEvent`, for all users
        who can see target channel.

        Parameters
        ----------
        emoji: :class:`ResolvableEmoji`
            The emoji to remove.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.
        user: Optional[ULIDOr[:class:`BaseUser`]]
            The user to remove reactions from.

            You must have :attr:`~Permissions.manage_messages` to provide this.
        remove_all: Optional[:class:`bool`]
            Whether to remove all reactions.

            You must have :attr:`~Permissions.manage_messages` to provide this.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+------------------------------------------------------------+
            | Value                 | Reason                                                     |
            +-----------------------+------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to remove reaction. |
            +-----------------------+------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+------------------------------------+
            | Value        | Reason                             |
            +--------------+------------------------------------+
            | ``NotFound`` | One of these:                      |
            |              |                                    |
            |              | - The channel was not found.       |
            |              | - The message was not found.       |
            |              | - The user provided did not react. |
            +--------------+------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.remove_reactions_from_message(
            self.channel_id, self.id, emoji, http_overrides=http_overrides, user=user, remove_all=remove_all
        )


@define(slots=True)
class PartialMessage(BaseMessage):
    """Represents partial message in channel on Stoat.

    This inherits from :class:`BaseMessage`.
    """

    content: UndefinedOr[str] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`str`]: The new message's content."""

    edited_at: UndefinedOr[datetime] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`~datetime.datetime`]: When the message was edited."""

    internal_embeds: UndefinedOr[list[StatelessEmbed]] = field(repr=True, kw_only=True)
    """UndefinedOr[List[:class:`StatelessEmbed`]]: The new message embeds."""

    pinned: UndefinedOr[bool] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`bool`]: Whether the message was just pinned."""

    reactions: UndefinedOr[dict[str, tuple[str, ...]]] = field(repr=True, kw_only=True)
    """UndefinedOr[Dict[:class:`str`, Tuple[:class:`str`, ...]]]: The new message's reactions."""

    @property
    def embeds(self) -> UndefinedOr[list[Embed]]:
        """UndefinedOr[List[:class:`Embed`]]: The new message embeds."""
        return (
            UNDEFINED
            if self.internal_embeds is UNDEFINED
            else [e.attach_state(self.state) for e in self.internal_embeds]
        )


@define(slots=True)
class MessageAppendData(BaseMessage):
    """Appended data to message in channel on Stoat.

    This inherits from :class:`BaseMessage`.
    """

    internal_embeds: UndefinedOr[list[StatelessEmbed]] = field(repr=True, kw_only=True)
    """UndefinedOr[List[:class:`StatelessEmbed`]]: The stateless embeds that were appended."""

    @property
    def embeds(self) -> UndefinedOr[list[Embed]]:
        """UndefinedOr[List[:class:`Embed`]]: The embeds that were appended."""
        return (
            UNDEFINED
            if self.internal_embeds is UNDEFINED
            else [e.attach_state(self.state) for e in self.internal_embeds]
        )


class BaseSystemEvent:
    """Represents system event within message."""

    __slots__ = ()


@define(slots=True, eq=True)
class TextSystemEvent(BaseSystemEvent):
    """A simple text system message.

    This inherits from :class:`BaseSystemEvent`.
    """

    content: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The event contents."""

    def attach_state(self, message: Message, /) -> TextSystemEvent:
        """:class:`TextSystemEvent` Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return self

    def to_dict(self) -> raw.TextSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'text',
            'content': self.content,
        }

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""
        return self.content


@define(slots=True)
class StatelessUserAddedSystemEvent(BaseSystemEvent):
    """An user was added to a group.

    This inherits from :class:`BaseSystemEvent`.
    """

    internal_user: typing.Union[User, str] = field(repr=False, kw_only=True)
    """Union[:class:`User`, :class:`str`]: The ID of the user that was added, or full user instance."""

    internal_by: typing.Union[User, str] = field(repr=False, kw_only=True)
    """Union[:class:`User`, :class:`str`]: The ID of the user that added this user, or full user instance."""

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that added this user."""
        if isinstance(self.internal_by, User):
            return self.internal_by
        return None

    def get_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was added."""
        if isinstance(self.internal_user, User):
            return self.internal_user
        return None

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, StatelessUserAddedSystemEvent)
            and self.user_id == other.user_id
            and self.by_id == other.by_id
        )

    @property
    def by(self) -> User:
        """:class:`User`: The user that added this user."""
        user = self.get_by()
        if user is None:
            raise NoData(
                what=self.by_id,
                type='StatelessUserAddedSystemEvent.by',
            )
        return user

    @property
    def by_id(self) -> str:
        """:class:`str`: The user's ID that added this user."""
        if isinstance(self.internal_by, User):
            return self.internal_by.id
        return self.internal_by

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        user = self.get_user()
        if user is None:
            user = '<Unknown User>'

        by = self.get_by()
        if by is None:
            by = '<Unknown User>'

        return f'{user} was added by {by}'

    @property
    def user(self) -> User:
        """:class:`User`: The user that was added."""
        user = self.get_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='StatelessUserAddedSystemEvent.user',
            )
        return user

    @property
    def user_id(self) -> str:
        """:class:`str`: The user's ID that was added."""
        if isinstance(self.internal_user, User):
            return self.internal_user.id
        return self.internal_user

    def attach_state(self, message: Message, /) -> UserAddedSystemEvent:
        """:class:`UserAddedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return UserAddedSystemEvent(
            message=message,
            internal_user=self.internal_user,
            internal_by=self.internal_by,
        )

    def to_dict(self) -> raw.UserAddedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'user_added',
            'by': self.by_id,
            'id': self.user_id,
        }


@define(slots=True)
class UserAddedSystemEvent(StatelessUserAddedSystemEvent):
    """An user was added to a group.

    This is a stateful version of :class:`StatelessUserAddedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was added."""
        if isinstance(self.internal_user, User):
            return self.internal_user

        state = self.message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughUserAddedSystemEventUserCacheContext(
                type=CacheContextType.user_through_user_added_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserAddedSystemEvent.user')
            else _USER_THROUGH_USER_ADDED_SYSTEM_EVENT_USER
        )

        return cache.get_user(
            self.internal_user,
            ctx,
        )

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that added this user."""
        if isinstance(self.internal_by, User):
            return self.internal_by

        state = self.message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughUserAddedSystemEventAuthorCacheContext(
                type=CacheContextType.user_through_user_added_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('UserAddedSystemEvent.by')
            else _USER_THROUGH_USER_ADDED_SYSTEM_EVENT_BY
        )

        return cache.get_user(
            self.internal_by,
            ctx,
        )


@define(slots=True)
class StatelessUserRemovedSystemEvent(BaseSystemEvent):
    """An user was removed from a group.

    This inherits from :class:`BaseSystemEvent`.
    """

    internal_user: typing.Union[User, str] = field(repr=False, kw_only=True)
    """Union[:class:`User`, :class:`str`]: The ID of the user that was removed, or full user instance."""

    internal_by: typing.Union[User, str] = field(repr=False, kw_only=True)
    """Union[:class:`User`, :class:`str`]: The ID of the user that removed this user, or full user instance."""

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that removed this user."""
        if isinstance(self.internal_by, User):
            return self.internal_by
        return None

    def get_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was removed."""
        if isinstance(self.internal_user, User):
            return self.internal_user
        return None

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, StatelessUserRemovedSystemEvent)
            and self.user_id == other.user_id
            and self.by_id == other.by_id
        )

    @property
    def by(self) -> User:
        """:class:`User`: The user that removed this user."""
        user = self.get_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='StatelessUserRemovedSystemEvent.by',
            )
        return user

    @property
    def by_id(self) -> str:
        """:class:`str`: The user's ID that removed this user."""
        if isinstance(self.internal_by, User):
            return self.internal_by.id
        return self.internal_by

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        user = self.get_user()
        if user is None:
            user = '<Unknown User>'

        by = self.get_by()
        if by is None:
            by = '<Unknown User>'

        return f'{user} was removed by {by}'

    @property
    def user(self) -> User:
        """:class:`User`: The user that was removed."""
        user = self.get_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='StatelessUserRemovedSystemEvent.user',
            )
        return user

    @property
    def user_id(self) -> str:
        """:class:`str`: The user's ID that was removed."""
        if isinstance(self.internal_user, User):
            return self.internal_user.id
        return self.internal_user

    def attach_state(self, message: Message, /) -> UserRemovedSystemEvent:
        """:class:`UserRemovedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return UserRemovedSystemEvent(
            message=message,
            internal_user=self.internal_user,
            internal_by=self.internal_by,
        )

    def to_dict(self) -> raw.UserRemoveSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'user_remove',
            'by': self.by_id,
            'id': self.user_id,
        }


@define(slots=True)
class UserRemovedSystemEvent(StatelessUserRemovedSystemEvent):
    """An user was removed from a group.

    This is a stateful version of :class:`StatelessUserRemovedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that removed this user."""
        if isinstance(self.internal_by, User):
            return self.internal_by

        state = self.message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughUserRemovedSystemEventAuthorCacheContext(
                type=CacheContextType.user_through_user_removed_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('UserRemovedSystemEvent.by')
            else _USER_THROUGH_USER_REMOVED_SYSTEM_EVENT_BY
        )

        return cache.get_user(
            self.internal_by,
            ctx,
        )

    def get_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was removed."""
        if isinstance(self.internal_user, User):
            return self.internal_user

        state = self.message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughUserRemovedSystemEventUserCacheContext(
                type=CacheContextType.user_through_user_removed_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserRemovedSystemEvent.user')
            else _USER_THROUGH_USER_REMOVED_SYSTEM_EVENT_USER
        )

        return cache.get_user(
            self.internal_user,
            ctx,
        )


@define(slots=True)
class StatelessUserJoinedSystemEvent(BaseSystemEvent):
    """An user joined a server.

    This inherits from :class:`BaseSystemEvent`.
    """

    internal_user: typing.Union[Member, User, str] = field(repr=False, kw_only=True)
    """Union[:class:`Member`, :class:`User`, :class:`str`]: The ID of the user that joined this server, or full member/user instance."""

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, StatelessUserJoinedSystemEvent) and self.user_id == other.user_id

    def get_user(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that joined this server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user

    def get_user_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that joined this server."""
        if isinstance(self.internal_user, Member):
            return self.internal_user
        return None

    def get_user_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that joined this server."""
        if isinstance(self.internal_user, Member):
            if isinstance(self.internal_user.internal_user, User):
                return self.internal_user.internal_user
        elif isinstance(self.internal_user, User):
            return self.internal_user
        return None

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        user = self.get_user()
        if user is None:
            user = '<Unknown User>'

        return f'{user} joined'

    @property
    def user(self) -> typing.Union[Member, User]:
        """Union[:class:`Member`, :class:`User`]: The user that joined this server."""
        user = self.get_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserJoinedSystemEvent.user',
            )
        return user

    @property
    def user_as_member(self) -> Member:
        """:class:`Member`: The user that joined this server."""
        user = self.get_user_as_member()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserJoinedSystemEvent.user_as_member',
            )
        return user

    @property
    def user_as_user(self) -> User:
        """:class:`User`: The user that joined this server."""
        user = self.get_user_as_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserJoinedSystemEvent.user_as_user',
            )
        return user

    @property
    def user_id(self) -> str:
        """:class:`str`: The user's ID that joined this server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user.id
        return self.internal_user

    def attach_state(self, message: Message, /) -> UserJoinedSystemEvent:
        """:class:`UserJoinedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return UserJoinedSystemEvent(
            message=message,
            internal_user=self.internal_user,
        )

    def to_dict(self) -> raw.UserJoinedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'user_joined',
            'id': self.user_id,
        }


@define(slots=True)
class UserJoinedSystemEvent(StatelessUserJoinedSystemEvent):
    """An user joined a server.

    This is a stateful version of :class:`StatelessUserJoinedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True)
    """:class:`Message`: The message that holds this system event."""

    def get_user(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that was added."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberOrUserThroughUserJoinedSystemEventUserCacheContext(
                type=CacheContextType.member_or_user_through_user_joined_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserJoinedSystemEvent.user')
            else _MEMBER_OR_USER_THROUGH_USER_JOINED_SYSTEM_EVENT_USER
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            server_id = channel.server_id
            ret = cache.get_server_member(server_id, self.internal_user, ctx)
        else:
            ret = None

        if ret is None:
            return cache.get_user(self.internal_user, ctx)
        return ret

    def get_user_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that was added."""
        if isinstance(self.internal_user, Member):
            return self.internal_user

        if isinstance(self.internal_user, User):
            user_id = self.internal_user.id
        else:
            user_id = self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberThroughUserJoinedSystemEventUserCacheContext(
                type=CacheContextType.member_through_user_joined_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserJoinedSystemEvent.user_as_member')
            else _MEMBER_THROUGH_USER_JOINED_SYSTEM_EVENT_USER
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            return cache.get_server_member(channel.server_id, user_id, ctx)
        return None

    def get_user_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was added."""
        if isinstance(self.internal_user, User):
            return self.internal_user

        if isinstance(self.internal_user, Member):
            if isinstance(self.internal_user.internal_user, User):
                return self.internal_user.internal_user
            user_id = self.internal_user.id
        else:
            user_id = self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughUserJoinedSystemEventUserCacheContext(
                type=CacheContextType.user_through_user_joined_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserJoinedSystemEvent.user_as_user')
            else _USER_THROUGH_USER_JOINED_SYSTEM_EVENT_USER
        )

        return cache.get_user(user_id, ctx)


@define(slots=True)
class StatelessUserLeftSystemEvent(BaseSystemEvent):
    """An user left a group or server.

    This inherits from :class:`BaseSystemEvent`.
    """

    internal_user: typing.Union[Member, User, str] = field(repr=False, kw_only=True)
    """Union[:class:`Member`, :class:`User`, :class:`str`]: The ID of the user that left this group/server, or full member/user instance."""

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, StatelessUserLeftSystemEvent) and self.user_id == other.user_id

    def get_user(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that left this group/server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user

    def get_user_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that left this group/server."""
        if isinstance(self.internal_user, Member):
            return self.internal_user
        return None

    def get_user_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that left this group/server."""
        if isinstance(self.internal_user, Member):
            if isinstance(self.internal_user.internal_user, User):
                return self.internal_user.internal_user
        elif isinstance(self.internal_user, User):
            return self.internal_user
        return None

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        user = self.get_user()
        if user is None:
            user = '<Unknown User>'

        return f'{user} left'

    @property
    def user(self) -> typing.Union[Member, User]:
        """Union[:class:`Member`, :class:`User`]: The user that left this group/server."""
        user = self.get_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserLeftSystemEvent.user',
            )
        return user

    @property
    def user_as_member(self) -> Member:
        """:class:`Member`: The user that left this group/server."""
        user = self.get_user_as_member()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserLeftSystemEvent.user_as_member',
            )
        return user

    @property
    def user_as_user(self) -> User:
        """:class:`User`: The user that left this group/server."""
        user = self.get_user_as_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserLeftSystemEvent.user_as_user',
            )
        return user

    @property
    def user_id(self) -> str:
        """:class:`str`: The user's ID that left this group/server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user.id
        return self.internal_user

    def attach_state(self, message: Message, /) -> UserLeftSystemEvent:
        """:class:`UserLeftSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return UserLeftSystemEvent(
            message=message,
            internal_user=self.internal_user,
        )

    def to_dict(self) -> raw.UserLeftSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'user_left',
            'id': self.user_id,
        }


@define(slots=True)
class UserLeftSystemEvent(StatelessUserLeftSystemEvent):
    """An user left a group or server.

    This is a stateful version of :class:`StatelessUserLeftSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_user(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that left this group/server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberOrUserThroughUserLeftSystemEventUserCacheContext(
                type=CacheContextType.member_or_user_through_user_left_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserLeftSystemEvent.user')
            else _MEMBER_OR_USER_THROUGH_USER_LEFT_SYSTEM_EVENT_USER
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            server_id = channel.server_id
            ret = cache.get_server_member(server_id, self.internal_user, ctx)
        else:
            ret = None

        if ret is None:
            return cache.get_user(self.internal_user, ctx)
        return ret

    def get_user_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that left this group/server."""
        if isinstance(self.internal_user, Member):
            return self.internal_user

        if isinstance(self.internal_user, User):
            user_id = self.internal_user.id
        else:
            user_id = self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberThroughUserLeftSystemEventUserCacheContext(
                type=CacheContextType.member_through_user_left_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserLeftSystemEvent.user_as_member')
            else _MEMBER_THROUGH_USER_LEFT_SYSTEM_EVENT_USER
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            return cache.get_server_member(channel.server_id, user_id, ctx)
        return None

    def get_user_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that left this group/server."""
        if isinstance(self.internal_user, User):
            return self.internal_user

        if isinstance(self.internal_user, Member):
            if isinstance(self.internal_user.internal_user, User):
                return self.internal_user.internal_user
            user_id = self.internal_user.id
        else:
            user_id = self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughUserLeftSystemEventUserCacheContext(
                type=CacheContextType.user_through_user_left_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserLeftSystemEvent.user_as_user')
            else _USER_THROUGH_USER_LEFT_SYSTEM_EVENT_USER
        )

        return cache.get_user(user_id, ctx)


@define(slots=True)
class StatelessUserKickedSystemEvent(BaseSystemEvent):
    """A member was kicked from a server.

    This inherits from :class:`BaseSystemEvent`.
    """

    internal_user: typing.Union[Member, User, str] = field(repr=False, kw_only=True)
    """Union[:class:`Member`, :class:`User`, :class:`str`]: The ID of the user that kicked from this server, or full member/user instance."""

    def get_user(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that was kicked from this server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user

    def get_user_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that was kicked from this server."""
        if isinstance(self.internal_user, Member):
            return self.internal_user
        return None

    def get_user_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was kicked from this server."""
        if isinstance(self.internal_user, Member):
            if isinstance(self.internal_user.internal_user, User):
                return self.internal_user.internal_user
        elif isinstance(self.internal_user, User):
            return self.internal_user
        return None

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, StatelessUserKickedSystemEvent) and self.user_id == other.user_id

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        user = self.get_user()
        if user is None:
            user = '<Unknown User>'

        return f'{user} was kicked'

    @property
    def user(self) -> typing.Union[Member, User]:
        """Union[:class:`Member`, :class:`User`]: The user that was kicked from this server."""
        user = self.get_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserKickedSystemEvent.user',
            )
        return user

    @property
    def user_as_member(self) -> Member:
        """:class:`Member`: The user that was kicked from this server."""
        user = self.get_user_as_member()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserKickedSystemEvent.user_as_member',
            )
        return user

    @property
    def user_as_user(self) -> User:
        """:class:`User`: The user that was kicked from this server."""
        user = self.get_user_as_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserKickedSystemEvent.user_as_user',
            )
        return user

    @property
    def user_id(self) -> str:
        """:class:`str`: The user's ID that was kicked from this server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user.id
        return self.internal_user

    def attach_state(self, message: Message, /) -> UserKickedSystemEvent:
        """:class:`UserKickedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return UserKickedSystemEvent(
            message=message,
            internal_user=self.internal_user,
        )

    def to_dict(self) -> raw.UserKickedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'user_kicked',
            'id': self.user_id,
        }


@define(slots=True)
class UserKickedSystemEvent(StatelessUserKickedSystemEvent):
    """A member was kicked from a server.

    This is a stateful version of :class:`StatelessUserKickedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_user(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that was kicked from this server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberOrUserThroughUserKickedSystemEventUserCacheContext(
                type=CacheContextType.member_or_user_through_user_kicked_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserKickedSystemEvent.user')
            else _MEMBER_OR_USER_THROUGH_USER_KICKED_SYSTEM_EVENT_USER
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            server_id = channel.server_id
            ret = cache.get_server_member(server_id, self.internal_user, ctx)
        else:
            ret = None

        if ret is None:
            return cache.get_user(self.internal_user, ctx)
        return ret

    def get_user_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that was kicked from this server."""
        if isinstance(self.internal_user, Member):
            return self.internal_user

        if isinstance(self.internal_user, User):
            user_id = self.internal_user.id
        else:
            user_id = self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberThroughUserKickedSystemEventUserCacheContext(
                type=CacheContextType.member_through_user_kicked_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserKickedSystemEvent.user_as_member')
            else _MEMBER_THROUGH_USER_KICKED_SYSTEM_EVENT_USER
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            return cache.get_server_member(channel.server_id, user_id, ctx)
        return None

    def get_user_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was kicked from this server."""
        if isinstance(self.internal_user, User):
            return self.internal_user

        if isinstance(self.internal_user, Member):
            if isinstance(self.internal_user.internal_user, User):
                return self.internal_user.internal_user
            user_id = self.internal_user.id
        else:
            user_id = self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughUserKickedSystemEventUserCacheContext(
                type=CacheContextType.user_through_user_kicked_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserKickedSystemEvent.user_as_user')
            else _USER_THROUGH_USER_KICKED_SYSTEM_EVENT_USER
        )

        return cache.get_user(user_id, ctx)


@define(slots=True)
class StatelessUserBannedSystemEvent(BaseSystemEvent):
    """An user was banned from a server.

    This inherits from :class:`BaseSystemEvent`.
    """

    internal_user: typing.Union[Member, User, str] = field(repr=False, kw_only=True)
    """Union[:class:`Member`, :class:`User`, :class:`str`]: The ID of the user that was banned from this server, or full member/user instance."""

    def get_user(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that was banned from this server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user

    def get_user_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that was banned from this server."""
        if isinstance(self.internal_user, Member):
            return self.internal_user
        return None

    def get_user_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was banned from this server."""
        if isinstance(self.internal_user, Member):
            if isinstance(self.internal_user.internal_user, User):
                return self.internal_user.internal_user
        elif isinstance(self.internal_user, User):
            return self.internal_user
        return None

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, StatelessUserBannedSystemEvent) and self.user_id == other.user_id

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        user = self.get_user()
        if user is None:
            user = '<Unknown User>'

        return f'{user} was banned'

    @property
    def user(self) -> typing.Union[Member, User]:
        """Union[:class:`Member`, :class:`User`]: The user that was banned from this server."""
        user = self.get_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserBannedSystemEvent.user',
            )
        return user

    @property
    def user_as_member(self) -> Member:
        """:class:`Member`: The user that was banned from this server."""
        user = self.get_user_as_member()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserBannedSystemEvent.user_as_member',
            )
        return user

    @property
    def user_as_user(self) -> User:
        """:class:`User`: The user that was banned from this server."""
        user = self.get_user_as_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='UserBannedSystemEvent.user_as_user',
            )
        return user

    @property
    def user_id(self) -> str:
        """:class:`str`: The user's ID that was kicked from this server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user.id
        return self.internal_user

    def attach_state(self, message: Message, /) -> UserBannedSystemEvent:
        """:class:`UserBannedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return UserBannedSystemEvent(
            message=message,
            internal_user=self.internal_user,
        )

    def to_dict(self) -> raw.UserBannedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'user_banned',
            'id': self.user_id,
        }


@define(slots=True)
class UserBannedSystemEvent(StatelessUserBannedSystemEvent):
    """An user was banned from a server.

    This is a stateful version of :class:`StatelessUserBannedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_user(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that was banned from this server."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberOrUserThroughUserBannedSystemEventUserCacheContext(
                type=CacheContextType.member_or_user_through_user_banned_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserBannedSystemEvent.user')
            else _MEMBER_OR_USER_THROUGH_USER_BANNED_SYSTEM_EVENT_USER
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            server_id = channel.server_id
            ret = cache.get_server_member(server_id, self.internal_user, ctx)
        else:
            ret = None

        if ret is None:
            return cache.get_user(self.internal_user, ctx)
        return ret

    def get_user_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that was banned from this server."""
        if isinstance(self.internal_user, Member):
            return self.internal_user

        if isinstance(self.internal_user, User):
            user_id = self.internal_user.id
        else:
            user_id = self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberThroughUserBannedSystemEventUserCacheContext(
                type=CacheContextType.member_through_user_banned_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserBannedSystemEvent.user_as_member')
            else _MEMBER_THROUGH_USER_BANNED_SYSTEM_EVENT_USER
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            return cache.get_server_member(channel.server_id, user_id, ctx)
        return None

    def get_user_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was banned from this server."""
        if isinstance(self.internal_user, User):
            return self.internal_user

        if isinstance(self.internal_user, Member):
            if isinstance(self.internal_user.internal_user, User):
                return self.internal_user.internal_user
            user_id = self.internal_user.id
        else:
            user_id = self.internal_user

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughUserBannedSystemEventUserCacheContext(
                type=CacheContextType.user_through_user_banned_system_event_user,
                system_message=self,
            )
            if state.provide_cache_context('UserBannedSystemEvent.user_as_user')
            else _USER_THROUGH_USER_BANNED_SYSTEM_EVENT_USER
        )

        return cache.get_user(user_id, ctx)


@define(slots=True)
class StatelessChannelRenamedSystemEvent(BaseSystemEvent):
    """An user renamed group.

    This inherits from :class:`BaseSystemEvent`.
    """

    name: str = field(repr=True, kw_only=True)
    """:class:`str`: The new name of this group."""

    internal_by: typing.Union[User, str] = field(repr=False, kw_only=True)
    """Union[:class:`User`, :class:`str`]: The ID of the user that renamed this group, or full user instance."""

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that renamed this group."""
        if isinstance(self.internal_by, User):
            return self.internal_by

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, StatelessChannelRenamedSystemEvent)
            and self.name == other.name
            and self.by_id == other.by_id
        )

    @property
    def by(self) -> User:
        """:class:`User`: The user that renamed this group."""
        by = self.get_by()
        if by is None:
            raise NoData(
                what=self.by_id,
                type='StatelessChannelRenamedSystemEvent.by',
            )
        return by

    @property
    def by_id(self) -> str:
        """:class:`str`: The user's ID that renamed this group."""
        if isinstance(self.internal_by, User):
            return self.internal_by.id
        return self.internal_by

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        by = self.get_by()
        if by is None:
            by = '<Unknown User>'

        return f'{by} renamed the channel to {self.name}'

    def attach_state(self, message: Message, /) -> ChannelRenamedSystemEvent:
        """:class:`ChannelRenamedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return ChannelRenamedSystemEvent(
            message=message,
            name=self.name,
            internal_by=self.internal_by,
        )

    def to_dict(self) -> raw.ChannelRenamedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'channel_renamed',
            'name': self.name,
            'by': self.by_id,
        }


@define(slots=True)
class ChannelRenamedSystemEvent(StatelessChannelRenamedSystemEvent):
    """An user renamed group.

    This is a stateful version of :class:`StatelessChannelRenamedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that renamed this group."""
        if isinstance(self.internal_by, User):
            return self.internal_by

        state = self.message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughChannelRenamedSystemEventAuthorCacheContext(
                type=CacheContextType.user_through_channel_renamed_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('ChannelRenamedSystemEvent.by')
            else _USER_THROUGH_CHANNEL_RENAMED_SYSTEM_EVENT_BY
        )

        return cache.get_user(
            self.internal_by,
            ctx,
        )


@define(slots=True)
class StatelessChannelDescriptionChangedSystemEvent(BaseSystemEvent):
    """An user changed group's description.

    This inherits from :class:`BaseSystemEvent`.
    """

    internal_by: typing.Union[User, str] = field(repr=False, kw_only=True)
    """Union[:class:`User`, :class:`str`]: The ID of the user that changed description of this group, or full user instance."""

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that changed description of this group."""
        if isinstance(self.internal_by, User):
            return self.internal_by

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, StatelessChannelDescriptionChangedSystemEvent)
            and self.by_id == other.by_id
        )

    @property
    def by(self) -> User:
        """:class:`User`: The user that changed description of this group."""
        by = self.get_by()
        if by is None:
            raise NoData(
                what=self.by_id,
                type='StatelessChannelDescriptionChangedSystemEvent.by',
            )
        return by

    @property
    def by_id(self) -> str:
        """:class:`str`: The user's ID that changed description of this group."""
        if isinstance(self.internal_by, User):
            return self.internal_by.id
        return self.internal_by

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        by = self.get_by()
        if by is None:
            by = '<Unknown User>'

        return f'{by} changed the channel description'

    def attach_state(self, message: Message, /) -> ChannelDescriptionChangedSystemEvent:
        """:class:`ChannelDescriptionChangedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return ChannelDescriptionChangedSystemEvent(
            message=message,
            internal_by=self.internal_by,
        )

    def to_dict(self) -> raw.ChannelDescriptionChangedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'channel_description_changed',
            'by': self.by_id,
        }


@define(slots=True)
class ChannelDescriptionChangedSystemEvent(StatelessChannelDescriptionChangedSystemEvent):
    """An user changed group's description.

    This is a stateful version of :class:`StatelessChannelDescriptionChangedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that changed description of this group."""
        if isinstance(self.internal_by, User):
            return self.internal_by

        state = self.message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughChannelDescriptionChangedSystemEventAuthorCacheContext(
                type=CacheContextType.user_through_channel_description_changed_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('ChannelDescriptionChangedSystemEvent.by')
            else _USER_THROUGH_CHANNEL_DESCRIPTION_CHANGED_SYSTEM_EVENT_BY
        )

        return cache.get_user(
            self.internal_by,
            ctx,
        )


@define(slots=True)
class StatelessChannelIconChangedSystemEvent(BaseSystemEvent):
    """An user changed group's icon.

    This inherits from :class:`BaseSystemEvent`.
    """

    internal_by: typing.Union[User, str] = field(repr=False, kw_only=True)
    """Union[:class:`User`, :class:`str`]: The ID of the user that changed icon of this group, or full user instance."""

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that changed icon of this group."""
        if isinstance(self.internal_by, User):
            return self.internal_by

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, StatelessChannelIconChangedSystemEvent) and self.by_id == other.by_id

    @property
    def by(self) -> User:
        """:class:`User`: The user that changed icon of this group."""
        by = self.get_by()
        if by is None:
            raise NoData(
                what=self.by_id,
                type='StatelessChannelIconChangedSystemEvent.by',
            )
        return by

    @property
    def by_id(self) -> str:
        """:class:`str`: The user's ID that changed icon of this group."""
        if isinstance(self.internal_by, User):
            return self.internal_by.id
        return self.internal_by

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        by = self.get_by()
        if by is None:
            by = '<Unknown User>'

        return f'{by} changed the channel icon'

    def attach_state(self, message: Message, /) -> ChannelIconChangedSystemEvent:
        """:class:`ChannelIconChangedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return ChannelIconChangedSystemEvent(
            message=message,
            internal_by=self.internal_by,
        )

    def to_dict(self) -> raw.ChannelIconChangedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'channel_icon_changed',
            'by': self.by_id,
        }


@define(slots=True)
class ChannelIconChangedSystemEvent(StatelessChannelIconChangedSystemEvent):
    """An user changed group's icon.

    This is a stateful version of :class:`StatelessChannelIconChangedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that changed icon of this group."""
        if isinstance(self.internal_by, User):
            return self.internal_by

        state = self.message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughChannelIconChangedSystemEventAuthorCacheContext(
                type=CacheContextType.user_through_channel_icon_changed_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('ChannelIconChangedSystemEvent.by')
            else _USER_THROUGH_CHANNEL_ICON_CHANGED_SYSTEM_EVENT_BY
        )

        return cache.get_user(
            self.internal_by,
            ctx,
        )


@define(slots=True)
class StatelessChannelOwnershipChangedSystemEvent(BaseSystemEvent):
    """A group owner transferred ownership to someone else.

    This inherits from :class:`BaseSystemEvent`.
    """

    internal_from: typing.Union[User, str] = field(repr=False, kw_only=True)
    """Union[:class:`User`, :class:`str`]: The ID of the user that was previous owner of this group, or full user instance."""

    internal_to: typing.Union[User, str] = field(repr=False, kw_only=True)
    """Union[:class:`User`, :class:`str`]: The ID of the user that became owner of this group, or full user instance."""

    def get_from(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was previous owner of this group."""
        if isinstance(self.internal_from, User):
            return self.internal_from

    def get_to(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that became owner of this group."""
        if isinstance(self.internal_to, User):
            return self.internal_to

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, StatelessChannelOwnershipChangedSystemEvent)
            and self.from_id == other.from_id
            and self.to_id == other.to_id
        )

    @property
    def from_(self) -> User:
        """:class:`User`: The user that was previous owner of this group."""
        user = self.get_from()
        if user is None:
            raise NoData(
                what=self.from_id,
                type='ChannelOwnershipChangedSystemEvent.from_',
            )
        return user

    @property
    def from_id(self) -> str:
        """:class:`str`: The user's ID that was previous owner of this group."""
        if isinstance(self.internal_from, User):
            return self.internal_from.id
        return self.internal_from

    @property
    def to(self) -> User:
        """:class:`User`: The user that became owner of this group."""
        user = self.get_to()
        if user is None:
            raise NoData(
                what=self.to_id,
                type='ChannelOwnershipChangedSystemEvent.to',
            )
        return user

    @property
    def to_id(self) -> str:
        """:class:`str`: The user's ID that became owner of this group."""
        if isinstance(self.internal_to, User):
            return self.internal_to.id
        return self.internal_to

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        before = self.get_from()
        if before is None:
            before = '<Unknown User>'
        after = self.get_to()
        if after is None:
            after = '<Unknown User>'

        return f'{before} gave {after} group ownership'

    def attach_state(self, message: Message, /) -> ChannelOwnershipChangedSystemEvent:
        """:class:`ChannelOwnershipChangedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return ChannelOwnershipChangedSystemEvent(
            message=message,
            internal_from=self.internal_from,
            internal_to=self.internal_to,
        )

    def to_dict(self) -> raw.ChannelOwnershipChangedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'channel_ownership_changed',
            'from': self.from_id,
            'to': self.to_id,
        }


@define(slots=True)
class ChannelOwnershipChangedSystemEvent(StatelessChannelOwnershipChangedSystemEvent):
    """A group owner transferred ownership to someone else.

    This is a stateful version of :class:`StatelessChannelOwnershipChangedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_from(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that was previous owner of this group."""
        if isinstance(self.internal_from, User):
            return self.internal_from

        state = self.message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughChannelOwnershipChangedSystemEventFromCacheContext(
                type=CacheContextType.user_through_channel_ownership_changed_system_event_from,
                system_message=self,
            )
            if state.provide_cache_context('ChannelOwnershipChangedSystemEvent.from_')
            else _USER_THROUGH_CHANNEL_OWNERSHIP_CHANGED_SYSTEM_EVENT_FROM
        )

        return cache.get_user(
            self.internal_from,
            ctx,
        )

    def get_to(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that became owner of this group."""
        if isinstance(self.internal_to, User):
            return self.internal_to

        state = self.message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughChannelOwnershipChangedSystemEventToCacheContext(
                type=CacheContextType.user_through_channel_ownership_changed_system_event_to,
                system_message=self,
            )
            if state.provide_cache_context('ChannelOwnershipChangedSystemEvent.to')
            else _USER_THROUGH_CHANNEL_OWNERSHIP_CHANGED_SYSTEM_EVENT_TO
        )

        return cache.get_user(
            self.internal_to,
            ctx,
        )


@define(slots=True)
class StatelessMessagePinnedSystemEvent(BaseSystemEvent):
    """A message was pinned.

    This inherits from :class:`BaseSystemEvent`.
    """

    pinned_message_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The ID of the message that was pinned."""

    internal_by: typing.Union[Member, User, str] = field(repr=False, kw_only=True)
    """Union[:class:`Member`, :class:`User`, :class:`str`]: The ID of the user that pinned a message, or full member/user instance."""

    def get_by(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that pinned a message."""
        if isinstance(self.internal_by, (Member, User)):
            return self.internal_by
        return None

    def get_by_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that pinned a message."""
        if isinstance(self.internal_by, Member):
            return self.internal_by
        return None

    def get_by_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that pinned a message."""
        if isinstance(self.internal_by, User):
            return self.internal_by
        elif isinstance(self.internal_by, Member) and isinstance(self.internal_by.internal_user, User):
            return self.internal_by.internal_user
        return None

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, StatelessMessagePinnedSystemEvent)
            and self.pinned_message_id == other.pinned_message_id
            and self.by_id == other.by_id
        )

    @property
    def by(self) -> typing.Union[Member, User]:
        """Union[:class:`Member`, :class:`User`]: The user that pinned a message."""
        user = self.get_by()
        if user is None:
            raise NoData(
                what=self.by_id,
                type='StatelessMessagePinnedSystemEvent.by',
            )
        return user

    @property
    def by_as_member(self) -> Member:
        """:class:`Member`: The user that pinned a message."""
        user = self.get_by_as_member()
        if user is None:
            raise NoData(
                what=self.by_id,
                type='StatelessMessagePinnedSystemEvent.by_as_member',
            )
        return user

    @property
    def by_as_user(self) -> User:
        """:class:`User`: The user that pinned a message."""
        user = self.get_by_as_user()
        if user is None:
            raise NoData(
                what=self.by_id,
                type='StatelessMessagePinnedSystemEvent.by_as_user',
            )
        return user

    @property
    def by_id(self) -> str:
        """:class:`str`: The user's ID that pinned a message."""
        if isinstance(self.internal_by, (Member, User)):
            return self.internal_by.id
        return self.internal_by

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        by = self.get_by()
        if by is None:
            by = '<Unknown User>'

        return f'{by} pinned a message to this channel'

    def attach_state(self, message: Message, /) -> MessagePinnedSystemEvent:
        """:class:`MessagePinnedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return MessagePinnedSystemEvent(
            message=message,
            pinned_message_id=self.pinned_message_id,
            internal_by=self.internal_by,
        )

    def to_dict(self) -> raw.MessagePinnedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'message_pinned',
            'id': self.pinned_message_id,
            'by': self.by_id,
        }


@define(slots=True)
class MessagePinnedSystemEvent(StatelessMessagePinnedSystemEvent):
    """A message was pinned.

    This is a stateful version of :class:`StatelessMessagePinnedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_by(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that pinned a message."""
        if isinstance(self.internal_by, (Member, User)):
            return self.internal_by

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberOrUserThroughMessagePinnedSystemEventAuthorCacheContext(
                type=CacheContextType.member_or_user_through_message_pinned_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('MessagePinnedSystemEvent.by')
            else _MEMBER_OR_USER_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_BY
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            server_id = channel.server_id
            ret = cache.get_server_member(server_id, self.internal_by, ctx)
        else:
            ret = None

        if ret is None:
            return cache.get_user(self.internal_by, ctx)
        return ret

    def get_by_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that pinned a message."""
        if isinstance(self.internal_by, Member):
            return self.internal_by

        if isinstance(self.internal_by, User):
            user_id = self.internal_by.id
        else:
            user_id = self.internal_by

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberThroughMessagePinnedSystemEventAuthorCacheContext(
                type=CacheContextType.member_through_message_pinned_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('MessagePinnedSystemEvent.by_as_member')
            else _MEMBER_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_BY
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            return cache.get_server_member(channel.server_id, user_id, ctx)
        return None

    def get_by_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that pinned a message."""
        if isinstance(self.internal_by, User):
            return self.internal_by

        if isinstance(self.internal_by, Member):
            if isinstance(self.internal_by.internal_user, User):
                return self.internal_by.internal_user
            user_id = self.internal_by.id
        else:
            user_id = self.internal_by

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughMessagePinnedSystemEventAuthorCacheContext(
                type=CacheContextType.user_through_message_pinned_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('MessagePinnedSystemEvent.by_as_user')
            else _USER_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_BY
        )

        return cache.get_user(user_id, ctx)

    def get_pinned_message(self) -> typing.Optional[Message]:
        """Optional[:class:`Message`]: The message that was pinned in this channel."""

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MessageThroughMessagePinnedSystemEventPinnedMessageCacheContext(
                type=CacheContextType.message_through_message_pinned_system_event_pinned_message,
                system_message=self,
            )
            if state.provide_cache_context('MessagePinnedSystemEvent.pinned_message')
            else _MESSAGE_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_PINNED_MESSAGE
        )

        return cache.get_message(message.channel_id, self.pinned_message_id, ctx)


@define(slots=True)
class StatelessMessageUnpinnedSystemEvent(BaseSystemEvent):
    """A message was unpinned.

    This inherits from :class:`BaseSystemEvent`.
    """

    unpinned_message_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The ID of the message that was unpinned."""

    internal_by: typing.Union[Member, User, str] = field(repr=False, kw_only=True)
    """Union[:class:`Member`, :class:`User`, :class:`str`]: The ID of the user that unpinned a message, or full member/user instance."""

    def get_by(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that unpinned a message."""
        if isinstance(self.internal_by, (Member, User)):
            return self.internal_by
        return None

    def get_by_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that unpinned a message."""
        if isinstance(self.internal_by, Member):
            return self.internal_by
        return None

    def get_by_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that unpinned a message."""
        if isinstance(self.internal_by, User):
            return self.internal_by
        elif isinstance(self.internal_by, Member) and isinstance(self.internal_by.internal_user, User):
            return self.internal_by.internal_user
        return None

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, StatelessMessageUnpinnedSystemEvent)
            and self.unpinned_message_id == other.unpinned_message_id
            and self.by_id == other.by_id
        )

    @property
    def by(self) -> typing.Union[Member, User]:
        """Union[:class:`Member`, :class:`User`]: The user that unpinned a message."""
        user = self.get_by()
        if user is None:
            raise NoData(
                what=self.by_id,
                type='StatelessMessageUnpinnedSystemEvent.by',
            )
        return user

    @property
    def by_as_member(self) -> Member:
        """:class:`Member`: The user that unpinned a message."""
        user = self.get_by_as_member()
        if user is None:
            raise NoData(
                what=self.by_id,
                type='StatelessMessageUnpinnedSystemEvent.by_as_member',
            )
        return user

    @property
    def by_as_user(self) -> User:
        """:class:`User`: The user that unpinned a message."""
        user = self.get_by_as_user()
        if user is None:
            raise NoData(
                what=self.by_id,
                type='StatelessMessageUnpinnedSystemEvent.by_as_user',
            )
        return user

    @property
    def by_id(self) -> str:
        """:class:`str`: The user's ID that unpinned a message."""
        if isinstance(self.internal_by, (Member, User)):
            return self.internal_by.id
        return self.internal_by

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        by = self.get_by()
        if by is None:
            by = '<Unknown User>'

        return f'{by} unpinned a message from this channel'

    def attach_state(self, message: Message, /) -> MessageUnpinnedSystemEvent:
        """:class:`MessageUnpinnedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return MessageUnpinnedSystemEvent(
            message=message,
            unpinned_message_id=self.unpinned_message_id,
            internal_by=self.internal_by,
        )

    def to_dict(self) -> raw.MessageUnpinnedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'message_unpinned',
            'id': self.unpinned_message_id,
            'by': self.by_id,
        }


@define(slots=True)
class MessageUnpinnedSystemEvent(StatelessMessageUnpinnedSystemEvent):
    """A message was unpinned.

    This is a stateful version of :class:`StatelessMessageUnpinnedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_by(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that unpinned a message."""
        if isinstance(self.internal_by, (Member, User)):
            return self.internal_by

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberOrUserThroughMessageUnpinnedSystemEventAuthorCacheContext(
                type=CacheContextType.member_or_user_through_message_unpinned_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('MessageUnpinnedSystemEvent.by')
            else _MEMBER_OR_USER_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_BY
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            server_id = channel.server_id
            ret = cache.get_server_member(server_id, self.internal_by, ctx)
        else:
            ret = None

        if ret is None:
            return cache.get_user(self.internal_by, ctx)
        return ret

    def get_by_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that unpinned a message."""
        if isinstance(self.internal_by, Member):
            return self.internal_by

        if isinstance(self.internal_by, User):
            user_id = self.internal_by.id
        else:
            user_id = self.internal_by

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MemberThroughMessageUnpinnedSystemEventAuthorCacheContext(
                type=CacheContextType.member_through_message_unpinned_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('MessageUnpinnedSystemEvent.by_as_member')
            else _MEMBER_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_BY
        )

        channel = cache.get_channel(message.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            return cache.get_server_member(channel.server_id, user_id, ctx)
        return None

    def get_by_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that unpinned a message."""
        if isinstance(self.internal_by, User):
            return self.internal_by

        if isinstance(self.internal_by, Member):
            if isinstance(self.internal_by.internal_user, User):
                return self.internal_by.internal_user
            user_id = self.internal_by.id
        else:
            user_id = self.internal_by

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughMessageUnpinnedSystemEventAuthorCacheContext(
                type=CacheContextType.user_through_message_unpinned_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('MessageUnpinnedSystemEvent.by_as_user')
            else _USER_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_BY
        )

        return cache.get_user(user_id, ctx)

    def get_unpinned_message(self) -> typing.Optional[Message]:
        """Optional[:class:`Message`]: The message that was unpinned from this channel."""

        message = self.message
        state = message.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            MessageThroughMessageUnpinnedSystemEventUnpinnedMessageCacheContext(
                type=CacheContextType.message_through_message_unpinned_system_event_unpinned_message,
                system_message=self,
            )
            if state.provide_cache_context('MessageUnpinnedSystemEvent.unpinned_message')
            else _MESSAGE_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_UNPINNED_MESSAGE
        )

        return cache.get_message(message.channel_id, self.unpinned_message_id, ctx)


@define(slots=True)
class StatelessCallStartedSystemEvent(BaseSystemEvent):
    """A call was just started in the channel.

    This inherits from :class:`BaseSystemEvent`.
    """

    internal_by: typing.Union[User, str] = field(repr=False, kw_only=True)
    """Union[:class:`User`, :class:`str`]: The ID of the user that started a call, or full user instance."""

    finished_at: typing.Optional[datetime] = field(repr=False, kw_only=True)
    """Optional[:class:`~datetime.datetime`]: When the call was finished.
    
    .. versionadded:: 1.2
    """

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, StatelessCallStartedSystemEvent) and self.by_id == other.by_id

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that started a call."""
        if isinstance(self.internal_by, User):
            return self.internal_by

    @property
    def by(self) -> User:
        """:class:`User`: The user that started a call."""
        user = self.get_by()
        if user is None:
            raise NoData(
                what=self.by_id,
                type='StatelessCallStartedSystemEvent.by',
            )
        return user

    @property
    def by_id(self) -> str:
        """:class:`str`: The user's ID that started a call."""
        if isinstance(self.internal_by, User):
            return self.internal_by.id
        return self.internal_by

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed system's content."""

        by = self.get_by()
        if by is None:
            by = '<Unknown User>'

        return f'{by} started a call.'

    def attach_state(self, message: Message, /) -> CallStartedSystemEvent:
        """:class:`CallStartedSystemEvent`: Attach a state to system event.

        Parameters
        ----------
        message: :class:`Message`
            The state to attach.
        """
        return CallStartedSystemEvent(
            message=message,
            internal_by=self.internal_by,
            finished_at=self.finished_at,
        )

    def to_dict(self) -> raw.CallStartedSystemMessage:
        """:class:`dict`: Convert system event to raw data."""
        return {
            'type': 'call_started',
            'by': self.by_id,
            'finished_at': None if self.finished_at is None else self.finished_at.isoformat(),
        }


@define(slots=True)
class CallStartedSystemEvent(StatelessCallStartedSystemEvent):
    """A call was just started in the channel.

    This is a stateful version of :class:`StatelessCallStartedSystemEvent`, and inherits from it.
    """

    message: Message = field(repr=False, kw_only=True, eq=False)
    """:class:`Message`: The message that holds this system event."""

    def get_by(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that started call."""
        if isinstance(self.internal_by, User):
            return self.internal_by

        state = self.message.state
        cache = state.cache
        if cache is None:
            return None

        ctx = (
            UserThroughCallStartedSystemEventAuthorCacheContext(
                type=CacheContextType.user_through_call_started_system_event_by,
                system_message=self,
            )
            if state.provide_cache_context('CallStartedSystemEvent.by')
            else _USER_THROUGH_CALL_STARTED_SYSTEM_EVENT_BY
        )

        return cache.get_user(
            self.internal_by,
            ctx,
        )


StatelessSystemEvent = typing.Union[
    TextSystemEvent,
    StatelessUserAddedSystemEvent,
    StatelessUserRemovedSystemEvent,
    StatelessUserJoinedSystemEvent,
    StatelessUserLeftSystemEvent,
    StatelessUserKickedSystemEvent,
    StatelessUserBannedSystemEvent,
    StatelessChannelRenamedSystemEvent,
    StatelessChannelDescriptionChangedSystemEvent,
    StatelessChannelIconChangedSystemEvent,
    StatelessChannelOwnershipChangedSystemEvent,
    StatelessMessagePinnedSystemEvent,
    StatelessMessageUnpinnedSystemEvent,
    StatelessCallStartedSystemEvent,
]

SystemEvent = typing.Union[
    TextSystemEvent,
    UserAddedSystemEvent,
    UserRemovedSystemEvent,
    UserJoinedSystemEvent,
    UserLeftSystemEvent,
    UserKickedSystemEvent,
    UserBannedSystemEvent,
    ChannelRenamedSystemEvent,
    ChannelDescriptionChangedSystemEvent,
    ChannelIconChangedSystemEvent,
    ChannelOwnershipChangedSystemEvent,
    MessagePinnedSystemEvent,
    MessageUnpinnedSystemEvent,
    CallStartedSystemEvent,
]


@define(slots=True)
class Message(BaseMessage):
    """Represents a message in channel on Stoat.

    This inherits from :class:`BaseMessage`.
    """

    nonce: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The unique value generated by client sending this message."""

    channel_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The channel's ID this message was sent in."""

    internal_author: typing.Union[Member, User, str] = field(repr=False, kw_only=True)
    """Union[:class:`Member`, :class:`User`, :class:`str`]: The ID of the user (or webhook) that sent this message, or full member/user instance."""

    webhook: typing.Optional[MessageWebhook] = field(repr=True, kw_only=True)
    """Optional[:class:`MessageWebhook`]: The webhook that sent this message."""

    content: str = field(repr=True, kw_only=True)
    """:class:`str`: The message's content."""

    internal_system_event: typing.Optional[StatelessSystemEvent] = field(repr=True, kw_only=True)
    """Optional[:class:`StatelessSystemEvent`]: The stateless system event information, occured in this message, if any."""

    internal_attachments: list[StatelessAsset] = field(repr=True, kw_only=True)
    """List[:class:`StatelessAsset`]: The stateless attachments on this message."""

    edited_at: typing.Optional[datetime] = field(repr=True, kw_only=True)
    """Optional[:class:`~datetime.datetime`]: Timestamp at which this message was last edited."""

    internal_embeds: list[StatelessEmbed] = field(repr=True, kw_only=True)
    """List[:class:`StatelessEmbed`]: The attached stateless embeds to this message."""

    mention_ids: list[str] = field(repr=True, kw_only=True)
    """List[:class:`str`]: The user's IDs mentioned in this message."""

    role_mention_ids: list[str] = field(repr=True, kw_only=True)
    """List[:class:`str`]: The role's IDs mentioned in this message."""

    replies: list[str] = field(repr=True, kw_only=True)
    """List[:class:`str`]: The message's IDs this message is replying to."""

    reactions: dict[str, tuple[str, ...]] = field(repr=True, kw_only=True)
    """Dict[:class:`str`, Tuple[:class:`str`, ...]]: The mapping of emojis to list of user IDs."""

    interactions: typing.Optional[MessageInteractions] = field(repr=True, kw_only=True)
    """Optional[:class:`MessageInteractions`]: The information about how this message should be interacted with."""

    masquerade: typing.Optional[MessageMasquerade] = field(repr=True, kw_only=True)
    """Optional[:class:`MessageMasquerade`]: The name and / or avatar overrides for this message."""

    pinned: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the message is pinned."""

    raw_flags: int = field(repr=True, kw_only=True)
    """:class:`int`: The message's flags raw value."""

    def locally_append(self, data: MessageAppendData, /) -> None:
        if data.internal_embeds is not UNDEFINED:
            self.internal_embeds.extend(data.internal_embeds)

    def locally_clear_reactions(self, emoji: str, /) -> None:
        self.reactions.pop(emoji, None)

    def locally_react(self, user_id: str, emoji: str, /) -> None:
        try:
            reaction = self.reactions[emoji]
        except KeyError:
            self.reactions[emoji] = (user_id,)
        else:
            self.reactions[emoji] = (*reaction, user_id)

    def locally_unreact(self, user_id: str, emoji: str, /) -> None:
        try:
            reaction = self.reactions[emoji]
        except KeyError:
            self.reactions[emoji] = ()
        else:
            self.reactions[emoji] = tuple(reactor_id for reactor_id in reaction if reactor_id != user_id)

    def locally_update(self, data: PartialMessage, /) -> None:
        """Locally updates message with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.

        Parameters
        ----------
        data: :class:`PartialMessage`
            The data to update message with.
        """
        if data.content is not UNDEFINED:
            self.content = data.content
        if data.edited_at is not UNDEFINED:
            self.edited_at = data.edited_at
        if data.internal_embeds is not UNDEFINED:
            self.internal_embeds = data.internal_embeds
        if data.pinned is not UNDEFINED:
            self.pinned = data.pinned
        if data.reactions is not UNDEFINED:
            self.reactions = data.reactions

    def get_author(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user that sent this message."""
        if isinstance(self.internal_author, (Member, User)):
            return self.internal_author

        if self.internal_author == ZID:
            return self.state.system

        state = self.state

        if self.webhook is not None:
            webhook = self.webhook
            webhook_id = self.author_id

            return User(
                state=state,
                id=webhook_id,
                name=webhook.name,
                discriminator='0000',
                internal_avatar=(
                    None
                    if webhook.avatar is None
                    else StatelessAsset(
                        id=webhook.avatar,
                        filename='',
                        metadata=AssetMetadata(
                            type=AssetMetadataType.image,
                            width=0,
                            height=0,
                        ),
                        content_type='',
                        size=0,
                        deleted=False,
                        reported=False,
                        message_id=None,
                        user_id=webhook_id,
                        server_id=None,
                        object_id=webhook_id,
                    )
                ),
                display_name=None,
                raw_badges=0,
                status=None,
                raw_flags=0,
                privileged=False,
                bot=None,
                relationship=RelationshipStatus.none,
                online=False,
            )

        cache = state.cache
        if cache is None:
            return None

        ctx = (
            MemberOrUserThroughMessageAuthorCacheContext(
                type=CacheContextType.member_or_user_through_message_author,
                message=self,
            )
            if state.provide_cache_context('Message.author')
            else _MEMBER_OR_USER_THROUGH_MESSAGE_AUTHOR
        )

        channel = cache.get_channel(self.channel_id, ctx)

        if isinstance(channel, BaseServerChannel):
            server_id = channel.server_id
            ret = cache.get_server_member(server_id, self.internal_author, ctx)
        else:
            ret = None

        if ret is None:
            return cache.get_user(self.internal_author, ctx)

        return ret

    def get_author_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user that sent this message."""
        if isinstance(self.internal_author, Member):
            return self.internal_author

        if isinstance(self.internal_author, User):
            user_id = self.internal_author.id
        else:
            user_id = self.internal_author

        if user_id == ZID:
            return None

        state = self.state

        if self.webhook is not None:
            return None

        cache = state.cache
        if cache is None:
            return None

        ctx = (
            MemberThroughMessageAuthorCacheContext(
                type=CacheContextType.member_through_message_author,
                message=self,
            )
            if state.provide_cache_context('Message.author_as_member')
            else _MEMBER_THROUGH_MESSAGE_AUTHOR
        )

        channel = cache.get_channel(self.channel_id, ctx)

        if not isinstance(channel, BaseServerChannel):
            return None

        return cache.get_server_member(channel.server_id, user_id, ctx)

    def get_author_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user that sent this message."""
        if isinstance(self.internal_author, Member):
            if isinstance(self.internal_author.internal_user, User):
                return self.internal_author.internal_user
            return None
        if isinstance(self.internal_author, User):
            return self.internal_author

        if self.internal_author == ZID:
            return self.state.system

        state = self.state

        if self.webhook is not None:
            webhook = self.webhook
            webhook_id = self.author_id

            return User(
                state=state,
                id=webhook_id,
                name=webhook.name,
                discriminator='0000',
                internal_avatar=None
                if webhook.avatar is None
                else StatelessAsset(
                    id=webhook.avatar,
                    filename='',
                    metadata=AssetMetadata(
                        type=AssetMetadataType.image,
                        width=0,
                        height=0,
                    ),
                    content_type='',
                    size=0,
                    deleted=False,
                    reported=False,
                    message_id=None,
                    user_id=webhook_id,
                    server_id=None,
                    object_id=webhook_id,
                ),
                display_name=None,
                raw_badges=0,
                status=None,
                raw_flags=0,
                privileged=False,
                bot=None,
                relationship=RelationshipStatus.none,
                online=False,
            )

        cache = state.cache
        if cache is None:
            return None

        ctx = (
            UserThroughMessageAuthorCacheContext(
                type=CacheContextType.user_through_message_author,
                message=self,
            )
            if state.provide_cache_context('Message.author_as_user')
            else _USER_THROUGH_MESSAGE_AUTHOR
        )

        return cache.get_user(self.internal_author, ctx)

    @property
    def attachments(self) -> list[Asset]:
        """List[:class:`Asset`]: The attachments on this message."""
        return [a.attach_state(self.state, 'attachments') for a in self.internal_attachments]

    @property
    def author(self) -> typing.Union[Member, User]:
        """Union[:class:`Member`, :class:`User`]: The user that sent this message."""
        author = self.get_author()
        if author is None:
            raise NoData(
                what=self.author_id,
                type='Message.author',
            )
        return author

    @property
    def author_as_member(self) -> Member:
        """:class:`Member`: The user that sent this message."""
        author = self.get_author_as_member()
        if author is None:
            raise NoData(
                what=self.author_id,
                type='Message.author_as_member',
            )
        return author

    @property
    def author_as_user(self) -> User:
        """:class:`User`: The user that sent this message."""
        author = self.get_author_as_user()
        if author is None:
            raise NoData(
                what=self.author_id,
                type='Message.author_as_user',
            )
        return author

    @property
    def author_id(self) -> str:
        """:class:`str`: The user's ID or webhook that sent this message."""
        if isinstance(self.internal_author, (Member, User)):
            return self.internal_author.id
        return self.internal_author

    @property
    def embeds(self) -> list[Embed]:
        """List[:class:`Embed`]: The attached embeds to this message."""
        return [e.attach_state(self.state) for e in self.internal_embeds]

    @property
    def flags(self) -> MessageFlags:
        """:class:`MessageFlags`: The message's flags."""
        ret = _new_message_flags(MessageFlags)
        ret.value = self.raw_flags
        return ret

    @property
    def mentions(self) -> list[typing.Union[Member, User]]:
        """List[Union[:class:`Member`, :class:`User`]]: The message's user mentions."""

        if not len(self.mention_ids):
            return []

        state = self.state
        cache = state.cache

        if cache is None:
            return []

        ctx = (
            MemberOrUsersThroughMessageMentionsCacheContext(
                type=CacheContextType.member_or_users_through_message_mentions,
                message=self,
            )
            if state.provide_cache_context('Message.mentions')
            else _MEMBER_OR_USERS_THROUGH_MESSAGE_MENTIONS
        )

        channel = cache.get_channel(self.channel_id, ctx)
        if channel is None or not isinstance(channel, BaseServerChannel):
            mentions = []
            for user_id in self.mention_ids:
                user = cache.get_user(user_id, ctx)
                if user is not None:
                    mentions.append(user)
            return mentions

        server_id = channel.server_id
        mentions = []

        for user_id in self.mention_ids:
            user = cache.get_server_member(server_id, user_id, ctx)
            if user is None:
                user = cache.get_user(user_id, ctx)
            if user is not None:
                mentions.append(user)

        return mentions

    @property
    def mentions_as_members(self) -> list[Member]:
        """List[:class:`Member`]: The message's user mentions as members."""

        if not len(self.mention_ids):
            return []

        state = self.state
        cache = state.cache

        if cache is None:
            return []

        ctx = (
            MembersThroughMessageMentionsCacheContext(
                type=CacheContextType.members_through_message_mentions,
                message=self,
            )
            if state.provide_cache_context('Message.mentions_as_members')
            else _MEMBERS_THROUGH_MESSAGE_MENTIONS
        )

        channel = cache.get_channel(self.channel_id, ctx)
        if channel is None or not isinstance(channel, BaseServerChannel):
            return []

        server_id = channel.server_id
        mentions = []

        for user_id in self.mention_ids:
            user = cache.get_server_member(server_id, user_id, ctx)
            if user is not None:
                mentions.append(user)

        return mentions

    @property
    def mentions_as_users(self) -> list[User]:
        """List[:class:`User`]: The message's user mentions."""

        if not len(self.mention_ids):
            return []

        state = self.state
        cache = state.cache

        if cache is None:
            return []

        ctx = (
            UsersThroughMessageMentionsCacheContext(
                type=CacheContextType.users_through_message_mentions,
                message=self,
            )
            if state.provide_cache_context('Message.mentions_as_users')
            else _USERS_THROUGH_MESSAGE_MENTIONS
        )

        mentions = []

        for user_id in self.mention_ids:
            user = cache.get_user(user_id, ctx)
            if user is not None:
                mentions.append(user)

        return mentions

    @property
    def role_mentions(self) -> list[Role]:
        """List[:class:`Role`]: The message's role mentions."""

        if not len(self.role_mention_ids):
            return []

        state = self.state
        cache = state.cache

        if cache is None:
            return []

        ctx = (
            RoleThroughMessageRoleMentionsCacheContext(
                type=CacheContextType.role_through_message_role_mentions,
                message=self,
            )
            if state.provide_cache_context('Message.role_mentions')
            else _ROLE_THROUGH_MESSAGE_ROLE_MENTIONS
        )

        channel = cache.get_channel(self.channel_id, ctx)
        if channel is None or not isinstance(channel, BaseServerChannel):
            return []

        server = cache.get_server(channel.server_id, ctx)
        if server is None:
            return []

        role_mentions = []
        for role_id in self.role_mention_ids:
            try:
                role = server.roles[role_id]
            except KeyError:
                pass
            else:
                role_mentions.append(role)
        return role_mentions

    @property
    def system_content(self) -> str:
        """:class:`str`: The displayed message's content."""

        system_event = self.system_event
        if system_event is None:
            return self.content

        return system_event.system_content

    @property
    def system_event(self) -> typing.Optional[SystemEvent]:
        """Optional[:class:`SystemEvent`]: The system event information, occured in this message, if any."""
        if self.internal_system_event is None:
            return None
        return self.internal_system_event.attach_state(self)

    def is_silent(self) -> bool:
        """:class:`bool`: Whether the message suppresses push notifications."""
        return self.flags.suppress_notifications

    def to_dict(self) -> raw.Message:
        """:class:`dict`: Convert message to raw data."""
        payload: dict[str, typing.Any] = {
            '_id': self.id,
        }
        if self.nonce is not None:
            payload['nonce'] = self.nonce
        payload['channel'] = self.channel_id

        if isinstance(self.internal_author, Member):
            user = self.internal_author.internal_user
            if isinstance(user, User):
                payload['author'] = user.id
                payload['user'] = user.to_dict()
            else:
                payload['author'] = user
            payload['member'] = self.internal_author.to_dict()
        elif isinstance(self.internal_author, User):
            payload['author'] = self.internal_author.id
            payload['user'] = self.internal_author.to_dict()
        else:
            payload['author'] = self.internal_author
        if self.webhook is not None:
            payload['webhook'] = self.webhook.to_dict()

        # TODO: Maybe add internal_content: Optional[str] and a property for backwards compatibilty?
        if len(self.content):
            payload['content'] = self.content
        if self.internal_system_event is not None:
            payload['system'] = self.internal_system_event.to_dict()
        if len(self.internal_attachments):
            payload['attachments'] = [a.to_dict('attachments') for a in self.internal_attachments]
        if self.edited_at is not None:
            payload['edited'] = self.edited_at.isoformat()
        if len(self.internal_embeds):
            payload['embeds'] = [e.to_dict() for e in self.internal_embeds]
        if len(self.mention_ids):
            payload['mentions'] = self.mention_ids
        if len(self.role_mention_ids):
            payload['role_mentions'] = self.role_mention_ids
        if len(self.replies):
            payload['replies'] = self.replies
        if len(self.reactions):
            payload['reactions'] = {k: list(v) for k, v in self.reactions.items()}
        if self.interactions is not None:
            payload['interactions'] = self.interactions.to_dict()
        if self.masquerade is not None:
            payload['masquerade'] = self.masquerade.to_dict()
        if self.pinned:
            payload['pinned'] = self.pinned
        if self.raw_flags != 0:
            payload['flags'] = self.raw_flags
        return payload  # type: ignore


Masquerade: typing.TypeAlias = MessageMasquerade

__all__ = (
    'Reply',
    'MessageInteractions',
    'MessageMasquerade',
    'SendableEmbed',
    'MessageWebhook',
    'BaseMessage',
    'PartialMessage',
    'MessageAppendData',
    'BaseSystemEvent',
    'TextSystemEvent',
    'StatelessUserAddedSystemEvent',
    'UserAddedSystemEvent',
    'StatelessUserRemovedSystemEvent',
    'UserRemovedSystemEvent',
    'StatelessUserJoinedSystemEvent',
    'UserJoinedSystemEvent',
    'StatelessUserLeftSystemEvent',
    'UserLeftSystemEvent',
    'StatelessUserKickedSystemEvent',
    'UserKickedSystemEvent',
    'StatelessUserBannedSystemEvent',
    'UserBannedSystemEvent',
    'StatelessChannelRenamedSystemEvent',
    'ChannelRenamedSystemEvent',
    'StatelessChannelDescriptionChangedSystemEvent',
    'ChannelDescriptionChangedSystemEvent',
    'StatelessChannelIconChangedSystemEvent',
    'ChannelIconChangedSystemEvent',
    'StatelessChannelOwnershipChangedSystemEvent',
    'ChannelOwnershipChangedSystemEvent',
    'StatelessMessagePinnedSystemEvent',
    'MessagePinnedSystemEvent',
    'StatelessMessageUnpinnedSystemEvent',
    'MessageUnpinnedSystemEvent',
    'StatelessCallStartedSystemEvent',
    'CallStartedSystemEvent',
    'StatelessSystemEvent',
    'SystemEvent',
    'Message',
    # backwards compatibilty
    'Masquerade',
)
