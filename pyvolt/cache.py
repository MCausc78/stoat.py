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

from abc import ABC, abstractmethod
import typing

from attrs import define, field

from .enums import Enum


if typing.TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from .abc import Messageable
    from .bot import Bot
    from .emoji import ServerEmoji, Emoji
    from .channel import (
        DMChannel,
        GroupChannel,
        BaseServerChannel,
        TextChannel,
        VoiceChannel,
        Channel,
        ChannelVoiceStateContainer,
    )
    from .client import Client
    from .emoji import BaseEmoji
    from .events import (
        ReadyEvent,
        PrivateChannelCreateEvent,
        ServerChannelCreateEvent,
        ChannelUpdateEvent,
        ChannelDeleteEvent,
        GroupRecipientAddEvent,
        GroupRecipientRemoveEvent,
        ChannelStartTypingEvent,
        ChannelStopTypingEvent,
        MessageAckEvent,
        MessageCreateEvent,
        MessageUpdateEvent,
        MessageAppendEvent,
        MessageDeleteEvent,
        MessageReactEvent,
        MessageUnreactEvent,
        MessageClearReactionEvent,
        MessageDeleteBulkEvent,
        ServerCreateEvent,
        ServerEmojiCreateEvent,
        ServerEmojiDeleteEvent,
        ServerUpdateEvent,
        ServerDeleteEvent,
        ServerMemberJoinEvent,
        ServerMemberUpdateEvent,
        ServerMemberRemoveEvent,
        RawServerRoleUpdateEvent,
        ServerRoleDeleteEvent,
        ReportCreateEvent,
        UserUpdateEvent,
        UserRelationshipUpdateEvent,
        UserSettingsUpdateEvent,
        UserPlatformWipeEvent,
        WebhookCreateEvent,
        WebhookUpdateEvent,
        WebhookDeleteEvent,
        SessionCreateEvent,
        SessionDeleteEvent,
        SessionDeleteAllEvent,
        VoiceChannelJoinEvent,
        VoiceChannelLeaveEvent,
        VoiceChannelMoveEvent,
        UserVoiceStateUpdateEvent,
        AuthenticatedEvent,
    )
    from .invite import (
        ServerPublicInvite,
        GroupPublicInvite,
        PrivateBaseInvite,
        GroupInvite,
        ServerInvite,
    )
    from .message import (
        BaseMessage,
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
        Message,
    )
    from .read_state import ReadState
    from .server import BaseRole, BaseServer, Server, BaseMember, Member
    from .webhook import Webhook
    from .user import BaseUser, User


class CacheContextType(Enum):
    custom = 'CUSTOM'
    undefined = 'UNDEFINED'
    user_request = 'USER_REQUEST'
    library_request = 'LIBRARY_REQUEST'

    ready_event = 'ReadyEvent'
    private_channel_create_event = 'PrivateChannelCreateEvent'
    server_channel_create_event = 'ServerChannelCreateEvent'
    channel_update_event = 'ChannelUpdateEvent'
    channel_delete_event = 'ChannelDeleteEvent'
    group_recipient_add_event = 'GroupRecipientAddEvent'
    group_recipient_remove_event = 'GroupRecipientRemoveEvent'
    channel_start_typing_event = 'ChannelStartTypingEvent'
    channel_stop_typing_event = 'ChannelStopTypingEvent'
    message_ack_event = 'MessageAckEvent'
    message_create_event = 'MessageCreateEvent'
    message_update_event = 'MessageUpdateEvent'
    message_append_event = 'MessageAppendEvent'
    message_delete_event = 'MessageDeleteEvent'
    message_react_event = 'MessageReactEvent'
    message_unreact_event = 'MessageUnreactEvent'
    message_clear_reaction_event = 'MessageClearReactionEvent'
    message_delete_bulk_event = 'MessageDeleteBulkEvent'
    server_create_event = 'ServerCreateEvent'
    server_emoji_create_event = 'ServerEmojiCreateEvent'
    server_emoji_delete_event = 'ServerEmojiDeleteEvent'
    server_update_event = 'ServerUpdateEvent'
    server_delete_event = 'ServerDeleteEvent'
    server_member_join_event = 'ServerMemberJoinEvent'
    server_member_update_event = 'ServerMemberUpdateEvent'
    server_member_remove_event = 'ServerMemberRemoveEvent'
    raw_server_role_update_event = 'RawServerRoleUpdateEvent'
    server_role_delete_event = 'ServerRoleDeleteEvent'
    report_create_event = 'ReportCreateEvent'
    user_update_event = 'UserUpdateEvent'
    user_platform_wipe_event = 'UserPlatformWipeEvent'
    user_relationship_update_event = 'UserRelationshipUpdateEvent'
    user_settings_update_event = 'UserSettingsUpdateEvent'
    webhook_create_event = 'WebhookCreateEvent'
    webhook_update_event = 'WebhookUpdateEvent'
    webhook_delete_event = 'WebhookDeleteEvent'
    session_create_event = 'SessionCreateEvent'
    session_delete_event = 'SessionDeleteEvent'
    session_delete_all_event = 'SessionDeleteAllEvent'
    voice_channel_join_event = 'VoiceChannelJoinEvent'
    voice_channel_leave_event = 'VoiceChannelLeaveEvent'
    voice_channel_move_event = 'VoiceChannelMoveEvent'
    user_voice_state_update_event = 'UserVoiceStateUpdateEvent'
    authenticated_event = 'AuthenticatedEvent'

    # Relationships
    message_through_messageable_getter = 'Messageable.get_message(): Optional[Message]'
    messages_through_messageable_getter = 'Messageable.messages: Dict[str, Message]'
    user_through_bot_owner = 'Bot.owner: User'
    user_through_dm_channel_initiator = 'DMChannel.initiator: User'
    message_through_dm_channel_last_message = 'DMChannel.last_message: Optional[Message]'
    read_state_through_dm_channel_read_state = 'DMChannel.read_state: ReadState'
    user_through_dm_channel_recipient = 'DMChannel.recipient: User'
    user_through_dm_channel_recipients = 'DMChannel.recipients: Tuple[User, User]'
    message_through_group_channel_last_message = 'GroupChannel.last_message: Optional[Message]'
    user_through_group_channel_owner = 'GroupChannel.owner: User'
    read_state_through_group_channel_read_state = 'GroupChannel.read_state: ReadState'
    user_through_group_channel_recipients = 'GroupChannel.recipients: List[User]'
    server_through_server_channel = 'BaseServerChannel.server: Server'
    message_through_text_channel_last_message = 'TextChannel.last_message: Optional[Message]'
    read_state_through_text_channel_read_state = 'TextChannel.read_state: ReadState'
    channel_voice_state_container_through_text_channel_voice_states = (
        'TextChannel.voice_states: ChannelVoiceStateContainer'
    )
    channel_voice_state_container_through_voice_channel_voice_states = (
        'VoiceChannel.voice_states: ChannelVoiceStateContainer'
    )

    channels_through_client_getter = 'Client.channels: Mapping[str, Channel]'
    emojis_through_client_getter = 'Client.emojis: Mapping[str, Emoji]'
    servers_through_client_getter = 'Client.servers: Mapping[str, Server]'
    users_through_client_getter = 'Client.users: Mapping[str, User]'
    user_ids_through_client_dm_channel_ids = 'Client.dm_channel_ids: Mapping[str, str]'
    channels_through_client_dm_channels = 'Client.dm_channels: Mapping[str, DMChannel]'
    channels_through_client_private_channels = 'Client.private_channels: Mapping[str, PrivateChannel]'
    channel_through_client_getter = 'Client.get_channel(): Optional[Channel]'
    emoji_through_client_getter = 'Client.get_emoji(): Optional[Emoji]'
    read_state_through_client_getter = 'Client.get_read_state(): Optional[ReadState]'
    server_through_client_getter = 'Client.get_server(): Optional[Server]'
    user_through_client_getter = 'Client.get_user(): Optional[User]'
    user_through_base_emoji_creator = 'BaseEmoji.creator: User'
    server_through_server_emoji_server = 'ServerEmoji.server: Server'
    server_through_server_public_invite_server = 'ServerPublicInvite.server: Server'
    channel_through_server_public_invite_channel = 'ServerPublicInvite.channel: ServerChannel'
    user_through_server_public_invite_user = 'ServerPublicInvite.user: User'
    channel_through_group_public_invite_channel = 'GroupPublicInvite.channel: GroupChannel'
    user_through_group_public_invite_user = 'GroupPublicInvite.user: User'
    user_through_private_base_invite_creator = 'PrivateBaseInvite.creator: User'
    channel_through_group_invite_channel = 'GroupInvite.channel: GroupChannel'
    server_through_server_invite_server = 'ServerInvite.server: Server'
    channel_through_server_invite_channel = 'ServerInvite.channel: ServerChannel'
    user_through_user_added_system_event_user = 'UserAddedSystemEvent.user: User'
    user_through_user_added_system_event_by = 'UserAddedSystemEvent.by: User'
    user_through_user_removed_system_event_user = 'UserRemovedSystemEvent.user: User'
    user_through_user_removed_system_event_by = 'UserRemovedSystemEvent.by: User'
    member_or_user_through_user_joined_system_event_user = 'UserJoinedSystemEvent.user: Union[Member, User]'
    member_or_user_through_user_left_system_event_user = 'UserLeftSystemEvent.user: Union[Member, User]'
    member_or_user_through_user_kicked_system_event_user = 'UserKickedSystemEvent.user: Union[Member, User]'
    member_or_user_through_user_banned_system_event_user = 'UserBannedSystemEvent.user: Union[Member, User]'
    user_through_channel_renamed_system_event_by = 'ChannelRenamedSystemEvent.by: User'
    user_through_channel_description_changed_system_event_by = 'ChannelDescriptionChangedSystemEvent.by: User'
    user_through_channel_icon_changed_system_event_by = 'ChannelIconChangedSystemEvent.by: User'
    user_through_channel_ownership_changed_system_event_from = 'ChannelOwnershipChangedSystemEvent.from_: User'
    user_through_channel_ownership_changed_system_event_to = 'ChannelOwnershipChangedSystemEvent.to: User'
    message_through_message_pinned_system_event_pinned_message = 'MessagePinnedSystemEvent.pinned_message: Message'
    member_or_user_through_message_pinned_system_event_by = 'MessagePinnedSystemEvent.by: Union[Member, User]'
    message_through_message_unpinned_system_event_unpinned_message = (
        'MessageUnpinnedSystemEvent.unpinned_message: Message'
    )
    member_or_user_through_message_unpinned_system_event_by = 'MessageUnpinnedSystemEvent.by: Union[Member, User]'
    user_through_call_started_system_event_by = 'CallStartedSystemEvent.by: User'
    channel_through_message_channel = 'Message.channel: Channel'
    server_through_message_server = 'Message.server: Optional[Server]'
    member_or_user_through_message_author = 'Message.author: Union[Member, User]'
    channel_through_read_state_channel = 'ReadState.channel: Channel'
    server_through_role_server = 'Role.server: Server'
    emoji_through_server_getter = 'Server.get_emoji(): Optional[Emoji]'
    member_through_server_getter = 'Server.get_member(): Optional[Member]'
    emojis_through_server_getter = 'Server.emojis: Dict[str, Emoji]'
    members_through_server_getter = 'Server.members: Dict[str, Member]'
    channel_through_server_getter = 'Server.get_channel(): Optional[ServerChannel]'
    channels_through_server_getter = 'Server.channels: List[ServerChannel]'
    member_through_server_owner = 'Server.owner: Member'
    server_through_member_server = 'Member.server: Server'
    user_through_member_getter = 'Member.user: User'
    user_through_user_bot_owner = 'User.bot_owner: User'
    channel_id_through_user_dm_channel_id = 'User.dm_channel_id: Optional[str]'
    channel_through_user_dm_channel = 'User.dm_channel: Optional[DMChannel]'
    user_through_webhook_creator = 'Webhook.creator: User'
    channel_through_webhook_channel = 'Webhook.channel: Union[GroupChannel, TextChannel]'


@define(slots=True)
class BaseCacheContext:
    """Represents a cache context."""

    type: CacheContextType = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.CacheContextType`: The context's type."""


@define(slots=True)
class UndefinedCacheContext(BaseCacheContext):
    """Represents a undefined cache context."""


@define(slots=True)
class EventCacheContext(BaseCacheContext):
    """Base class for cache contexts created by WebSocket events."""


@define(slots=True)
class ReadyEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ReadyEvent`."""

    event: ReadyEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ReadyEvent`: The event involved."""


@define(slots=True)
class PrivateChannelCreateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.PrivateChannelCreateEvent`."""

    event: PrivateChannelCreateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.PrivateChannelCreateEvent`: The event involved."""


@define(slots=True)
class ServerChannelCreateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ServerChannelCreateEvent`."""

    event: ServerChannelCreateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerChannelCreateEvent`: The event involved."""


@define(slots=True)
class ChannelUpdateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ChannelUpdateEvent`."""

    event: ChannelUpdateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ChannelUpdateEvent`: The event involved."""


@define(slots=True)
class ChannelDeleteEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ChannelDeleteEvent`."""

    event: ChannelDeleteEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ChannelDeleteEvent`: The event involved."""


@define(slots=True)
class GroupRecipientAddEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.GroupRecipientAddEvent`."""

    event: GroupRecipientAddEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.GroupRecipientAddEvent`: The event involved."""


@define(slots=True)
class GroupRecipientRemoveEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.GroupRecipientRemoveEvent`."""

    event: GroupRecipientRemoveEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.GroupRecipientRemoveEvent`: The event involved."""


@define(slots=True)
class ChannelStartTypingEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ChannelStartTypingEvent`."""

    event: ChannelStartTypingEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ChannelStartTypingEvent`: The event involved."""


@define(slots=True)
class ChannelStopTypingEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ChannelStopTypingEvent`."""

    event: ChannelStopTypingEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ChannelStopTypingEvent`: The event involved."""


@define(slots=True)
class MessageAckEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.MessageAckEvent`."""

    event: MessageAckEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.MessageAckEvent`: The event involved."""


@define(slots=True)
class MessageCreateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.MessageCreateEvent`."""

    event: MessageCreateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.MessageCreateEvent`: The event involved."""


@define(slots=True)
class MessageUpdateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.MessageUpdateEvent`."""

    event: MessageUpdateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.MessageUpdateEvent`: The event involved."""


@define(slots=True)
class MessageAppendEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.MessageAppendEvent`."""

    event: MessageAppendEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.MessageAppendEvent`: The event involved."""


@define(slots=True)
class MessageDeleteEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.MessageDeleteEvent`."""

    event: MessageDeleteEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.MessageDeleteEvent`: The event involved."""


@define(slots=True)
class MessageReactEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.MessageReactEvent`."""

    event: MessageReactEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.MessageReactEvent`: The event involved."""


@define(slots=True)
class MessageUnreactEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.MessageUnreactEvent`."""

    event: MessageUnreactEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.MessageUnreactEvent`: The event involved."""


@define(slots=True)
class MessageClearReactionEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.MessageClearReactionEvent`."""

    event: MessageClearReactionEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.MessageClearReactionEvent`: The event involved."""


@define(slots=True)
class MessageDeleteBulkEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.MessageDeleteBulkEvent`."""

    event: MessageDeleteBulkEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.MessageDeleteBulkEvent`: The event involved."""


@define(slots=True)
class ServerCreateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ServerCreateEvent`."""

    event: ServerCreateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerCreateEvent`: The event involved."""


@define(slots=True)
class ServerEmojiCreateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ServerEmojiCreateEvent`."""

    event: ServerEmojiCreateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerEmojiCreateEvent`: The event involved."""


@define(slots=True)
class ServerEmojiDeleteEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ServerEmojiDeleteEvent`."""

    event: ServerEmojiDeleteEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerEmojiDeleteEvent`: The event involved."""


@define(slots=True)
class ServerUpdateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ServerUpdateEvent`."""

    event: ServerUpdateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerUpdateEvent`: The event involved."""


@define(slots=True)
class ServerDeleteEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ServerDeleteEvent`."""

    event: ServerDeleteEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerDeleteEvent`: The event involved."""


@define(slots=True)
class ServerMemberJoinEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ServerMemberJoinEvent`."""

    event: ServerMemberJoinEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerMemberJoinEvent`: The event involved."""


@define(slots=True)
class ServerMemberUpdateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ServerMemberUpdateEvent`."""

    event: ServerMemberUpdateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerMemberUpdateEvent`: The event involved."""


@define(slots=True)
class ServerMemberRemoveEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ServerMemberRemoveEvent`."""

    event: ServerMemberRemoveEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerMemberRemoveEvent`: The event involved."""


@define(slots=True)
class RawServerRoleUpdateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.RawServerRoleUpdateEvent`."""

    event: RawServerRoleUpdateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.RawServerRoleUpdateEvent`: The event involved."""


@define(slots=True)
class ServerRoleDeleteEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ServerRoleDeleteEvent`."""

    event: ServerRoleDeleteEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerRoleDeleteEvent`: The event involved."""


@define(slots=True)
class ReportCreateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.ReportCreateEvent`."""

    event: ReportCreateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ReportCreateEvent`: The event involved."""


@define(slots=True)
class UserUpdateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.UserUpdateEvent`."""

    event: UserUpdateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.UserUpdateEvent`: The event involved."""


@define(slots=True)
class UserRelationshipUpdateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.UserRelationshipUpdateEvent`."""

    event: UserRelationshipUpdateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.UserRelationshipUpdateEvent`: The event involved."""


@define(slots=True)
class UserSettingsUpdateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.UserSettingsUpdateEvent`."""

    event: UserSettingsUpdateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.UserSettingsUpdateEvent`: The event involved."""


@define(slots=True)
class UserPlatformWipeEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.UserPlatformWipeEvent`."""

    event: UserPlatformWipeEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.UserPlatformWipeEvent`: The event involved."""


@define(slots=True)
class WebhookCreateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.WebhookCreateEvent`."""

    event: WebhookCreateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.WebhookCreateEvent`: The event involved."""


@define(slots=True)
class WebhookUpdateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.WebhookUpdateEvent`."""

    event: WebhookUpdateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.WebhookUpdateEvent`: The event involved."""


@define(slots=True)
class WebhookDeleteEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.WebhookDeleteEvent`."""

    event: WebhookDeleteEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.WebhookDeleteEvent`: The event involved."""


@define(slots=True)
class SessionCreateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.SessionCreateEvent`."""

    event: SessionCreateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.SessionCreateEvent`: The event involved."""


@define(slots=True)
class SessionDeleteEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.SessionDeleteEvent`."""

    event: SessionDeleteEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.SessionDeleteEvent`: The event involved."""


@define(slots=True)
class SessionDeleteAllEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.SessionDeleteAllEvent`."""

    event: SessionDeleteAllEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.SessionDeleteAllEvent`: The event involved."""


@define(slots=True)
class VoiceChannelJoinEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.VoiceChannelJoinEvent`."""

    event: VoiceChannelJoinEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.VoiceChannelJoinEvent`: The event involved."""


@define(slots=True)
class VoiceChannelLeaveEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.VoiceChannelLeaveEvent`."""

    event: VoiceChannelLeaveEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.VoiceChannelLeaveEvent`: The event involved."""


@define(slots=True)
class VoiceChannelMoveEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.VoiceChannelMoveEvent`."""

    event: VoiceChannelMoveEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.VoiceChannelMoveEvent`: The event involved."""


@define(slots=True)
class UserVoiceStateUpdateEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.UserVoiceStateUpdateEvent`."""

    event: UserVoiceStateUpdateEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.UserVoiceStateUpdateEvent`: The event involved."""


@define(slots=True)
class AuthenticatedEventCacheContext(EventCacheContext):
    """Represents a cache context that involves a :class:`.AuthenticatedEvent`."""

    event: AuthenticatedEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.AuthenticatedEvent`: The event involved."""


@define(slots=True)
class EntityCacheContext(BaseCacheContext):
    """Represents a cache context that involves an entity."""


@define(slots=True)
class MessageableCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`~pyvolt.abc.Messageable` entity."""

    entity: Messageable = field(repr=True, hash=True, kw_only=True, eq=True)


@define(slots=True)
class BotCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.Bot` entity."""

    bot: Bot = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.Bot`: The bot involved."""


@define(slots=True)
class DMChannelCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.DMChannel` entity."""

    channel: DMChannel = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.DMChannel`: The channel involved."""


@define(slots=True)
class GroupChannelCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.GroupChannel` entity."""

    channel: GroupChannel = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.GroupChannel`: The channel involved."""


@define(slots=True)
class BaseServerChannelCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.BaseServerChannel` entity."""

    channel: BaseServerChannel = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.BaseServerChannel`: The channel involved."""


@define(slots=True)
class TextChannelCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.TextChannel` entity."""

    channel: TextChannel = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.TextChannel`: The channel involved."""


@define(slots=True)
class VoiceChannelCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.VoiceChannel` entity."""

    channel: VoiceChannel = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.VoiceChannel`: The channel involved."""


@define(slots=True)
class BaseEmojiCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.BaseEmoji` entity."""

    emoji: BaseEmoji = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.BaseEmoji`: The emoji involved."""


@define(slots=True)
class ServerEmojiCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.ServerEmoji` entity."""

    emoji: ServerEmoji = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerEmoji`: The emoji involved."""


@define(slots=True)
class ClientCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.Client`."""

    client: Client = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.Client`: The client involved."""


@define(slots=True)
class ServerPublicInviteCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.ServerPublicInvite` entity."""

    invite: ServerPublicInvite = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerPublicInvite`: The invite involved."""


@define(slots=True)
class GroupPublicInviteCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.GroupPublicInvite` entity."""

    invite: GroupPublicInvite = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.GroupPublicInvite`: The invite involved."""


@define(slots=True)
class PrivateBaseInviteCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.PrivateBaseInvite` entity."""

    invite: PrivateBaseInvite = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.PrivateBaseInvite`: The invite involved."""


@define(slots=True)
class GroupInviteCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.GroupInvite` entity."""

    invite: GroupInvite = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.GroupInvite`: The invite involved."""


@define(slots=True)
class ServerInviteCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.ServerInvite` entity."""

    invite: ServerInvite = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ServerInvite`: The invite involved."""


@define(slots=True)
class BaseMessageCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.BaseMessage` entity."""

    message: BaseMessage = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.BaseMessage`: The message involved."""


@define(slots=True)
class MessageCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.Message` entity."""

    message: Message = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.Message`: The message involved."""


@define(slots=True)
class ReadStateCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.ReadState` entity."""

    read_state: ReadState = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.ReadState`: The read state involved."""


@define(slots=True)
class BaseRoleCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.BaseRole` entity."""

    role: BaseRole = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.BaseRole`: The role involved."""


@define(slots=True)
class BaseServerCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.BaseServer` entity."""

    server: BaseServer = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.BaseServer`: The server involved."""


@define(slots=True)
class BaseMemberCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.BaseMember` entity."""

    member: BaseMember = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.BaseMember`: The member involved."""


@define(slots=True)
class ServerCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.Server` entity."""

    server: Server = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.Server`: The server involved."""


@define(slots=True)
class BaseUserCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.BaseUser` entity."""

    user: BaseUser = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.BaseUser`: The user involved."""


@define(slots=True)
class UserCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.User` entity."""

    user: User = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.User`: The user involved."""


@define(slots=True)
class WebhookCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.Webhook` entity."""

    webhook: Webhook = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.Webhook`: The webhook involved."""


@define(slots=True)
class UserAddedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserAddedSystemEvent` entity."""

    system_message: StatelessUserAddedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessUserAddedSystemEvent`: The system message involved."""


@define(slots=True)
class UserRemovedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserRemovedSystemEvent` entity."""

    system_message: StatelessUserRemovedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessUserRemovedSystemEvent`: The system message involved."""


@define(slots=True)
class UserJoinedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessStatelessUserJoinedSystemEvent` entity."""

    system_message: StatelessUserJoinedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessUserJoinedSystemEvent`: The system message involved."""


@define(slots=True)
class UserLeftSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserLeftSystemEvent` entity."""

    system_message: StatelessUserLeftSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessUserLeftSystemEvent`: The system message involved."""


@define(slots=True)
class UserKickedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserKickedSystemEvent` entity."""

    system_message: StatelessUserKickedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessUserKickedSystemEvent`: The system message involved."""


@define(slots=True)
class UserBannedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserBannedSystemEvent` entity."""

    system_message: StatelessUserBannedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessUserBannedSystemEvent`: The system message involved."""


@define(slots=True)
class ChannelRenamedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessChannelRenamedSystemEvent` entity."""

    system_message: StatelessChannelRenamedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessChannelRenamedSystemEvent`: The system message involved."""


@define(slots=True)
class ChannelDescriptionChangedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessChannelDescriptionChangedSystemEvent` entity."""

    system_message: StatelessChannelDescriptionChangedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessChannelDescriptionChangedSystemEvent`: The system message involved."""


@define(slots=True)
class ChannelIconChangedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessChannelIconChangedSystemEvent` entity."""

    system_message: StatelessChannelIconChangedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessChannelIconChangedSystemEvent`: The system message involved."""


@define(slots=True)
class ChannelOwnershipChangedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessChannelOwnershipChangedSystemEvent` entity."""

    system_message: StatelessChannelOwnershipChangedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessChannelOwnershipChangedSystemEvent`: The system message involved."""


@define(slots=True)
class MessagePinnedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessMessagePinnedSystemEvent` entity."""

    system_message: StatelessMessagePinnedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessMessagePinnedSystemEvent`: The system message involved."""


@define(slots=True)
class MessageUnpinnedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessMessageUnpinnedSystemEvent` entity."""

    system_message: StatelessMessageUnpinnedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessMessageUnpinnedSystemEvent`: The system message involved."""


@define(slots=True)
class CallStartedSystemEventCacheContext(EntityCacheContext):
    """Represents a cache context that involves an :class:`.StatelessCallStartedSystemEvent` entity."""

    system_message: StatelessCallStartedSystemEvent = field(repr=True, hash=True, kw_only=True, eq=True)
    """:class:`.StatelessCallStartedSystemEvent`: The system message involved."""


@define(slots=True)
class MessageThroughMessageableGetterCacheContext(MessageableCacheContext):
    """Represents a cache context that involves an :class:`~pyvolt.abc.Messageable` entity, wishing to retrieve single message from target."""


@define(slots=True)
class MessagesThroughMessageableGetterCacheContext(MessageableCacheContext):
    """Represents a cache context that involves an :class:`~pyvolt.abc.Messageable` entity, wishing to retrieve all messages in target."""


@define(slots=True)
class UserThroughBotOwnerCacheContext(BotCacheContext):
    """Represents a cache context that involves an :class:`.Bot` entity, wishing to retrieve bot's owner."""


@define(slots=True)
class UserThroughDMChannelInitiatorCacheContext(DMChannelCacheContext):
    """Represents a cache context that involves an :class:`.DMChannel`, wishing to retrieve DM channel's initiator."""


@define(slots=True)
class MessageThroughDMChannelLastMessageCacheContext(DMChannelCacheContext):
    """Represents a cache context that involves an :class:`.DMChannel`, wishing to retrieve last DM channel's message."""


@define(slots=True)
class ReadStateThroughDMChannelReadStateCacheContext(DMChannelCacheContext):
    """Represents a cache context that involves an :class:`.DMChannel`, wishing to retrieve DM channel's read state."""


@define(slots=True)
class UserThroughDMChannelRecipientCacheContext(DMChannelCacheContext):
    """Represents a cache context that involves an :class:`.DMChannel`, wishing to retrieve DM channel's recipient."""


@define(slots=True)
class UserThroughDMChannelRecipientsCacheContext(DMChannelCacheContext):
    """Represents a cache context that involves an :class:`.DMChannel`, wishing to retrieve DM channel's recipients."""


@define(slots=True)
class MessageThroughGroupChannelLastMessageCacheContext(GroupChannelCacheContext):
    """Represents a cache context that involves an :class:`.GroupChannel`, wishing to retrieve last group channel's message."""


@define(slots=True)
class ReadStateThroughGroupChannelReadStateCacheContext(GroupChannelCacheContext):
    """Represents a cache context that involves an :class:`.GroupChannel`, wishing to retrieve group channel's read state."""


@define(slots=True)
class UserThroughGroupChannelOwnerCacheContext(GroupChannelCacheContext):
    """Represents a cache context that involves an :class:`.GroupChannel`, wishing to retrieve group channel's owner."""


@define(slots=True)
class UserThroughGroupChannelRecipientsCacheContext(GroupChannelCacheContext):
    """Represents a cache context that involves an :class:`.GroupChannel`, wishing to retrieve group channel's recipients."""


@define(slots=True)
class ServerThroughServerChannelCacheContext(BaseServerChannelCacheContext):
    """Represents a cache context that involves an :class:`.BaseServerChannel`, wishing to retrieve server the channel belongs to."""


@define(slots=True)
class MessageThroughTextChannelLastMessageCacheContext(TextChannelCacheContext):
    """Represents a cache context that involves an :class:`.TextChannel`, wishing to retrieve last text channel's message."""


@define(slots=True)
class UserThroughUserAddedSystemEventUserCacheContext(UserAddedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserAddedSystemEvent`, wishing to retrieve system message's user."""


@define(slots=True)
class UserThroughUserAddedSystemEventAuthorCacheContext(UserAddedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserAddedSystemEvent`, wishing to retrieve system message's author."""


@define(slots=True)
class UserThroughUserRemovedSystemEventUserCacheContext(UserRemovedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserRemovedSystemEvent`, wishing to retrieve system message's user."""


@define(slots=True)
class UserThroughUserRemovedSystemEventAuthorCacheContext(UserRemovedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserRemovedSystemEvent`, wishing to retrieve system message's author."""


@define(slots=True)
class MemberOrUserThroughUserJoinedSystemEventUserCacheContext(UserJoinedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserJoinedSystemEvent`, wishing to retrieve system message's user."""


@define(slots=True)
class MemberOrUserThroughUserLeftSystemEventUserCacheContext(UserLeftSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserLeftSystemEvent`, wishing to retrieve system message's user."""


@define(slots=True)
class MemberOrUserThroughUserKickedSystemEventUserCacheContext(UserKickedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserKickedSystemEvent`, wishing to retrieve system message's user."""


@define(slots=True)
class MemberOrUserThroughUserBannedSystemEventUserCacheContext(UserBannedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessUserBannedSystemEvent`, wishing to retrieve system message's user."""


@define(slots=True)
class UserThroughChannelRenamedSystemEventAuthorCacheContext(ChannelRenamedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessChannelRenamedSystemEvent`, wishing to retrieve system message's author."""


@define(slots=True)
class UserThroughChannelDescriptionChangedSystemEventAuthorCacheContext(
    ChannelDescriptionChangedSystemEventCacheContext
):
    """Represents a cache context that involves an :class:`.StatelessChannelDescriptionChangedSystemEvent`, wishing to retrieve system message's author."""


@define(slots=True)
class UserThroughChannelIconChangedSystemEventAuthorCacheContext(ChannelIconChangedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessChannelIconChangedSystemEvent`, wishing to retrieve system message's author."""


@define(slots=True)
class UserThroughChannelOwnershipChangedSystemEventFromCacheContext(ChannelOwnershipChangedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessChannelOwnershipChangedSystemEvent`, wishing to retrieve system message's old group owner."""


@define(slots=True)
class UserThroughChannelOwnershipChangedSystemEventToCacheContext(ChannelOwnershipChangedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessChannelOwnershipChangedSystemEvent`, wishing to retrieve system message's new group owner."""


@define(slots=True)
class MessageThroughMessagePinnedSystemEventPinnedMessageCacheContext(MessagePinnedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessMessagePinnedSystemEvent`, wishing to retrieve system message's pinned message."""


@define(slots=True)
class MemberOrUserThroughMessagePinnedSystemEventAuthorCacheContext(MessagePinnedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessMessagePinnedSystemEvent`, wishing to retrieve system message's author."""


@define(slots=True)
class MessageThroughMessageUnpinnedSystemEventUnpinnedMessageCacheContext(MessageUnpinnedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessMessageUnpinnedSystemEvent`, wishing to retrieve system message's pinned message."""


@define(slots=True)
class MemberOrUserThroughMessageUnpinnedSystemEventAuthorCacheContext(MessageUnpinnedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessMessageUnpinnedSystemEvent`, wishing to retrieve system message's author."""


@define(slots=True)
class UserThroughCallStartedSystemEventAuthorCacheContext(CallStartedSystemEventCacheContext):
    """Represents a cache context that involves an :class:`.StatelessCallStartedSystemEvent`, wishing to retrieve system message's author."""


@define(slots=True)
class ChannelThroughMessageChannelCacheContext(BaseMessageCacheContext):
    """Represents a cache context that involves an :class:`.BaseMessage`, wishing to retrieve message's channel."""


@define(slots=True)
class ServerThroughMessageServerCacheContext(BaseMessageCacheContext):
    """Represents a cache context that involves an :class:`.BaseMessage`, wishing to retrieve message's server."""


@define(slots=True)
class MemberOrUserThroughMessageAuthorCacheContext(MessageCacheContext):
    """Represents a cache context that involves an :class:`.Message`, wishing to retrieve message's author."""


@define(slots=True)
class ReadStateThroughTextChannelReadStateCacheContext(TextChannelCacheContext):
    """Represents a cache context that involves an :class:`.TextChannel`, wishing to retrieve text channel's read state."""


@define(slots=True)
class ServerThroughRoleServerCacheContext(BaseRoleCacheContext):
    """Represents a cache context that involves an :class:`.BaseRole`, wishing to retrieve role's server."""


@define(slots=True)
class ChannelVoiceStateContainerThroughTextChannelVoiceStatesCacheContext(TextChannelCacheContext):
    """Represents a cache context that involves an :class:`.TextChannel`, wishing to retrieve channel's voice states."""


@define(slots=True)
class ChannelVoiceStateContainerThroughVoiceChannelVoiceStatesCacheContext(VoiceChannelCacheContext):
    """Represents a cache context that involves an :class:`.VoiceChannel`, wishing to retrieve channel's voice states."""


@define(slots=True)
class UserThroughBaseEmojiCreatorCacheContext(BaseEmojiCacheContext):
    """Represents a cache context that involves an :class:`.BaseEmoji`, wishing to retrieve emoji's creator."""


@define(slots=True)
class ServerThroughServerEmojiServerCacheContext(ServerEmojiCacheContext):
    """Represents a cache context that involves an :class:`.ServerEmoji`, wishing to retrieve emoji's server."""


@define(slots=True)
class ServerThroughServerPublicInviteServerCacheContext(ServerPublicInviteCacheContext):
    """Represents a cache context that involves an :class:`.ServerPublicInvite`, wishing to retrieve destination server."""


@define(slots=True)
class ChannelThroughServerPublicInviteChannelCacheContext(ServerPublicInviteCacheContext):
    """Represents a cache context that involves an :class:`.ServerPublicInvite`, wishing to retrieve destination channel."""


@define(slots=True)
class UserThroughServerPublicInviteUserCacheContext(ServerPublicInviteCacheContext):
    """Represents a cache context that involves an :class:`.ServerPublicInvite`, wishing to retrieve invite's creator."""


@define(slots=True)
class ChannelThroughGroupPublicInviteChannelCacheContext(GroupPublicInviteCacheContext):
    """Represents a cache context that involves an :class:`.GroupPublicInviteCacheContext`, wishing to retrieve destination group channel."""


@define(slots=True)
class UserThroughGroupPublicInviteUserCacheContext(GroupPublicInviteCacheContext):
    """Represents a cache context that involves an :class:`.GroupPublicInviteCacheContext`, wishing to retrieve invite's creator.."""


@define(slots=True)
class UserThroughPrivateBaseInviteCreatorCacheContext(PrivateBaseInviteCacheContext):
    """Represents a cache context that involves an :class:`.PrivateBaseInviteCacheContext`, wishing to retrieve invite's creator."""


@define(slots=True)
class ChannelThroughGroupInviteChannelCacheContext(GroupInviteCacheContext):
    """Represents a cache context that involves an :class:`.GroupInviteCacheContext`, wishing to retrieve destination group channel."""


@define(slots=True)
class ServerThroughServerInviteServerCacheContext(ServerInviteCacheContext):
    """Represents a cache context that involves an :class:`.ServerInviteCacheContext`, wishing to retrieve destination server."""


@define(slots=True)
class ChannelThroughServerInviteChannelCacheContext(ServerInviteCacheContext):
    """Represents a cache context that involves an :class:`.ServerInviteCacheContext`, wishing to retrieve destination server channel."""


@define(slots=True)
class ChannelThroughReadStateChannelCacheContext(ReadStateCacheContext):
    """Represents a cache context that involves an :class:`.ReadState`, wishing to retrieve read state's channel."""


@define(slots=True)
class EmojiThroughServerGetterCacheContext(BaseServerCacheContext):
    """Represents a cache context that involves an :class:`.BaseServer`, wishing to retrieve server emoji."""


@define(slots=True)
class MemberThroughServerGetterCacheContext(BaseServerCacheContext):
    """Represents a cache context that involves an :class:`.BaseServer`, wishing to retrieve server member."""


@define(slots=True)
class EmojisThroughServerGetterCacheContext(BaseServerCacheContext):
    """Represents a cache context that involves an :class:`.BaseServer`, wishing to retrieve server's emojis."""


@define(slots=True)
class MembersThroughServerGetterCacheContext(BaseServerCacheContext):
    """Represents a cache context that involves an :class:`.BaseServer`, wishing to retrieve server's members."""


@define(slots=True)
class ChannelThroughServerGetterCacheContext(BaseServerCacheContext):
    """Represents a cache context that involves an :class:`.BaseServer`, wishing to retrieve server channel."""


@define(slots=True)
class ChannelsThroughServerGetterCacheContext(BaseServerCacheContext):
    """Represents a cache context that involves an :class:`.BaseServer`, wishing to retrieve server's channels."""


@define(slots=True)
class MemberThroughServerOwnerCacheContext(ServerCacheContext):
    """Represents a cache context that involves an :class:`.Server`, wishing to retrieve server's owner."""


@define(slots=True)
class UserThroughBaseMemberGetterCacheContext(BaseMemberCacheContext):
    """Represents a cache context that involves an :class:`.BaseMember`, wishing to retrieve member's user."""


@define(slots=True)
class UserThroughUserBotOwnerCacheContext(UserCacheContext):
    """Represents a cache context that involves an :class:`.User`, wishing to retrieve owner of bot user."""


@define(slots=True)
class ChannelIDThroughUserDMChannelIDCacheContext(BaseUserCacheContext):
    """Represents a cache context that involves an :class:`.BaseUser`, wishing to retrieve ID of the DM channel with this user."""


@define(slots=True)
class ChannelThroughUserDMChannelIDCacheContext(BaseUserCacheContext):
    """Represents a cache context that involves an :class:`.BaseUser`, wishing to retrieve the DM channel with this user."""


@define(slots=True)
class UserThroughWebhookCreatorCacheContext(WebhookCacheContext):
    """Represents a cache context that involves an :class:`.Webhook`, wishing to retrieve webhook's creator."""


@define(slots=True)
class ChannelThroughWebhookChannelCacheContext(WebhookCacheContext):
    """Represents a cache context that involves an :class:`.Webhook`, wishing to retrieve webhook's channel."""


_UNDEFINED: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(type=CacheContextType.undefined)
_USER_REQUEST: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(type=CacheContextType.user_request)
_READY_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(type=CacheContextType.ready_event)
_PRIVATE_CHANNEL_CREATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.private_channel_create_event,
)
_SERVER_CHANNEL_CREATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_channel_create_event,
)
_CHANNEL_UPDATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_update_event,
)
_CHANNEL_DELETE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_delete_event,
)
_GROUP_RECIPIENT_ADD_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.group_recipient_add_event,
)
_GROUP_RECIPIENT_REMOVE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.group_recipient_remove_event,
)
_CHANNEL_START_TYPING_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_start_typing_event,
)
_CHANNEL_STOP_TYPING_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_stop_typing_event,
)
_MESSAGE_ACK_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(type=CacheContextType.message_ack_event)
_MESSAGE_CREATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_create_event,
)
_MESSAGE_UPDATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_update_event,
)
_MESSAGE_APPEND_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_append_event,
)
_MESSAGE_DELETE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_delete_event,
)
_MESSAGE_REACT_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_react_event,
)
_MESSAGE_UNREACT_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_unreact_event,
)
_MESSAGE_CLEAR_REACTION_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_clear_reaction_event,
)
_MESSAGE_DELETE_BULK_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_delete_bulk_event,
)
_SERVER_CREATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_create_event,
)
_SERVER_EMOJI_CREATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_emoji_create_event,
)
_SERVER_EMOJI_DELETE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_emoji_delete_event,
)
_SERVER_UPDATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_update_event,
)
_SERVER_DELETE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_delete_event,
)
_SERVER_MEMBER_JOIN_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_member_join_event,
)
_SERVER_MEMBER_UPDATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_member_update_event,
)
_SERVER_MEMBER_REMOVE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_member_remove_event,
)
_RAW_SERVER_ROLE_UPDATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.raw_server_role_update_event,
)
_SERVER_ROLE_DELETE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_role_delete_event,
)
_REPORT_CREATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.report_create_event,
)
_USER_UPDATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(type=CacheContextType.user_update_event)
_USER_RELATIONSHIP_UPDATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_relationship_update_event,
)
_USER_SETTINGS_UPDATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_settings_update_event,
)
_USER_PLATFORM_WIPE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_platform_wipe_event,
)
_WEBHOOK_CREATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.webhook_create_event,
)
_WEBHOOK_UPDATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.webhook_update_event,
)
_WEBHOOK_DELETE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.webhook_delete_event,
)
_SESSION_CREATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.session_create_event,
)
_SESSION_DELETE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.session_delete_event,
)
_SESSION_DELETE_ALL_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.session_delete_all_event,
)
_VOICE_CHANNEL_JOIN_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.voice_channel_join_event,
)
_VOICE_CHANNEL_LEAVE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.voice_channel_leave_event,
)
_VOICE_CHANNEL_MOVE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.voice_channel_move_event,
)
_USER_VOICE_STATE_UPDATE_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_voice_state_update_event,
)
_AUTHENTICATED_EVENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.authenticated_event,
)
_MESSAGE_THROUGH_MESSAGEABLE_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_through_messageable_getter,
)
_MESSAGES_THROUGH_MESSAGEABLE_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.messages_through_messageable_getter,
)
_USER_THROUGH_BOT_OWNER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_bot_owner,
)
_USER_THROUGH_DM_CHANNEL_INITIATOR: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_dm_channel_initiator,
)
_MESSAGE_THROUGH_DM_CHANNEL_LAST_MESSAGE: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_through_dm_channel_last_message,
)
_READ_STATE_THROUGH_DM_CHANNEL_READ_STATE: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.read_state_through_dm_channel_read_state,
)
_SERVER_THROUGH_ROLE_SERVER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_through_role_server,
)
_USER_THROUGH_DM_CHANNEL_RECIPIENT: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_dm_channel_recipient,
)
_USER_THROUGH_DM_CHANNEL_RECIPIENTS: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_dm_channel_recipients,
)
_MESSAGE_THROUGH_GROUP_CHANNEL_LAST_MESSAGE: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_through_group_channel_last_message,
)
_USER_THROUGH_GROUP_CHANNEL_OWNER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_group_channel_owner,
)
_READ_STATE_THROUGH_GROUP_CHANNEL_READ_STATE: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.read_state_through_group_channel_read_state,
)
_USER_THROUGH_GROUP_CHANNEL_RECIPIENTS: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_group_channel_recipients,
)
_SERVER_THROUGH_SERVER_CHANNEL: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_through_server_channel,
)
_MESSAGE_THROUGH_TEXT_CHANNEL_LAST_MESSAGE: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.message_through_text_channel_last_message,
)
_READ_STATE_THROUGH_TEXT_CHANNEL_READ_STATE: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.read_state_through_text_channel_read_state,
)
_CHANNEL_VOICE_STATE_CONTAINER_THROUGH_TEXT_CHANNEL_VOICE_STATES: typing.Final[UndefinedCacheContext] = (
    UndefinedCacheContext(
        type=CacheContextType.channel_voice_state_container_through_text_channel_voice_states,
    )
)
_CHANNEL_VOICE_STATE_CONTAINER_THROUGH_VOICE_CHANNEL_VOICE_STATES: typing.Final[UndefinedCacheContext] = (
    UndefinedCacheContext(
        type=CacheContextType.channel_voice_state_container_through_voice_channel_voice_states,
    )
)

_CHANNELS_THROUGH_CLIENT_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channels_through_client_getter,
)
_EMOJIS_THROUGH_CLIENT_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.emojis_through_client_getter,
)
_SERVERS_THROUGH_CLIENT_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.servers_through_client_getter,
)
_USERS_THROUGH_CLIENT_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.users_through_client_getter,
)
_USER_IDS_THROUGH_CLIENT_DM_CHANNELS: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_ids_through_client_dm_channel_ids,
)
_CHANNELS_THROUGH_CLIENT_DM_CHANNELS: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channels_through_client_dm_channels,
)
_CHANNELS_THROUGH_CLIENT_PRIVATE_CHANNELS: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channels_through_client_private_channels,
)
_CHANNEL_THROUGH_CLIENT_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channels_through_client_private_channels,
)
_EMOJI_THROUGH_CLIENT_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.emoji_through_client_getter,
)
_READ_STATE_THROUGH_CLIENT_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.read_state_through_client_getter,
)
_SERVER_THROUGH_CLIENT_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_through_client_getter,
)
_USER_THROUGH_CLIENT_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_client_getter,
)
_USER_THROUGH_BASE_EMOJI_CREATOR: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_base_emoji_creator,
)
_SERVER_THROUGH_SERVER_EMOJI_SERVER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_through_server_emoji_server,
)
_SERVER_THROUGH_SERVER_PUBLIC_INVITE_SERVER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_through_server_public_invite_server,
)
_CHANNEL_THROUGH_SERVER_PUBLIC_INVITE_CHANNEL: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_through_server_public_invite_channel,
)
_USER_THROUGH_SERVER_PUBLIC_INVITE_USER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_server_public_invite_user,
)
_CHANNEL_THROUGH_GROUP_PUBLIC_INVITE_CHANNEL: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_through_group_public_invite_channel,
)
_USER_THROUGH_GROUP_PUBLIC_INVITE_USER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_group_public_invite_user,
)
_USER_THROUGH_PRIVATE_BASE_INVITE_CREATOR: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_private_base_invite_creator,
)
_CHANNEL_THROUGH_GROUP_INVITE_CHANNEL: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_through_group_invite_channel,
)
_SERVER_THROUGH_SERVER_INVITE_SERVER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_through_server_invite_server,
)
_CHANNEL_THROUGH_SERVER_INVITE_CHANNEL: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_through_server_invite_channel,
)
_USER_THROUGH_USER_ADDED_SYSTEM_EVENT_USER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_user_added_system_event_user,
)
_USER_THROUGH_USER_ADDED_SYSTEM_EVENT_BY: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_user_added_system_event_by,
)
_USER_THROUGH_USER_REMOVED_SYSTEM_EVENT_USER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_user_removed_system_event_user,
)
_USER_THROUGH_USER_REMOVED_SYSTEM_EVENT_BY: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_user_removed_system_event_by,
)
_MEMBER_OR_USER_THROUGH_USER_JOINED_SYSTEM_EVENT_USER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.member_or_user_through_user_joined_system_event_user,
)
_MEMBER_OR_USER_THROUGH_USER_LEFT_SYSTEM_EVENT_USER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.member_or_user_through_user_left_system_event_user,
)
_MEMBER_OR_USER_THROUGH_USER_KICKED_SYSTEM_EVENT_USER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.member_or_user_through_user_kicked_system_event_user,
)
_MEMBER_OR_USER_THROUGH_USER_BANNED_SYSTEM_EVENT_USER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.member_or_user_through_user_banned_system_event_user,
)
_USER_THROUGH_CHANNEL_RENAMED_SYSTEM_EVENT_BY: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_channel_renamed_system_event_by,
)
_USER_THROUGH_CHANNEL_DESCRIPTION_CHANGED_SYSTEM_EVENT_BY: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_channel_description_changed_system_event_by,
)
_USER_THROUGH_CHANNEL_ICON_CHANGED_SYSTEM_EVENT_BY: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_channel_icon_changed_system_event_by,
)
_USER_THROUGH_CHANNEL_OWNERSHIP_CHANGED_SYSTEM_EVENT_FROM: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_channel_ownership_changed_system_event_from,
)
_USER_THROUGH_CHANNEL_OWNERSHIP_CHANGED_SYSTEM_EVENT_TO: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_channel_ownership_changed_system_event_to,
)
_MESSAGE_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_PINNED_MESSAGE: typing.Final[UndefinedCacheContext] = (
    UndefinedCacheContext(
        type=CacheContextType.message_through_message_pinned_system_event_pinned_message,
    )
)
_MEMBER_OR_USER_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_BY: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.member_or_user_through_message_pinned_system_event_by,
)
_MESSAGE_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_UNPINNED_MESSAGE: typing.Final[UndefinedCacheContext] = (
    UndefinedCacheContext(
        type=CacheContextType.message_through_message_unpinned_system_event_unpinned_message,
    )
)
_MEMBER_OR_USER_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_BY: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.member_or_user_through_message_unpinned_system_event_by,
)
_USER_THROUGH_CALL_STARTED_SYSTEM_EVENT_BY: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_call_started_system_event_by,
)
_CHANNEL_THROUGH_MESSAGE_CHANNEL: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_through_message_channel,
)
_SERVER_THROUGH_MESSAGE_SERVER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.server_through_message_server,
)
_MEMBER_OR_USER_THROUGH_MESSAGE_AUTHOR: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.member_or_user_through_message_author,
)
_CHANNEL_THROUGH_READ_STATE_CHANNEL: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_through_read_state_channel,
)
_EMOJI_THROUGH_SERVER_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.emoji_through_server_getter,
)
_MEMBER_THROUGH_SERVER_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.member_through_server_getter,
)
_EMOJIS_THROUGH_SERVER_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.emojis_through_server_getter,
)
_MEMBERS_THROUGH_SERVER_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.members_through_server_getter,
)
_CHANNEL_THROUGH_SERVER_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_through_server_getter,
)
_CHANNELS_THROUGH_SERVER_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channels_through_server_getter,
)
_MEMBER_THROUGH_SERVER_OWNER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.member_through_server_owner,
)
_USER_THROUGH_USER_BOT_OWNER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_user_bot_owner,
)
_CHANNEL_THROUGH_USER_DM_CHANNEL: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_through_user_dm_channel,
)
_CHANNEL_ID_THROUGH_USER_DM_CHANNEL_ID: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_id_through_user_dm_channel_id,
)
_USER_THROUGH_MEMBER_GETTER: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_member_getter,
)
_USER_THROUGH_WEBHOOK_CREATOR: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.user_through_webhook_creator,
)
_CHANNEL_THROUGH_WEBHOOK_CHANNEL: typing.Final[UndefinedCacheContext] = UndefinedCacheContext(
    type=CacheContextType.channel_through_webhook_channel,
)

ProvideCacheContextIn = typing.Literal[
    # Events
    'ReadyEvent',
    'PrivateChannelCreateEvent',
    'ServerChannelCreateEvent',
    'ChannelUpdateEvent',
    'ChannelDeleteEvent',
    'GroupRecipientAddEvent',
    'GroupRecipientRemoveEvent',
    'ChannelStartTypingEvent',
    'ChannelStopTypingEvent',
    'MessageAckEvent',
    'MessageCreateEvent',
    'MessageUpdateEvent',
    'MessageAppendEvent',
    'MessageDeleteEvent',
    'MessageReactEvent',
    'MessageUnreactEvent',
    'MessageClearReactionEvent',
    'MessageDeleteBulkEvent',
    'ServerCreateEvent',
    'ServerEmojiCreateEvent',
    'ServerEmojiDeleteEvent',
    'ServerUpdateEvent',
    'ServerDeleteEvent',
    'ServerMemberJoinEvent',
    'ServerMemberUpdateEvent',
    'ServerMemberRemoveEvent',
    'RawServerRoleUpdateEvent',
    'ServerRoleDeleteEvent',
    'ReportCreateEvent',
    'UserUpdateEvent',
    'UserRelationshipUpdateEvent',
    'UserSettingsUpdateEvent',
    'UserPlatformWipeEvent',
    'WebhookCreateEvent',
    'WebhookUpdateEvent',
    'WebhookDeleteEvent',
    'SessionCreateEvent',
    'SessionDeleteEvent',
    'SessionDeleteAllEvent',
    'VoiceChannelJoinEvent',
    'VoiceChannelLeaveEvent',
    'UserVoiceStateUpdateEvent',
    'AuthenticatedEvent',
    # Relationships
    'Messageable.get_message()',
    'Messageable.messages',
    'Bot.owner',
    'DMChannel.initiator',
    'DMChannel.last_message',
    'DMChannel.read_state',
    'DMChannel.recipient',
    'DMChannel.recipients',
    'GroupChannel.last_message',
    'GroupChannel.owner',
    'GroupChannel.read_state',
    'GroupChannel.recipients',
    'BaseServerChannel.server',
    'TextChannel.read_state',
    'TextChannel.voice_states',
    'VoiceChannel.voice_states',
    'BaseEmoji.creator',
    'ServerEmoji.server',
    'Client.channels',
    'Client.emojis',
    'Client.servers',
    'Client.users',
    'Client.dm_channel_ids',
    'Client.dm_channels',
    'Client.private_channels',
    'Client.get_channel()',
    'Client.get_emoji()',
    'Client.get_read_state()',
    'Client.get_server()',
    'Client.get_user()',
    'ServerPublicInvite.server',
    'ServerPublicInvite.channel',
    'ServerPublicInvite.user',
    'GroupPublicInvite.channel',
    'GroupPublicInvite.user',
    'PrivateBaseInvite.creator',
    'GroupInvite.channel',
    'ServerInvite.server',
    'ServerInvite.channel',
    'UserAddedSystemEvent.user',
    'UserAddedSystemEvent.by',
    'UserRemovedSystemEvent.user',
    'UserRemovedSystemEvent.by',
    'UserJoinedSystemEvent.user',
    'UserLeftSystemEvent.user',
    'UserKickedSystemEvent.user',
    'UserBannedSystemEvent.user',
    'ChannelRenamedSystemEvent.by',
    'ChannelDescriptionChangedSystemEvent.by',
    'ChannelIconChangedSystemEvent.by',
    'ChannelOwnershipChangedSystemEvent.from_',
    'ChannelOwnershipChangedSystemEvent.to',
    'MessagePinnedSystemEvent.pinned_message',
    'MessagePinnedSystemEvent.by',
    'MessageUnpinnedSystemEvent.unpinned_message',
    'MessageUnpinnedSystemEvent.by',
    'CallStartedSystemEvent.by',
    'Message.channel',
    'Message.server',
    'Message.author',
    'ReadState.channel',
    'Role.server',
    'Server.get_emoji()',
    'Server.get_member()',
    'Server.emojis',
    'Server.members',
    'Server.get_channel()',
    'Server.channels',
    'Server.owner',
    'Member.server',
    'Member.user',
    'User.bot_owner',
    'User.dm_channel_id',
    'User.dm_channel',
    'Webhook.creator',
    'Webhook.channel',
]


class Cache(ABC):
    """An ABC that represents cache.

    .. note::
        This class might not be what you're looking for.
        Head over to :class:`.EmptyCache` and :class:`.MapCache` for implementations.
    """

    __slots__ = ()

    ############
    # Channels #
    ############

    @abstractmethod
    def get_channel(self, channel_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Channel]:
        """Optional[:class:`.Channel`]: Retrieves a channel using ID.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    def get_all_channels(self, ctx: BaseCacheContext, /) -> Sequence[Channel]:
        """Sequence[:class:`.Channel`]: Retrieves all available channels as sequence.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        return list(self.get_channels_mapping(ctx).values())

    @abstractmethod
    def get_channels_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, Channel]:
        """Mapping[:class:`str`, :class:`.Channel`]: Retrieves all available channels as mapping.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def store_channel(self, channel: Channel, ctx: BaseCacheContext, /) -> None:
        """Stores a channel.

        Parameters
        ----------
        channel: :class:`.Channel`
            The channel to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_channel(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        """Deletes a channel.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """

        ...

    @abstractmethod
    def get_private_channels_mapping(
        self, ctx: BaseCacheContext, /
    ) -> Mapping[str, typing.Union[DMChannel, GroupChannel]]:
        """Mapping[:class:`str`, Union[:class:`.DMChannel`, :class:`.GroupChannel`]]: Retrieve all private channels as mapping.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    ####################
    # Channel Messages #
    ####################
    @abstractmethod
    def get_message(self, channel_id: str, message_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Message]:
        """Optional[:class:`.Message`]: Retrieves a message in channel using channel and message IDs.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        message_id: :class:`str`
            The message's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    def get_all_messages_of(self, channel_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Sequence[Message]]:
        """Optional[Sequence[:class:`.Message`]]: Retrieves all messages from a channel.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ms = self.get_messages_mapping_of(channel_id, ctx)
        if ms is None:
            return None
        return list(ms.values())

    @abstractmethod
    def get_messages_mapping_of(
        self, channel_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[Mapping[str, Message]]:
        """Optional[Mapping[:class:`str`, :class:`.Message`]]: Retrieves all messages from a channel as mapping.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def store_message(self, message: Message, ctx: BaseCacheContext, /) -> None:
        """Stores a message.

        Parameters
        ----------
        message: :class:`.Message`
            The message to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_message(self, channel_id: str, message_id: str, ctx: BaseCacheContext, /) -> None:
        """Deletes a message from channel.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        message_id: :class:`str`
            The message's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_messages_of(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        """Deletes all messages from a channel.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    ###############
    # Read States #
    ###############
    @abstractmethod
    def get_read_state(self, channel_id: str, ctx: BaseCacheContext, /) -> typing.Optional[ReadState]:
        """Optional[:class:`.ReadState`]: Retrieves a read state using channel ID.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    def get_all_read_states(self, ctx: BaseCacheContext, /) -> Sequence[ReadState]:
        """Sequence[:class:`.ReadState`]: Retrieves all available read states as sequence.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        return list(self.get_read_states_mapping(ctx).values())

    @abstractmethod
    def get_read_states_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, ReadState]:
        """Mapping[:class:`str`, :class:`.ReadState`]: Retrieves all available read states as mapping.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def store_read_state(self, read_state: ReadState, ctx: BaseCacheContext, /) -> None:
        """Stores a channel.

        Parameters
        ----------
        channel: :class:`.Channel`
            The channel to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_read_state(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        """Deletes a read state.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    ##########
    # Emojis #
    ##########

    @abstractmethod
    def get_emoji(self, emoji_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Emoji]:
        """Optional[:class:`.Emoji`]: Retrieves an emoji using ID.

        Parameters
        ----------
        emoji_id: :class:`str`
            The emoji's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    def get_all_emojis(self, ctx: BaseCacheContext, /) -> Sequence[Emoji]:
        """Sequence[:class:`.Emoji`]: Retrieves all available emojis as sequence.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        return list(self.get_emojis_mapping(ctx).values())

    @abstractmethod
    def get_emojis_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, Emoji]:
        """Mapping[:class:`str`, :class:`.Emoji`]: Retrieves all available emojis as mapping.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def get_server_emojis_mapping(
        self,
    ) -> Mapping[str, Mapping[str, ServerEmoji]]:
        """Mapping[:class:`str`, Mapping[:class:`str`, :class:`.ServerEmoji`]]: Retrieves all available server emojis as mapping of server ID to mapping of emoji IDs."""
        ...

    @abstractmethod
    def get_server_emojis_mapping_of(
        self, server_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[Mapping[str, ServerEmoji]]:
        """Optional[Mapping[:class:`str`, :class:`.ServerEmoji`]]: Retrieves all emojis from a server as mapping.

        Parameters
        ----------
        server_id: :class:`str`
            The server's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_server_emojis_of(self, server_id: str, ctx: BaseCacheContext, /) -> None:
        """Deletes all emojis from a server.

        Parameters
        ----------
        server_id: :class:`str`
            The server's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def store_emoji(self, emoji: Emoji, ctx: BaseCacheContext, /) -> None:
        """Stores an emoji.

        Parameters
        ----------
        emoji: :class:`.Emoji`
            The emoji to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_emoji(self, emoji_id: str, server_id: typing.Optional[str], ctx: BaseCacheContext, /) -> None:
        """Deletes an emoji from server.

        Parameters
        ----------
        emoji_id: :class:`str`
            The emoji's ID.
        server_id: Optional[:class:`str`]
            The server's ID. ``None`` if server ID is unavailable.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    ###########
    # Servers #
    ###########

    @abstractmethod
    def get_server(self, server_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Server]:
        """Optional[:class:`.Server`]: Retrieves a server using ID.

        Parameters
        ----------
        server_id: :class:`str`
            The server's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    def get_all_servers(self, ctx: BaseCacheContext, /) -> Sequence[Server]:
        """Sequence[:class:`.Server`]: Retrieves all available servers as sequence.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        return list(self.get_servers_mapping(ctx).values())

    @abstractmethod
    def get_servers_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, Server]:
        """Mapping[:class:`str`, :class:`.Server`]: Retrieves all available servers as mapping.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def store_server(self, server: Server, ctx: BaseCacheContext, /) -> None:
        """Stores a server.

        Parameters
        ----------
        server: :class:`.Server`
            The server to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_server(self, server_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Server]:
        """Deletes a server.

        Parameters
        ----------
        server_id: :class:`str`
            The server's ID.
        ctx: :class:`.BaseCacheContext`
            The context.

        Returns
        -------
        Optional[:class:`.Server`]
            The server removed from the cache, if any.
        """
        ...

    ##################
    # Server Members #
    ##################
    @abstractmethod
    def get_server_member(self, server_id: str, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Member]:
        """Optional[:class:`.Member`]: Retrieves a member in server using server and user IDs.

        Parameters
        ----------
        server_id: :class:`str`
            The server's ID.
        user_id: :class:`str`
            The user's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    def get_all_server_members_of(self, server_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Sequence[Member]]:
        """Optional[Sequence[:class:`.Member`]]: Retrieves all members from a server.

        Parameters
        ----------
        server_id: :class:`str`
            The server's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ms = self.get_server_members_mapping_of(server_id, ctx)
        if ms is None:
            return None
        return list(ms.values())

    @abstractmethod
    def get_server_members_mapping_of(
        self, server_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[Mapping[str, Member]]:
        """Optional[Mapping[:class:`str`, :class:`.Member`]]: Retrieves all members from a server as mapping.

        Parameters
        ----------
        server_id: :class:`str`
            The server's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def bulk_store_server_members(
        self,
        server_id: str,
        members: dict[str, Member],
        ctx: BaseCacheContext,
        /,
    ) -> None:
        """Stores server members in bulk.

        Parameters
        ----------
        server_id: :class:`str`
            The server's ID to store members in.
        members: Dict[:class:`str`, :class:`.Member`]
            The members to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def overwrite_server_members(
        self,
        server_id: str,
        members: dict[str, Member],
        ctx: BaseCacheContext,
        /,
    ) -> None:
        """Overwrites members of a server.

        Parameters
        ----------
        server_id: :class:`str`
            The server's ID to overwrite members in.
        members: Dict[:class:`str`, :class:`.Member`]
            The member to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def store_server_member(self, member: Member, ctx: BaseCacheContext, /) -> None:
        """Stores a member.

        Parameters
        ----------
        member: :class:`.Member`
            The member to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_server_member(self, server_id: str, user_id: str, ctx: BaseCacheContext, /) -> None:
        """Deletes a member from server.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        member_id: :class:`str`
            The member user's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_server_members_of(self, server_id: str, ctx: BaseCacheContext, /) -> None:
        """Deletes all members from a server.

        Parameters
        ----------
        server_id: :class:`str`
            The server's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def get_servers_member_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, Mapping[str, Member]]:
        """Mapping[:class:`str`, Mapping[:class:`str`, :class:`.Member`]]: Retrieves all available server members as mapping.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    #########
    # Users #
    #########
    @abstractmethod
    def get_user(self, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[User]:
        """Optional[:class:`.User`]: Retrieves a user using ID.

        Parameters
        ----------
        user_id: :class:`str`
            The user's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    def get_all_users(self, ctx: BaseCacheContext, /) -> Sequence[User]:
        """Sequence[:class:`.User`]: Retrieves all available users as sequence.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        return list(self.get_users_mapping(ctx).values())

    @abstractmethod
    def get_users_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, User]:
        """Mapping[:class:`str`, :class:`.User`]: Retrieves all available users as mapping.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def store_user(self, user: User, ctx: BaseCacheContext, /) -> None:
        """Stores an user.

        Parameters
        ----------
        user: :class:`.User`
            The user to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_user(self, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[User]:
        """Removes an user from cache.

        Parameters
        ----------
        user_id: :class:`str`
            The ID of the user to remove from cache.
        ctx: :class:`.BaseCacheContext`
            The context.

        Returns
        -------
        Optional[:class:`.User`]
            The removed user.
        """
        ...

    @abstractmethod
    def bulk_store_users(self, users: dict[str, User], ctx: BaseCacheContext, /) -> None:
        """Stores users in bulk.

        Parameters
        ----------
        users: Dict[:class:`str`, :class:`.User`]
            The users to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    ############################
    # Private Channels by User #
    ############################
    @abstractmethod
    def get_private_channel_by_user(self, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[str]:
        """Optional[:class:`str`]: Retrieves a private channel ID using user ID.

        Parameters
        ----------
        user_id: :class:`str`
            The user's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    def get_all_private_channels_by_users(self, ctx: BaseCacheContext, /) -> Sequence[str]:
        """Sequence[:class:`str`]: Retrieves all available DM channel IDs as sequence.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        return list(self.get_private_channels_by_users_mapping(ctx).values())

    @abstractmethod
    def get_private_channels_by_users_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, str]:
        """Mapping[:class:`str`, :class:`str`]: Retrieves all available DM channel IDs as mapping of user IDs.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def store_private_channel_by_user(self, channel: DMChannel, ctx: BaseCacheContext, /) -> None:
        """Stores a DM channel.

        Parameters
        ----------
        channel: :class:`.DMChannel`
            The channel to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    # Should be implemented in `delete_channel`, or in event
    @abstractmethod
    def delete_private_channel_by_user(self, user_id: str, ctx: BaseCacheContext, /) -> None:
        """Deletes a DM channel by user ID.

        Parameters
        ----------
        user_id: :class:`str`
            The user's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """

        ...

    ########################
    # Channel Voice States #
    ########################
    @abstractmethod
    def get_channel_voice_state(
        self, channel_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[ChannelVoiceStateContainer]: ...

    def get_all_channel_voice_states(self, ctx: BaseCacheContext, /) -> Sequence[ChannelVoiceStateContainer]:
        """Sequence[:class:`.ChannelVoiceStateContainer`]: Retrieves all available channel voice state containers as sequence.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        return list(self.get_channel_voice_states_mapping(ctx).values())

    @abstractmethod
    def get_channel_voice_states_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, ChannelVoiceStateContainer]:
        """Mapping[:class:`str`, :class:`.ChannelVoiceStateContainer`]: Retrieves all available channel voice state containers as mapping of channel IDs.

        Parameters
        ----------
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def store_channel_voice_state(self, container: ChannelVoiceStateContainer, ctx: BaseCacheContext, /) -> None:
        """Stores a channel voice state container.

        Parameters
        ----------
        container: :class:`.ChannelVoiceStateContainer`
            The container to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def bulk_store_channel_voice_states(
        self, containers: dict[str, ChannelVoiceStateContainer], ctx: BaseCacheContext, /
    ) -> None:
        """Stores channel voice state containers in bulk.

        Parameters
        ----------
        containers: Dict[:class:`str`, :class:`.ChannelVoiceStateContainer`]
            The containers to store.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...

    @abstractmethod
    def delete_channel_voice_state(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        """Deletes a channel voice state container by channel ID.

        Parameters
        ----------
        channel_id: :class:`str`
            The channel's ID.
        ctx: :class:`.BaseCacheContext`
            The context.
        """
        ...


class EmptyCache(Cache):
    """Implementation of cache which doesn't actually store anything."""

    __slots__ = ()

    ############
    # Channels #
    ############

    def get_channel(self, channel_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Channel]:
        return None

    def get_channels_mapping(self, ctx: BaseCacheContext, /) -> dict[str, Channel]:
        return {}

    def store_channel(self, channel: Channel, ctx: BaseCacheContext, /) -> None:
        pass

    def delete_channel(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        pass

    def get_private_channels_mapping(
        self, ctx: BaseCacheContext, /
    ) -> dict[str, typing.Union[DMChannel, GroupChannel]]:
        return {}

    ####################
    # Channel Messages #
    ####################
    def get_message(self, channel_id: str, message_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Message]:
        return None

    def get_messages_mapping_of(
        self, channel_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[Mapping[str, Message]]:
        return None

    def store_message(self, message: Message, ctx: BaseCacheContext, /) -> None:
        pass

    def delete_message(self, channel_id: str, message_id: str, ctx: BaseCacheContext, /) -> None:
        pass

    def delete_messages_of(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        pass

    ###############
    # Read States #
    ###############
    def get_read_state(self, channel_id: str, ctx: BaseCacheContext, /) -> typing.Optional[ReadState]:
        return None

    def get_read_states_mapping(self, ctx: BaseCacheContext, /) -> dict[str, ReadState]:
        return {}

    def store_read_state(self, read_state: ReadState, ctx: BaseCacheContext, /) -> None:
        pass

    def delete_read_state(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        pass

    ##########
    # Emojis #
    ##########

    def get_emoji(self, emoji_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Emoji]:
        return None

    def get_emojis_mapping(self, ctx: BaseCacheContext, /) -> dict[str, Emoji]:
        return {}

    def get_server_emojis_mapping(
        self,
    ) -> dict[str, dict[str, ServerEmoji]]:
        return {}

    def get_server_emojis_mapping_of(
        self, server_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[dict[str, ServerEmoji]]:
        return None

    def delete_server_emojis_of(self, server_id: str, ctx: BaseCacheContext, /) -> None:
        pass

    def store_emoji(self, emoji: Emoji, ctx: BaseCacheContext, /) -> None:
        pass

    def delete_emoji(self, emoji_id: str, server_id: typing.Optional[str], ctx: BaseCacheContext, /) -> None:
        pass

    ###########
    # Servers #
    ###########

    def get_server(self, server_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Server]:
        return None

    def get_servers_mapping(self, ctx: BaseCacheContext, /) -> dict[str, Server]:
        return {}

    def store_server(self, server: Server, ctx: BaseCacheContext, /) -> None:
        pass

    def delete_server(self, server_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Server]:
        pass

    ##################
    # Server Members #
    ##################
    def get_server_member(self, server_id: str, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Member]:
        return None

    def get_server_members_mapping_of(
        self, server_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[dict[str, Member]]:
        return None

    def bulk_store_server_members(
        self,
        server_id: str,
        members: dict[str, Member],
        ctx: BaseCacheContext,
        /,
    ) -> None:
        pass

    def overwrite_server_members(
        self,
        server_id: str,
        members: dict[str, Member],
        ctx: BaseCacheContext,
        /,
    ) -> None:
        pass

    def store_server_member(self, member: Member, ctx: BaseCacheContext, /) -> None:
        pass

    def delete_server_member(self, server_id: str, user_id: str, ctx: BaseCacheContext, /) -> None:
        pass

    def delete_server_members_of(self, server_id: str, ctx: BaseCacheContext, /) -> None:
        pass

    def get_servers_member_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, Mapping[str, Member]]:
        return {}

    #########
    # Users #
    #########

    def get_user(self, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[User]:
        return None

    def get_users_mapping(self, ctx: BaseCacheContext, /) -> dict[str, User]:
        return {}

    def store_user(self, user: User, ctx: BaseCacheContext, /) -> None:
        return None

    def delete_user(self, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[User]:
        return None

    def bulk_store_users(self, users: dict[str, User], ctx: BaseCacheContext, /) -> None:
        pass

    ############################
    # Private Channels by User #
    ############################
    def get_private_channel_by_user(self, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[str]:
        return None

    def get_private_channels_by_users_mapping(self, ctx: BaseCacheContext, /) -> dict[str, str]:
        return {}

    def store_private_channel_by_user(self, channel: DMChannel, ctx: BaseCacheContext, /) -> None:
        pass

    def delete_private_channel_by_user(self, user_id: str, ctx: BaseCacheContext, /) -> None:
        pass

    ########################
    # Channel Voice States #
    ########################
    def get_channel_voice_state(
        self, channel_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[ChannelVoiceStateContainer]:
        return None

    def get_channel_voice_states_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, ChannelVoiceStateContainer]:
        return {}

    def store_channel_voice_state(self, container: ChannelVoiceStateContainer, ctx: BaseCacheContext, /) -> None:
        pass

    def bulk_store_channel_voice_states(
        self, containers: dict[str, ChannelVoiceStateContainer], ctx: BaseCacheContext, /
    ) -> None:
        pass

    def delete_channel_voice_state(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        pass


V = typing.TypeVar('V')


def _put0(d: dict[str, V], k: str, max_size: int, required_keys: int = 1, /) -> bool:  # noqa: ARG001
    if max_size == 0:
        return False
    map_size = len(d)
    if map_size != 0 and max_size > 0 and len(d) >= max_size:
        keys = []
        i = 0
        for key in d.keys():
            keys.append(key)
            if i >= required_keys:
                break
            i += 1
        for key in keys:
            del d[key]
    return True


def _put1(d: dict[str, V], k: str, v: V, max_size: int, /) -> None:
    if _put0(d, k, max_size):
        d[k] = v


class MapCache(Cache):
    """Implementation of :class:`.Cache` ABC based on :class:`dict`'s.

    Parameters of this class accept negative value to represent infinite count.

    Parameters
    ----------
    channels_max_size: :class:`int`
        How many channels can have cache. Defaults to ``-1``.
    emojis_max_size: :class:`int`
        How many emojis can have cache. Defaults to ``-1``.
    messages_max_size: :class:`int`
        How many messages can have cache per channel. Defaults to ``1000``.
    private_channels_by_user_max_size: :class:`int`
        How many DM channels by user can have cache. Defaults to ``-1``.
    private_channels_max_size: :class:`int`
        How many private channels can have cache. Defaults to ``-1``.
    read_states_max_size: :class:`int`
        How many read states can have cache. Defaults to ``-1``.
    server_emojis_max_size: :class:`int`
        How many server emojis can have cache. Defaults to ``-1``.
    server_members_max_size: :class:`int`
        How many server members can have cache. Defaults to ``-1``.
    servers_max_size: :class:`int`
        How many servers can have cache. Defaults to ``-1``.
    users_max_size: :class:`int`
        How many users can have cache. Defaults to ``-1``.
    channel_voice_states_max_size: :class:`int`
        How many channel voice state containers can have cache. Defaults to ``-1``.
    """

    __slots__ = (
        '_channels',
        '_channels_max_size',
        '_channel_voice_states',
        '_channel_voice_states_max_size',
        '_emojis',
        '_emojis_max_size',
        '_private_channels',
        '_private_channels_by_user',
        '_private_channels_by_user_max_size',
        '_private_channels_max_size',
        '_messages',
        '_messages_max_size',
        '_read_states',
        '_read_states_max_size',
        '_servers',
        '_servers_max_size',
        '_server_emojis',
        '_server_emojis_max_size',
        '_server_members',
        '_server_members_max_size',
        '_users',
        '_users_max_size',
    )

    def __init__(
        self,
        *,
        channels_max_size: int = -1,
        emojis_max_size: int = -1,
        messages_max_size: int = 1000,
        private_channels_by_user_max_size: int = -1,
        private_channels_max_size: int = -1,
        read_states_max_size: int = -1,
        server_emojis_max_size: int = -1,
        server_members_max_size: int = -1,
        servers_max_size: int = -1,
        users_max_size: int = -1,
        channel_voice_states_max_size: int = -1,
    ) -> None:
        self._channels: dict[str, Channel] = {}
        self._channels_max_size: int = channels_max_size
        self._emojis: dict[str, Emoji] = {}
        self._emojis_max_size: int = emojis_max_size
        self._private_channels: dict[str, typing.Union[DMChannel, GroupChannel]] = {}
        self._private_channels_by_user: dict[str, str] = {}
        self._private_channels_by_user_max_size: int = private_channels_by_user_max_size
        self._private_channels_max_size: int = private_channels_max_size
        self._messages: dict[str, dict[str, Message]] = {}
        self._messages_max_size = messages_max_size
        self._read_states: dict[str, ReadState] = {}
        self._read_states_max_size: int = read_states_max_size
        self._servers: dict[str, Server] = {}
        self._servers_max_size: int = servers_max_size
        self._server_emojis: dict[str, dict[str, ServerEmoji]] = {}
        self._server_emojis_max_size: int = server_emojis_max_size
        self._server_members: dict[str, dict[str, Member]] = {}
        self._server_members_max_size: int = server_members_max_size
        self._users: dict[str, User] = {}
        self._users_max_size: int = users_max_size
        self._channel_voice_states: dict[str, ChannelVoiceStateContainer] = {}
        self._channel_voice_states_max_size: int = channel_voice_states_max_size

    ############
    # Channels #
    ############
    def get_channel(self, channel_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Channel]:
        return self._channels.get(channel_id)

    def get_channels_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, Channel]:
        return self._channels

    def store_channel(self, channel: Channel, ctx: BaseCacheContext, /) -> None:
        _put1(self._channels, channel.id, channel, self._channels_max_size)

        from .channel import DMChannel, GroupChannel

        if isinstance(channel, (DMChannel, GroupChannel)):
            _put1(self._private_channels, channel.id, channel, self._private_channels_max_size)

    def delete_channel(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        self._channels.pop(channel_id, None)

    def get_private_channels_mapping(
        self, ctx: BaseCacheContext, /
    ) -> Mapping[str, typing.Union[DMChannel, GroupChannel]]:
        return self._private_channels

    ####################
    # Channel Messages #
    ####################
    def get_message(self, channel_id: str, message_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Message]:
        messages = self._messages.get(channel_id)
        if messages:
            return messages.get(message_id)
        return None

    def get_messages_mapping_of(
        self, channel_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[Mapping[str, Message]]:
        return self._messages.get(channel_id)

    def store_message(self, message: Message, ctx: BaseCacheContext, /) -> None:
        from .server import Member
        from .user import User

        author = message._author
        if isinstance(author, Member):
            self.store_server_member(author, ctx)
            message._author = author.id
        elif isinstance(author, User):
            self.store_user(author, ctx)
            message._author = author.id

        d = self._messages.get(message.channel_id)
        if d is None:
            if self._messages_max_size == 0:
                return
            self._messages[message.channel_id] = {message.id: message}
        else:
            _put1(d, message.id, message, self._messages_max_size)

    def delete_message(self, channel_id: str, message_id: str, ctx: BaseCacheContext, /) -> None:
        messages = self._messages.get(channel_id)
        if messages:
            messages.pop(message_id, None)

    def delete_messages_of(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        self._messages.pop(channel_id, None)

    ###############
    # Read States #
    ###############
    def get_read_state(self, channel_id: str, ctx: BaseCacheContext, /) -> typing.Optional[ReadState]:
        return self._read_states.get(channel_id)

    def get_read_states_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, ReadState]:
        return self._read_states

    def store_read_state(self, read_state: ReadState, ctx: BaseCacheContext, /) -> None:
        _put1(
            self._read_states,
            read_state.channel_id,
            read_state,
            self._read_states_max_size,
        )

    def delete_read_state(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        self._read_states.pop(channel_id, None)

    ##########
    # Emojis #
    ##########

    def get_emoji(self, emoji_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Emoji]:
        return self._emojis.get(emoji_id)

    def get_emojis_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, Emoji]:
        return self._emojis

    def get_server_emojis_mapping(
        self,
    ) -> Mapping[str, Mapping[str, ServerEmoji]]:
        return self._server_emojis

    def get_server_emojis_mapping_of(
        self, server_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[Mapping[str, ServerEmoji]]:
        return self._server_emojis.get(server_id)

    def delete_server_emojis_of(self, server_id: str, ctx: BaseCacheContext, /) -> None:
        self._server_emojis.pop(server_id, None)

    def store_emoji(self, emoji: Emoji, ctx: BaseCacheContext, /) -> None:
        from .emoji import ServerEmoji

        if isinstance(emoji, ServerEmoji):
            server_id = emoji.server_id
            if _put0(self._server_emojis, server_id, self._server_emojis_max_size):
                se = self._server_emojis
                s = se.get(server_id)
                if s is not None:
                    s[emoji.id] = emoji
                else:
                    se[server_id] = {emoji.id: emoji}
        _put1(self._emojis, emoji.id, emoji, self._emojis_max_size)

    def delete_emoji(self, emoji_id: str, server_id: typing.Optional[str], ctx: BaseCacheContext, /) -> None:
        from .emoji import ServerEmoji

        emoji = self._emojis.pop(emoji_id, None)

        server_ids: tuple[str, ...] = ()
        if isinstance(emoji, ServerEmoji):
            if server_id:
                server_ids = (server_id, emoji.server_id)
            else:
                server_ids = (emoji.server_id,)

        for server_id in server_ids:
            server_emojis = self._server_emojis.get(server_id, {})
            server_emojis.pop(emoji_id, None)

    ###########
    # Servers #
    ###########

    def get_server(self, server_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Server]:
        return self._servers.get(server_id)

    def get_servers_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, Server]:
        return self._servers

    def store_server(self, server: Server, ctx: BaseCacheContext, /) -> None:
        if server.id not in self._server_emojis:
            _put1(self._server_emojis, server.id, {}, self._server_emojis_max_size)

        if (
            _put0(self._server_members, server.id, self._server_members_max_size)
            and server.id not in self._server_members
        ):
            self._server_members[server.id] = {}
        _put1(self._servers, server.id, server, self._servers_max_size)

    def delete_server(self, server_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Server]:
        return self._servers.pop(server_id, None)

    ##################
    # Server Members #
    ##################
    def get_server_member(self, server_id: str, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[Member]:
        d = self._server_members.get(server_id)
        if d is None:
            return None
        return d.get(user_id)

    def get_server_members_mapping_of(
        self, server_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[Mapping[str, Member]]:
        return self._server_members.get(server_id)

    def bulk_store_server_members(
        self,
        server_id: str,
        members: dict[str, Member],
        ctx: BaseCacheContext,
        /,
    ) -> None:
        d = self._server_members.get(server_id)
        if d is None:
            self._server_members[server_id] = members
        else:
            d.update(members)

    def overwrite_server_members(
        self,
        server_id: str,
        members: dict[str, Member],
        ctx: BaseCacheContext,
        /,
    ) -> None:
        self._server_members[server_id] = members

    def store_server_member(self, member: Member, ctx: BaseCacheContext, /) -> None:
        from .user import User

        if isinstance(member._user, User):
            self.store_user(member._user, ctx)
            member._user = member._user.id
        d = self._server_members.get(member.server_id)
        if d is None:
            if self._server_members_max_size == 0:
                return
            self._server_members[member.server_id] = {member.id: member}
        else:
            _put1(d, member.id, member, self._server_members_max_size)

    def delete_server_member(self, server_id: str, user_id: str, ctx: BaseCacheContext, /) -> None:
        members = self._server_members.get(server_id)
        if members:
            members.pop(user_id, None)

    def delete_server_members_of(self, server_id: str, ctx: BaseCacheContext, /) -> None:
        self._server_members.pop(server_id, None)

    def get_servers_member_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, Mapping[str, Member]]:
        return self._server_members

    #########
    # Users #
    #########

    def get_user(self, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[User]:
        return self._users.get(user_id)

    def get_users_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, User]:
        return self._users

    def store_user(self, user: User, ctx: BaseCacheContext, /) -> None:
        _put1(self._users, user.id, user, self._users_max_size)

    def delete_user(self, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[User]:
        return self._users.pop(user_id, None)

    def bulk_store_users(self, users: Mapping[str, User], ctx: BaseCacheContext, /) -> None:
        self._users.update(users)

    ############################
    # Private Channels by User #
    ############################
    def get_private_channel_by_user(self, user_id: str, ctx: BaseCacheContext, /) -> typing.Optional[str]:
        return self._private_channels_by_user.get(user_id)

    def get_private_channels_by_users_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, str]:
        return self._private_channels_by_user

    def store_private_channel_by_user(self, channel: DMChannel, ctx: BaseCacheContext, /) -> None:
        _put1(self._private_channels_by_user, channel.recipient_id, channel.id, self._private_channels_by_user_max_size)

    def delete_private_channel_by_user(self, user_id: str, ctx: BaseCacheContext, /) -> None:
        self._private_channels_by_user.pop(user_id, None)

    ########################
    # Channel Voice States #
    ########################
    def get_channel_voice_state(
        self, channel_id: str, ctx: BaseCacheContext, /
    ) -> typing.Optional[ChannelVoiceStateContainer]:
        return self._channel_voice_states.get(channel_id)

    def get_channel_voice_states_mapping(self, ctx: BaseCacheContext, /) -> Mapping[str, ChannelVoiceStateContainer]:
        return self._channel_voice_states

    def store_channel_voice_state(self, container: ChannelVoiceStateContainer, ctx: BaseCacheContext, /) -> None:
        _put1(self._channel_voice_states, container.channel_id, container, self._channel_voice_states_max_size)

    def bulk_store_channel_voice_states(
        self, containers: dict[str, ChannelVoiceStateContainer], ctx: BaseCacheContext, /
    ) -> None:
        self._channel_voice_states.update(containers)

    def delete_channel_voice_state(self, channel_id: str, ctx: BaseCacheContext, /) -> None:
        self._channel_voice_states.pop(channel_id, None)


# re-export internal functions as well for future usage
__all__ = (
    'CacheContextType',
    'BaseCacheContext',
    'UndefinedCacheContext',
    'PrivateChannelCreateEventCacheContext',
    'ServerChannelCreateEventCacheContext',
    'ChannelUpdateEventCacheContext',
    'ChannelDeleteEventCacheContext',
    'GroupRecipientAddEventCacheContext',
    'GroupRecipientRemoveEventCacheContext',
    'ChannelStartTypingEventCacheContext',
    'ChannelStopTypingEventCacheContext',
    'MessageAckEventCacheContext',
    'MessageCreateEventCacheContext',
    'MessageUpdateEventCacheContext',
    'MessageAppendEventCacheContext',
    'MessageDeleteEventCacheContext',
    'MessageReactEventCacheContext',
    'MessageUnreactEventCacheContext',
    'MessageClearReactionEventCacheContext',
    'MessageDeleteBulkEventCacheContext',
    'ServerCreateEventCacheContext',
    'ServerEmojiCreateEventCacheContext',
    'ServerEmojiDeleteEventCacheContext',
    'ServerUpdateEventCacheContext',
    'ServerDeleteEventCacheContext',
    'ServerMemberJoinEventCacheContext',
    'ServerMemberUpdateEventCacheContext',
    'ServerMemberRemoveEventCacheContext',
    'RawServerRoleUpdateEventCacheContext',
    'ServerRoleDeleteEventCacheContext',
    'ReportCreateEventCacheContext',
    'UserUpdateEventCacheContext',
    'UserRelationshipUpdateEventCacheContext',
    'UserSettingsUpdateEventCacheContext',
    'UserPlatformWipeEventCacheContext',
    'WebhookCreateEventCacheContext',
    'WebhookUpdateEventCacheContext',
    'WebhookDeleteEventCacheContext',
    'SessionCreateEventCacheContext',
    'SessionDeleteEventCacheContext',
    'SessionDeleteAllEventCacheContext',
    'VoiceChannelJoinEventCacheContext',
    'VoiceChannelLeaveEventCacheContext',
    'VoiceChannelMoveEventCacheContext',
    'UserVoiceStateUpdateEventCacheContext',
    'AuthenticatedEventCacheContext',
    'EntityCacheContext',
    'MessageableCacheContext',
    'BotCacheContext',
    'DMChannelCacheContext',
    'GroupChannelCacheContext',
    'BaseEmojiCacheContext',
    'ServerEmojiCacheContext',
    'ClientCacheContext',
    'ServerPublicInviteCacheContext',
    'GroupPublicInviteCacheContext',
    'PrivateBaseInviteCacheContext',
    'GroupInviteCacheContext',
    'ServerInviteCacheContext',
    'BaseMessageCacheContext',
    'MessageCacheContext',
    'ReadStateCacheContext',
    'BaseRoleCacheContext',
    'BaseServerChannelCacheContext',
    'BaseMemberCacheContext',
    'ServerCacheContext',
    'BaseUserCacheContext',
    'UserCacheContext',
    'WebhookCacheContext',
    'MessageThroughMessageableGetterCacheContext',
    'MessagesThroughMessageableGetterCacheContext',
    # 'MessageableMessagesGetterCacheContext',
    'UserThroughBotOwnerCacheContext',
    'UserThroughDMChannelInitiatorCacheContext',
    'MessageThroughDMChannelLastMessageCacheContext',
    'ReadStateThroughDMChannelReadStateCacheContext',
    'UserThroughDMChannelRecipientCacheContext',
    'UserThroughDMChannelRecipientsCacheContext',
    'MessageThroughGroupChannelLastMessageCacheContext',
    'ReadStateThroughGroupChannelReadStateCacheContext',
    'UserThroughGroupChannelOwnerCacheContext',
    'UserThroughGroupChannelRecipientsCacheContext',
    'ServerThroughServerChannelCacheContext',
    'MessageThroughTextChannelLastMessageCacheContext',
    'UserThroughUserAddedSystemEventUserCacheContext',
    'UserThroughUserAddedSystemEventAuthorCacheContext',
    'UserThroughUserRemovedSystemEventUserCacheContext',
    'UserThroughUserRemovedSystemEventAuthorCacheContext',
    'MemberOrUserThroughUserJoinedSystemEventUserCacheContext',
    'MemberOrUserThroughUserLeftSystemEventUserCacheContext',
    'MemberOrUserThroughUserKickedSystemEventUserCacheContext',
    'MemberOrUserThroughUserBannedSystemEventUserCacheContext',
    'UserThroughChannelRenamedSystemEventAuthorCacheContext',
    'UserThroughChannelDescriptionChangedSystemEventAuthorCacheContext',
    'UserThroughChannelIconChangedSystemEventAuthorCacheContext',
    'UserThroughChannelOwnershipChangedSystemEventFromCacheContext',
    'UserThroughChannelOwnershipChangedSystemEventToCacheContext',
    'MessageThroughMessagePinnedSystemEventPinnedMessageCacheContext',
    'MemberOrUserThroughMessagePinnedSystemEventAuthorCacheContext',
    'MessageThroughMessageUnpinnedSystemEventUnpinnedMessageCacheContext',
    'MemberOrUserThroughMessageUnpinnedSystemEventAuthorCacheContext',
    'UserThroughCallStartedSystemEventAuthorCacheContext',
    'ChannelThroughMessageChannelCacheContext',
    'ServerThroughMessageServerCacheContext',
    'MemberOrUserThroughMessageAuthorCacheContext',
    'ReadStateThroughTextChannelReadStateCacheContext',
    'ServerThroughRoleServerCacheContext',
    'ChannelVoiceStateContainerThroughTextChannelVoiceStatesCacheContext',
    'ChannelVoiceStateContainerThroughVoiceChannelVoiceStatesCacheContext',
    'UserThroughBaseEmojiCreatorCacheContext',
    'ServerThroughServerEmojiServerCacheContext',
    'ServerThroughServerPublicInviteServerCacheContext',
    'ChannelThroughServerPublicInviteChannelCacheContext',
    'UserThroughServerPublicInviteUserCacheContext',
    'ChannelThroughGroupPublicInviteChannelCacheContext',
    'UserThroughGroupPublicInviteUserCacheContext',
    'UserThroughPrivateBaseInviteCreatorCacheContext',
    'ChannelThroughGroupInviteChannelCacheContext',
    'ServerThroughServerInviteServerCacheContext',
    'ChannelThroughServerInviteChannelCacheContext',
    'ChannelThroughReadStateChannelCacheContext',
    'EmojiThroughServerGetterCacheContext',
    'MemberThroughServerGetterCacheContext',
    'EmojisThroughServerGetterCacheContext',
    'MembersThroughServerGetterCacheContext',
    'ChannelThroughServerGetterCacheContext',
    'ChannelsThroughServerGetterCacheContext',
    'UserThroughBaseMemberGetterCacheContext',
    'UserThroughUserBotOwnerCacheContext',
    'ChannelIDThroughUserDMChannelIDCacheContext',
    'ChannelThroughUserDMChannelIDCacheContext',
    'UserThroughWebhookCreatorCacheContext',
    'ChannelThroughWebhookChannelCacheContext',
    '_UNDEFINED',
    '_USER_REQUEST',
    '_READY_EVENT',
    '_PRIVATE_CHANNEL_CREATE_EVENT',
    '_SERVER_CHANNEL_CREATE_EVENT',
    '_CHANNEL_UPDATE_EVENT',
    '_CHANNEL_DELETE_EVENT',
    '_GROUP_RECIPIENT_ADD_EVENT',
    '_GROUP_RECIPIENT_REMOVE_EVENT',
    '_CHANNEL_START_TYPING_EVENT',
    '_CHANNEL_STOP_TYPING_EVENT',
    '_MESSAGE_ACK_EVENT',
    '_MESSAGE_CREATE_EVENT',
    '_MESSAGE_UPDATE_EVENT',
    '_MESSAGE_APPEND_EVENT',
    '_MESSAGE_DELETE_EVENT',
    '_MESSAGE_REACT_EVENT',
    '_MESSAGE_UNREACT_EVENT',
    '_MESSAGE_CLEAR_REACTION_EVENT',
    '_MESSAGE_DELETE_BULK_EVENT',
    '_SERVER_CREATE_EVENT',
    '_SERVER_EMOJI_CREATE_EVENT',
    '_SERVER_EMOJI_DELETE_EVENT',
    '_SERVER_UPDATE_EVENT',
    '_SERVER_DELETE_EVENT',
    '_SERVER_MEMBER_JOIN_EVENT',
    '_SERVER_MEMBER_UPDATE_EVENT',
    '_SERVER_MEMBER_REMOVE_EVENT',
    '_RAW_SERVER_ROLE_UPDATE_EVENT',
    '_SERVER_ROLE_DELETE_EVENT',
    '_REPORT_CREATE_EVENT',
    '_USER_UPDATE_EVENT',
    '_USER_RELATIONSHIP_UPDATE_EVENT',
    '_USER_SETTINGS_UPDATE_EVENT',
    '_USER_PLATFORM_WIPE_EVENT',
    '_WEBHOOK_CREATE_EVENT',
    '_WEBHOOK_UPDATE_EVENT',
    '_WEBHOOK_DELETE_EVENT',
    '_SESSION_CREATE_EVENT',
    '_SESSION_DELETE_EVENT',
    '_SESSION_DELETE_ALL_EVENT',
    '_VOICE_CHANNEL_JOIN_EVENT',
    '_VOICE_CHANNEL_LEAVE_EVENT',
    '_VOICE_CHANNEL_MOVE_EVENT',
    '_USER_VOICE_STATE_UPDATE_EVENT',
    '_AUTHENTICATED_EVENT',
    '_MESSAGE_THROUGH_MESSAGEABLE_GETTER',
    '_MESSAGES_THROUGH_MESSAGEABLE_GETTER',
    '_USER_THROUGH_BOT_OWNER',
    '_USER_THROUGH_DM_CHANNEL_INITIATOR',
    '_MESSAGE_THROUGH_DM_CHANNEL_LAST_MESSAGE',
    '_READ_STATE_THROUGH_DM_CHANNEL_READ_STATE',
    '_SERVER_THROUGH_ROLE_SERVER',
    '_USER_THROUGH_DM_CHANNEL_RECIPIENT',
    '_USER_THROUGH_DM_CHANNEL_RECIPIENTS',
    '_MESSAGE_THROUGH_GROUP_CHANNEL_LAST_MESSAGE',
    '_USER_THROUGH_GROUP_CHANNEL_OWNER',
    '_READ_STATE_THROUGH_GROUP_CHANNEL_READ_STATE',
    '_USER_THROUGH_GROUP_CHANNEL_RECIPIENTS',
    '_SERVER_THROUGH_SERVER_CHANNEL',
    '_MESSAGE_THROUGH_TEXT_CHANNEL_LAST_MESSAGE',
    '_READ_STATE_THROUGH_TEXT_CHANNEL_READ_STATE',
    '_CHANNEL_VOICE_STATE_CONTAINER_THROUGH_TEXT_CHANNEL_VOICE_STATES',
    '_CHANNEL_VOICE_STATE_CONTAINER_THROUGH_VOICE_CHANNEL_VOICE_STATES',
    '_CHANNELS_THROUGH_CLIENT_GETTER',
    '_EMOJIS_THROUGH_CLIENT_GETTER',
    '_SERVERS_THROUGH_CLIENT_GETTER',
    '_USERS_THROUGH_CLIENT_GETTER',
    '_USER_IDS_THROUGH_CLIENT_DM_CHANNELS',
    '_CHANNELS_THROUGH_CLIENT_DM_CHANNELS',
    '_CHANNELS_THROUGH_CLIENT_PRIVATE_CHANNELS',
    '_CHANNEL_THROUGH_CLIENT_GETTER',
    '_EMOJI_THROUGH_CLIENT_GETTER',
    '_READ_STATE_THROUGH_CLIENT_GETTER',
    '_SERVER_THROUGH_CLIENT_GETTER',
    '_USER_THROUGH_CLIENT_GETTER',
    '_USER_THROUGH_BASE_EMOJI_CREATOR',
    '_SERVER_THROUGH_SERVER_EMOJI_SERVER',
    '_SERVER_THROUGH_SERVER_PUBLIC_INVITE_SERVER',
    '_CHANNEL_THROUGH_SERVER_PUBLIC_INVITE_CHANNEL',
    '_USER_THROUGH_SERVER_PUBLIC_INVITE_USER',
    '_CHANNEL_THROUGH_GROUP_PUBLIC_INVITE_CHANNEL',
    '_USER_THROUGH_GROUP_PUBLIC_INVITE_USER',
    '_USER_THROUGH_PRIVATE_BASE_INVITE_CREATOR',
    '_CHANNEL_THROUGH_GROUP_INVITE_CHANNEL',
    '_SERVER_THROUGH_SERVER_INVITE_SERVER',
    '_CHANNEL_THROUGH_SERVER_INVITE_CHANNEL',
    '_USER_THROUGH_USER_ADDED_SYSTEM_EVENT_USER',
    '_USER_THROUGH_USER_ADDED_SYSTEM_EVENT_BY',
    '_USER_THROUGH_USER_REMOVED_SYSTEM_EVENT_USER',
    '_USER_THROUGH_USER_REMOVED_SYSTEM_EVENT_BY',
    '_MEMBER_OR_USER_THROUGH_USER_JOINED_SYSTEM_EVENT_USER',
    '_MEMBER_OR_USER_THROUGH_USER_LEFT_SYSTEM_EVENT_USER',
    '_MEMBER_OR_USER_THROUGH_USER_KICKED_SYSTEM_EVENT_USER',
    '_MEMBER_OR_USER_THROUGH_USER_BANNED_SYSTEM_EVENT_USER',
    '_USER_THROUGH_CHANNEL_RENAMED_SYSTEM_EVENT_BY',
    '_USER_THROUGH_CHANNEL_DESCRIPTION_CHANGED_SYSTEM_EVENT_BY',
    '_USER_THROUGH_CHANNEL_ICON_CHANGED_SYSTEM_EVENT_BY',
    '_USER_THROUGH_CHANNEL_OWNERSHIP_CHANGED_SYSTEM_EVENT_FROM',
    '_USER_THROUGH_CHANNEL_OWNERSHIP_CHANGED_SYSTEM_EVENT_TO',
    '_MESSAGE_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_PINNED_MESSAGE',
    '_MEMBER_OR_USER_THROUGH_MESSAGE_PINNED_SYSTEM_EVENT_BY',
    '_MESSAGE_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_UNPINNED_MESSAGE',
    '_MEMBER_OR_USER_THROUGH_MESSAGE_UNPINNED_SYSTEM_EVENT_BY',
    '_USER_THROUGH_CALL_STARTED_SYSTEM_EVENT_BY',
    '_CHANNEL_THROUGH_MESSAGE_CHANNEL',
    '_SERVER_THROUGH_MESSAGE_SERVER',
    '_MEMBER_OR_USER_THROUGH_MESSAGE_AUTHOR',
    '_CHANNEL_THROUGH_READ_STATE_CHANNEL',
    '_EMOJI_THROUGH_SERVER_GETTER',
    '_MEMBER_THROUGH_SERVER_GETTER',
    '_EMOJIS_THROUGH_SERVER_GETTER',
    '_MEMBERS_THROUGH_SERVER_GETTER',
    '_CHANNEL_THROUGH_SERVER_GETTER',
    '_CHANNELS_THROUGH_SERVER_GETTER',
    '_MEMBER_THROUGH_SERVER_OWNER',
    '_USER_THROUGH_USER_BOT_OWNER',
    '_CHANNEL_THROUGH_USER_DM_CHANNEL',
    '_CHANNEL_ID_THROUGH_USER_DM_CHANNEL_ID',
    '_USER_THROUGH_MEMBER_GETTER',
    '_USER_THROUGH_WEBHOOK_CREATOR',
    '_CHANNEL_THROUGH_WEBHOOK_CHANNEL',
    'ProvideCacheContextIn',
    'Cache',
    'EmptyCache',
    '_put0',
    '_put1',
    'MapCache',
)
