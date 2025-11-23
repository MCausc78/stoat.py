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

from attrs import define, field

from .base import Base
from .enums import AuditLogEntryActionType
from .server import Member
from .user import User

if typing.TYPE_CHECKING:
    from . import raw
    from .channel import PartialChannel
    from .permissions import PermissionOverride
    from .server import PartialRole, PartialServer, PartialMember


@define(slots=True, eq=True)
class AuditLogEntry(Base):
    """Represents an audit log entry.

    Most of fields will be set to their zero value (empty string, 0, empty array) if the type.
    """

    server_id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The ID of the server."""

    reason: typing.Optional[str] = field(repr=True, kw_only=True, eq=True)
    """Optional[:class:`str`]: The reason for the action."""

    user_id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The ID of the user who performed the action."""

    action: AuditLogEntryAction = field(repr=True, kw_only=True, eq=True)
    """:class:`AuditLogEntryAction`: Details about the action."""

    def __hash__(self) -> int:
        return hash((self.id, self.server_id))

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

    type: AuditLogEntryActionType = field(repr=True, kw_only=True, eq=True)
    """:class:`AuditLogEntryActionType`: The type of the action."""

    channel_id: str = field(default='', repr=True, kw_only=True, eq=True)
    """:class:`str`: The ID of the channel."""

    channel_update: PartialChannel = field(repr=True, kw_only=True, eq=True)
    """:class:`PartialChannel`: The updated channel as it was updated."""

    count: int = field(default=0, repr=True, kw_only=True, eq=True)
    """:class:`int`: The count of deleted messages."""

    emoji_id: str = field(default='', repr=True, kw_only=True, eq=True)
    """:class:`str`: The ID of the emoji."""

    internal_user: typing.Union[Member, User, str] = field(
        default='',
        repr=False,
        kw_only=True,
        # In case of hydration, the ID always should be used for comparsion
        eq=lambda target: target.id if isinstance(target, (Member, User)) else target,
    )
    """Union[:class:`Member`, :class:`User`, :class:`str`]: The ID of the user, or full member/user instance."""

    invite_code: str = field(default='', repr=True, kw_only=True, eq=True)
    """:class:`str`: The ID of the invite."""

    member_update: PartialMember = field(repr=True, kw_only=True, eq=True)
    """:class:`PartialMember`: The updated member as it was updated."""

    name: str = field(default='', repr=True, kw_only=True, eq=True)
    """:class:`str`: The name of the affected entity."""

    permissions: PermissionOverride = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The permissions of the affected entity."""

    positions: list[str] = field(repr=True, kw_only=True, eq=True)
    """List[:class:`str`]: The new IDs of roles with their index in list representing their rank."""

    role_id: str = field(default='', repr=True, kw_only=True, eq=True)
    """:class:`str`: The ID of the role."""

    role_update: PartialRole = field(repr=True, kw_only=True, eq=True)
    """:class:`PartialRole`: The updated role as it was updated."""

    server_update: PartialServer = field(repr=True, kw_only=True, eq=True)
    """:class:`PartialServer`: The updated server as it was updated."""

    webhook_id: str = field(default='', repr=True, kw_only=True, eq=True)
    """:class:`str`: The ID of the webhook."""

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

        raise TypeError(f'Cannot serialize action of type {self.type!r}')


__slots__ = (
    'AuditLogEntry',
    'AuditLogEntryAction',
)
