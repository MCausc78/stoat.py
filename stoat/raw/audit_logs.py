from __future__ import annotations

import typing
import typing_extensions

from .basic import Bool
from .channels import PartialChannel, FieldsChannel
from .permissions import Override
from .server_members import Member, PartialMember, FieldsMember
from .servers import PartialServer, PartialRole, FieldsServer, FieldsRole
from .users import User


class AuditLogEntry(typing.TypedDict):
    _id: str
    server: str
    reason: typing.Optional[str]
    user: str
    action: AuditLogEntryAction


class AuditLogEntryMessageDeleteAction(typing.TypedDict):
    type: typing.Literal['MessageDelete']
    author: str
    channel: str


class AuditLogEntryMessageBulkDeleteAction(typing.TypedDict):
    type: typing.Literal['MessageBulkDelete']
    channel: str
    count: int


class AuditLogEntryBanCreateAction(typing.TypedDict):
    type: typing.Literal['BanCreate']
    user: str


class AuditLogEntryBanDeleteAction(typing.TypedDict):
    type: typing.Literal['BanDelete']
    user: str


class AuditLogEntryChannelCreateAction(typing.TypedDict):
    type: typing.Literal['ChannelCreate']
    channel: str


class AuditLogEntryChannelEditAction(typing.TypedDict):
    type: typing.Literal['ChannelEdit']
    channel: str
    remove: typing_extensions.NotRequired[list[FieldsChannel]]
    partial: PartialChannel


class AuditLogEntryChannelRolePermissionsEditAction(typing.TypedDict):
    type: typing.Literal['ChannelRolePermissionsEdit']
    channel: str
    role: str
    permissions: Override


class AuditLogEntryChannelDeleteAction(typing.TypedDict):
    type: typing.Literal['ChannelDelete']
    channel: str


class AuditLogEntryMemberEditAction(typing.TypedDict):
    type: typing.Literal['MemberEdit']
    user: str
    remove: typing_extensions.NotRequired[list[FieldsMember]]
    partial: PartialMember


class AuditLogEntryMemberKickAction(typing.TypedDict):
    type: typing.Literal['MemberKick']
    user: str


class AuditLogEntryServerEditAction(typing.TypedDict):
    type: typing.Literal['ServerEdit']
    remove: typing_extensions.NotRequired[list[FieldsServer]]
    partial: PartialServer


class AuditLogEntryRoleEditAction(typing.TypedDict):
    type: typing.Literal['RoleEdit']
    role: str
    remove: typing_extensions.NotRequired[list[FieldsRole]]
    partial: PartialRole


class AuditLogEntryRoleCreateAction(typing.TypedDict):
    type: typing.Literal['RoleCreate']
    role: str


class AuditLogEntryRoleDeleteAction(typing.TypedDict):
    type: typing.Literal['RoleDelete']
    role: str
    name: str


class AuditLogEntryRolesReorderAction(typing.TypedDict):
    type: typing.Literal['RolesReorder']
    positions: list[str]


class AuditLogEntryInviteDeleteAction(typing.TypedDict):
    type: typing.Literal['InviteDelete']
    invite: str
    channel: str


class AuditLogEntryWebhookCreateAction(typing.TypedDict):
    type: typing.Literal['WebhookCreate']
    webhook: str
    channel: str


class AuditLogEntryEmojiDeleteAction(typing.TypedDict):
    type: typing.Literal['EmojiDelete']
    emoji: str
    name: str


AuditLogEntryAction = typing.Union[
    AuditLogEntryMessageDeleteAction,
    AuditLogEntryMessageBulkDeleteAction,
    AuditLogEntryBanCreateAction,
    AuditLogEntryBanDeleteAction,
    AuditLogEntryChannelCreateAction,
    AuditLogEntryChannelEditAction,
    AuditLogEntryChannelRolePermissionsEditAction,
    AuditLogEntryChannelDeleteAction,
    AuditLogEntryMemberEditAction,
    AuditLogEntryMemberKickAction,
    AuditLogEntryServerEditAction,
    AuditLogEntryRoleEditAction,
    AuditLogEntryRoleCreateAction,
    AuditLogEntryRoleDeleteAction,
    AuditLogEntryRolesReorderAction,
    AuditLogEntryInviteDeleteAction,
    AuditLogEntryWebhookCreateAction,
    AuditLogEntryEmojiDeleteAction,
]


class OptionsAuditLogQuery(typing.TypedDict):
    user: typing_extensions.NotRequired[str]
    type: typing_extensions.NotRequired[str]
    before: typing_extensions.NotRequired[str]
    after: typing_extensions.NotRequired[str]
    limit: typing_extensions.NotRequired[int]
    include_users: typing_extensions.NotRequired[Bool]


class AuditLogsAndUsersAuditLogQueryResponse(typing.TypedDict):
    audit_logs: list[AuditLogEntry]
    users: list[User]
    members: list[Member]


AuditLogQueryResponse = typing.Union[list[AuditLogEntry], AuditLogsAndUsersAuditLogQueryResponse]
