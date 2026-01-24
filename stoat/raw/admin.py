from __future__ import annotations

import typing
import typing_extensions

from .safety_reports import Report
from .server_members import Member, MemberWithUserResponse
from .servers import Server
from .users import User


class AdminAuditItemCreate(typing.TypedDict):
    mod: str
    action: AdminAuditItemActions
    case: str
    target: typing.Optional[str]
    context: typing.Optional[str]


class AdminAuditItem(typing.TypedDict):
    id: str
    mod: str
    action: AdminAuditItemActions
    case: str
    target: typing.Optional[str]
    context: typing.Optional[str]
    timestamp: str


class AdminCommentCreate(typing.TypedDict):
    case: typing.Optional[str]
    object: str
    content: str


class AdminCommentEdit(typing.TypedDict):
    content: str


class AdminComment(typing.TypedDict):
    id: str
    case: typing_extensions.NotRequired[str]
    object: str
    user: str
    edited_at: typing.Optional[str]
    content: typing_extensions.NotRequired[str]
    system_message: typing_extensions.NotRequired[AdminAuditItemActions]
    system_message_target: typing_extensions.NotRequired[str]
    system_message_context: typing_extensions.NotRequired[str]


class AdminCaseCreate(typing.TypedDict):
    owner: typing.Optional[str]
    title: typing.Optional[str]
    initial_reports: list[str]


class AdminCaseEdit(typing.TypedDict):
    owner: typing_extensions.NotRequired[str]
    title: typing_extensions.NotRequired[str]
    add_reports: typing_extensions.NotRequired[list[str]]
    remove_reports: typing_extensions.NotRequired[list[str]]


class AdminCase(typing.TypedDict):
    id: str
    short_id: str
    owner: str
    title: str
    status: str  # "Open"
    closed_at: typing.Optional[str]
    tags: list[str]
    reports: list[Report]


class AdminStrike(typing.TypedDict):
    id: str
    target: str
    mod: str
    case: typing_extensions.NotRequired[str]
    associated_action: typing_extensions.NotRequired[str]
    overruled: typing_extensions.NotRequired[bool]
    reason: str
    mod_context: typing_extensions.NotRequired[str]


class AdminStrikeCreate(typing.TypedDict):
    target: str
    case: typing.Optional[str]
    associated_action: typing.Optional[str]  # 1-25 chars
    reason: str  # max 2000 chars
    mod_context: typing.Optional[str]  # max 2000 chars


class AdminStrikeEdit(typing.TypedDict):
    case: typing_extensions.NotRequired[str]
    associated_action: typing_extensions.NotRequired[str]  # 1-25 chars
    reason: typing_extensions.NotRequired[str]  # max 2000 chars
    mod_context: typing_extensions.NotRequired[str]  # max 2000 chars


class AdminToken(typing.TypedDict):
    id: str
    user: str
    token: str
    expiry: str


class AdminTokenCreate(typing.TypedDict):
    expiry: str


class AdminUser(typing.TypedDict):
    id: str
    platform_user_id: str
    email: str
    active: bool
    permissions: int
    revolt_user: typing_extensions.NotRequired[User]


class AdminUserCreate(typing.TypedDict):
    # Should be 26 chars exactly, but its 10-20 (min-max) for now
    platform_user_id: str
    email: str
    active: bool
    permissions: int


class AdminUserEdit(typing.TypedDict):
    # Should be 26 chars exactly, but its 10-20 (min-max) for now
    platform_user_id: typing_extensions.NotRequired[str]
    email: typing_extensions.NotRequired[str]
    active: typing_extensions.NotRequired[bool]
    permissions: typing_extensions.NotRequired[int]


AdminAuditItemActions = typing.Literal[
    'CreateAdminUser',
    'EditAdminUser',
    'CreateToken',
    'RevokeToken',
    'CommentCreate',
    'CommentEdit',
    'CommentFetchForObject',
    'ServerFetch',
    'ServerFetchParticipants',
    'ServerFetchMembers',
    'ServerAddMember',
    'ServerChangeOwner',
    'ServerCreateInvite',
    'ServerDeleteInvite',
    'ServerDeleteAllInvites',
    'ServerDelete',
    'ServerEdit',
    'ServerRemoveMember',
    'ServerSetFlags',
    'ServerInstanceBanAllMembers',
    'ServerBanMember',
    'ServerUnbanMember',
]


class AdminServerResponse(typing.TypedDict):
    server: Server
    owner: User
    comments: list[AdminComment]


class AdminServerParticipantsResponse(typing.TypedDict):
    users: list[User]
    members: list[Member]
    sort_strategy: str


class AdminMemberWithUserAndOffsetResponse(typing.TypedDict):
    after: typing.Optional[int]
    users: list[MemberWithUserResponse]
