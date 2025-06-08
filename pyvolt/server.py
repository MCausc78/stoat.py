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
from datetime import datetime, timedelta
import typing

from . import routes, utils
from .abc import Messageable, Connectable
from .base import Base
from .bot import BaseBot
from .cache import (
    CacheContextType,
    MembersThroughRoleMembersCacheContext,
    ServerThroughRoleServerCacheContext,
    EmojiThroughServerGetterCacheContext,
    MemberThroughServerGetterCacheContext,
    EmojisThroughServerGetterCacheContext,
    MembersThroughServerGetterCacheContext,
    ChannelThroughServerGetterCacheContext,
    ChannelsThroughServerGetterCacheContext,
    MemberThroughServerMeCacheContext,
    MemberOrUserThroughServerOwnerCacheContext,
    MemberThroughServerOwnerCacheContext,
    UserThroughServerOwnerCacheContext,
    ServerThroughMemberServerCacheContext,
    UserThroughMemberUserCacheContext,
    UserThroughMemberBotOwnerCacheContext,
    ChannelIDThroughMemberDMChannelIDCacheContext,
    ChannelThroughMemberDMChannelCacheContext,
    UserThroughMemberNameCacheContext,
    UserThroughMemberDiscriminatorCacheContext,
    UserThroughMemberDisplayNameCacheContext,
    UserThroughMemberInternalAvatarCacheContext,
    UserThroughMemberRawBadgesCacheContext,
    UserThroughMemberStatusCacheContext,
    UserThroughMemberRawFlagsCacheContext,
    UserThroughMemberPrivilegedCacheContext,
    UserThroughMemberBotCacheContext,
    UserThroughMemberRelationshipCacheContext,
    UserThroughMemberOnlineCacheContext,
    UserThroughMemberTagCacheContext,
    ServerThroughMemberRolesCacheContext,
    ServerThroughMemberServerPermissionsCacheContext,
    ServerThroughMemberTopRoleCacheContext,
    _MEMBERS_THROUGH_ROLE_MEMBERS,
    _SERVER_THROUGH_ROLE_SERVER,
    _EMOJI_THROUGH_SERVER_GETTER,
    _MEMBER_THROUGH_SERVER_GETTER,
    _EMOJIS_THROUGH_SERVER_GETTER,
    _MEMBERS_THROUGH_SERVER_GETTER,
    _CHANNEL_THROUGH_SERVER_GETTER,
    _CHANNELS_THROUGH_SERVER_GETTER,
    _MEMBER_THROUGH_SERVER_ME,
    _MEMBER_OR_USER_THROUGH_SERVER_OWNER,
    _MEMBER_THROUGH_SERVER_OWNER,
    _USER_THROUGH_SERVER_OWNER,
    _SERVER_THROUGH_MEMBER_SERVER,
    _USER_THROUGH_MEMBER_USER,
    _USER_THROUGH_MEMBER_BOT_OWNER,
    _CHANNEL_ID_THROUGH_MEMBER_DM_CHANNEL_ID,
    _CHANNEL_THROUGH_MEMBER_DM_CHANNEL,
    _USER_THROUGH_MEMBER_NAME,
    _USER_THROUGH_MEMBER_DISCRIMINATOR,
    _USER_THROUGH_MEMBER_DISPLAY_NAME,
    _USER_THROUGH_MEMBER_INTERNAL_AVATAR,
    _USER_THROUGH_MEMBER_RAW_BADGES,
    _USER_THROUGH_MEMBER_STATUS,
    _USER_THROUGH_MEMBER_RAW_FLAGS,
    _USER_THROUGH_MEMBER_PRIVILEGED,
    _USER_THROUGH_MEMBER_BOT,
    _USER_THROUGH_MEMBER_RELATIONSHIP,
    _USER_THROUGH_MEMBER_ONLINE,
    _USER_THROUGH_MEMBER_TAG,
    _SERVER_THROUGH_MEMBER_ROLES,
    _SERVER_THROUGH_MEMBER_SERVER_PERMISSIONS,
    _SERVER_THROUGH_MEMBER_TOP_ROLE,
)
from .cdn import StatelessAsset, Asset, ResolvableResource
from .core import (
    UNDEFINED,
    UndefinedOr,
    ULIDOr,
    resolve_id,
)
from .emoji import ServerEmoji
from .enums import ChannelType, ContentReportReason, RelationshipStatus, UserReportReason
from .errors import NoData
from .flags import Permissions, ServerFlags, UserBadges, UserFlags
from .permissions import Permissions, PermissionOverride
from .user import (
    UserStatus,
    UserProfile,
    Mutuals,
    BaseUser,
    DisplayUser,
    BotUserMetadata,
    User,
)


if typing.TYPE_CHECKING:
    from collections.abc import Mapping

    from . import raw
    from .channel import (
        SavedMessagesChannel,
        DMChannel,
        ChannelVoiceMetadata,
        TextChannel,
        VoiceChannel,
        ServerChannel,
        TextableChannel,
        PartialMessageable,
    )
    from .http import HTTPOverrideOptions
    from .invite import ServerInvite
    from .message import BaseMessage
    from .state import State

_new_permissions = Permissions.__new__
_new_server_flags = ServerFlags.__new__
_new_user_badges = UserBadges.__new__
_new_user_flags = UserFlags.__new__


class Category:
    """Represents a category containing channels in Revolt server.

    Parameters
    ----------
    id: :class:`str`
        The category's ID. Must be between 1 and 32 characters long.
    title: :class:`str`
        The category's title. Must be between 1 and 32 characters long.

    Attributes
    ----------
    id: :class:`str`
        The category's ID.
    title: :class:`str`
        The category's title.
    channels: List[:class:`str`]
        The channel's IDs inside this category.
    """

    __slots__ = ('id', 'title', 'channels')

    def __init__(
        self,
        id: ULIDOr[Category],
        title: str,
        channels: list[ULIDOr[ServerChannel]],
    ) -> None:
        self.id: str = resolve_id(id)
        self.title: str = title
        self.channels: list[str] = list(map(resolve_id, channels))

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, Category) and self.id == other.id

    def to_dict(self) -> raw.Category:
        """:class:`dict`: Convert category to raw data."""

        return {
            'id': self.id,
            'title': self.title,
            'channels': self.channels,
        }


class SystemMessageChannels:
    """Represents system message channel assignments in a Revolt server.

    Attributes
    ----------
    user_joined: Optional[:class:`str`]
        The channel's ID to send user join messages in.
    user_left: Optional[:class:`str`]
        The channel's ID to send user left messages in.
    user_kicked: Optional[:class:`str`]
        The channel's ID to send user kicked messages in.
    user_banned: Optional[:class:`str`]
        The channel's ID to send user banned messages in.
    """

    __slots__ = ('user_joined', 'user_left', 'user_kicked', 'user_banned')

    def __init__(
        self,
        *,
        user_joined: typing.Optional[ULIDOr[typing.Union[TextableChannel, PartialMessageable]]] = None,
        user_left: typing.Optional[ULIDOr[typing.Union[TextableChannel, PartialMessageable]]] = None,
        user_kicked: typing.Optional[ULIDOr[typing.Union[TextableChannel, PartialMessageable]]] = None,
        user_banned: typing.Optional[ULIDOr[typing.Union[TextableChannel, PartialMessageable]]] = None,
    ) -> None:
        self.user_joined: typing.Optional[str] = None if user_joined is None else resolve_id(user_joined)
        self.user_left: typing.Optional[str] = None if user_left is None else resolve_id(user_left)
        self.user_kicked: typing.Optional[str] = None if user_kicked is None else resolve_id(user_kicked)
        self.user_banned: typing.Optional[str] = None if user_banned is None else resolve_id(user_banned)

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, SystemMessageChannels)
            and (
                self.user_joined == other.user_joined
                and self.user_left == other.user_left
                and self.user_kicked == other.user_kicked
                and self.user_banned == other.user_banned
            )
        )

    def to_dict(self) -> raw.SystemMessageChannels:
        """:class:`dict`: Convert system message channels configuration to raw data."""

        payload: raw.SystemMessageChannels = {}
        if self.user_joined is not None:
            payload['user_joined'] = self.user_joined
        if self.user_left is not None:
            payload['user_left'] = self.user_left
        if self.user_kicked is not None:
            payload['user_kicked'] = self.user_kicked
        if self.user_banned is not None:
            payload['user_banned'] = self.user_banned
        return payload


@define(slots=True)
class BaseRole(Base):
    """Represents a base role in Revolt server.

    This inherits from :class:`.Base`.
    """

    server_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The server's ID the role belongs to."""

    def get_server(self) -> typing.Optional[Server]:
        """Optional[:class:`.Server`]: The server this role belongs to."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ServerThroughRoleServerCacheContext(
                type=CacheContextType.server_through_role_server,
                role=self,
            )
            if state.provide_cache_context('Role.server')
            else _SERVER_THROUGH_ROLE_SERVER
        )

        return cache.get_server(self.server_id, ctx)

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, BaseRole) and self.id == other.id

    @property
    def members(self) -> list[Member]:
        """List[:class:`.Member`]: The members who have this role."""

        state = self.state
        cache = state.cache

        if cache is None:
            return []

        ctx = (
            MembersThroughRoleMembersCacheContext(
                type=CacheContextType.members_through_role_members,
                role=self,
            )
            if state.provide_cache_context('Role.members')
            else _MEMBERS_THROUGH_ROLE_MEMBERS
        )

        members = cache.get_server_members_mapping_of(self.server_id, ctx)
        if members is None:
            return []

        role_id = self.id
        return [member for member in members.values() if role_id in member.role_ids]

    @property
    def server(self) -> Server:
        """:class:`.Server`: The server this role belongs to."""
        server = self.get_server()
        if server is None:
            raise NoData(
                what=self.server_id,
                type='Role.server',
            )
        return server

    async def delete(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Deletes the role.

        You must have :attr:`~Permissions.manage_roles` to do this.

        Fires :class:`.ServerRoleDeleteEvent` for all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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

            +-----------------------+----------------------------------------------------------------------------+
            | Value                 | Reason                                                                     |
            +-----------------------+----------------------------------------------------------------------------+
            | ``NotElevated``       | Rank of your top role is higher than rank of role you're trying to delete. |
            +-----------------------+----------------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to delete role.                     |
            +-----------------------+----------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/role was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.delete_role(self.server_id, self.id, http_overrides=http_overrides)

    async def edit(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        name: UndefinedOr[str] = UNDEFINED,
        color: UndefinedOr[typing.Optional[str]] = UNDEFINED,
        hoist: UndefinedOr[bool] = UNDEFINED,
        rank: UndefinedOr[int] = UNDEFINED,
    ) -> Role:
        """|coro|

        Edits the role.

        You must have :attr:`~Permissions.manage_roles` to do this.

        Fires :class:`.RawServerRoleUpdateEvent` for all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        name: UndefinedOr[:class:`str`]
            The new role name. Must be between 1 and 32 characters long.
        color: UndefinedOr[Optional[:class:`str`]]
            The new role color. Must be a valid CSS color.
        hoist: UndefinedOr[:class:`bool`]
            Whether this role should be displayed separately.
        rank: UndefinedOr[:class:`int`]
            The new ranking position. The smaller value is, the more role takes priority.

            .. deprecated:: 1.2

                Use :meth:`~BaseServer.bulk_edit_role_ranks` instead.

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

            +-----------------------+---------------------------------------------------------------------------------+
            | Value                 | Reason                                                                          |
            +-----------------------+---------------------------------------------------------------------------------+
            | ``NotElevated``       | One of these:                                                                   |
            |                       |                                                                                 |
            |                       | - Rank of your top role is higher than rank of role you're trying to edit.      |
            |                       | - Rank of your top role is higher than rank you're trying to set for this role. |
            +-----------------------+---------------------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to edit role.                            |
            +-----------------------+---------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/role was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Role`
            The newly updated role.
        """
        return await self.state.http.edit_role(
            self.server_id,
            self.id,
            http_overrides=http_overrides,
            name=name,
            color=color,
            hoist=hoist,
            rank=rank,
        )

    async def set_permissions(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        allow: Permissions = Permissions.none(),
        deny: Permissions = Permissions.none(),
    ) -> Server:
        """|coro|

        Sets permissions for this role.

        You must have :attr:`~Permissions.manage_permissions` to do this.

        Fires :class:`.RawServerRoleUpdateEvent` for all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        allow: :class:`.Permissions`
            The permissions to allow.
        deny: :class:`.Permissions`
            The permissions to deny.

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

            +----------------------------------+--------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                               |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``CannotGiveMissingPermissions`` | Your new provided permissions contained permissions you didn't have.                 |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``NotElevated``                  | Rank of your top role is higher than rank of role you're trying to set override for. |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to edit permissions for this role.            |
            +----------------------------------+--------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/role was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Server`
            The updated server with new permissions.
        """

        return await self.state.http.set_server_permissions_for_role(
            self.server_id, self.id, http_overrides=http_overrides, allow=allow, deny=deny
        )


@define(slots=True)
class PartialRole(BaseRole):
    """Represents a partial role for the server.

    Unmodified fields will have :data:`.UNDEFINED` value.

    This inherits from :class:`.BaseRole`.
    """

    name: UndefinedOr[str] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`str`]: The new role's name."""

    permissions: UndefinedOr[PermissionOverride] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`.PermissionOverride`]: The new role's permissions."""

    color: UndefinedOr[typing.Optional[str]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`str`]]: The new role's color. This can be any valid CSS color."""

    hoist: UndefinedOr[bool] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`bool`]: Whether this role should be shown separately on the member sidebar."""

    rank: UndefinedOr[int] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`int`]: The new role's rank."""

    def into_full(self) -> typing.Optional[Role]:
        """Optional[:class:`.Role`]: Tries transform this partial role into full object. This is useful when caching role."""
        if (
            self.name is not UNDEFINED
            and self.permissions is not UNDEFINED
            and self.hoist is not UNDEFINED
            and self.rank is not UNDEFINED
        ):
            color = None if not self.color is not UNDEFINED else self.color
            return Role(
                state=self.state,
                id=self.id,
                server_id=self.server_id,
                name=self.name,
                permissions=self.permissions,
                color=color,
                hoist=self.hoist,
                rank=self.rank,
            )


@define(slots=True)
class Role(BaseRole):
    """Represents a role in Revolt server.

    This inherits from :class:`.BaseRole`.
    """

    name: str = field(repr=True, kw_only=True)
    """:class:`str`: The role's name."""

    permissions: PermissionOverride = field(repr=True, kw_only=True)
    """:class:`.PermissionOverride`: Permissions available to this role."""

    color: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The role's color. This is valid CSS color."""

    hoist: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether this role should be shown separately on the member sidebar."""

    rank: int = field(repr=True, kw_only=True)
    """:class:`int`: The role's rank."""

    def locally_update(self, data: PartialRole, /) -> None:
        """Locally updates role with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.
        """
        if data.name is not UNDEFINED:
            self.name = data.name
        if data.permissions is not UNDEFINED:
            self.permissions = data.permissions
        if data.color is not UNDEFINED:
            self.color = data.color
        if data.hoist is not UNDEFINED:
            self.hoist = data.hoist
        if data.rank is not UNDEFINED:
            self.rank = data.rank

    def to_dict(self) -> raw.Role:
        """:class:`dict`: Convert role to raw data."""

        if self.color is None:
            payload = {
                'name': self.name,
                'permissions': self.permissions.to_field_dict(),
            }
        else:
            payload = {
                'name': self.name,
                'permissions': self.permissions.to_field_dict(),
                'colour': self.color,
            }

        if self.hoist:
            payload['hoist'] = self.hoist

        payload['rank'] = self.rank

        return payload  # type: ignore


@define(slots=True)
class BaseServer(Base):
    """Represents a server on Revolt.

    This inherits from :class:`.Base`.
    """

    def get_emoji(self, emoji_id: str, /) -> typing.Optional[ServerEmoji]:
        """Retrieves a server emoji from cache.

        Parameters
        ----------
        emoji_id: :class:`str`
            The emoji ID.

        Returns
        -------
        Optional[:class:`.ServerEmoji`]
            The emoji or ``None`` if not found.
        """
        state = self.state
        cache = state.cache

        if cache is None:
            return

        ctx = (
            EmojiThroughServerGetterCacheContext(
                type=CacheContextType.emoji_through_server_getter,
                server=self,
            )
            if state.provide_cache_context('Server.get_emoji()')
            else _EMOJI_THROUGH_SERVER_GETTER
        )
        emoji = cache.get_emoji(emoji_id, ctx)

        if emoji is not None:
            assert isinstance(emoji, ServerEmoji)
            if emoji.server_id != self.id:
                return None
        return emoji

    def get_member(self, user_id: str, /) -> typing.Optional[Member]:
        """Retrieves a server member from cache.

        Parameters
        ----------
        user_id: :class:`str`
            The user ID.

        Returns
        -------
        Optional[:class:`.Member`]
            The member or ``None`` if not found.
        """
        state = self.state
        cache = state.cache

        if cache is None:
            return

        ctx = (
            MemberThroughServerGetterCacheContext(
                type=CacheContextType.member_through_server_getter,
                server=self,
            )
            if state.provide_cache_context('Server.get_member()')
            else _MEMBER_THROUGH_SERVER_GETTER
        )
        return cache.get_server_member(self.id, user_id, ctx)

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, BaseServer) and self.id == other.id

    @property
    def emojis(self) -> Mapping[str, ServerEmoji]:
        """Mapping[:class:`str`, :class:`.ServerEmoji`]: Returns all emojis of this server."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            EmojisThroughServerGetterCacheContext(
                type=CacheContextType.emojis_through_server_getter,
                server=self,
            )
            if state.provide_cache_context('Server.emojis')
            else _EMOJIS_THROUGH_SERVER_GETTER
        )

        return cache.get_server_emojis_mapping_of(self.id, ctx) or {}

    @property
    def members(self) -> Mapping[str, Member]:
        """Mapping[:class:`str`, :class:`.Member`]: Returns all members of this server."""
        state = self.state
        cache = state.cache

        if cache is None:
            return {}

        ctx = (
            MembersThroughServerGetterCacheContext(
                type=CacheContextType.members_through_server_getter,
                server=self,
            )
            if state.provide_cache_context('Server.members')
            else _MEMBERS_THROUGH_SERVER_GETTER
        )

        return cache.get_server_members_mapping_of(self.id, ctx) or {}

    async def add_bot(
        self,
        bot: ULIDOr[typing.Union[BaseBot, BaseUser]],
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> None:
        """|coro|

        Invites a bot to a server or group.

        You must have :attr:`~Permissions.manage_server` to do this.

        For servers, fires :class:`.ServerCreateEvent` for bot, :class:`.ServerMemberJoinEvent` and :class:`.MessageCreateEvent` for all server members.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        bot: ULIDOr[Union[:class:`.BaseBot`, :class:`.BaseUser`]]
            The bot.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +-----------+-------------------------------------------+
            | Value     | Reason                                    |
            +-----------+-------------------------------------------+
            | ``IsBot`` | The current token belongs to bot account. |
            +-----------+-------------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+-----------------------------------------------------+
            | Value                 | Reason                                              |
            +-----------------------+-----------------------------------------------------+
            | ``Banned``            | The bot was banned in target server.                |
            +-----------------------+-----------------------------------------------------+
            | ``BotIsPrivate``      | You do not own the bot to add it.                   |
            +-----------------------+-----------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to add bots. |
            +-----------------------+-----------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------------+
            | Value        | Reason                        |
            +--------------+-------------------------------+
            | ``NotFound`` | The bot/server was not found. |
            +--------------+-------------------------------+
        :class:`Conflict`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------+-------------------------------+
            | Value               | Reason                        |
            +---------------------+-------------------------------+
            | ``AlreadyInServer`` | The bot is already in server. |
            +---------------------+-------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.invite_bot(bot, http_overrides=http_overrides, server=self.id)

    async def ban(
        self,
        user: typing.Union[str, BaseUser, BaseMember],
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        reason: typing.Optional[str] = None,
    ) -> Ban:
        """|coro|

        Bans an user from the server.

        You must have :attr:`~Permissions.ban_members` to do this.

        May fire :class:`.ServerMemberRemoveEvent` for banned user and all server members.

        Parameters
        ----------
        user: Union[:class:`str`, :class:`.BaseUser`, :class:`.BaseMember`]
            The user to ban from the server.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        reason: Optional[:class:`str`]
            The ban reason. Can be only up to 1024 characters long.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------------+--------------------------------+
            | Value                    | Reason                         |
            +--------------------------+--------------------------------+
            | ``CannotRemoveYourself`` | You tried to ban yourself.     |
            +--------------------------+--------------------------------+
            | ``FailedValidation``     | The payload was invalid.       |
            +--------------------------+--------------------------------+
            | ``InvalidOperation``     | You tried to ban server owner. |
            +--------------------------+--------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+-------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                              |
            +----------------------------------+-------------------------------------------------------------------------------------+
            | ``NotElevated``                  | Rank of your top role is higher than rank of top role of user you're trying to ban. |
            +----------------------------------+-------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to ban members.                              |
            +----------------------------------+-------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/user was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Ban`
            The created ban.
        """
        return await self.state.http.ban(self.id, user, http_overrides=http_overrides, reason=reason)

    async def bulk_edit_role_ranks(
        self, ranks: list[ULIDOr[BaseRole]], *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> Server:
        """|coro|

        Edits ranks of all roles in bulk.

        You must have :attr:`~Permissions.manage_roles` to do this.

        Fires :class:`ServerRoleRanksUpdateEvent` for all server members.

        Parameters
        ----------
        ranks: List[ULIDOr[:class:`BaseRole`]]
            A list of roles that should be reordered, where their position in list represents their new rank.

            For example, we have following roles:

            - Owner
            - Administrator
            - Moderator
            - Member

            Passing ``[member_role_id, moderator_role_id, administrator_role_id, owner_role_id]``
            would result in following hierachy:

            - Member has rank=3
            - Moderator has rank=2
            - Administrator has rank=1
            - Owner has rank=0

            Must contain all roles.
        http_overrides: Optional[:class:`HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        -------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+---------------------------------------------------------------+
            | Value                |                                                               |
            +----------------------+---------------------------------------------------------------+
            | ``InvalidOperation`` | One of server roles was not specified in ``ranks`` parameter. |
            +----------------------+---------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+-------------------------------------------------------------------------------------+
            | Value                 | Reason                                                                              |
            +-----------------------+-------------------------------------------------------------------------------------+
            | ``NotElevated``       | Rank of your top role is higher than rank of roles you were trying to edit rank of. |
            +-----------------------+-------------------------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to edit role ranks.                          |
            +-----------------------+-------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/role was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`Server`
            The server with updated role ranks.
        """
        return await self.state.http.bulk_edit_role_ranks(self.id, ranks, http_overrides=http_overrides)

    @typing.overload
    async def create_channel(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        type: None = ...,
        name: str,
        description: typing.Optional[str] = ...,
        nsfw: typing.Optional[bool] = ...,
    ) -> TextChannel: ...

    @typing.overload
    async def create_channel(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        type: typing.Literal[ChannelType.text] = ...,
        name: str,
        description: typing.Optional[str] = ...,
        nsfw: typing.Optional[bool] = ...,
        voice: typing.Optional[ChannelVoiceMetadata] = ...,
    ) -> TextChannel: ...

    @typing.overload
    async def create_channel(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        type: typing.Literal[ChannelType.voice] = ...,
        name: str,
        description: typing.Optional[str] = ...,
        nsfw: typing.Optional[bool] = ...,
        voice: typing.Optional[ChannelVoiceMetadata] = ...,
    ) -> VoiceChannel: ...

    async def create_channel(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        type: typing.Optional[ChannelType] = None,
        name: str,
        description: typing.Optional[str] = None,
        nsfw: typing.Optional[bool] = None,
        voice: typing.Optional[ChannelVoiceMetadata] = None,
    ) -> ServerChannel:
        """|coro|

        Create a new text or voice channel within server.

        You must have :attr:`~Permissions.manage_channels` to do this.

        Fires :class:`.ServerChannelCreateEvent` for all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        type: Optional[:class:`.ChannelType`]
            The channel type. Defaults to :attr:`.ChannelType.text` if not provided.
        name: :class:`str`
            The channel name. Must be between 1 and 32 characters.
        description: Optional[:class:`str`]
            The channel description. Can be only up to 1024 characters.
        nsfw: Optional[:class:`bool`]
            To mark channel as NSFW or not.
        voice: Optional[:class:`.ChannelVoiceMetadata`]
            The voice-specific metadata for this channel.

            .. versionadded:: 1.2

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------+-----------------------------------------------------------------+
            | Value               | Reason                                                          |
            +---------------------+-----------------------------------------------------------------+
            | ``TooManyChannels`` | The server has too many channels than allowed on this instance. |
            +---------------------+-----------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+----------------------------------------------------------------------+
            | Value                 | Reason                                                               |
            +-----------------------+----------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to create channels in server. |
            +-----------------------+----------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.ServerChannel`
            The channel created in server.
        """

        return await self.state.http.create_server_channel(
            self.id,
            http_overrides=http_overrides,
            type=type,
            name=name,
            description=description,
            nsfw=nsfw,
            voice=voice,
        )

    async def create_server_emoji(
        self,
        name: str,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        nsfw: typing.Optional[bool] = None,
        image: ResolvableResource,
    ) -> ServerEmoji:
        """|coro|

        Creates an emoji in server.

        You must have :attr:`~Permissions.manage_customization` to do this.

        Fires :class:`.EmojiCreateEvent` for all server members.

        .. note::
            Prior to API v0.8.4, this could only be used by non-bot accounts.

        Parameters
        ----------
        name: :class:`str`
            The emoji name. Must be between 1 and 32 chars long. Can only contain ASCII digits, underscore and lowercase letters.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        nsfw: Optional[:class:`bool`]
            Whether the emoji is NSFW or not. Defaults to ``False``.
        image: :class:`.ResolvableResource`
            The emoji data.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+----------------------------------------------------------------------------------------------------------------------------+
            | Value                | Reason                                                                                                                     |
            +----------------------+----------------------------------------------------------------------------------------------------------------------------+
            | ``FailedValidation`` | The payload was invalid.                                                                                                   |
            +----------------------+----------------------------------------------------------------------------------------------------------------------------+
            | ``IsBot``            | The current token belongs to bot account. Only applicable to instances running API whose version is lower than ``v0.8.3``. |
            +----------------------+----------------------------------------------------------------------------------------------------------------------------+
            | ``TooManyEmoji``     | The server has too many emojis than allowed on this instance.                                                              |
            +----------------------+----------------------------------------------------------------------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+--------------------------------------------------------------------+
            | Value                 | Reason                                                             |
            +-----------------------+--------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to create emojis in server. |
            +-----------------------+--------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/file was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.ServerEmoji`
            The created emoji.
        """
        return await self.state.http.create_server_emoji(
            self.id,
            http_overrides=http_overrides,
            name=name,
            nsfw=nsfw,
            image=image,
        )

    async def create_text_channel(
        self,
        name: str,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        description: typing.Optional[str] = None,
        nsfw: typing.Optional[bool] = None,
        voice: typing.Optional[ChannelVoiceMetadata] = None,
    ) -> TextChannel:
        """|coro|

        Create a new text channel within server.

        You must have :attr:`~Permissions.manage_channels` to do this.

        Fires :class:`.ServerChannelCreateEvent` for all server members.

        Parameters
        ----------
        name: :class:`str`
            The channel name. Must be between 1 and 32 characters.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        description: Optional[:class:`str`]
            The channel description. Can be only up to 1024 characters.
        nsfw: Optional[:class:`bool`]
            To mark channel as NSFW or not.
        voice: Optional[:class:`.ChannelVoiceMetadata`]
            The voice-specific metadata for this channel.

            .. versionadded:: 1.2

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------+-----------------------------------------------------------------+
            | Value               | Reason                                                          |
            +---------------------+-----------------------------------------------------------------+
            | ``TooManyChannels`` | The server has too many channels than allowed on this instance. |
            +---------------------+-----------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+----------------------------------------------------------------------+
            | Value                 | Reason                                                               |
            +-----------------------+----------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to create channels in server. |
            +-----------------------+----------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.TextChannel`
            The channel created in server.
        """
        channel = await self.create_channel(
            http_overrides=http_overrides,
            type=ChannelType.text,
            name=name,
            description=description,
            nsfw=nsfw,
            voice=voice,
        )
        return channel

    async def create_voice_channel(
        self,
        name: str,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        description: typing.Optional[str] = None,
        nsfw: typing.Optional[bool] = None,
        voice: typing.Optional[ChannelVoiceMetadata] = None,
    ) -> VoiceChannel:
        """|coro|

        Create a new voice channel within server.

        You must have :attr:`~Permissions.manage_channels` to do this.

        Fires :class:`.ServerChannelCreateEvent` for all server members.

        Parameters
        ----------
        name: :class:`str`
            The channel name. Must be between 1 and 32 characters.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        description: Optional[:class:`str`]
            The channel description. Can be only up to 1024 characters.
        nsfw: Optional[:class:`bool`]
            To mark channel as NSFW or not.
        voice: Optional[:class:`.ChannelVoiceMetadata`]
            The voice-specific metadata for this channel.

            .. versionadded:: 1.2

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------+-----------------------------------------------------------------+
            | Value               | Reason                                                          |
            +---------------------+-----------------------------------------------------------------+
            | ``TooManyChannels`` | The server has too many channels than allowed on this instance. |
            +---------------------+-----------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+----------------------------------------------------------------------+
            | Value                 | Reason                                                               |
            +-----------------------+----------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to create channels in server. |
            +-----------------------+----------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.VoiceChannel`
            The channel created in server.
        """
        channel = await self.create_channel(
            type=ChannelType.voice,
            http_overrides=http_overrides,
            name=name,
            description=description,
            nsfw=nsfw,
            voice=voice,
        )
        return channel

    async def create_role(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        name: str,
        rank: typing.Optional[int] = None,
    ) -> Role:
        """|coro|

        Creates a new server role.

        You must have :attr:`~Permissions.manage_roles` to do this.

        Fires :class:`.RawServerRoleUpdateEvent` for all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        name: :class:`str`
            The role name. Must be between 1 and 32 characters long.
        rank: Optional[:class:`int`]
            The ranking position. The smaller value is, the more role takes priority.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+--------------------------------------------------------------+
            | Value                | Reason                                                       |
            +----------------------+--------------------------------------------------------------+
            | ``FailedValidation`` | The payload was invalid.                                     |
            +----------------------+--------------------------------------------------------------+
            | ``TooManyRoles``     | The server has too many roles than allowed on this instance. |
            +----------------------+--------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+----------------------------------------------------------------------------+
            | Value                 | Reason                                                                     |
            +-----------------------+----------------------------------------------------------------------------+
            | ``NotElevated``       | Rank of your top role is higher than rank of role you're trying to create. |
            +-----------------------+----------------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to create role in this server.      |
            +-----------------------+----------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/role was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Role`
            The role created in server.
        """

        return await self.state.http.create_role(self.id, http_overrides=http_overrides, name=name, rank=rank)

    async def delete(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Deletes a server if owner, or leaves otherwise.

        Fires :class:`.ServerDeleteEvent` (if owner) or :class:`.ServerMemberRemoveEvent` for all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """
        return await self.state.http.delete_server(self.id, http_overrides=http_overrides)

    async def edit(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        mfa_ticket: typing.Optional[str] = None,
        name: UndefinedOr[str] = UNDEFINED,
        description: UndefinedOr[typing.Optional[str]] = UNDEFINED,
        icon: UndefinedOr[typing.Optional[ResolvableResource]] = UNDEFINED,
        banner: UndefinedOr[typing.Optional[ResolvableResource]] = UNDEFINED,
        categories: UndefinedOr[typing.Optional[list[Category]]] = UNDEFINED,
        system_messages: UndefinedOr[typing.Optional[SystemMessageChannels]] = UNDEFINED,
        flags: UndefinedOr[ServerFlags] = UNDEFINED,
        discoverable: UndefinedOr[bool] = UNDEFINED,
        analytics: UndefinedOr[bool] = UNDEFINED,
        owner: UndefinedOr[typing.Union[str, BaseUser, BaseMember]] = UNDEFINED,
    ) -> Server:
        """|coro|

        Edits the server.

        To provide any of parameters below (except for ``categories``, ``discoverable`` and ``flags``), you must have :attr:`~Permissions.manage_server`.

        Fires :class:`.ServerUpdateEvent` for all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        mfa_ticket: Optional[:class:`str`]
            The valid MFA ticket token. Must be provided if ``owner`` is provided as well.
        name: UndefinedOr[:class:`str`]
            The new server name. Must be between 1 and 32 characters long.
        description: UndefinedOr[Optional[:class:`str`]]
            The new server description. Can be only up to 1024 characters.
        icon: UndefinedOr[Optional[:class:`.ResolvableResource`]]
            The new server icon.
        banner: UndefinedOr[Optional[:class:`.ResolvableResource`]]
            The new server banner.
        categories: UndefinedOr[Optional[List[:class:`.Category`]]]
            The new server categories structure.

            You must have :attr:`~Permissions.manage_channels`.
        system_messsages: UndefinedOr[Optional[:class:`.SystemMessageChannels`]]
            The new system message channels configuration.
        flags: UndefinedOr[:class:`.ServerFlags`]
            The new server flags. You must be a privileged user to provide this.
        discoverable: UndefinedOr[:class:`bool`]
            Whether this server is public and should show up on `Revolt Discover <https://rvlt.gg>`_.

            The new server flags. You must be a privileged user to provide this.
        analytics: UndefinedOr[:class:`bool`]
            Whether analytics should be collected for this server. Must be enabled in order to show up on `Revolt Discover <https://rvlt.gg>`_.
        owner: UndefinedOr[Union[:class:`str`, :class:`.BaseUser`, :class:`.BaseMember`]]
            The member to transfer ownership to.

            You must own the server, or be a privileged user to provide this.

            The target user must be not a bot.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+--------------------------------------------+
            | Value                | Reason                                     |
            +----------------------+--------------------------------------------+
            | ``FailedValidation`` | The payload was invalid.                   |
            +----------------------+--------------------------------------------+
            | ``InvalidOperation`` | One of these:                              |
            |                      |                                            |
            |                      | - More than 2 categories had same channel. |
            |                      | - You tried to transfer ownership to bot.  |
            +----------------------+--------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+----------------------------------------+
            | Value                  | Reason                                 |
            +------------------------+----------------------------------------+
            | ``InvalidCredentials`` | The provided MFA ticket was invalid.   |
            +------------------------+----------------------------------------+
            | ``InvalidSession``     | The current bot/user token is invalid. |
            +------------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+----------------------------------------------------------------------------------------------+
            | Value                 | Reason                                                                                       |
            +-----------------------+----------------------------------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to edit server details.                               |
            +-----------------------+----------------------------------------------------------------------------------------------+
            | ``NotOwner``          | You provided ``owner`` parameter but you do not own the server or are not a privileged user. |
            +-----------------------+----------------------------------------------------------------------------------------------+
            | ``NotPrivileged``     | You provided ``discoverable`` or ``flags`` parameters but you are not a privileged user.     |
            +-----------------------+----------------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------------------------------------------+
            | Value        | Reason                                                         |
            +--------------+----------------------------------------------------------------+
            | ``NotFound`` | One of these:                                                  |
            |              |                                                                |
            |              | - The server was not found.                                    |
            |              | - One of channels in one of provided categories was not found. |
            +--------------+----------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Server`
            The newly updated server.
        """
        return await self.state.http.edit_server(
            self.id,
            http_overrides=http_overrides,
            mfa_ticket=mfa_ticket,
            name=name,
            description=description,
            icon=icon,
            banner=banner,
            categories=categories,
            system_messages=system_messages,
            flags=flags,
            discoverable=discoverable,
            analytics=analytics,
            owner=owner,
        )

    async def fetch(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        populate_channels: typing.Optional[bool] = None,
    ) -> Server:
        """|coro|

        Retrieves the server.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        populate_channels: Optional[:class:`bool`]
            Whether to populate :attr:`Server.channels`.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+

        Returns
        -------
        :class:`.Server`
            The retrieved server.
        """
        return await self.state.http.get_server(
            self.id, http_overrides=http_overrides, populate_channels=populate_channels
        )

    async def fetch_bans(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> list[Ban]:
        """|coro|

        Retrieves all bans on the server.

        You must have :attr:`~Permissions.ban_members` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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

            +-----------------------+--------------------------------------------------------------+
            | Value                 | Reason                                                       |
            +-----------------------+--------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to retrieve all bans. |
            +-----------------------+--------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`.Ban`]
            The ban entries.
        """
        return await self.state.http.get_bans(self.id, http_overrides=http_overrides)

    async def fetch_emojis(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> list[ServerEmoji]:
        """|coro|

        Retrieves all custom :class:`ServerEmoji`'s that belong to the server.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`.ServerEmoji`]
            The retrieved emojis.
        """
        return await self.state.http.get_server_emojis(self.id, http_overrides=http_overrides)

    async def fetch_invites(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> list[ServerInvite]:
        """|coro|

        Retrieves all invites that belong to the server.

        You must have :attr:`~Permissions.manage_server` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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

            +-----------------------+--------------------------------------------------------------------+
            | Value                 | Reason                                                             |
            +-----------------------+--------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to retrieve server invites. |
            +-----------------------+--------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`.ServerInvite`]
            The retrieved invites.
        """
        return await self.state.http.get_server_invites(self.id, http_overrides=http_overrides)

    async def fetch_member(
        self,
        member: typing.Union[str, BaseUser, BaseMember],
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> Member:
        """|coro|

        Retrieves a member.

        Parameters
        ----------
        member: Union[:class:`str`, :class:`.BaseUser`, :class:`.BaseMember`]
            The user to retrieve.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Member`
            The retrieved member.
        """
        return await self.state.http.get_member(self.id, member, http_overrides=http_overrides)

    async def fetch_members(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        exclude_offline: typing.Optional[bool] = None,
    ) -> list[Member]:
        """|coro|

        Retrieves all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        exclude_offline: Optional[:class:`bool`]
            Whether to exclude offline users.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`.Member`]
            The retrieved members.
        """
        return await self.state.http.get_members(
            self.id, http_overrides=http_overrides, exclude_offline=exclude_offline
        )

    async def fetch_member_list(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        exclude_offline: typing.Optional[bool] = None,
    ) -> MemberList:
        """|coro|

        Retrieves server member list.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        exclude_offline: Optional[:class:`bool`]
            Whether to exclude offline users.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.MemberList`
            The member list.
        """
        return await self.state.http.get_member_list(
            self.id, http_overrides=http_overrides, exclude_offline=exclude_offline
        )

    async def fetch_role(
        self, role: ULIDOr[BaseRole], *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> Role:
        """|coro|

        Retrieves a server role.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        role: ULIDOr[:class:`.BaseRole`]
            The role to retrieve.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/role was not found. |
            +--------------+--------------------------------+

        Returns
        -------
        :class:`.Role`
            The retrieved role.
        """
        return await self.state.http.get_role(self.id, role, http_overrides=http_overrides)

    async def join(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> Server:
        """|coro|

        Joins the server.

        Fires :class:`ServerCreateEvent` for the current user, :class:`ServerMemberJoinEvent` and optionally :class:`MessageCreateEvent`,
        both for all server members.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-------------------------------------------+
            | Value              | Reason                                    |
            +--------------------+-------------------------------------------+
            | ``IsBot``          | The current token belongs to bot account. |
            +--------------------+-------------------------------------------+
            | ``TooManyServers`` | You're participating in too many servers. |
            +--------------------+-------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +------------+----------------------------+
            | Value      | Reason                     |
            +------------+----------------------------+
            | ``Banned`` | You're banned from server. |
            +------------+----------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+------------------------------------------+
            | Value        | Reason                                   |
            +--------------+------------------------------------------+
            | ``NotFound`` | The invite/channel/server was not found. |
            +--------------+------------------------------------------+
        :class:`Conflict`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------+--------------------------------+
            | Value               | Reason                         |
            +---------------------+--------------------------------+
            | ``AlreadyInServer`` | The user is already in server. |
            +---------------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Server`
            The server you just joined.
        """
        server = await self.state.http.accept_invite(self.id, http_overrides=http_overrides)
        return server  # type: ignore

    async def kick(
        self,
        member: typing.Union[str, BaseUser, BaseMember],
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> None:
        """|coro|

        Kicks a member from the server.

        Fires :class:`.ServerMemberRemoveEvent` for kicked user and all server members.

        Parameters
        ----------
        member: Union[:class:`str`, :class:`.BaseUser`, :class:`.BaseMember`]
            The member to kick.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------------+---------------------------------+
            | Value                    | Reason                          |
            +--------------------------+---------------------------------+
            | ``CannotRemoveYourself`` | You tried to kick yourself.     |
            +--------------------------+---------------------------------+
            | ``InvalidOperation``     | You tried to kick server owner. |
            +--------------------------+---------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+-------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                              |
            +----------------------------------+-------------------------------------------------------------------------------------+
            | ``NotElevated``                  | Rank of your top role is higher than rank of top role of user you're trying to ban. |
            +----------------------------------+-------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to ban members.                              |
            +----------------------------------+-------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/user was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """
        return await self.state.http.kick_member(self.id, member, http_overrides=http_overrides)

    async def leave(
        self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None, silent: typing.Optional[bool] = None
    ) -> None:
        """|coro|

        Leaves a server if not owner, or deletes otherwise.

        Fires :class:`.ServerMemberRemoveEvent` or :class:`.ServerDeleteEvent` (if owner) for all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        silent: Optional[:class:`bool`]
            Whether to silently leave server or not.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-----------------------------------------+
            | Value              | Reason                                  |
            +--------------------+-----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid.  |
            +--------------------+-----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """
        return await self.state.http.leave_server(self.id, http_overrides=http_overrides, silent=silent)

    async def mark_server_as_read(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Marks all channels in a server as read.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.mark_server_as_read(self.id, http_overrides=http_overrides)

    async def query_members_by_name(
        self, query: str, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> list[Member]:
        """|coro|

        Query members by a given name.

        .. warning::
            This API is not stable and may be removed in the future.

        Parameters
        ----------
        query: :class:`str`
            The query to search members for.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`.Member`]
            The members matched.
        """
        return await self.state.http.query_members_by_name(self.id, query)

    async def report(
        self,
        reason: ContentReportReason,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        additional_context: typing.Optional[str] = None,
    ) -> None:
        """|coro|

        Report the server to the instance moderation team.

        Fires :class:`.ReportCreateEvent` internally (but not fired over WebSocket).

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        reason: :class:`.ContentReportReason`
            The reason for reporting.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        additional_context: Optional[:class:`str`]
            The additional context for moderation team. Can be only up to 1000 characters.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------------+--------------------------------------+
            | Value                    | Reason                               |
            +--------------------------+--------------------------------------+
            | ``CannotReportYourself`` | You tried to report your own server. |
            +--------------------------+--------------------------------------+
            | ``FailedValidation``     | The payload was invalid.             |
            +--------------------------+--------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The server was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.report_server(
            self.id, reason, http_overrides=http_overrides, additional_context=additional_context
        )

    async def set_role_permissions(
        self,
        role: ULIDOr[BaseRole],
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        allow: Permissions = Permissions.none(),
        deny: Permissions = Permissions.none(),
    ) -> Server:
        """|coro|

        Sets permissions for the specified server role.

        You must have :attr:`~Permissions.manage_permissions` to do this.

        Fires :class:`.RawServerRoleUpdateEvent` for all server members.

        Parameters
        ----------
        role: ULIDOr[:class:`.BaseRole`]
            The role.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        allow: :class:`.Permissions`
            The permissions to allow for the specified role.
        deny: :class:`.Permissions`
            The permissions to deny for the specified role.

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

            +----------------------------------+--------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                               |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``CannotGiveMissingPermissions`` | Your new provided permissions contained permissions you didn't have.                 |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``NotElevated``                  | Rank of your top role is higher than rank of role you're trying to set override for. |
            +----------------------------------+--------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to edit permissions for this role.            |
            +----------------------------------+--------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/role was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Server`
            The updated server with new permissions.
        """
        return await self.state.http.set_server_permissions_for_role(
            self.id, role, http_overrides=http_overrides, allow=allow, deny=deny
        )

    async def set_default_permissions(
        self, permissions: Permissions, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> Server:
        """|coro|

        Sets default permissions for everyone in a server.

        You must have :attr:`~Permissions.manage_permissions` to do this.

        Fires :class:`.ServerUpdateEvent` for all server members.

        Parameters
        ----------
        permissions: :class:`.Permissions`
            The new permissions.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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

            +----------------------------------+-------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                              |
            +----------------------------------+-------------------------------------------------------------------------------------+
            | ``CannotGiveMissingPermissions`` | Your new provided permissions contained permissions you didn't have.                |
            +----------------------------------+-------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to edit default permissions for this server. |
            +----------------------------------+-------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------+
            | Value        | Reason                     |
            +--------------+----------------------------+
            | ``NotFound`` | The channel was not found. |
            +--------------+----------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Server`
            The newly updated server.
        """

        return await self.state.http.set_default_server_permissions(self.id, permissions, http_overrides=http_overrides)

    async def subscribe(self) -> None:
        """|coro|

        Subscribes to this server.
        """
        await self.state.shard.subscribe_to(self.id)

    async def unban(
        self, user: ULIDOr[BaseUser], *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> None:
        """|coro|

        Unbans an user from the server.

        You must have :attr:`~Permissions.ban_members` to do this.

        Parameters
        ----------
        user: ULIDOr[:class:`.BaseUser`]
            The user to unban from the server.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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

            +-----------------------+----------------------------------------------------------+
            | Value                 | Reason                                                   |
            +-----------------------+----------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to unban members. |
            +-----------------------+----------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.unban(self.id, user, http_overrides=http_overrides)


@define(slots=True)
class PartialServer(BaseServer):
    """Represents a partial server on Revolt.

    Unmodified fields will have ``UNDEFINED`` value.

    This inherits from :class:`.BaseServer`.
    """

    name: UndefinedOr[str] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`str`]: The new server's name."""

    owner_id: UndefinedOr[str] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`str`]: The new user's ID who owns this server."""

    description: UndefinedOr[typing.Optional[str]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`str`]]: The new server's description."""

    channel_ids: UndefinedOr[list[str]] = field(repr=True, kw_only=True)
    """UndefinedOr[List[:class:`str`]]: The server's channels now."""

    categories: UndefinedOr[typing.Optional[list[Category]]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[List[:class:`.Category`]]]: The server's categories now."""

    system_messages: UndefinedOr[typing.Optional[SystemMessageChannels]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`.SystemMessageChannels`]]: The new server's system message assignments."""

    raw_default_permissions: UndefinedOr[int] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`int`]: The raw value of new default permissions for everyone."""

    internal_icon: UndefinedOr[typing.Optional[StatelessAsset]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`.StatelessAsset`]]: The new server's icon, if any."""

    internal_banner: UndefinedOr[typing.Optional[StatelessAsset]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`.StatelessAsset`]]: The new server's banner, if any."""

    raw_flags: UndefinedOr[int] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`int`]: The new server's flags raw value."""

    discoverable: UndefinedOr[bool] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`bool`]: Whether the server is publicly discoverable."""

    analytics: UndefinedOr[bool] = field(repr=True, kw_only=True)
    """UndefinedOr[:class:`bool`]: Whether the server activity is being analyzed in real-time."""

    @property
    def default_permissions(self) -> UndefinedOr[Permissions]:
        """UndefinedOr[:class:`.Permissions`]: The new default permissions for everyone."""
        if self.raw_default_permissions is UNDEFINED:
            return self.raw_default_permissions
        ret = _new_permissions(Permissions)
        ret.value = self.raw_default_permissions
        return ret

    @property
    def flags(self) -> UndefinedOr[ServerFlags]:
        """UndefinedOr[:class:`.ServerFlags`]: The new server's flags."""
        if self.raw_flags is UNDEFINED:
            return self.raw_flags
        ret = _new_server_flags(ServerFlags)
        ret.value = self.raw_flags
        return ret

    @property
    def icon(self) -> UndefinedOr[typing.Optional[Asset]]:
        """UndefinedOr[Optional[:class:`.Asset`]]: The stateful server icon."""
        return self.internal_icon and self.internal_icon.attach_state(self.state, 'icons')

    @property
    def banner(self) -> UndefinedOr[typing.Optional[Asset]]:
        """UndefinedOr[Optional[:class:`.Asset`]]: The stateful server banner."""
        return self.internal_banner and self.internal_banner.attach_state(self.state, 'banners')


def sort_member_roles(
    target_role_ids: list[str],
    /,
    *,
    safe: bool = True,
    server_roles: dict[str, Role],
) -> list[Role]:
    """Sorts the member roles.

    Parameters
    ----------
    target_role_ids: List[:class:`str`]
        The IDs of roles to sort (:attr:`.Member.role_ids`).
    safe: :class:`bool`
        Whether to raise exception or not if role is missing in cache.
    server_roles: Dict[:class:`str`, :class:`.Role`]
        The mapping of role IDs to role objects (:attr:`.Server.roles`).

    Raises
    ------
    NoData
        The role is not found in cache.

    Returns
    -------
    List[:class:`.Role`]
        The sorted result, in ascending order.
    """
    if not safe:
        return sorted(
            (server_roles[tr] for tr in target_role_ids if tr in server_roles),
            key=lambda role: role.rank,
            reverse=True,
        )
    try:
        return sorted(
            (server_roles[tr] for tr in target_role_ids),
            key=lambda role: role.rank,
            reverse=True,
        )
    except KeyError as ke:
        raise NoData(what=ke.args[0], type='Role')


def calculate_server_permissions(
    target_roles: list[Role],
    target_timeout: typing.Optional[datetime],
    /,
    *,
    default_permissions: Permissions,
    can_publish: bool = True,
    can_receive: bool = True,
) -> Permissions:
    """Calculates the permissions in :class:`.Server` scope.

    Parameters
    ----------
    target_roles: List[:class:`.Role`]
        The target member's roles. Should be empty list if calculating against :class:`.User`,
        or ``pyvolt.sort_member_roles(member.roles, server_roles=server.roles)`` if calculating
        against member.
    target_timeout: Optional[:class:`~datetime.datetime`]
        The target timeout, if applicable (:attr:`.Member.timed_out_until`).
    default_permissions: :class:`Permissions`
        The default channel permissions (:attr:`.Server.default_permissions`).
    can_publish: :class:`bool`
        Whether the member can send voice data. Defaults to ``True``.
    can_receive: :class:`bool`
        Whether the member can receive voice data. Defaults to ``True``.

    Returns
    -------
    :class:`.Permissions`
        The calculated permissions.
    """
    result = default_permissions.copy()

    for role in target_roles:
        result |= role.permissions.allow
        result &= ~role.permissions.deny

    if target_timeout is not None and target_timeout <= utils.utcnow():
        result.send_messages = False

    if not can_publish:
        result.speak = False

    if not can_receive:
        result.listen = False

    return result


@define(slots=True)
class Server(BaseServer):
    """Represents a server on Revolt.

    This inherits from :class:`.BaseServer`.
    """

    owner_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID who owns this server."""

    name: str = field(repr=True, kw_only=True)
    """:class:`str`: The server's name."""

    description: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The server's description."""

    internal_channels: tuple[typing.Literal[True], list[str]] | tuple[typing.Literal[False], list[ServerChannel]] = (
        field(repr=True, kw_only=True)
    )

    categories: typing.Optional[list[Category]] = field(repr=True, kw_only=True)
    """Optional[List[:class:`.Category`]]: The server's categories."""

    system_messages: typing.Optional[SystemMessageChannels] = field(repr=True, kw_only=True)
    """Optional[:class:`.SystemMessageChannels`]: The configuration for sending system event messages."""

    roles: dict[str, Role] = field(repr=True, kw_only=True)
    """Dict[:class:`str`, :class:`.Role`]: The server's roles."""

    raw_default_permissions: int = field(repr=True, kw_only=True)
    """:class:`int`: The raw value of default permissions for everyone."""

    internal_icon: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`.StatelessAsset`]: The stateless server's icon."""

    internal_banner: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`.StatelessAsset`]: The stateless server's banner."""

    raw_flags: int = field(repr=True, kw_only=True)
    """:class:`int`: The server's flags raw value."""

    nsfw: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the server is flagged as not safe for work."""

    analytics: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the server activity is being analyzed in real-time."""

    discoverable: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the server is publicly discoverable."""

    def get_channel(self, channel_id: str, /) -> typing.Optional[ServerChannel]:
        """Retrieves a server channel from cache.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel ID.

        Returns
        -------
        Optional[:class:`.ServerChannel`]
            The channel or ``None`` if not found.
        """
        state = self.state
        cache = state.cache

        if cache is None:
            return

        from .channel import ServerChannel

        ctx = (
            ChannelThroughServerGetterCacheContext(
                type=CacheContextType.channel_through_server_getter,
                server=self,
            )
            if state.provide_cache_context('Server.get_channel()')
            else _CHANNEL_THROUGH_SERVER_GETTER
        )

        channel = cache.get_channel(channel_id, ctx)
        if channel is not None:
            assert isinstance(channel, ServerChannel)
            if channel.server_id != self.id and not len(channel.server_id):
                return None
            return channel

        if self.internal_channels[0]:
            return None

        for ch in self.internal_channels[1]:
            t: ServerChannel = ch  # type: ignore
            if t.id == channel_id:
                return t

    def get_me(self) -> typing.Optional[Member]:
        """Optional[:class:`.Member`]: The own user for this server."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        state.my_id

        ctx = (
            MemberThroughServerMeCacheContext(
                type=CacheContextType.member_through_server_me,
                server=self,
            )
            if state.provide_cache_context('Server.me')
            else _MEMBER_THROUGH_SERVER_ME
        )

        return cache.get_server_member(self.id, state.my_id, ctx)

    def get_owner(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`.Member`, :class:`.User`]]: The server's owner."""

        state = self.state
        cache = state.cache

        if cache is None:
            return

        ctx = (
            MemberOrUserThroughServerOwnerCacheContext(
                type=CacheContextType.member_or_user_through_server_owner,
                server=self,
            )
            if state.provide_cache_context('Server.owner')
            else _MEMBER_OR_USER_THROUGH_SERVER_OWNER
        )

        member = cache.get_server_member(self.id, self.owner_id, ctx)
        if member is None:
            return cache.get_user(self.owner_id, ctx)
        return member

    def get_owner_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`.Member`]: The server's owner."""

        state = self.state
        cache = state.cache

        if cache is None:
            return

        ctx = (
            MemberThroughServerOwnerCacheContext(
                type=CacheContextType.member_through_server_owner,
                server=self,
            )
            if state.provide_cache_context('Server.owner_as_member')
            else _MEMBER_THROUGH_SERVER_OWNER
        )

        return cache.get_server_member(self.id, self.owner_id, ctx)

    def get_owner_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`.User`]: The server's owner."""

        state = self.state
        cache = state.cache

        if cache is None:
            return

        ctx = (
            UserThroughServerOwnerCacheContext(
                type=CacheContextType.user_through_server_owner,
                server=self,
            )
            if state.provide_cache_context('Server.owner_as_user')
            else _USER_THROUGH_SERVER_OWNER
        )

        return cache.get_user(self.owner_id, ctx)

    @property
    def banner(self) -> typing.Optional[Asset]:
        """Optional[:class:`.Asset`]: The server banner."""
        return self.internal_banner and self.internal_banner.attach_state(self.state, 'banners')

    @property
    def channel_ids(self) -> list[str]:
        """List[:class:`str`]: The IDs of channels within this server."""
        if self.internal_channels[0]:
            return self.internal_channels[1]  # type: ignore
        else:
            return [channel.id for channel in self.internal_channels[1]]  # type: ignore

    @property
    def channels(self) -> list[ServerChannel]:
        """List[:class:`.ServerChannel`]: The channels within this server."""

        if not self.internal_channels[0]:
            return self.internal_channels[1]  # type: ignore

        state = self.state
        cache = state.cache

        if cache is None:
            return []

        from .channel import TextChannel, VoiceChannel

        ctx = (
            ChannelsThroughServerGetterCacheContext(
                type=CacheContextType.channels_through_server_getter,
                server=self,
            )
            if state.provide_cache_context('Server.channels')
            else _CHANNELS_THROUGH_SERVER_GETTER
        )

        channels = []
        for channel_id in self.internal_channels[1]:
            id: str = channel_id  # type: ignore
            channel = cache.get_channel(id, ctx)

            if channel is not None:
                if channel.__class__ not in (
                    TextChannel,
                    VoiceChannel,
                ) or not isinstance(channel, (TextChannel, VoiceChannel)):
                    raise TypeError(f'Cache have given us incorrect channel type: {channel.__class__!r}')
                channels.append(channel)
        return channels

    @property
    def default_permissions(self) -> Permissions:
        """:class:`.Permissions`: The default permissions for everyone."""
        ret = _new_permissions(Permissions)
        ret.value = self.raw_default_permissions
        return ret

    @property
    def flags(self) -> ServerFlags:
        """:class:`.ServerFlags`: The server's flags."""
        ret = _new_server_flags(ServerFlags)
        ret.value = self.raw_flags
        return ret

    @property
    def icon(self) -> typing.Optional[Asset]:
        """Optional[:class:`.Asset`]: The server icon."""
        return self.internal_icon and self.internal_icon.attach_state(self.state, 'icons')

    @property
    def me(self) -> Member:
        """:class:`.Member`: The own user for this server."""

        me = self.get_me()
        if me is None:
            raise NoData(what='', type='Server.me')
        return me

    @property
    def owner(self) -> typing.Union[Member, User]:
        """Union[:class:`.Member`, :class:`.User`]: The server's owner."""

        owner = self.get_owner()
        if owner is None:
            raise NoData(what=self.owner_id, type='Server.owner')
        return owner

    @property
    def owner_as_member(self) -> Member:
        """:class:`.Member`: The server's owner."""

        owner = self.get_owner_as_member()
        if owner is None:
            raise NoData(what=self.owner_id, type='Server.owner_as_member')
        return owner

    @property
    def owner_as_user(self) -> User:
        """:class:`.User`: The server's owner."""

        owner = self.get_owner_as_user()
        if owner is None:
            raise NoData(what=self.owner_id, type='Server.owner_as_user')
        return owner

    def is_verified(self) -> bool:
        """:class:`bool`: Whether the server is verified."""
        return self.flags.verified

    def is_official(self) -> bool:
        """:class:`bool`: Whether the server is ran by Revolt team."""
        return self.flags.official

    def locally_update(self, data: PartialServer, /) -> None:
        """Locally updates server with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.
            You likely want to use :meth:`.BaseServer.edit` method instead.
        """
        if data.owner_id is not UNDEFINED:
            self.owner_id = data.owner_id
        if data.name is not UNDEFINED:
            self.name = data.name
        if data.description is not UNDEFINED:
            self.description = data.description
        if data.channel_ids is not UNDEFINED:
            self.internal_channels = (True, data.channel_ids)
        if data.categories is not UNDEFINED:
            self.categories = data.categories or []
        if data.system_messages is not UNDEFINED:
            self.system_messages = data.system_messages
        if data.raw_default_permissions is not UNDEFINED:
            self.raw_default_permissions = data.raw_default_permissions
        if data.internal_icon is not UNDEFINED:
            self.internal_icon = data.internal_icon
        if data.internal_banner is not UNDEFINED:
            self.internal_banner = data.internal_banner
        if data.raw_flags is not UNDEFINED:
            self.raw_flags = data.raw_flags
        if data.discoverable is not UNDEFINED:
            self.discoverable = data.discoverable
        if data.analytics is not UNDEFINED:
            self.analytics = data.analytics

    def permissions_for(
        self,
        member: typing.Union[Member, User],
        /,
        *,
        safe: bool = True,
        with_ownership: bool = True,
        include_timeout: bool = True,
    ) -> Permissions:
        """Calculate permissions for given member.

        Parameters
        ----------
        member: Union[:class:`.Member`, :class:`.User`]
            The member to calculate permissions for.
        safe: :class:`bool`
            Whether to raise exception or not if role is missing in cache.
        with_ownership: :class:`bool`
            Whether to account for ownership.
        include_timeout: :class:`bool`
            Whether to account for timeout.

        Raises
        ------
        NoData
            The role is not found in cache.

        Returns
        -------
        :class:`Permissions`
            The calculated permissions.
        """

        if with_ownership and member.id == self.owner_id:
            return Permissions.all()

        if isinstance(member, User):
            return calculate_server_permissions([], None, default_permissions=self.default_permissions)

        return calculate_server_permissions(
            sort_member_roles(member.role_ids, safe=safe, server_roles=self.roles),
            member.timed_out_until if include_timeout else None,
            default_permissions=self.default_permissions,
            can_publish=member.can_publish,
            can_receive=member.can_receive,
        )

    def prepare_cached(self) -> list[ServerChannel]:
        """List[:class:`.ServerChannel`]: Prepares the server to be cached."""
        if self.internal_channels[0]:
            return []
        channels = self.internal_channels[1]
        self.internal_channels = (True, self.channel_ids)
        return channels  # type: ignore

    @typing.overload
    def to_dict(self, *, with_channels: typing.Literal[False] = ...) -> raw.Server: ...

    @typing.overload
    def to_dict(self, *, with_channels: typing.Literal[True]) -> raw.ServerWithChannels: ...

    def to_dict(self, *, with_channels: bool = False) -> typing.Union[raw.ServerWithChannels, raw.Server]:
        """:class:`dict`: Convert server to raw data.

        Parameters
        ----------
        with_channels: :class:`bool`
            Whether to include channel objects instead of their IDs in ``channels`` key when serializing. Defaults to ``False``.
        """
        payload: dict[str, typing.Any] = {
            '_id': self.id,
            'owner': self.owner_id,
            'name': self.name,
        }
        if self.description is not None:
            payload['description'] = self.description
        if with_channels:
            payload['channels'] = [channel.to_dict() for channel in self.channels]
        else:
            payload['channels'] = self.channel_ids
        if self.categories is not None:
            payload['categories'] = [category.to_dict() for category in self.categories]
        if self.system_messages is not None:
            payload['system_messages'] = self.system_messages.to_dict()

        if len(self.roles):
            payload['roles'] = {k: v.to_dict() for k, v in self.roles.items()}
        payload['default_permissions'] = self.raw_default_permissions
        if self.internal_icon is not None:
            payload['icon'] = self.internal_icon.to_dict('icons')
        if self.internal_banner is not None:
            payload['banner'] = self.internal_banner.to_dict('banners')
        if self.raw_flags != 0:
            payload['flags'] = self.raw_flags
        if self.nsfw:
            payload['nsfw'] = self.nsfw
        if self.analytics:
            payload['analytics'] = self.analytics
        if self.discoverable:
            payload['discoverable'] = self.discoverable
        return payload  # type: ignore

    def upsert_role(self, role: typing.Union[PartialRole, Role], /) -> None:
        """Locally upserts role into :attr:`Server.roles` mapping.

        .. warning::
            This is called by library internally to keep cache up to date.
            You likely want to use :meth:`BaseServer.create_role` or :meth:`BaseRole.edit` instead.

        Parameters
        ----------
        role: Union[:class:`.PartialRole`, :class:`.Role`]
            The role to upsert.
        """
        if isinstance(role, PartialRole):
            self.roles[role.id].locally_update(role)
        else:
            self.roles[role.id] = role


@define(slots=True)
class Ban:
    """Represents a server ban on Revolt."""

    server_id: str = field(repr=False, kw_only=True)
    """:class:`str`: The server's ID."""

    user_id: str = field(repr=False, kw_only=True)
    """:class:`str`: The user's ID that was banned."""

    reason: typing.Optional[str] = field(repr=False, kw_only=True)
    """Optional[:class:`str`]: The ban's reason."""

    user: typing.Optional[DisplayUser] = field(repr=False, kw_only=True)
    """Optional[:class:`.DisplayUser`]: The user that was banned."""

    def __hash__(self) -> int:
        return hash((self.server_id, self.user_id))

    def __eq__(self, other: object, /) -> bool:
        return (
            self is other
            or isinstance(other, Ban)
            and (self.server_id == other.server_id and self.user_id == other.user_id)
        )

    def to_dict(self) -> raw.ServerBan:
        """:class:`dict`: Convert server ban to raw data."""
        return {
            '_id': {
                'server': self.server_id,
                'user': self.user_id,
            },
            'reason': self.reason,
        }


@define(slots=True)
class BaseMember(Connectable, Messageable):
    """Represents a Revolt base member to a :class:`Server`.

    This inherits from :class:`~pyvolt.abc.Connectable` and :class:`~pyvolt.abc.Messageable`.
    """

    state: State = field(repr=False, kw_only=True)
    """:class:`.State`: State that controls this member."""

    server_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The server's ID the member in."""

    internal_user: typing.Union[User, str] = field(repr=True, kw_only=True)
    """Union[:class:`.User`, :class:`str`]: The ID of the user, or full user instance."""

    def get_bot_owner(self) -> tuple[typing.Optional[User], str]:
        """Returns the user who created this bot user.

        Returns
        -------
        Tuple[Optional[:class:`.User`], :class:`str`]
            The bot owner and their ID (may be empty if user is not a bot).
        """

        if isinstance(self.internal_user, User):
            return self.internal_user.get_bot_owner()

        state = self.state
        cache = state.cache

        if cache is None:
            return (None, '')

        ctx = (
            UserThroughMemberBotOwnerCacheContext(
                type=CacheContextType.user_through_member_bot_owner,
                member=self,
            )
            if state.provide_cache_context('Member.bot_owner')
            else _USER_THROUGH_MEMBER_BOT_OWNER
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return (None, '')

        bot = user.bot

        if bot is None:
            return (None, '')

        return (cache.get_user(bot.owner_id, ctx), bot.owner_id)

    def get_channel_id(self) -> str:
        return self.dm_channel_id or ''

    def get_server(self) -> typing.Optional[Server]:
        """Optional[:class:`.Server`]: The server this member belongs to."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ServerThroughMemberServerCacheContext(
                type=CacheContextType.server_through_member_server,
                member=self,
            )
            if state.provide_cache_context('Member.server')
            else _SERVER_THROUGH_MEMBER_SERVER
        )

        return cache.get_server(self.server_id, ctx)

    def get_user(self) -> typing.Optional[User]:
        """Optional[:class:`.User`]: The user."""
        if isinstance(self.internal_user, User):
            return self.internal_user

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughMemberUserCacheContext(
                type=CacheContextType.user_through_member_user,
                member=self,
            )
            if state.provide_cache_context('Member.user')
            else _USER_THROUGH_MEMBER_USER
        )

        return cache.get_user(self.internal_user, ctx)

    def __eq__(self, other: object, /) -> bool:
        if self is other:
            return True

        return isinstance(other, (BaseMember, BaseUser)) and self.id == other.id

    def eq(self, other: object, /) -> bool:
        """:class:`bool`: Checks whether two members are equal.

        .. versionadded:: 1.2
        """
        if self is other:
            return True

        return (
            (isinstance(other, BaseMember) and self.server_id == other.server_id) or isinstance(other, BaseUser)
        ) and self.id == other.id

    def __ne__(self, other: object, /) -> bool:
        if self is other:
            return False

        if isinstance(other, (BaseMember, BaseUser)):
            return self.id != other.id

        return True

    def ne(self, other: object, /) -> bool:
        """:class:`bool`: Checks whether two members are not equal.

        .. versionadded:: 1.2
        """
        if self is other:
            return False

        if isinstance(other, BaseMember):
            return self.server_id != other.server_id and self.id != other.id

        if isinstance(other, BaseUser):
            return self.id != other.id

        return True

    def __hash__(self) -> int:
        return hash((self.server_id, self.id))

    def __str__(self) -> str:
        user = self.get_user()
        return '' if user is None else str(user)

    @property
    def user(self) -> User:
        """:class:`.User`: The user."""

        user = self.get_user()
        if user is None:
            raise NoData(
                what=self.id,
                type='Member.user',
            )
        return user

    @property
    def bot_owner(self) -> typing.Optional[User]:
        """Optional[:class:`.User`]: Returns the user who created this bot user."""

        bot_owner, bot_owner_id = self.get_bot_owner()
        if bot_owner is None and len(bot_owner_id):
            raise NoData(
                what=bot_owner_id,
                type='Member.bot_owner',
            )
        return bot_owner

    @property
    def id(self) -> str:
        """:class:`str`: The ID of the member user."""
        if isinstance(self.internal_user, User):
            return self.internal_user.id
        return self.internal_user

    @property
    def default_avatar_url(self) -> str:
        """:class:`str`: The URL to member user's default avatar."""
        return self.state.http.url_for(routes.USERS_GET_DEFAULT_AVATAR.compile(user_id=self.id))

    @property
    def mention(self) -> str:
        """:class:`str`: The member user mention."""
        return f'<@{self.id}>'

    @property
    def dm_channel_id(self) -> typing.Optional[str]:
        """Optional[:class:`str`]: The ID of the private channel with this member."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelIDThroughMemberDMChannelIDCacheContext(
                type=CacheContextType.channel_id_through_member_dm_channel_id,
                member=self,
            )
            if state.provide_cache_context('Member.dm_channel_id')
            else _CHANNEL_ID_THROUGH_MEMBER_DM_CHANNEL_ID
        )

        return cache.get_private_channel_by_user(self.id, ctx)

    pm_id = dm_channel_id

    @property
    def dm_channel(self) -> typing.Optional[DMChannel]:
        """Optional[:class:`.DMChannel`]: The private channel with this member."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelThroughMemberDMChannelCacheContext(
                type=CacheContextType.channel_through_member_dm_channel,
                member=self,
            )
            if state.provide_cache_context('Member.dm_channel')
            else _CHANNEL_THROUGH_MEMBER_DM_CHANNEL
        )

        channel_id = cache.get_private_channel_by_user(self.id, ctx)
        if channel_id is None:
            return None

        channel = cache.get_channel(channel_id, ctx)
        if channel is not None:
            from .channel import DMChannel

            assert isinstance(channel, DMChannel)

        return channel

    pm = dm_channel

    @property
    def name(self) -> str:
        """:class:`str`: The member's username."""
        if isinstance(self.internal_user, User):
            return self.internal_user.name

        state = self.state
        cache = state.cache

        if cache is None:
            return ''

        ctx = (
            UserThroughMemberNameCacheContext(
                type=CacheContextType.user_through_member_name,
                member=self,
            )
            if state.provide_cache_context('Member.name')
            else _USER_THROUGH_MEMBER_NAME
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return ''

        return user.name

    @property
    def discriminator(self) -> str:
        """:class:`str`: The member user's discriminator."""
        if isinstance(self.internal_user, User):
            return self.internal_user.discriminator

        state = self.state
        cache = state.cache

        if cache is None:
            return ''

        ctx = (
            UserThroughMemberDiscriminatorCacheContext(
                type=CacheContextType.user_through_member_discriminator,
                member=self,
            )
            if state.provide_cache_context('Member.discriminator')
            else _USER_THROUGH_MEMBER_DISCRIMINATOR
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return ''

        return user.discriminator

    @property
    def display_name(self) -> typing.Optional[str]:
        """Optional[:class:`str`]: The member user's display name."""
        if isinstance(self.internal_user, User):
            return self.internal_user.display_name

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughMemberDisplayNameCacheContext(
                type=CacheContextType.user_through_member_display_name,
                member=self,
            )
            if state.provide_cache_context('Member.display_name')
            else _USER_THROUGH_MEMBER_DISPLAY_NAME
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return None

        return user.display_name

    @property
    def internal_avatar(self) -> typing.Optional[StatelessAsset]:
        """Optional[:class:`.StatelessAsset`]: The stateless avatar of the member user."""
        if isinstance(self.internal_user, User):
            return self.internal_user.internal_avatar

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughMemberInternalAvatarCacheContext(
                type=CacheContextType.user_through_member_internal_avatar,
                member=self,
            )
            if state.provide_cache_context('Member.internal_avatar')
            else _USER_THROUGH_MEMBER_INTERNAL_AVATAR
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return None

        return user.internal_avatar

    @property
    def avatar(self) -> typing.Optional[Asset]:
        """Optional[:class:`.Asset`]: The avatar of the member user."""
        return self.internal_avatar and self.internal_avatar.attach_state(self.state, 'avatars')

    @property
    def raw_badges(self) -> int:
        """:class:`int`: The member user's badges raw value."""
        if isinstance(self.internal_user, User):
            return self.internal_user.raw_badges

        state = self.state
        cache = state.cache

        if cache is None:
            return 0

        ctx = (
            UserThroughMemberRawBadgesCacheContext(
                type=CacheContextType.user_through_member_raw_badges,
                member=self,
            )
            if state.provide_cache_context('Member.raw_badges')
            else _USER_THROUGH_MEMBER_RAW_BADGES
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return 0

        return user.raw_badges

    @property
    def badges(self) -> UserBadges:
        """:class:`.UserBadges`: The member user's badges."""
        ret = _new_user_badges(UserBadges)
        ret.value = self.raw_badges
        return ret

    @property
    def status(self) -> typing.Optional[UserStatus]:
        """Optional[:class:`.UserStatus`]: The current member user's status."""
        if isinstance(self.internal_user, User):
            return self.internal_user.status

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughMemberStatusCacheContext(
                type=CacheContextType.user_through_member_status,
                member=self,
            )
            if state.provide_cache_context('Member.status')
            else _USER_THROUGH_MEMBER_STATUS
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return None

        return user.status

    @property
    def raw_flags(self) -> int:
        """:class:`int`: The member user's flags raw value."""
        if isinstance(self.internal_user, User):
            return self.internal_user.raw_flags

        state = self.state
        cache = state.cache

        if cache is None:
            return 0

        ctx = (
            UserThroughMemberRawFlagsCacheContext(
                type=CacheContextType.user_through_member_raw_flags,
                member=self,
            )
            if state.provide_cache_context('Member.raw_flags')
            else _USER_THROUGH_MEMBER_RAW_FLAGS
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return 0

        return user.raw_flags

    @property
    def flags(self) -> UserFlags:
        """:class:`.UserFlags`: The member user's flags."""
        ret = _new_user_flags(UserFlags)
        ret.value = self.raw_flags
        return ret

    @property
    def privileged(self) -> bool:
        """:class:`bool`: Whether the member user is privileged."""
        if isinstance(self.internal_user, User):
            return self.internal_user.privileged

        state = self.state
        cache = state.cache

        if cache is None:
            return False

        ctx = (
            UserThroughMemberPrivilegedCacheContext(
                type=CacheContextType.user_through_member_privileged,
                member=self,
            )
            if state.provide_cache_context('Member.privileged')
            else _USER_THROUGH_MEMBER_PRIVILEGED
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return False

        return user.privileged

    @property
    def bot(self) -> typing.Optional[BotUserMetadata]:
        """Optional[:class:`.BotUserMetadata`]: The information about the bot."""
        if isinstance(self.internal_user, User):
            return self.internal_user.bot

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughMemberBotCacheContext(
                type=CacheContextType.user_through_member_bot,
                member=self,
            )
            if state.provide_cache_context('Member.bot')
            else _USER_THROUGH_MEMBER_BOT
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return None

        return user.bot

    @property
    def relationship(self) -> RelationshipStatus:
        """:class:`RelationshipStatus`: The current user's relationship with this member user."""
        if isinstance(self.internal_user, User):
            return self.internal_user.relationship

        state = self.state
        cache = state.cache

        if cache is None:
            return RelationshipStatus.none

        ctx = (
            UserThroughMemberRelationshipCacheContext(
                type=CacheContextType.user_through_member_relationship,
                member=self,
            )
            if state.provide_cache_context('Member.relationship')
            else _USER_THROUGH_MEMBER_RELATIONSHIP
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return RelationshipStatus.none

        return user.relationship

    @property
    def online(self) -> bool:
        """:class:`bool`: Whether the member user is currently online."""
        if isinstance(self.internal_user, User):
            return self.internal_user.online

        state = self.state
        cache = state.cache

        if cache is None:
            return False

        ctx = (
            UserThroughMemberOnlineCacheContext(
                type=CacheContextType.user_through_member_online,
                member=self,
            )
            if state.provide_cache_context('Member.online')
            else _USER_THROUGH_MEMBER_ONLINE
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return False

        return user.online

    @property
    def tag(self) -> str:
        """:class:`str`: The tag of the member user.

        Assuming that :attr:`Member.name` is ``'kotlin.Unit'`` and :attr:`Mmeber.discriminator` is ``'3510'``,
        example output would be ``'kotlin.Unit#3510'``.
        """
        if isinstance(self.internal_user, User):
            return self.internal_user.tag

        state = self.state
        cache = state.cache

        if cache is None:
            return ''

        ctx = (
            UserThroughMemberTagCacheContext(
                type=CacheContextType.user_through_member_tag,
                member=self,
            )
            if state.provide_cache_context('Member.tag')
            else _USER_THROUGH_MEMBER_TAG
        )

        user = cache.get_user(self.internal_user, ctx)

        if user is None:
            return ''

        return user.tag

    async def ban(
        self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None, reason: typing.Optional[str] = None
    ) -> Ban:
        """|coro|

        Bans an user from the server.

        You must have :attr:`~Permissions.ban_members` to do this.

        May fire :class:`.ServerMemberRemoveEvent` for banned user and all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        reason: Optional[:class:`str`]
            The ban reason. Can be only up to 1024 characters long.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------------+--------------------------------+
            | Value                    | Reason                         |
            +--------------------------+--------------------------------+
            | ``CannotRemoveYourself`` | You tried to ban yourself.     |
            +--------------------------+--------------------------------+
            | ``FailedValidation``     | The payload was invalid.       |
            +--------------------------+--------------------------------+
            | ``InvalidOperation``     | You tried to ban server owner. |
            +--------------------------+--------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+-------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                              |
            +----------------------------------+-------------------------------------------------------------------------------------+
            | ``NotElevated``                  | Rank of your top role is higher than rank of top role of user you're trying to ban. |
            +----------------------------------+-------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to ban members.                              |
            +----------------------------------+-------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/user was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Ban`
            The created ban.
        """

        return await self.state.http.ban(self.server_id, self.id, http_overrides=http_overrides, reason=reason)

    async def fetch_channel_id(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> str:
        channel_id = self.dm_channel_id
        if channel_id:
            return channel_id

        channel = await self.open_dm(http_overrides=http_overrides)
        return channel.id

    async def fetch_default_avatar(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> bytes:
        """|coro|

        Return a default user avatar based on the given ID.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Returns
        -------
        :class:`bytes`
            The image in PNG format.
        """
        return await self.state.http.get_default_avatar(self.id, http_overrides=http_overrides)

    async def fetch_flags(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> UserFlags:
        """|coro|

        Retrieves flags for user.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Returns
        -------
        :class:`.UserFlags`
            The retrieved flags.
        """
        return await self.state.http.get_user_flags(self.id, http_overrides=http_overrides)

    async def fetch_profile(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> UserProfile:
        """|coro|

        Retrieve profile of an user.

        You must have :attr:`~UserPermissions.view_profile` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +------------------------+----------------------------------------+
            | Value                  | Reason                                 |
            +------------------------+----------------------------------------+
            | ``InvalidSession``     | The current bot/user token is invalid. |
            +------------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+--------------------------------------------------------------+
            | Value                     | Reason                                                       |
            +---------------------------+--------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to view user profile. |
            +---------------------------+--------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+

        Returns
        -------
        :class:`.UserProfile`
            The retrieved user profile.
        """

        return await self.state.http.get_user_profile(self.id, http_overrides=http_overrides)

    async def edit(
        self,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        nick: UndefinedOr[typing.Optional[str]] = UNDEFINED,
        avatar: UndefinedOr[typing.Optional[ResolvableResource]] = UNDEFINED,
        roles: UndefinedOr[typing.Optional[list[ULIDOr[BaseRole]]]] = UNDEFINED,
        timeout: UndefinedOr[typing.Optional[typing.Union[datetime, timedelta, float, int]]] = UNDEFINED,
        can_publish: UndefinedOr[typing.Optional[bool]] = UNDEFINED,
        can_receive: UndefinedOr[typing.Optional[bool]] = UNDEFINED,
        voice: UndefinedOr[ULIDOr[typing.Union[TextChannel, VoiceChannel]]] = UNDEFINED,
    ) -> Member:
        """|coro|

        Edits the member.

        Fires :class:`.ServerMemberUpdateEvent` for all server members,
        and optionally fires multiple/single :class:`.ServerChannelCreateEvent` / :class:`.ChannelDeleteEvent` events for target member if ``roles`` parameter is provided.

        For Livekit instances:

        - If ``voice`` parameter is provided, fires :class:`.VoiceChannelMoveEvent` / :class:`.VoiceChannelLeaveEvent`
          if specified as ``None``, otherwise :class:`.VoiceChannelLeaveEvent` is fired. The specified events are fired for all users who can see voice channel the member is currently in.
        - If any of ``roles``, ``can_publish`` or ``can_receive`` parameters is provided, may fire :class:`.UserVoiceStateUpdateEvent` for all users who can see voice channel the member is currently in.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        nick: UndefinedOr[Optional[:class:`str`]]
            The member's new nick. Use ``None`` to remove the nickname.

            To provide this, you must have :attr:`~Permissions.manage_nicknames` if changing other member's nick.
            Otherwise, :attr:`~Permissions.change_nickname` is required instead.
        avatar: UndefinedOr[Optional[:class:`.ResolvableResource`]]
            The member's new avatar. Use ``None`` to remove the avatar.

            You can only change your own server avatar.

            You must have :attr:`~Permissions.change_avatar` to provide this.
        roles: UndefinedOr[Optional[List[ULIDOr[:class:`.BaseRole`]]]]
            The member's new list of roles. This *replaces* the roles.

            You must have :attr:`~Permissions.assign_roles` to provide this.
        timeout: UndefinedOr[Optional[Union[:class:`~datetime.datetime`, :class:`~datetime.timedelta`, :class:`float`, :class:`int`]]]
            The duration/date the member's timeout should expire, or ``None`` to remove the timeout.

            This must be a timezone-aware datetime object. Consider using :func:`pyvolt.utils.utcnow()`.

            You must have :attr:`~Permissions.timeout_members` to provide this.
        can_publish: UndefinedOr[Optional[:class:`bool`]]
            Whether the member should send voice data.

            You must have :attr:`~Permissions.mute_members` to provide this.
        can_receive: UndefinedOr[Optional[:class:`bool`]]
            Whether the member should receive voice data.

            You must have :attr:`~Permissions.deafen_members` to provide this.
        voice: UndefinedOr[ULIDOr[Union[:class:`.TextChannel`, :class:`.VoiceChannel`]]]
            The voice channel to move the member to.

            You must have :attr:`~Permissions.move_members` to provide this.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+-------------------------------------------------------------------------------------------------------------------+
            | Value                     | Reason                                                                                                            |
            +---------------------------+-------------------------------------------------------------------------------------------------------------------+
            | ``CannotTimeoutYourself`` | You tried to time out yourself.                                                                                   |
            +---------------------------+-------------------------------------------------------------------------------------------------------------------+
            | ``LivekitUnavailable``    | The voice server is unavailable. Only applicable to instances using Livekit.                                      |
            +---------------------------+-------------------------------------------------------------------------------------------------------------------+
            | ``NotAVoiceChannel``      | The channel passed in ``voice`` parameter was not voice-like channel. Only applicable to instances using Livekit. |
            +---------------------------+-------------------------------------------------------------------------------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-----------------------+----------------------------------------------------------------------------------+
            | Value                 | Reason                                                                           |
            +-----------------------+----------------------------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to edit this member.                      |
            +-----------------------+----------------------------------------------------------------------------------+
            | ``NotElevated``       | Ranking of one of roles you tried to add is lower than ranking of your top role. |
            +-----------------------+----------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+--------------------------------------------------------------------+
            | Value              | Reason                                                             |
            +--------------------+--------------------------------------------------------------------+
            | ``InvalidRole``    | One of provided roles passed in ``roles`` parameter was not found. |
            +--------------------+--------------------------------------------------------------------+
            | ``NotFound``       | The server/member was not found.                                   |
            +--------------------+--------------------------------------------------------------------+
            | ``UnknownChannel`` | The channel passed in ``voice`` parameter was not found.           |
            +--------------------+--------------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+-----------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                              | Populated attributes                                                |
            +-------------------+-----------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database.      | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+-----------------------------------------------------+---------------------------------------------------------------------+
            | ``InternalError`` | Somehow something went wrong during editing member. |                                                                     |
            +-------------------+-----------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Member`
            The newly updated member.
        """
        return await self.state.http.edit_member(
            self.server_id,
            self.id,
            http_overrides=http_overrides,
            nick=nick,
            avatar=avatar,
            roles=roles,
            timeout=timeout,
            can_publish=can_publish,
            can_receive=can_receive,
            voice=voice,
        )

    async def kick(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> None:
        """|coro|

        Kicks the member from the server.

        Fires :class:`.ServerMemberRemoveEvent` for kicked user and all server members.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------------+---------------------------------+
            | Value                    | Reason                          |
            +--------------------------+---------------------------------+
            | ``CannotRemoveYourself`` | You tried to kick yourself.     |
            +--------------------------+---------------------------------+
            | ``InvalidOperation``     | You tried to kick server owner. |
            +--------------------------+---------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------------------+-------------------------------------------------------------------------------------+
            | Value                            | Reason                                                                              |
            +----------------------------------+-------------------------------------------------------------------------------------+
            | ``NotElevated``                  | Rank of your top role is higher than rank of top role of user you're trying to ban. |
            +----------------------------------+-------------------------------------------------------------------------------------+
            | ``MissingPermission``            | You do not have the proper permissions to ban members.                              |
            +----------------------------------+-------------------------------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+--------------------------------+
            | Value        | Reason                         |
            +--------------+--------------------------------+
            | ``NotFound`` | The server/user was not found. |
            +--------------+--------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """
        return await self.state.http.kick_member(self.server_id, self.id, http_overrides=http_overrides)

    async def mutual_friend_ids(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> list[str]:
        """|coro|

        Retrieves a list of mutual friend user IDs with another user.

        You must have :attr:`~UserPermissions.view_profile` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+----------------------------------------------+
            | Value                | Reason                                       |
            +----------------------+----------------------------------------------+
            | ``InvalidOperation`` | You tried to retrieve mutuals with yourself. |
            +----------------------+----------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+--------------------------------------------------------------+
            | Value                     | Reason                                                       |
            +---------------------------+--------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to view user profile. |
            +---------------------------+--------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`str`]
            The found mutual friend user IDs.
        """

        mutuals = await self.state.http.get_mutuals_with(self.id, http_overrides=http_overrides)
        return mutuals.user_ids

    async def mutual_server_ids(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> list[str]:
        """|coro|

        Retrieves a list of mutual server IDs with another user.

        You must have :attr:`~UserPermissions.view_profile` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+----------------------------------------------+
            | Value                | Reason                                       |
            +----------------------+----------------------------------------------+
            | ``InvalidOperation`` | You tried to retrieve mutuals with yourself. |
            +----------------------+----------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+--------------------------------------------------------------+
            | Value                     | Reason                                                       |
            +---------------------------+--------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to view user profile. |
            +---------------------------+--------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        List[:class:`str`]
            The found mutual server IDs.
        """
        mutuals = await self.state.http.get_mutuals_with(self.id, http_overrides=http_overrides)
        return mutuals.server_ids

    async def mutuals(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> Mutuals:
        """|coro|

        Retrieves a list of mutual friends and servers with another user.

        You must have :attr:`~UserPermissions.view_profile` to do this.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +----------------------+----------------------------------------------+
            | Value                | Reason                                       |
            +----------------------+----------------------------------------------+
            | ``InvalidOperation`` | You tried to retrieve mutuals with yourself. |
            +----------------------+----------------------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+--------------------------------------------------------------+
            | Value                     | Reason                                                       |
            +---------------------------+--------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to view user profile. |
            +---------------------------+--------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Mutuals`
            The found mutuals.
        """
        return await self.state.http.get_mutuals_with(self.id, http_overrides=http_overrides)

    async def open_dm(
        self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None
    ) -> typing.Union[SavedMessagesChannel, DMChannel]:
        """|coro|

        Retrieve a DM (or create if it doesn't exist) with another user.

        If target is current user, a :class:`.SavedMessagesChannel` is always returned.

        You must have :attr:`~UserPermissions.send_messages` to do this.

        May fire :class:`.PrivateChannelCreateEvent` for the current user and user you opened DM with.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
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
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+-------------------------------------------------------------------+
            | Value                     | Reason                                                            |
            +---------------------------+-------------------------------------------------------------------+
            | ``MissingUserPermission`` | You do not have the proper permissions to open DM with this user. |
            +---------------------------+-------------------------------------------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        Union[:class:`.SavedMessagesChannel`, :class:`.DMChannel`]
            The private channel.
        """

        return await self.state.http.open_dm(self.id, http_overrides=http_overrides)

    async def remove_friend(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> User:
        """|coro|

        Removes the user from friend list.

        Fires :class:`.UserRelationshipUpdateEvent` for the current user and user you removed from friend list.

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +-----------+-----------------------------------------------------------------------------------------+
            | Value     | Reason                                                                                  |
            +-----------+-----------------------------------------------------------------------------------------+
            | ``IsBot`` | Either the current user or user you tried to deny friend request from are bot accounts. |
            +-----------+-----------------------------------------------------------------------------------------+
        :class:`NoEffect`
            You tried to deny friend request from user you had no friend request sent from/to.
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.User`
            The user you removed from friend list.
        """

        return await self.state.http.remove_friend(self.id, http_overrides=http_overrides)

    async def report(
        self,
        reason: UserReportReason,
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
        additional_context: typing.Optional[str] = None,
        message_context: typing.Optional[ULIDOr[BaseMessage]] = None,
    ) -> None:
        """|coro|

        Report the user to the instance moderation team.

        Fires :class:`.ReportCreateEvent` internally (but not fired over WebSocket).

        .. note::
            This can only be used by non-bot accounts.

        Parameters
        ----------
        reason: :class:`.UserReportReason`
            The reason for reporting user.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.
        additional_context: Optional[:class:`str`]
            The additional context for moderation team. Can be only up to 1000 characters.
        message_context: Optional[ULIDOr[:class:`.BaseMessage`]]
            The message context.

            Internally, 15 messages around provided message will be snapshotted for context. All attachments of provided message are snapshotted as well.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------------+-------------------------------+
            | Value                    | Reason                        |
            +--------------------------+-------------------------------+
            | ``CannotReportYourself`` | You tried to report yourself. |
            +--------------------------+-------------------------------+
            | ``FailedValidation``     | The payload was invalid.      |
            +--------------------------+-------------------------------+
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------------+
            | Value        | Reason                          |
            +--------------+---------------------------------+
            | ``NotFound`` | The user/message was not found. |
            +--------------+---------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """

        return await self.state.http.report_user(
            self.id,
            reason,
            http_overrides=http_overrides,
            additional_context=additional_context,
            message_context=message_context,
        )

    async def timeout(
        self,
        length: typing.Optional[typing.Union[datetime, timedelta, float, int]],
        *,
        http_overrides: typing.Optional[HTTPOverrideOptions] = None,
    ) -> Member:
        """|coro|

        Timeouts the member.

        You must have :attr:`~Permissions.timeout_members` to do this.

        Fires :class:`.ServerMemberUpdateEvent` for all server members.

        Parameters
        ----------
        length: UndefinedOr[Optional[Union[:class:`~datetime.datetime`, :class:`~datetime.timedelta`, :class:`float`, :class:`int`]]]
            The duration/date the member's timeout should expire, or ``None`` to remove the timeout.

            This must be a timezone-aware datetime object. Consider using :func:`pyvolt.utils.utcnow()`.
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`HTTPException`
            Possible values for :attr:`~HTTPException.type`:

            +---------------------------+---------------------------------+
            | Value                     | Reason                          |
            +---------------------------+---------------------------------+
            | ``CannotTimeoutYourself`` | You tried to time out yourself. |
            +---------------------------+---------------------------------+
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
            | ``MissingPermission`` | You do not have the proper permissions to edit this member. |
            +-----------------------+-------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+----------------------------------+
            | Value        | Reason                           |
            +--------------+----------------------------------+
            | ``NotFound`` | The server/member was not found. |
            +--------------+----------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+-----------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                              | Populated attributes                                                |
            +-------------------+-----------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database.      | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+-----------------------------------------------------+---------------------------------------------------------------------+
            | ``InternalError`` | Somehow something went wrong during editing member. |                                                                     |
            +-------------------+-----------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.Member`
            The newly updated member.
        """
        return await self.state.http.edit_member(self.server_id, self.id, http_overrides=http_overrides, timeout=length)

    async def unblock(self, *, http_overrides: typing.Optional[HTTPOverrideOptions] = None) -> User:
        """|coro|

        Unblocks an user.

        Fires :class:`.UserRelationshipUpdateEvent` for the current user and unblocked user.

        .. note::
            This is not supposed to be used by bot accounts.

        Parameters
        ----------
        http_overrides: Optional[:class:`.HTTPOverrideOptions`]
            The HTTP request overrides.

        Raises
        ------
        :class:`NoEffect`
            You tried to block yourself or someone that you didn't had blocked.
        :class:`Unauthorized`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-------------------------+
            | Value        | Reason                  |
            +--------------+-------------------------+
            | ``NotFound`` | The user was not found. |
            +--------------+-------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                               | Populated attributes                                                |
            +-------------------+------------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database.       | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------------+---------------------------------------------------------------------+
            | ``InternalError`` | Somehow something went wrong during unblocking user. |                                                                     |
            +-------------------+------------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.User`
            The unblocked user.
        """
        return await self.state.http.unblock_user(self.id, http_overrides=http_overrides)

    def is_sentinel(self) -> bool:
        """:class:`bool`: Returns whether the user is sentinel (Revolt#0000)."""
        return self is self.state.system


@define(slots=True)
class PartialMember(BaseMember):
    """Represents a partial Revolt member to a :class:`Server`.

    Unmodified fields will have :data:`.UNDEFINED` value.

    This inherits from :class:`.BaseMember`.
    """

    nick: UndefinedOr[typing.Optional[str]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`str`]]: The new member's nick."""

    internal_server_avatar: UndefinedOr[typing.Optional[StatelessAsset]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`.StatelessAsset`]]: The new member's avatar."""

    role_ids: UndefinedOr[list[str]] = field(repr=True, kw_only=True)
    """UndefinedOr[List[:class:`str`]]: The new member's roles."""

    timed_out_until: UndefinedOr[typing.Optional[datetime]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`~datetime.datetime`]]: When member's time out expires now."""

    can_publish: UndefinedOr[typing.Optional[bool]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`bool`]]: Whether the member can send voice data now."""

    can_receive: UndefinedOr[typing.Optional[bool]] = field(repr=True, kw_only=True)
    """UndefinedOr[Optional[:class:`bool`]]: Whether the member can receive voice data now."""

    @property
    def server_avatar(self) -> UndefinedOr[typing.Optional[Asset]]:
        """UndefinedOr[Optional[:class:`.Asset`]]: The member's avatar on server."""
        return self.internal_server_avatar and self.internal_server_avatar.attach_state(self.state, 'avatars')


@define(slots=True)
class Member(BaseMember):
    """Represents a Revolt member to a :class:`.Server`.

    This inherits from :class:`.BaseMember`.
    """

    joined_at: datetime = field(repr=True, kw_only=True)
    """:class:`~datetime.datetime`: When the member joined the server."""

    nick: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The member's nick."""

    internal_server_avatar: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`.StatelessAsset`]: The member's avatar on server."""

    role_ids: list[str] = field(repr=True, kw_only=True)
    """List[:class:`str`]: The member's roles."""

    timed_out_until: typing.Optional[datetime] = field(repr=True, kw_only=True)
    """Optional[:class:`~datetime.datetime`]: The timestamp this member is timed out until."""

    can_publish: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the member can send voice data."""

    can_receive: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the member can receive voice data."""

    def locally_update(self, data: PartialMember, /) -> None:
        """Locally updates member with provided data.

        .. warning::
            This is called by library internally to keep cache up to date.

        Parameters
        ----------
        data: :class:`.PartialMember`
            The data to update member with.
        """
        if data.nick is not UNDEFINED:
            self.nick = data.nick
        if data.internal_server_avatar is not UNDEFINED:
            self.internal_server_avatar = data.internal_server_avatar
        if data.role_ids is not UNDEFINED:
            self.role_ids = data.role_ids or []
        if data.can_publish is not UNDEFINED:
            self.can_publish = True if data.can_publish is None else data.can_publish
        if data.can_receive is not UNDEFINED:
            self.can_receive = True if data.can_receive is None else data.can_receive

    @property
    def roles(self) -> list[Role]:
        """List[:class:`.Role`]: The member's roles."""

        state = self.state
        cache = state.cache

        if cache is None:
            return []

        ctx = (
            ServerThroughMemberRolesCacheContext(
                type=CacheContextType.server_through_member_roles,
                member=self,
            )
            if state.provide_cache_context('Member.roles')
            else _SERVER_THROUGH_MEMBER_ROLES
        )

        server = cache.get_server(self.server_id, ctx)
        if server is None:
            return []

        roles = []
        for role_id in self.role_ids:
            try:
                role = server.roles[role_id]
            except KeyError:
                pass
            else:
                roles.append(role)

        return roles

    @property
    def server_avatar(self) -> typing.Optional[Asset]:
        """Optional[:class:`.Asset`]: The member's avatar on server."""
        return self.internal_server_avatar and self.internal_server_avatar.attach_state(self.state, 'avatars')

    @property
    def server_permissions(self) -> Permissions:
        """:class:`.Permissions`: The permissions for this member in the server."""

        state = self.state
        cache = state.cache

        if cache is None:
            raise NoData(what=self.server_id, type='Member.server_permissions')

        ctx = (
            ServerThroughMemberServerPermissionsCacheContext(
                type=CacheContextType.server_through_member_server_permissions,
                member=self,
            )
            if state.provide_cache_context('Member.server_permissions')
            else _SERVER_THROUGH_MEMBER_SERVER_PERMISSIONS
        )

        server = cache.get_server(self.server_id, ctx)
        if server is None:
            raise NoData(what=self.server_id, type='Member.server_permissions')

        return server.permissions_for(self)

    @property
    def top_role(self) -> typing.Optional[Role]:
        """Optional[:class:`.Role`]: The member's top role."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ServerThroughMemberTopRoleCacheContext(
                type=CacheContextType.server_through_member_top_role,
                member=self,
            )
            if state.provide_cache_context('Member.top_role')
            else _SERVER_THROUGH_MEMBER_TOP_ROLE
        )

        server = cache.get_server(self.server_id, ctx)
        if server is None:
            return None

        roles = sort_member_roles(self.role_ids, safe=False, server_roles=server.roles)

        if len(roles):
            return roles[-1]

        return None

    def to_dict(self) -> raw.Member:
        """:class:`dict`: Convert server member to raw data."""
        payload: raw.Member = {
            '_id': {
                'server': self.server_id,
                'user': self.id,
            },
            'joined_at': self.joined_at.isoformat(),
        }
        if self.nick is not None:
            payload['nickname'] = self.nick
        if self.internal_server_avatar is not None:
            payload['avatar'] = self.internal_server_avatar.to_dict('avatars')
        if len(self.role_ids):
            payload['roles'] = self.role_ids
        if self.timed_out_until is not None:
            payload['timeout'] = self.timed_out_until.isoformat()
        return payload


@define(slots=True)
class MemberList:
    """A list of members in a server."""

    members: list[Member] = field(repr=True, kw_only=True)
    """List[:class:`.Member`]: The members in server."""

    users: list[User] = field(repr=True, kw_only=True)
    """List[:class:`.User`]: The users."""


__all__ = (
    'Category',
    'SystemMessageChannels',
    'BaseRole',
    'PartialRole',
    'Role',
    'BaseServer',
    'PartialServer',
    'sort_member_roles',
    'calculate_server_permissions',
    'Server',
    'Ban',
    'BaseMember',
    'PartialMember',
    'Member',
    'MemberList',
)
