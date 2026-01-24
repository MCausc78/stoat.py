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

# from .core import UNDEFINED, UndefinedOr
from .enums import AdminAuditItemActionType

if typing.TYPE_CHECKING:
    from datetime import datetime

    from . import raw
    from .safety_reports import Report
    from .user import User


@define(slots=True, eq=True)
class AdminAuditItem(Base):
    """Represents an audit item for the platform moderator.

    .. versionadded:: 1.3
    """

    moderator_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The admin user's ID that performed the action."""

    action_type: AdminAuditItemActionType = field(repr=True, kw_only=True)
    """:class:`AdminAuditItemActionType`: The action's type."""

    case_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The case's ID."""

    target_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The targeted object's ID."""

    context: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The additional context."""

    timestamp: datetime = field(repr=True, kw_only=True)
    """:class:`~datetime.datetime`: When the action occured."""

    def __hash__(self) -> int:
        return hash(self.id)

    def to_dict(self) -> raw.AdminAuditItem:
        """:class:`dict`: Convert audit item to raw data."""
        return {
            'id': self.id,
            'mod': self.moderator_id,
            'action': self.action_type.value,
            'case': self.case_id,
            'target': self.target_id,
            'context': self.context,
            'timestamp': self.timestamp.isoformat(),
        }


@define(slots=True, eq=True)
class BaseAdminComment(Base):
    """Represents a base comment on an object (user / server), visible and created by platform moderators.

    .. versionadded:: 1.3
    """


@define(slots=True, eq=True)
class AdminComment(BaseAdminComment):
    """Represents a comment on an object (user / server), visible and created by platform moderators.

    .. versionadded:: 1.3
    """

    case_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The case's ID."""

    object_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The object's ID the comment is for."""

    user_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The admin user's ID that created this comment."""

    edited_at: typing.Optional[datetime] = field(repr=True, kw_only=True)
    """Optional[:class:`~datetime.datetime`]: When the comment was edited."""

    content: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The comment's content."""

    system_message: typing.Optional[AdminAuditItemActionType] = field(repr=True, kw_only=True)
    """Optional[:class:`AdminAuditItemActionType`]: The system event that happened."""

    system_message_target: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The system message's target (user / server) ID."""

    system_message_context: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The system message's raw context."""

    def to_dict(self) -> raw.AdminComment:
        """:class:`dict`: Convert comment to raw data."""
        payload: raw.AdminComment = {'id': self.id}  # type: ignore
        if self.case_id is not None:
            payload['case'] = self.case_id
        payload['object'] = self.object_id
        payload['user'] = self.user_id
        if self.content is not None:
            payload['content'] = self.content
        if self.system_message is not None:
            payload['system_message'] = self.system_message.value
        if self.system_message_target is not None:
            payload['system_message_target'] = self.system_message_target
        if self.system_message_context is not None:
            payload['system_message_context'] = self.system_message_context
        return payload


@define(slots=True, eq=True)
class BaseAdminCase(Base):
    """Represents a base case that is being investigated by platform moderators. Includes relevant reports.

    .. versionadded:: 1.3
    """


@define(slots=True, eq=True)
class AdminCase(BaseAdminCase):
    """Represents a case that is being investigated by platform moderators. Includes relevant reports.

    .. versionadded:: 1.3
    """

    short_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The short case's ID. Typically this is last 7 characters of the ID."""

    # It's unclear what the ID refers to
    owner_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The case owner user's ID."""

    title: str = field(repr=True, kw_only=True)
    """:class:`str`: The case's title."""

    status: str = field(repr=True, kw_only=True)
    """:class:`str`: The case's status."""

    closed_at: typing.Optional[datetime] = field(repr=True, kw_only=True)
    """Optional[:class:`~datetime.datetime`]: When the case was closed."""

    tags: list[str] = field(repr=True, kw_only=True)
    """List[:class:`str`]: The case's tags."""

    reports: list[Report] = field(repr=True, kw_only=True)
    """List[:class:`Report`]: The reports assigned to the case."""

    def to_dict(self) -> raw.AdminCase:
        """:class:`dict`: Convert case to raw data."""
        return {
            'id': self.id,
            'short_id': self.short_id,
            'owner': self.owner_id,
            'title': self.title,
            'status': self.status,
            'closed_at': None if self.closed_at is None else self.closed_at.isoformat(),
            'tags': self.tags,
            'reports': [r.to_dict() for r in self.reports],
        }


@define(slots=True, eq=True)
class AdminStrike(Base):
    """Represents a strike for target (user / server) given by platform moderators.

    .. versionadded:: 1.3
    """

    target_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The target's ID the strike is for."""

    moderator_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The admin user's ID that created the strike."""

    case_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The case's ID that caused the strike."""

    associated_action: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The associated action."""

    overruled: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the strike has been overruled and therefore removed."""

    reason: str = field(repr=True, kw_only=True)
    """:class:`str`: The reason for the strike."""

    moderator_context: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The context added by the moderator."""

    def to_dict(self) -> raw.AdminStrike:
        """:class:`dict`: Convert strike to raw data."""
        payload: raw.AdminStrike = {
            'id': self.id,
            'target': self.target_id,
            'mod': self.moderator_id,
        }  # type: ignore
        if self.case_id is not None:
            payload['case'] = self.case_id
        if self.associated_action is not None:
            payload['associated_action'] = self.associated_action
        if self.overruled:
            payload['overruled'] = self.overruled
        payload['reason'] = self.reason
        if self.moderator_context is not None:
            payload['mod_context'] = self.moderator_context
        return payload


@define(slots=True, eq=True)
class BaseAdminToken(Base):
    """Represents a base admin user account's token.

    .. versionadded:: 1.3
    """


@define(slots=True, eq=True)
class AdminToken(BaseAdminToken):
    """Represents an admin user account's token.

    .. versionadded:: 1.3
    """

    user_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The ID of the admin user the token belongs to."""

    token: str = field(repr=True, kw_only=True)
    """:class:`str`: The secret token string."""

    expires_at: datetime = field(repr=True, kw_only=True)
    """:class:`~datetime.datetime`: When the token expires."""

    def to_dict(self) -> raw.AdminToken:
        """:class:`dict`: Convert token to raw data."""
        return {
            'id': self.id,
            'user': self.user_id,
            'token': self.token,
            'expiry': self.expires_at.isoformat(),
        }


@define(slots=True, eq=True)
class BaseAdminUser(Base):
    """Represents a base admin user.

    .. versionadded:: 1.3
    """


@define(slots=True, eq=True)
class AdminUser(BaseAdminUser):
    """Represents an admin user.

    .. versionadded:: 1.3
    """

    platform_user_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The ID of the platform user the admin user belongs to."""

    email: str = field(repr=True, kw_only=True)
    """:class:`str`: The internal admin user's email."""

    active: bool = field(repr=True, kw_only=True)
    """:class:`str`: Whether the admin user can use the API."""

    raw_permissions: int = field(repr=True, kw_only=True)
    """:class:`int`: The raw admin user's permissions."""

    platform_user: typing.Optional[User] = field(repr=True, kw_only=True)
    """Optional[:class:`User`]: The platform user. Only filled if retrieved from :meth:`HTTPClient.get_admin_users`."""

    def to_dict(self) -> raw.AdminUser:
        """:class:`dict`: Convert admin user to raw data."""
        payload: raw.AdminUser = {
            'id': self.id,
            'platform_user_id': self.platform_user_id,
            'email': self.email,
            'active': self.active,
            'permissions': self.raw_permissions,
        }
        if self.platform_user is not None:
            payload['revolt_user'] = self.platform_user.to_dict()
        return payload


__all__ = (
    'AdminAuditItem',
    'BaseAdminComment',
    'AdminComment',
    'BaseAdminCase',
    'AdminCase',
    'AdminStrike',
    'BaseAdminToken',
    'AdminToken',
    'BaseAdminUser',
    'AdminUser',
)
