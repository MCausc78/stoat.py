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
    ServerThroughServerPublicInviteServerCacheContext,
    ChannelThroughServerPublicInviteChannelCacheContext,
    UserThroughServerPublicInviteUserCacheContext,
    ChannelThroughGroupPublicInviteChannelCacheContext,
    UserThroughGroupPublicInviteUserCacheContext,
    UserThroughPrivateBaseInviteCreatorCacheContext,
    ChannelThroughGroupInviteChannelCacheContext,
    ServerThroughServerInviteServerCacheContext,
    ChannelThroughServerInviteChannelCacheContext,
    _SERVER_THROUGH_SERVER_PUBLIC_INVITE_SERVER,
    _CHANNEL_THROUGH_SERVER_PUBLIC_INVITE_CHANNEL,
    _USER_THROUGH_SERVER_PUBLIC_INVITE_USER,
    _CHANNEL_THROUGH_GROUP_PUBLIC_INVITE_CHANNEL,
    _USER_THROUGH_GROUP_PUBLIC_INVITE_USER,
    _USER_THROUGH_PRIVATE_BASE_INVITE_CREATOR,
    _CHANNEL_THROUGH_GROUP_INVITE_CHANNEL,
    _SERVER_THROUGH_SERVER_INVITE_SERVER,
    _CHANNEL_THROUGH_SERVER_INVITE_CHANNEL,
)
from .channel import GroupChannel, ServerChannel
from .cdn import StatelessAsset, Asset
from .errors import NoData
from .flags import ServerFlags

if typing.TYPE_CHECKING:
    from .server import Server
    from .state import State
    from .user import User

_new_server_flags = ServerFlags.__new__


@define(slots=True)
class BaseInvite:
    """Represents a invite on Revolt."""

    state: State = field(repr=False, kw_only=True)
    """:class:`.State`: State that controls this invite."""

    code: str = field(repr=True, kw_only=True)
    """:class:`str`: The invite's code."""

    def __hash__(self) -> int:
        return hash(self.code)

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, BaseInvite) and self.code == other.code

    async def accept(self) -> typing.Union[Server, GroupChannel]:
        """|coro|

        Accepts an invite.

        .. note::
            This can only be used by non-bot accounts.

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

            +-----------------------+-------------------------------------------------+
            | Value                 | Reason                                          |
            +-----------------------+-------------------------------------------------+
            | ``Banned``            | You're banned from server.                      |
            +-----------------------+-------------------------------------------------+
            | ``GroupTooLarge``     | The group exceeded maximum count of recipients. |
            +-----------------------+-------------------------------------------------+
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
            | ``AlreadyInGroup``  | The user is already in group.  |
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
        Union[:class:`.Server`, :class:`.GroupChannel`]
            The joined server or group.
        """

        return await self.state.http.accept_invite(self.code)

    async def delete(self) -> None:
        """|coro|

        Deletes the invite.

        You must have :class:`~Permissions.manage_server` if deleting server invite.

        There is an alias for this called :meth:`~.revoke`.

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

            +-----------------------+---------------------------------------------------------------+
            | Value                 | Reason                                                        |
            +-----------------------+---------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to delete this invite. |
            +-----------------------+---------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The invite was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """
        return await self.state.http.delete_invite(self.code)

    async def revoke(self) -> None:
        """|coro|

        Deletes the invite.

        You must have :class:`~Permissions.manage_server` if deleting server invite.

        This is an alias of :meth:`~.delete`.

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

            +-----------------------+---------------------------------------------------------------+
            | Value                 | Reason                                                        |
            +-----------------------+---------------------------------------------------------------+
            | ``MissingPermission`` | You do not have the proper permissions to delete this invite. |
            +-----------------------+---------------------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+---------------------------+
            | Value        | Reason                    |
            +--------------+---------------------------+
            | ``NotFound`` | The invite was not found. |
            +--------------+---------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
        """
        return await self.state.http.delete_invite(self.code)


@define(slots=True)
class ServerPublicInvite(BaseInvite):
    """Represents a public invite to server channel."""

    server_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The server's ID this invite points to."""

    server_name: str = field(repr=True, kw_only=True)
    """:class:`str`: The server's name."""

    internal_server_icon: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`.StatelessAsset`]: The server's stateless icon."""

    internal_server_banner: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`.StatelessAsset`]: The server's stateless banner.."""

    raw_server_flags: int = field(repr=True, kw_only=True)
    """:class:`int`: The server's flags raw value."""

    channel_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The destination channel's ID."""

    channel_name: str = field(repr=True, kw_only=True)
    """:class:`str`: The destination channel's name."""

    channel_description: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The destination channel's description."""

    user_name: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's name who created this invite."""

    internal_user_avatar: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`.StatelessAsset`]: The user's stateless avatar who created this invite."""

    member_count: int = field(repr=True, kw_only=True)
    """:class:`int`: The count of members in target server."""

    def get_server(self) -> typing.Optional[Server]:
        """Optional[:class:`.Server`]: The server this invite points to."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ServerThroughServerPublicInviteServerCacheContext(
                type=CacheContextType.server_through_server_public_invite_server,
                invite=self,
            )
            if state.provide_cache_context('ServerPublicInvite.server')
            else _SERVER_THROUGH_SERVER_PUBLIC_INVITE_SERVER
        )

        return cache.get_server(self.server_id, ctx)

    def get_channel(self) -> typing.Optional[ServerChannel]:
        """Optional[:class:`.ServerChannel`]: The destination channel."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelThroughServerPublicInviteChannelCacheContext(
                type=CacheContextType.channel_through_server_public_invite_channel,
                invite=self,
            )
            if state.provide_cache_context('ServerPublicInvite.channel')
            else _CHANNEL_THROUGH_SERVER_PUBLIC_INVITE_CHANNEL
        )

        channel = cache.get_channel(self.channel_id, ctx)
        if channel is not None:
            assert isinstance(channel, ServerChannel)
        return channel

    def get_user(self) -> typing.Optional[User]:
        """Optional[:class:`.User`]: The (guessed) user who created this invite.

        This always will return accurate user if user has avatar, but might incorrectly find user if avatar is missing.
        """
        state = self.state
        cache = state.cache
        if cache is None:
            return None

        user_name = self.user_name
        user_avatar_id = None if self.internal_user_avatar is None else self.internal_user_avatar.id

        predicate = (
            (lambda user, /: user.name == user_name and user.internal_avatar is None)
            if user_avatar_id is None
            else (
                lambda user, /: user.name == user_name
                and user.internal_avatar is not None
                and user.internal_avatar.id == user_avatar_id
            )
        )

        ctx = (
            UserThroughServerPublicInviteUserCacheContext(
                type=CacheContextType.user_through_server_public_invite_user,
                invite=self,
            )
            if state.provide_cache_context('ServerPublicInvite.user')
            else _USER_THROUGH_SERVER_PUBLIC_INVITE_USER
        )

        for user in cache.get_users_mapping(ctx).values():
            if predicate(user):
                return user

        return None

    @property
    def server(self) -> Server:
        """:class:`.Server`: The server this invite points to."""

        server = self.get_server()
        if server is None:
            raise NoData(
                what=self.server_id,
                type='ServerPublicInvite.server',
            )
        return server

    @property
    def server_flags(self) -> ServerFlags:
        """:class:`.ServerFlags`: The server's flags."""
        ret = _new_server_flags(ServerFlags)
        ret.value = self.raw_server_flags
        return ret

    @property
    def server_icon(self) -> typing.Optional[Asset]:
        """Optional[:class:`.Asset`]: The icon of the server."""
        return self.internal_server_icon and self.internal_server_icon.attach_state(self.state, 'icons')

    @property
    def server_banner(self) -> typing.Optional[Asset]:
        """Optional[:class:`.Asset`]: The banner of the server."""
        return self.internal_server_banner and self.internal_server_banner.attach_state(self.state, 'banners')

    @property
    def channel(self) -> ServerChannel:
        """:class:`.ServerChannel`: The destination channel."""

        channel = self.get_channel()
        if channel is None:
            raise NoData(
                what=self.channel_id,
                type='ServerPublicInvite.channel',
            )
        return channel

    @property
    def user(self) -> User:
        """:class:`.User`: The (guessed) user who created this invite.

        This always will return accurate user if user has avatar, but might incorrectly find user if avatar is missing.
        """

        user = self.get_user()
        if user is None:
            raise NoData(
                what='',
                type='ServerPublicInvite.user',
            )
        return user

    @property
    def user_avatar(self) -> typing.Optional[Asset]:
        """Optional[:class:`.Asset`]: The user's avatar who created this invite."""
        return self.internal_user_avatar and self.internal_user_avatar.attach_state(self.state, 'avatars')

    async def accept(self) -> Server:
        """|coro|

        Accepts an invite.

        .. note::
            This can only be used by non-bot accounts.

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
            The joined server.
        """
        from .server import Server

        server = await super().accept()
        assert isinstance(server, Server)
        return server


@define(slots=True)
class GroupPublicInvite(BaseInvite):
    """Represents a public invite to group channel."""

    channel_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The destination channel's ID."""

    channel_name: str = field(repr=True, kw_only=True)
    """:class:`str`: The destination channel's name."""

    channel_description: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The destination channel's description."""

    user_name: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's name who created this invite."""

    internal_user_avatar: typing.Optional[StatelessAsset] = field(repr=True, kw_only=True)
    """Optional[:class:`.StatelessAsset`]: The user's stateless avatar who created this invite."""

    def get_channel(self) -> typing.Optional[GroupChannel]:
        """Optional[:class:`.GroupChannel`]: The destination channel."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelThroughGroupPublicInviteChannelCacheContext(
                type=CacheContextType.channel_through_group_public_invite_channel,
                invite=self,
            )
            if state.provide_cache_context('GroupPublicInvite.channel')
            else _CHANNEL_THROUGH_GROUP_PUBLIC_INVITE_CHANNEL
        )

        channel = cache.get_channel(self.channel_id, ctx)
        if channel is not None:
            assert isinstance(channel, GroupChannel)
        return channel

    def get_user(self) -> typing.Optional[User]:
        """Optional[:class:`.User`]: The (guessed) user who created this invite.

        This always will return accurate user if user has avatar, but might incorrectly find user if avatar is missing.
        """
        state = self.state
        cache = state.cache
        if cache is None:
            return None

        user_name = self.user_name
        user_avatar_id = None if self.internal_user_avatar is None else self.internal_user_avatar.id

        predicate = (
            (lambda user, /: user.name == user_name and user.internal_avatar is None)
            if user_avatar_id is None
            else (
                lambda user, /: user.name == user_name
                and user.internal_avatar is not None
                and user.internal_avatar.id == user_avatar_id
            )
        )

        ctx = (
            UserThroughGroupPublicInviteUserCacheContext(
                type=CacheContextType.user_through_group_public_invite_user,
                invite=self,
            )
            if state.provide_cache_context('GroupPublicInvite.user')
            else _USER_THROUGH_GROUP_PUBLIC_INVITE_USER
        )

        for user in cache.get_users_mapping(ctx).values():
            if predicate(user):
                return user

        return None

    @property
    def channel(self) -> GroupChannel:
        """:class:`.GroupChannel`: The destination channel."""

        channel = self.get_channel()
        if channel is None:
            raise NoData(
                what=self.channel_id,
                type='GroupPublicInvite.channel',
            )
        return channel

    @property
    def user(self) -> User:
        """:class:`.User`: The (guessed) user who created this invite.

        This always will return accurate user if user has avatar, but might incorrectly find user if avatar is missing.
        """

        user = self.get_user()
        if user is None:
            raise NoData(
                what='',
                type='GroupPublicInvite.user',
            )
        return user

    @property
    def user_avatar(self) -> typing.Optional[Asset]:
        """Optional[:class:`.Asset`]: The user's avatar who created this invite."""
        return self.internal_user_avatar and self.internal_user_avatar.attach_state(self.state, 'avatars')

    async def accept(self) -> GroupChannel:
        """|coro|

        Accepts an invite.

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

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+-------------------------------------------------+
            | Value             | Reason                                          |
            +-------------------+-------------------------------------------------+
            | ``GroupTooLarge`` | The group exceeded maximum count of recipients. |
            +-------------------+-------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-----------------------------------+
            | Value        | Reason                            |
            +--------------+-----------------------------------+
            | ``NotFound`` | The invite/channel was not found. |
            +--------------+-----------------------------------+
        :class:`Conflict`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-------------------------------+
            | Value              | Reason                        |
            +--------------------+-------------------------------+
            | ``AlreadyInGroup`` | The user is already in group. |
            +--------------------+-------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.GroupChannel`
            The joined group.
        """
        group = await super().accept()
        return group  # type: ignore


@define(slots=True)
class UnknownPublicInvite(BaseInvite):
    """Represents a public invite that is not recognized by library yet."""

    payload: dict[str, typing.Any] = field(repr=True, kw_only=True)
    """Dict[:class:`str`, Any]: The raw invite data."""


PublicInvite = typing.Union[ServerPublicInvite, GroupPublicInvite, UnknownPublicInvite]


@define(slots=True)
class PrivateBaseInvite(BaseInvite):
    """Represents a private invite on Revolt."""

    creator_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID who created this invite."""

    def get_creator(self) -> typing.Optional[User]:
        """Optional[:class:`.User`]: The user who created this invite."""
        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            UserThroughPrivateBaseInviteCreatorCacheContext(
                type=CacheContextType.user_through_private_base_invite_creator,
                invite=self,
            )
            if state.provide_cache_context('PrivateBaseInvite.creator')
            else _USER_THROUGH_PRIVATE_BASE_INVITE_CREATOR
        )

        return cache.get_user(self.creator_id, ctx)

    @property
    def creator(self) -> User:
        """:class:`.User`: The user who created this invite."""

        creator = self.get_creator()
        if creator is None:
            raise NoData(
                what=self.creator_id,
                type='PrivateBaseInvite.creator',
            )
        return creator


@define(slots=True)
class GroupInvite(PrivateBaseInvite):
    """Represents a group invite on Revolt."""

    channel_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The group channel's ID this invite points to."""

    def get_channel(self) -> typing.Optional[GroupChannel]:
        """Optional[:class:`.GroupChannel`]: The group channel this invite points to."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelThroughGroupInviteChannelCacheContext(
                type=CacheContextType.channel_through_group_invite_channel,
                invite=self,
            )
            if state.provide_cache_context('GroupInvite.channel')
            else _CHANNEL_THROUGH_GROUP_INVITE_CHANNEL
        )

        channel = cache.get_channel(self.channel_id, ctx)
        if channel is not None:
            assert isinstance(channel, GroupChannel)
        return channel

    @property
    def channel(self) -> GroupChannel:
        """:class:`.GroupChannel`: The group channel this invite points to."""

        channel = self.get_channel()
        if channel is None:
            raise NoData(
                what=self.channel_id,
                type='GroupInvite.channel',
            )
        return channel

    async def accept(self) -> GroupChannel:
        """|coro|

        Accepts an invite.

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

            +--------------------+----------------------------------------+
            | Value              | Reason                                 |
            +--------------------+----------------------------------------+
            | ``InvalidSession`` | The current bot/user token is invalid. |
            +--------------------+----------------------------------------+
        :class:`Forbidden`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+-------------------------------------------------+
            | Value             | Reason                                          |
            +-------------------+-------------------------------------------------+
            | ``GroupTooLarge`` | The group exceeded maximum count of recipients. |
            +-------------------+-------------------------------------------------+
        :class:`NotFound`
            Possible values for :attr:`~HTTPException.type`:

            +--------------+-----------------------------------+
            | Value        | Reason                            |
            +--------------+-----------------------------------+
            | ``NotFound`` | The invite/channel was not found. |
            +--------------+-----------------------------------+
        :class:`Conflict`
            Possible values for :attr:`~HTTPException.type`:

            +--------------------+-------------------------------+
            | Value              | Reason                        |
            +--------------------+-------------------------------+
            | ``AlreadyInGroup`` | The user is already in group. |
            +--------------------+-------------------------------+
        :class:`InternalServerError`
            Possible values for :attr:`~HTTPException.type`:

            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | Value             | Reason                                         | Populated attributes                                                |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+
            | ``DatabaseError`` | Something went wrong during querying database. | :attr:`~HTTPException.collection`, :attr:`~HTTPException.operation` |
            +-------------------+------------------------------------------------+---------------------------------------------------------------------+

        Returns
        -------
        :class:`.GroupChannel`
            The joined group.
        """
        group = await super().accept()
        return group  # type: ignore


@define(slots=True)
class ServerInvite(PrivateBaseInvite):
    """Represents a server invite on Revolt."""

    server_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The server's ID this invite points to."""

    channel_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The server channel's ID this invite points to."""

    def get_server(self) -> typing.Optional[Server]:
        """Optional[:class:`.Server`]: The server this invite points to."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ServerThroughServerInviteServerCacheContext(
                type=CacheContextType.server_through_server_invite_server,
                invite=self,
            )
            if state.provide_cache_context('ServerInvite.server')
            else _SERVER_THROUGH_SERVER_INVITE_SERVER
        )

        return cache.get_server(self.server_id, ctx)

    def get_channel(self) -> typing.Optional[ServerChannel]:
        """Optional[:class:`.ServerChannel`]: The server channel this invite points to."""

        state = self.state
        cache = state.cache

        if cache is None:
            return None

        ctx = (
            ChannelThroughServerInviteChannelCacheContext(
                type=CacheContextType.channel_through_server_invite_channel,
                invite=self,
            )
            if state.provide_cache_context('ServerInvite.channel')
            else _CHANNEL_THROUGH_SERVER_INVITE_CHANNEL
        )

        channel = cache.get_channel(self.channel_id, ctx)
        if channel is not None:
            assert isinstance(channel, ServerChannel)
        return channel

    @property
    def server(self) -> Server:
        """:class:`.Server`: The server this invite points to."""

        server = self.get_server()
        if server is None:
            raise NoData(
                what=self.server_id,
                type='ServerInvite.server',
            )
        return server

    @property
    def channel(self) -> ServerChannel:
        """:class:`.ServerChannel`: The server channel this invite points to."""

        channel = self.get_channel()
        if channel is None:
            raise NoData(
                what=self.channel_id,
                type='ServerInvite.channel',
            )
        return channel

    async def accept(self) -> Server:
        """|coro|

        Accepts an invite.

        .. note::
            This can only be used by non-bot accounts.

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
            The joined server.
        """
        from .server import Server

        server = await super().accept()
        assert isinstance(server, Server)
        return server


Invite = typing.Union[GroupInvite, ServerInvite]

__all__ = (
    'BaseInvite',
    'ServerPublicInvite',
    'GroupPublicInvite',
    'UnknownPublicInvite',
    'PublicInvite',
    'PrivateBaseInvite',
    'GroupInvite',
    'ServerInvite',
    'Invite',
)
