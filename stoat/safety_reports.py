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
from .enums import ReportStatus, ReportedContentType

if typing.TYPE_CHECKING:
    from datetime import datetime

    from . import raw
    from .enums import ContentReportReason, UserReportReason


@define(slots=True)
class BaseReport(Base):
    """Represents an user-generated platform moderation report on Stoat.

    This inherits from :class:`Base`.
    """

    author_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID who created this report."""

    case_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The internal case's ID.
    
    .. versionadded:: 1.3
    """

    content: ReportedContent = field(repr=True, kw_only=True)
    """:class:`ReportedContent`: The reported content."""

    additional_context: str = field(repr=True, kw_only=True)
    """:class:`str`: The additional context included in report."""

    notes: str = field(repr=True, kw_only=True)
    """:class:`str`: The additional notes included in report."""

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object, /) -> bool:
        return self is other or isinstance(other, BaseReport) and self.id == other.id


@define(slots=True)
class CreatedReport(BaseReport):
    """Represents a created report on Stoat.

    This inherits from :class:`BaseReport`.
    """

    @property
    def status(self) -> typing.Literal[ReportStatus.created]:
        """Literal[:attr:`.ReportStatus.created`]: The report's status."""
        return ReportStatus.created

    def to_dict(self) -> raw.CreatedReport:
        """:class:`dict`: Convert report to raw data.

        .. versionadded:: 1.3
        """
        return {
            '_id': self.id,
            'author_id': self.author_id,
            'case_id': self.case_id,
            'content': self.content.to_dict(),
            'additional_context': self.additional_context,
            'status': 'Created',
            'notes': self.notes,
        }


@define(slots=True)
class RejectedReport(BaseReport):
    """Represents a rejected report on Stoat.

    This inherits from :class:`BaseReport`.
    """

    rejection_reason: str = field(repr=True, kw_only=True)
    """:class:`str`: The reason why this report was rejected."""

    closed_at: typing.Optional[datetime] = field(repr=True, kw_only=True)
    """Optional[:class:`~datetime.datetime`]: When the report was closed."""

    @property
    def status(self) -> typing.Literal[ReportStatus.rejected]:
        """Literal[:attr:`.ReportStatus.rejected`]: The report's status."""
        return ReportStatus.rejected

    def to_dict(self) -> raw.RejectedReport:
        """:class:`dict`: Convert report to raw data.

        .. versionadded:: 1.3
        """
        return {
            '_id': self.id,
            'author_id': self.author_id,
            'case_id': self.case_id,
            'content': self.content.to_dict(),
            'additional_context': self.additional_context,
            'status': 'Rejected',
            'rejection_reason': self.rejection_reason,
            'closed_at': None if self.closed_at is None else self.closed_at.isoformat(),
            'notes': self.notes,
        }


@define(slots=True)
class ResolvedReport(BaseReport):
    """Represents a resolved report on Stoat.

    This inherits from :class:`BaseReport`.
    """

    closed_at: typing.Optional[datetime] = field(repr=True, kw_only=True)
    """Optional[:class:`~datetime.datetime`]: When the report was closed."""

    @property
    def status(self) -> typing.Literal[ReportStatus.resolved]:
        """Literal[:attr:`.ReportStatus.resolved`]: The report's status."""
        return ReportStatus.resolved

    def to_dict(self) -> raw.ResolvedReport:
        """:class:`dict`: Convert report to raw data.

        .. versionadded:: 1.3
        """
        return {
            '_id': self.id,
            'author_id': self.author_id,
            'case_id': self.case_id,
            'content': self.content.to_dict(),
            'additional_context': self.additional_context,
            'status': 'Resolved',
            'closed_at': None if self.closed_at is None else self.closed_at.isoformat(),
            'notes': self.notes,
        }


Report = typing.Union[CreatedReport, RejectedReport, ResolvedReport]


@define(slots=True)
class BaseReportedContent:
    """Represents content being reported."""

    target_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The target's ID."""


@define(slots=True)
class MessageReportedContent(BaseReportedContent):
    """Represents a message being reported.

    This inherits from :class:`BaseReportedContent`.
    """

    reason: ContentReportReason = field(repr=True, kw_only=True)
    """:class:`ContentReportReason`: The reason why message was reported."""

    @property
    def type(self) -> typing.Literal[ReportedContentType.message]:
        """Literal[:attr:`.ReportedContentType.message`]: The content's type."""
        return ReportedContentType.message

    def to_dict(self) -> raw.MessageReportedContent:
        """:class:`dict`: Convert reported content to raw data.

        .. versionadded:: 1.3
        """
        return {
            'type': 'Message',
            'id': self.target_id,
            'report_reason': self.reason.value,
        }


@define(slots=True)
class ServerReportedContent(BaseReportedContent):
    """Represents a server being reported.

    This inherits from :class:`BaseReportedContent`.
    """

    reason: ContentReportReason = field(repr=True, kw_only=True)
    """:class:`ContentReportReason`: The reason why server was reported."""

    @property
    def type(self) -> typing.Literal[ReportedContentType.server]:
        """Literal[:attr:`.ReportedContentType.server`]: The content's type."""
        return ReportedContentType.server

    def to_dict(self) -> raw.ServerReportedContent:
        """:class:`dict`: Convert reported content to raw data.

        .. versionadded:: 1.3
        """
        return {
            'type': 'Server',
            'id': self.target_id,
            'report_reason': self.reason.value,
        }


@define(slots=True)
class UserReportedContent(BaseReportedContent):
    """Represents an user being reported.

    This inherits from :class:`BaseReportedContent`.
    """

    reason: UserReportReason = field(repr=True, kw_only=True)
    """:class:`UserReportReason`: The reason why user was reported."""

    message_id: typing.Optional[str] = field(repr=True, kw_only=True)
    """Optional[:class:`str`]: The message's ID with report context."""

    @property
    def type(self) -> typing.Literal[ReportedContentType.user]:
        """Literal[:attr:`.ReportedContentType.user`]: The content's type."""
        return ReportedContentType.user

    def to_dict(self) -> raw.UserReportedContent:
        """:class:`dict`: Convert reported content to raw data.

        .. versionadded:: 1.3
        """
        payload: raw.UserReportedContent = {
            'type': 'User',
            'id': self.target_id,
            'report_reason': self.reason.value,
        }
        if self.message_id is not None:
            payload['message_id'] = self.message_id
        return payload


ReportedContent = typing.Union[MessageReportedContent, ServerReportedContent, UserReportedContent]

__all__ = (
    'BaseReport',
    'CreatedReport',
    'RejectedReport',
    'ResolvedReport',
    'Report',
    'BaseReportedContent',
    'MessageReportedContent',
    'ServerReportedContent',
    'UserReportedContent',
    'ReportedContent',
)
