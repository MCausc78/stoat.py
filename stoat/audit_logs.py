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

from attrs import Factory, define, field

from .base import Base
from .cache import (
    CacheContextType,
    MemberOrUserThroughAuditLogEntryUserCacheContext,
    MemberThroughAuditLogEntryUserCacheContext,
    UserThroughAuditLogEntryUserCacheContext,
    MemberOrUserThroughAuditLogEntryActionUserCacheContext,
    MemberThroughAuditLogEntryActionUserCacheContext,
    UserThroughAuditLogEntryActionUserCacheContext,
    _MEMBER_OR_USER_THROUGH_AUDIT_LOG_ENTRY_USER,
    _MEMBER_THROUGH_AUDIT_LOG_ENTRY_USER,
    _USER_THROUGH_AUDIT_LOG_ENTRY_USER,
    _MEMBER_OR_USER_THROUGH_AUDIT_LOG_ENTRY_ACTION_USER,
    _MEMBER_THROUGH_AUDIT_LOG_ENTRY_ACTION_USER,
    _USER_THROUGH_AUDIT_LOG_ENTRY_ACTION_USER,
)
from .enums import AuditLogEntryActionType
from .errors import NoData
from .server import Member
from .user import User

if typing.TYPE_CHECKING:
    from . import raw
    from .channel import PartialChannel
    from .permissions import PermissionOverride
    from .server import PartialRole, PartialServer, PartialMember
    from .state import State


@define(slots=True, eq=True)
class AuditLogEntry(Base):
    """Represents an audit log entry.

    Most of fields will be set to their zero value (empty string, 0, empty array) if the type.
    """

    server_id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The ID of the server."""

    reason: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The reason for the action."""

    internal_user: typing.Union[Member, User, str] = field(
        default='',
        repr=False,
        kw_only=True,
        # In case of hydration, the ID always should be used for comparsion
        eq=lambda target: target.id if isinstance(target, (Member, User)) else target,
    )
    """Union[:class:`Member`, :class:`User`, :class:`str`]: The ID of the user who performed the action, or full member/user instance."""

    action: AuditLogEntryAction = field(repr=True, kw_only=True, eq=True)
    """:class:`AuditLogEntryAction`: Details about the action."""

    def get_user(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The user who performed the action."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user

        state = self.state
        cache = state.cache
        if cache is None:
            return None

        ctx = (
            MemberOrUserThroughAuditLogEntryUserCacheContext(
                type=CacheContextType.member_or_user_through_audit_log_entry_user,
                entry=self,
            )
            if state.provide_cache_context('AuditLogEntry.user')
            else _MEMBER_OR_USER_THROUGH_AUDIT_LOG_ENTRY_USER
        )

        ret = cache.get_server_member(self.server_id, self.internal_user, ctx)

        if ret is None:
            return cache.get_user(self.internal_user, ctx)

        return ret

    def get_user_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The user who performed the action."""
        if isinstance(self.internal_user, Member):
            return self.internal_user

        if isinstance(self.internal_user, User):
            user_id = self.internal_user.id
        else:
            user_id = self.internal_user

        state = self.state
        cache = state.cache
        if cache is None:
            return None

        ctx = (
            MemberThroughAuditLogEntryUserCacheContext(
                type=CacheContextType.member_through_audit_log_entry_user,
                entry=self,
            )
            if state.provide_cache_context('AuditLogEntry.user_as_member')
            else _MEMBER_THROUGH_AUDIT_LOG_ENTRY_USER
        )

        return cache.get_server_member(self.server_id, user_id, ctx)

    def get_user_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The user who performed the action."""
        if isinstance(self.internal_user, Member):
            if isinstance(self.internal_user.internal_user, User):
                return self.internal_user.internal_user
            return None
        if isinstance(self.internal_user, User):
            return self.internal_user

        state = self.state
        cache = state.cache
        if cache is None:
            return None

        ctx = (
            UserThroughAuditLogEntryUserCacheContext(
                type=CacheContextType.user_through_audit_log_entry_user,
                entry=self,
            )
            if state.provide_cache_context('AuditLogEntry.user_as_user')
            else _USER_THROUGH_AUDIT_LOG_ENTRY_USER
        )

        return cache.get_user(self.internal_user, ctx)

    def __hash__(self) -> int:
        return hash((self.id, self.server_id))

    @property
    def user(self) -> typing.Union[Member, User]:
        """Union[:class:`Member`, :class:`User`]: The user who performed the action."""
        user = self.get_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='AuditLogEntry.user',
            )
        return user

    @property
    def user_id(self) -> str:
        """:class:`str`: The ID of the user."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user.id
        return self.internal_user

    @property
    def user_as_member(self) -> Member:
        """:class:`Member`: The user who performed the action."""
        user = self.get_user_as_member()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='AuditLogEntry.user_as_member',
            )
        return user

    @property
    def user_as_user(self) -> User:
        """:class:`User`: The user who performed the action."""
        user = self.get_user_as_user()
        if user is None:
            raise NoData(
                what=self.user_id,
                type='AuditLogEntry.user_as_user',
            )
        return user

    def to_dict(self) -> raw.AuditLogEntry:
        """:class:`dict`: Convert audit log entry to raw data."""
        return {
            '_id': self.id,
            'server': self.server_id,
            'reason': self.reason,
            'user': self.user_id,
            'action': self.action.to_dict(),
        }


@define(hash=True, slots=True, eq=True)
class AuditLogEntryAction:
    """Represents an audit log entry action.

    Most of fields will be set to their zero value (empty string, 0, empty array) if the type.
    """

    state: State = field(repr=False, kw_only=True, eq=False)
    """:class:`State`: The state that controls the parent entry."""

    type: AuditLogEntryActionType = field(repr=True, kw_only=True, eq=True)
    """:class:`AuditLogEntryActionType`: The type of the action."""

    channel_id: str = field(default='', repr=False, kw_only=True, eq=True)
    """:class:`str`: The ID of the channel."""

    count: int = field(default=0, repr=False, kw_only=True, eq=True)
    """:class:`int`: The count of deleted messages."""

    emoji_id: str = field(default='', repr=False, kw_only=True, eq=True)
    """:class:`str`: The ID of the emoji."""

    internal_channel_update: typing.Optional[PartialChannel] = field(default=None, repr=False, kw_only=True, eq=True)
    """Optional[:class:`PartialChannel`]: The updated channel as it was updated."""

    internal_member_update: typing.Optional[PartialMember] = field(default=None, repr=False, kw_only=True, eq=True)
    """:class:`PartialMember`: The updated member as it was updated."""

    internal_payload: typing.Optional[dict[str, typing.Any]] = field(default=None, repr=False, kw_only=True, eq=True)
    """Optional[Dict[:class:`str`, Any]]: The raw audit log entry action data."""

    internal_role_update: typing.Optional[PartialRole] = field(default=None, repr=False, kw_only=True, eq=True)
    """Optional[:class:`PartialRole`]: The updated role as it was updated."""

    internal_server_update: typing.Optional[PartialServer] = field(default=None, repr=False, kw_only=True, eq=True)
    """Optional[:class:`PartialServer`]: The updated server as it was updated."""

    internal_user: typing.Union[Member, User, str] = field(
        default='',
        repr=False,
        kw_only=True,
        # In case of hydration, the ID always should be used for comparsion
        eq=lambda target: target.id if isinstance(target, (Member, User)) else target,
    )
    """Union[:class:`Member`, :class:`User`, :class:`str`]: The ID of the affected user, or full member/user instance."""

    invite_code: str = field(default='', repr=False, kw_only=True, eq=True)
    """:class:`str`: The ID of the invite."""

    name: str = field(default='', repr=False, kw_only=True, eq=True)
    """:class:`str`: The name of the affected entity."""

    permissions: PermissionOverride = field(default=Factory(PermissionOverride), repr=False, kw_only=True, eq=True)
    """:class:`PermissionOverride`: The permissions of the affected entity."""

    positions: list[str] = field(default=Factory(list), repr=False, kw_only=True, eq=True)
    """List[:class:`str`]: The new IDs of roles with their index in list representing their rank."""

    role_id: str = field(default='', repr=False, kw_only=True, eq=True)
    """:class:`str`: The ID of the affected role."""

    server_id: str = field(default='', repr=False, kw_only=True, eq=True)
    """:class:`str`: The ID of the affected server."""

    webhook_id: str = field(default='', repr=False, kw_only=True, eq=True)
    """:class:`str`: The ID of the affected webhook."""

    def get_user(self) -> typing.Optional[typing.Union[Member, User]]:
        """Optional[Union[:class:`Member`, :class:`User`]]: The affected user."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user

        state = self.state
        cache = state.cache
        if cache is None:
            return None

        ctx = (
            MemberOrUserThroughAuditLogEntryActionUserCacheContext(
                type=CacheContextType.member_or_user_through_audit_log_entry_action_user,
                action=self,
            )
            if state.provide_cache_context('AuditLogEntryAction.user')
            else _MEMBER_OR_USER_THROUGH_AUDIT_LOG_ENTRY_ACTION_USER
        )

        ret = cache.get_server_member(self.server_id, self.internal_user, ctx)

        if ret is None:
            return cache.get_user(self.internal_user, ctx)

        return ret

    def get_user_as_member(self) -> typing.Optional[Member]:
        """Optional[:class:`Member`]: The affected user."""
        if isinstance(self.internal_user, Member):
            return self.internal_user

        if isinstance(self.internal_user, User):
            user_id = self.internal_user.id
        else:
            user_id = self.internal_user

        state = self.state
        cache = state.cache
        if cache is None:
            return None

        ctx = (
            MemberThroughAuditLogEntryActionUserCacheContext(
                type=CacheContextType.member_through_audit_log_entry_action_user,
                action=self,
            )
            if state.provide_cache_context('AuditLogEntryAction.user_as_member')
            else _MEMBER_THROUGH_AUDIT_LOG_ENTRY_ACTION_USER
        )

        return cache.get_server_member(self.server_id, user_id, ctx)

    def get_user_as_user(self) -> typing.Optional[User]:
        """Optional[:class:`User`]: The affected user."""
        if isinstance(self.internal_user, Member):
            if isinstance(self.internal_user.internal_user, User):
                return self.internal_user.internal_user
            return None
        if isinstance(self.internal_user, User):
            return self.internal_user

        state = self.state
        cache = state.cache
        if cache is None:
            return None

        ctx = (
            UserThroughAuditLogEntryActionUserCacheContext(
                type=CacheContextType.user_through_audit_log_entry_action_user,
                action=self,
            )
            if state.provide_cache_context('AuditLogEntryAction.user_as_user')
            else _USER_THROUGH_AUDIT_LOG_ENTRY_ACTION_USER
        )

        return cache.get_user(self.internal_user, ctx)

    @property
    def channel_update(self) -> PartialChannel:
        """:class:`PartialChannel`: The updated channel as it was updated."""
        if self.internal_channel_update is None:
            raise NoData(
                what='',
                type='AuditLogEntryAction.channel_update',
                hint='the audit log entry action type is not channel_update',
            )
        return self.internal_channel_update

    @property
    def member_update(self) -> PartialMember:
        """:class:`PartialMember`: The updated member as it was updated."""
        if self.internal_member_update is None:
            raise NoData(
                what='',
                type='AuditLogEntryAction.member_update',
                hint='the audit log entry action type is not member_update',
            )
        return self.internal_member_update

    @property
    def role_update(self) -> PartialRole:
        """:class:`PartialRole`: The updated role as it was updated."""
        if self.internal_role_update is None:
            raise NoData(
                what='',
                type='AuditLogEntryAction.role_update',
                hint='the audit log entry action type is not role_update',
            )
        return self.internal_role_update

    @property
    def server_update(self) -> PartialServer:
        """:class:`PartialServer`: The updated server as it was updated."""
        if self.internal_server_update is None:
            raise NoData(
                what='',
                type='AuditLogEntryAction.server_update',
                hint='the audit log entry action type is not server_update',
            )
        return self.internal_server_update

    @property
    def user_id(self) -> str:
        """:class:`str`: The ID of the user."""
        if isinstance(self.internal_user, (Member, User)):
            return self.internal_user.id
        return self.internal_user

    def to_dict(self) -> raw.AuditLogEntryAction:
        """:class:`dict`: Convert audit log entry action to raw data."""

        if self.type is AuditLogEntryActionType.message_delete:
            return {
                'type': 'MessageDelete',
                'author': self.user_id,
                'channel': self.channel_id,
            }
        elif self.type is AuditLogEntryActionType.message_bulk_delete:
            return {
                'type': 'MessageBulkDelete',
                'channel': self.channel_id,
                'count': self.count,
            }
        elif self.type is AuditLogEntryActionType.ban:
            return {
                'type': 'BanCreate',
                'user': self.user_id,
            }
        elif self.type is AuditLogEntryActionType.unban:
            return {
                'type': 'BanDelete',
                'user': self.user_id,
            }
        elif self.type is AuditLogEntryActionType.channel_create:
            return {
                'type': 'ChannelCreate',
                'channel': self.channel_id,
            }
        elif self.type is AuditLogEntryActionType.channel_update:
            payload: dict[str, typing.Any] = {
                'type': 'ChannelEdit',
                'channel': self.channel_id,
            }
            fields = self.channel_update.get_clear_fields()
            if fields:
                payload['remove'] = fields
            payload['partial'] = self.channel_update.to_dict()
            return payload  # type: ignore
        elif self.type is AuditLogEntryActionType.channel_role_permissions_update:
            return {
                'type': 'ChannelRolePermissionsEdit',
                'channel': self.channel_id,
                'role': self.role_id,
                'permissions': self.permissions.to_dict(),
            }
        elif self.type is AuditLogEntryActionType.channel_delete:
            return {
                'type': 'ChannelDelete',
                'channel': self.channel_id,
            }
        elif self.type is AuditLogEntryActionType.member_update:
            payload: dict[str, typing.Any] = {
                'type': 'MemberEdit',
                'user': self.user_id,
            }
            fields = self.member_update.get_clear_fields()
            if fields:
                payload['remove'] = fields
            payload['partial'] = self.member_update.to_dict()
            return payload  # type: ignore
        elif self.type is AuditLogEntryActionType.member_remove:
            return {
                'type': 'MemberKick',
                'user': self.user_id,
            }
        elif self.type is AuditLogEntryActionType.server_update:
            payload: dict[str, typing.Any] = {
                'type': 'ServerEdit',
            }
            fields = self.server_update.get_clear_fields()
            if fields:
                payload['remove'] = fields
            payload['partial'] = self.server_update.to_dict()
            return payload  # type: ignore
        elif self.type is AuditLogEntryActionType.role_update:
            payload: dict[str, typing.Any] = {
                'type': 'RoleEdit',
                'role': self.role_id,
            }
            fields = self.role_update.get_clear_fields()
            if fields:
                payload['remove'] = fields
            payload['partial'] = self.role_update.to_dict()
            return payload  # type: ignore
        elif self.type is AuditLogEntryActionType.role_create:
            return {
                'type': 'RoleCreate',
                'role': self.role_id,
            }
        elif self.type is AuditLogEntryActionType.role_delete:
            return {
                'type': 'RoleDelete',
                'role': self.role_id,
                'name': self.name,
            }
        elif self.type is AuditLogEntryActionType.roles_reorder:
            return {
                'type': 'RolesReorder',
                'positions': self.positions,
            }
        elif self.type is AuditLogEntryActionType.invite_delete:
            return {
                'type': 'InviteDelete',
                'invite': self.invite_code,
                'channel': self.channel_id,
            }
        elif self.type is AuditLogEntryActionType.webhook_create:
            return {
                'type': 'WebhookCreate',
                'webhook': self.webhook_id,
                'channel': self.channel_id,
            }
        elif self.type is AuditLogEntryActionType.emoji_delete:
            return {
                'type': 'EmojiDelete',
                'emoji': self.emoji_id,
                'name': self.name,
            }
        elif self.internal_payload is None:
            raise TypeError(f'Cannot serialize action of type {self.type!r}')
        else:
            return self.internal_payload  # type: ignore


__all__ = (
    'AuditLogEntry',
    'AuditLogEntryAction',
)
