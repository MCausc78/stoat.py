.. currentmodule:: pyvolt

Cache
=====

The following section documents everything related to cache.

Abstract Base Classes
---------------------

Cache
~~~~~

.. attributetable:: Cache

.. autoclass:: Cache
    :members:

Implementations
---------------

EmptyCache
~~~~~~~~~~

.. attributetable:: EmptyCache

.. autoclass:: EmptyCache
    :show-inheritance:
    :inherited-members:

MapCache
~~~~~~~~

.. attributetable:: MapCache

.. autoclass:: MapCache
    :show-inheritance:
    :inherited-members:

CacheContextType
~~~~~~~~~~~~~~~~

.. class:: CacheContextType

    Specifies a type of cache context.

    .. attribute:: custom

        The context is custom.
    .. attribute:: undefined

        The context is not provided.
    .. attribute:: ready_event

        The context relates to :class:`.ReadyEvent` event.
    .. attribute:: private_channel_create_event

        The context relates to :class:`.PrivateChannelCreateEvent` event.
    .. attribute:: server_channel_create_event

        The context relates to :class:`.ServerChannelCreateEvent` event.
    .. attribute:: channel_update_event

        The context relates to :class:`.ChannelUpdateEvent` event.
    .. attribute:: channel_delete_event

        The context relates to :class:`.ChannelDeleteEvent` event.
    .. attribute:: group_recipient_add_event

        The context relates to :class:`.GroupRecipientAddEvent` event.
    .. attribute:: group_recipient_remove_event

        The context relates to :class:`.GroupRecipientRemoveEvent` event.
    .. attribute:: channel_start_typing_event

        The context relates to :class:`.ChannelStartTypingEvent` event.
    .. attribute:: channel_stop_typing_event

        The context relates to :class:`.ChannelStopTypingEvent` event.
    .. attribute:: message_ack_event

        The context relates to :class:`.MessageAckEvent` event.
    .. attribute:: message_create_event

        The context relates to :class:`.MessageCreateEvent` event.
    .. attribute:: message_update_event

        The context relates to :class:`.MessageUpdateEvent` event.
    .. attribute:: message_append_event

        The context relates to :class:`.MessageAppendEvent` event.
    .. attribute:: message_delete_event

        The context relates to :class:`.MessageDeleteEvent` event.
    .. attribute:: message_react_event

        The context relates to :class:`.MessageReactEvent` event.
    .. attribute:: message_unreact_event

        The context relates to :class:`.MessageUnreactEvent` event.
    .. attribute:: message_clear_reaction_event

        The context relates to :class:`.MessageClearReactionEvent` event.
    .. attribute:: message_delete_bulk_event

        The context relates to :class:`.MessageDeleteBulkEvent` event.
    .. attribute:: server_create_event

        The context relates to :class:`.ServerCreateEvent` event.
    .. attribute:: server_emoji_create_event

        The context relates to :class:`.ServerEmojiCreateEvent` event.
    .. attribute:: server_emoji_delete_event

        The context relates to :class:`.ServerEmojiDeleteEvent` event.
    .. attribute:: server_update_event

        The context relates to :class:`.ServerUpdateEvent` event.
    .. attribute:: server_delete_event

        The context relates to :class:`.ServerDeleteEvent` event.
    .. attribute:: server_member_join_event

        The context relates to :class:`.ServerMemberJoinEvent` event.
    .. attribute:: server_member_update_event

        The context relates to :class:`.ServerMemberUpdateEvent` event.
    .. attribute:: server_member_remove_event

        The context relates to :class:`.ServerMemberRemoveEvent` event.
    .. attribute:: raw_server_role_update_event

        The context relates to :class:`.RawServerRoleUpdateEvent` event.
    .. attribute:: server_role_delete_event

        The context relates to :class:`.ServerRoleDeleteEvent` event.
    .. attribute:: report_create_event

        The context relates to :class:`.ReportCreateEvent` event.
    .. attribute:: user_update_event

        The context relates to :class:`.UserUpdateEvent` event.
    .. attribute:: user_platform_wipe_event

        The context relates to :class:`.UserPlatformWipeEvent` event.
    .. attribute:: user_relationship_update_event

        The context relates to :class:`.UserRelationshipUpdateEvent` event.
    .. attribute:: user_settings_update_event

        The context relates to :class:`.UserSettingsUpdateEvent` event.
    .. attribute:: webhook_create_event

        The context relates to :class:`.WebhookCreateEvent` event.
    .. attribute:: webhook_update_event

        The context relates to :class:`.WebhookUpdateEvent` event.
    .. attribute:: webhook_delete_event

        The context relates to :class:`.WebhookDeleteEvent` event.
    .. attribute:: session_create_event

        The context relates to :class:`.SessionCreateEvent` event.
    .. attribute:: session_delete_event

        The context relates to :class:`.SessionDeleteEvent` event.
    .. attribute:: session_delete_all_event

        The context relates to :class:`.SessionDeleteAllEvent` event.
    .. attribute:: voice_channel_join_event

        The context relates to :class:`.VoiceChannelJoinEvent` event.
    .. attribute:: voice_channel_leave_event

        The context relates to :class:`.VoiceChannelLeaveEvent` event.
    .. attribute:: voice_channel_move_event

        The context relates to :class:`.VoiceChannelMoveEvent` event.
    .. attribute:: user_voice_state_update_event

        The context relates to :class:`.UserVoiceStateUpdateEvent` event.
    .. attribute:: authenticated_event

        The context relates to :class:`.AuthenticatedEvent` event.
    .. attribute:: message_through_messageable_getter

        The context comes from :meth:`Messageable.get_message`.
    .. attribute:: messages_through_messageable_getter

        The context comes from :attr:`Messageable.messages`.
    .. attribute:: user_through_bot_owner

        The context comes from :attr:`Bot.owner`.
    .. attribute:: user_through_dm_channel_initiator

        The context comes from :attr:`DMChannel.initiator`.
    .. attribute:: message_through_dm_channel_last_message

        The context comes from :attr:`DMChannel.last_message`.
    .. attribute:: read_state_through_dm_channel_read_state

        The context comes from :attr:`DMChannel.read_state`.
    .. attribute:: user_through_dm_channel_recipient

        The context comes from :attr:`DMChannel.recipient`.
    .. attribute:: user_through_dm_channel_recipients

        The context comes from :attr:`DMChannel.recipients`.
    .. attribute:: message_through_group_channel_last_message

        The context comes from :attr:`GroupChannel.last_message`.
    .. attribute:: user_through_group_channel_owner

        The context comes from :attr:`GroupChannel.owner`.
    .. attribute:: read_state_through_group_channel_read_state

        The context comes from :attr:`GroupChannel.read_state`.
    .. attribute:: user_through_group_channel_recipients

        The context comes from :attr:`GroupChannel.recipients`.
    .. attribute:: member_through_server_channel_me

        The context comes from :attr:`BaseServerChannel.me`.
    .. attribute:: server_through_server_channel_server

        The context comes from :attr:`BaseServerChannel.server`.
    .. attribute:: message_through_text_channel_last_message

        The context comes from :attr:`TextChannel.last_message`.
    .. attribute:: read_state_through_text_channel_read_state

        The context comes from :attr:`TextChannel.read_state`.
    .. attribute:: channel_voice_state_container_through_text_channel_voice_states

        The context comes from :attr:`TextChannel.voice_states`.
    .. attribute:: channel_voice_state_container_through_voice_channel_voice_states

        The context comes from :attr:`VoiceChannel.voice_states`.
    .. attribute:: channels_through_client_getter

        The context comes from :attr:`Client.channels`.
    .. attribute:: emojis_through_client_getter

        The context comes from :attr:`Client.emojis`.
    .. attribute:: server_members_through_client_getter
        
        The context comes from :attr:`Client.members`
    .. attribute:: read_states_through_client_getter

        The context comes from :attr:`Client.read_states`.
    .. attribute:: servers_through_client_getter

        The context comes from :attr:`Client.servers`.
    .. attribute:: users_through_client_getter

        The context comes from :attr:`Client.users`.
    .. attribute:: voice_states_through_client_getter

        The context comes from :attr:`Client.voice_states`
    .. attribute:: user_ids_through_client_dm_channel_ids

        The context comes from :attr:`Client.dm_channel_ids`.
    .. attribute:: channels_through_client_dm_channels

        The context comes from :attr:`Client.dm_channels`.
    .. attribute:: channels_through_client_private_channels

        The context comes from :attr:`Client.private_channels`.
    .. attribute:: channel_through_client_getter

        The context comes from :meth:`Client.get_channel`.
    .. attribute:: emoji_through_client_getter

        The context comes from :meth:`Client.get_emoji`.
    .. attribute:: read_state_through_client_getter

        The context comes from :meth:`Client.get_read_state`.
    .. attribute:: server_through_client_getter

        The context comes from :meth:`Client.get_server`.
    .. attribute:: user_through_client_getter

        The context comes from :meth:`Client.get_user`.
    .. attribute:: member_or_user_through_server_emoji_creator
        
        The context comes from :attr:`ServerEmoji.creator`
    .. attribute:: member_through_server_emoji_creator
        
        The context comes from :attr:`ServerEmoji.creator_as_member`
    .. attribute:: user_through_server_emoji_creator
        
        The context comes from :attr:`ServerEmoji.creator_as_user`
    .. attribute:: user_through_detached_emoji_creator
        
        The context comes from :attr:`ServeBaseEmojirEmoji.creator`
    .. attribute:: server_through_server_emoji_server

        The context comes from :attr:`ServerEmoji.server`.
    .. attribute:: server_through_server_public_invite_server

        The context comes from :attr:`ServerPublicInvite.server`.
    .. attribute:: channel_through_server_public_invite_channel

        The context comes from :attr:`ServerPublicInvite.channel`.
    .. attribute:: user_through_server_public_invite_user

        The context comes from :attr:`ServerPublicInvite.user`.
    .. attribute:: channel_through_group_public_invite_channel

        The context comes from :attr:`GroupPublicInvite.channel`.
    .. attribute:: user_through_group_public_invite_user

        The context comes from :attr:`GroupPublicInvite.user`.
    .. attribute:: channel_through_group_invite_channel

        The context comes from :attr:`GroupInvite.channel`.
    .. attribute:: user_through_group_invite_creator

        The context comes from :attr:`GroupInvite.creator`.
    .. attribute:: server_through_server_invite_server

        The context comes from :attr:`ServerInvite.server`.
    .. attribute:: channel_through_server_invite_channel

        The context comes from :attr:`ServerInvite.channel`.
    .. attribute:: member_or_user_through_server_invite_creator
    
        The context comes from :attr:`ServerInvite.creator`.
    .. attribute:: member_through_server_invite_creator
    
        The context comes from :attr:`ServerInvite.creator_as_member`.
    .. attribute:: user_through_server_invite_creator
    
        The context comes from :attr:`ServerInvite.creator_as_user`.
    .. attribute:: user_through_user_added_system_event_user

        The context comes from :attr:`UserAddedSystemEvent.user`.
    .. attribute:: user_through_user_added_system_event_by

        The context comes from :attr:`UserAddedSystemEvent.by`.
    .. attribute:: user_through_user_removed_system_event_user

        The context comes from :attr:`UserRemovedSystemEvent.user`.
    .. attribute:: user_through_user_removed_system_event_by

        The context comes from :attr:`UserRemovedSystemEvent.by`.
    .. attribute:: member_or_user_through_user_joined_system_event_user

        The context comes from :attr:`UserJoinedSystemEvent.user`.
    .. attribute:: member_through_user_joined_system_event_user

        The context comes from :attr:`UserJoinedSystemEvent.user_as_member`.
    .. attribute:: user_through_user_joined_system_event_user

        The context comes from :attr:`UserJoinedSystemEvent.user_as_user`.
    .. attribute:: member_or_user_through_user_left_system_event_user

        The context comes from :attr:`UserLeftSystemEvent.user`.
    .. attribute:: member_through_user_left_system_event_user

        The context comes from :attr:`UserLeftSystemEvent.user_as_member`.
    .. attribute:: user_through_user_left_system_event_user

        The context comes from :attr:`UserLeftSystemEvent.user_as_user`.
    .. attribute:: member_or_user_through_user_kicked_system_event_user

        The context comes from :attr:`UserKickedSystemEvent.user`.
    .. attribute:: member_through_user_kicked_system_event_user

        The context comes from :attr:`UserKickedSystemEvent.user_as_member`.
    .. attribute:: user_through_user_kicked_system_event_user

        The context comes from :attr:`UserKickedSystemEvent.user_as_user`.
    .. attribute:: member_or_user_through_user_banned_system_event_user

        The context comes from :attr:`UserBannedSystemEvent.user`.
    .. attribute:: member_through_user_banned_system_event_user

        The context comes from :attr:`UserBannedSystemEvent.user_as_member`.
    .. attribute:: user_through_user_banned_system_event_user

        The context comes from :attr:`UserBannedSystemEvent.user_as_user`.
    .. attribute:: user_through_channel_renamed_system_event_by

        The context comes from :attr:`ChannelRenamedSystemEvent.by`.
    .. attribute:: user_through_channel_description_changed_system_event_by

        The context comes from :attr:`ChannelDescriptionChangedSystemEvent.by`.
    .. attribute:: user_through_channel_icon_changed_system_event_by

        The context comes from :attr:`ChannelIconChangedSystemEvent.by`.
    .. attribute:: user_through_channel_ownership_changed_system_event_from

        The context comes from :attr:`ChannelOwnershipChangedSystemEvent.from_`.
    .. attribute:: user_through_channel_ownership_changed_system_event_to

        The context comes from :attr:`ChannelOwnershipChangedSystemEvent.to`.
    .. attribute:: message_through_message_pinned_system_event_pinned_message

        The context comes from :attr:`MessagePinnedSystemEvent.pinned_message`.
    .. attribute:: member_or_user_through_message_pinned_system_event_by

        The context comes from :attr:`MessagePinnedSystemEvent.by`.
    .. attribute:: member_through_message_pinned_system_event_by

        The context comes from :attr:`MessagePinnedSystemEvent.by_as_member`.
    .. attribute:: user_through_message_pinned_system_event_by

        The context comes from :attr:`MessagePinnedSystemEvent.by_as_user`.
    .. attribute:: message_through_message_unpinned_system_event_unpinned_message

        The context comes from :attr:`MessageUnpinnedSystemEvent.unpinned_message`.
    .. attribute:: member_or_user_through_message_unpinned_system_event_by

        The context comes from :attr:`MessageUnpinnedSystemEvent.by`.
    .. attribute:: member_through_message_unpinned_system_event_by

        The context comes from :attr:`MessageUnpinnedSystemEvent.by_as_member`.
    .. attribute:: user_through_message_unpinned_system_event_by

        The context comes from :attr:`MessageUnpinnedSystemEvent.by_as_user`.
    .. attribute:: user_through_call_started_system_event_by

        The context comes from :attr:`CallStartedSystemEvent.by`.
    .. attribute:: channel_through_message_channel

        The context comes from :attr:`Message.channel`.
    .. attribute:: server_through_message_server

        The context comes from :attr:`Message.server`.
    .. attribute:: member_or_user_through_message_author

        The context comes from :attr:`Message.author`.
    .. attribute:: member_through_message_author

        The context comes from :attr:`Message.author_as_member`.
    .. attribute:: user_through_message_author

        The context comes from :attr:`Message.author_as_user`.
    .. attribute:: member_or_users_through_message_mentions
        
        The context comes from :attr:`Message.mentions`.
    .. attribute:: members_through_message_mentions
    
        The context comes from :attr:`Message.mentions_as_members`.
    .. attribute:: users_through_message_mentions
    
        The context comes from :attr:`Message.mentions_as_users`.
    .. attribute:: role_through_message_role_mentions
    
        The context comes from :attr:`Message.role_mentions`.
    .. attribute:: channel_through_read_state_channel

        The context comes from :attr:`ReadState.channel`.
    .. attribute:: members_through_role_members
        
        The context comes from :attr:`Role.members`.
    .. attribute:: server_through_role_server

        The context comes from :attr:`Role.server`.
    .. attribute:: emoji_through_server_getter

        The context comes from :meth:`Server.get_emoji`.
    .. attribute:: member_through_server_getter

        The context comes from :meth:`Server.get_member`.
    .. attribute:: emojis_through_server_getter

        The context comes from :attr:`Server.emojis`.
    .. attribute:: members_through_server_getter

        The context comes from :attr:`Server.members`.
    .. attribute:: channel_through_server_getter

        The context comes from :meth:`Server.get_channel`.
    .. attribute:: channels_through_server_getter

        The context comes from :attr:`Server.channels`.
    .. attribute:: member_through_server_me
        
        The context comes from :attr:`Server.me`.
    .. attribute:: member_or_user_through_server_owner

        The context comes from :attr:`Server.owner`.
    .. attribute:: member_through_server_owner

        The context comes from :attr:`Server.owner_as_member`.
    .. attribute:: user_through_server_owner

        The context comes from :attr:`Server.owner_as_user`.
    .. attribute:: server_through_member_server

        The context comes from :attr:`Member.server`.
    .. attribute:: user_through_member_user

        The context comes from :attr:`Member.user`.
    .. attribute:: user_through_member_bot_owner

        The context comes from :attr:`Member.bot_owner`.
    .. attribute:: channel_id_through_member_dm_channel_id

        The context comes from :attr:`Member.dm_channel_id`.
    .. attribute:: channel_through_member_dm_channel

        The context comes from :attr:`Member.dm_channel`.
    .. attribute:: user_through_member_name

        The context comes from :attr:`Member.name`.
    .. attribute:: user_through_member_discriminator

        The context comes from :attr:`Member.discriminator`.
    .. attribute:: user_through_member_display_name

        The context comes from :attr:`Member.display_name`.
    .. attribute:: user_through_member_internal_avatar

        The context comes from :attr:`Member.internal_avatar`.
    .. attribute:: user_through_member_raw_badges

        The context comes from :attr:`Member.raw_badges`.
    .. attribute:: user_through_member_status

        The context comes from :attr:`Member.status`.
    .. attribute:: user_through_member_raw_flags

        The context comes from :attr:`Member.raw_flags`.
    .. attribute:: user_through_member_privileged

        The context comes from :attr:`Member.privileged`.
    .. attribute:: user_through_member_bot

        The context comes from :attr:`Member.bot`.
    .. attribute:: user_through_member_relationship

        The context comes from :attr:`Member.relationship`.
    .. attribute:: user_through_member_online

        The context comes from :attr:`Member.online`.
    .. attribute:: user_through_member_tag

        The context comes from :attr:`Member.tag`.
    .. attribute:: server_through_member_roles
    
        The context comes from :attr:`Member.roles`.
    .. attribute:: server_through_member_server_permissions
    
        The context comes from :attr:`Member.server_permissions`.
    .. attribute:: server_through_member_top_role
    
        The context comes from :attr:`Member.top_role`.
    .. attribute:: user_through_user_bot_owner

        The context comes from :attr:`User.bot_owner`.
    .. attribute:: channel_id_through_user_dm_channel_id

        The context comes from :attr:`User.dm_channel_id`.
    .. attribute:: channel_through_user_dm_channel

        The context comes from :attr:`User.dm_channel`.
    .. attribute:: member_or_user_through_webhook_creator

        The context comes from :attr:`Webhook.creator`.
    .. attribute:: member_through_webhook_creator

        The context comes from :attr:`Webhook.creator_as_member`.
    .. attribute:: user_through_webhook_creator

        The context comes from :attr:`Webhook.creator_as_user`.
    .. attribute:: channel_through_webhook_channel

        The context comes from :attr:`Webhook.channel`.

BaseCacheContext
~~~~~~~~~~~~~~~~

.. attributetable:: BaseCacheContext

.. autoclass:: BaseCacheContext
    :members:

UndefinedCacheContext
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UndefinedCacheContext

.. autoclass:: UndefinedCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

PrivateChannelCreateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: PrivateChannelCreateEventCacheContext

.. autoclass:: PrivateChannelCreateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerChannelCreateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerChannelCreateEventCacheContext

.. autoclass:: ServerChannelCreateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelUpdateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelUpdateEventCacheContext

.. autoclass:: ChannelUpdateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelDeleteEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelDeleteEventCacheContext

.. autoclass:: ChannelDeleteEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

GroupRecipientAddEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: GroupRecipientAddEventCacheContext

.. autoclass:: GroupRecipientAddEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

GroupRecipientRemoveEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: GroupRecipientRemoveEventCacheContext

.. autoclass:: GroupRecipientRemoveEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelStartTypingEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelStartTypingEventCacheContext

.. autoclass:: ChannelStartTypingEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelStopTypingEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelStopTypingEventCacheContext

.. autoclass:: ChannelStopTypingEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageAckEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageAckEventCacheContext

.. autoclass:: MessageAckEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageCreateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageCreateEventCacheContext

.. autoclass:: MessageCreateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageUpdateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageUpdateEventCacheContext

.. autoclass:: MessageUpdateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageAppendEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageAppendEventCacheContext

.. autoclass:: MessageAppendEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageDeleteEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageDeleteEventCacheContext

.. autoclass:: MessageDeleteEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageReactEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageReactEventCacheContext

.. autoclass:: MessageReactEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageUnreactEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageUnreactEventCacheContext

.. autoclass:: MessageUnreactEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageClearReactionEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageClearReactionEventCacheContext

.. autoclass:: MessageClearReactionEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageDeleteBulkEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageDeleteBulkEventCacheContext

.. autoclass:: MessageDeleteBulkEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerCreateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerCreateEventCacheContext

.. autoclass:: ServerCreateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerEmojiCreateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerEmojiCreateEventCacheContext

.. autoclass:: ServerEmojiCreateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerEmojiDeleteEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerEmojiDeleteEventCacheContext

.. autoclass:: ServerEmojiDeleteEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerUpdateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerUpdateEventCacheContext

.. autoclass:: ServerUpdateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerDeleteEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerDeleteEventCacheContext

.. autoclass:: ServerDeleteEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerMemberJoinEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerMemberJoinEventCacheContext

.. autoclass:: ServerMemberJoinEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerMemberUpdateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerMemberUpdateEventCacheContext

.. autoclass:: ServerMemberUpdateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerMemberRemoveEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerMemberRemoveEventCacheContext

.. autoclass:: ServerMemberRemoveEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

RawServerRoleUpdateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: RawServerRoleUpdateEventCacheContext

.. autoclass:: RawServerRoleUpdateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerRoleDeleteEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerRoleDeleteEventCacheContext

.. autoclass:: ServerRoleDeleteEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ReportCreateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ReportCreateEventCacheContext

.. autoclass:: ReportCreateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserUpdateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserUpdateEventCacheContext

.. autoclass:: UserUpdateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserRelationshipUpdateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserRelationshipUpdateEventCacheContext

.. autoclass:: UserRelationshipUpdateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserSettingsUpdateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserSettingsUpdateEventCacheContext

.. autoclass:: UserSettingsUpdateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserPlatformWipeEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserPlatformWipeEventCacheContext

.. autoclass:: UserPlatformWipeEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

WebhookCreateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: WebhookCreateEventCacheContext

.. autoclass:: WebhookCreateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

WebhookUpdateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: WebhookUpdateEventCacheContext

.. autoclass:: WebhookUpdateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

WebhookDeleteEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: WebhookDeleteEventCacheContext

.. autoclass:: WebhookDeleteEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

SessionCreateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: SessionCreateEventCacheContext

.. autoclass:: SessionCreateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

SessionDeleteEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: SessionDeleteEventCacheContext

.. autoclass:: SessionDeleteEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

SessionDeleteAllEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: SessionDeleteAllEventCacheContext

.. autoclass:: SessionDeleteAllEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

VoiceChannelJoinEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: VoiceChannelJoinEventCacheContext

.. autoclass:: VoiceChannelJoinEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

VoiceChannelLeaveEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: VoiceChannelLeaveEventCacheContext

.. autoclass:: VoiceChannelLeaveEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

VoiceChannelMoveEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: VoiceChannelMoveEventCacheContext

.. autoclass:: VoiceChannelMoveEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserVoiceStateUpdateEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserVoiceStateUpdateEventCacheContext

.. autoclass:: UserVoiceStateUpdateEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

AuthenticatedEventCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: AuthenticatedEventCacheContext

.. autoclass:: AuthenticatedEventCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

EntityCacheContext
~~~~~~~~~~~~~~~~~~

.. attributetable:: EntityCacheContext

.. autoclass:: EntityCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageableCacheContext
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageableCacheContext

.. autoclass:: MessageableCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

BotCacheContext
~~~~~~~~~~~~~~~

.. attributetable:: BotCacheContext

.. autoclass:: BotCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

DMChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: DMChannelCacheContext

.. autoclass:: DMChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

GroupChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: GroupChannelCacheContext

.. autoclass:: GroupChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

BaseEmojiCacheContext
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: BaseEmojiCacheContext

.. autoclass:: BaseEmojiCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerEmojiCacheContext
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerEmojiCacheContext

.. autoclass:: ServerEmojiCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ClientCacheContext
~~~~~~~~~~~~~~~~~~

.. attributetable:: ClientCacheContext

.. autoclass:: ClientCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerPublicInviteCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerPublicInviteCacheContext

.. autoclass:: ServerPublicInviteCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

GroupPublicInviteCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: GroupPublicInviteCacheContext

.. autoclass:: GroupPublicInviteCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

GroupInviteCacheContext
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: GroupInviteCacheContext

.. autoclass:: GroupInviteCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerInviteCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerInviteCacheContext

.. autoclass:: ServerInviteCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

BaseMessageCacheContext
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: BaseMessageCacheContext

.. autoclass:: BaseMessageCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageCacheContext
~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageCacheContext

.. autoclass:: MessageCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ReadStateCacheContext
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ReadStateCacheContext

.. autoclass:: ReadStateCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

BaseRoleCacheContext
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: BaseRoleCacheContext

.. autoclass:: BaseRoleCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

BaseServerChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: BaseServerChannelCacheContext

.. autoclass:: BaseServerChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

BaseMemberCacheContext
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: BaseMemberCacheContext

.. autoclass:: BaseMemberCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberCacheContext
~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberCacheContext

.. autoclass:: MemberCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerCacheContext
~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerCacheContext

.. autoclass:: ServerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

BaseUserCacheContext
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: BaseUserCacheContext

.. autoclass:: BaseUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserCacheContext
~~~~~~~~~~~~~~~~

.. attributetable:: UserCacheContext

.. autoclass:: UserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

WebhookCacheContext
~~~~~~~~~~~~~~~~~~~

.. attributetable:: WebhookCacheContext

.. autoclass:: WebhookCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageThroughMessageableGetterCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageThroughMessageableGetterCacheContext

.. autoclass:: MessageThroughMessageableGetterCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessagesThroughMessageableGetterCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessagesThroughMessageableGetterCacheContext

.. autoclass:: MessagesThroughMessageableGetterCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughBotOwnerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughBotOwnerCacheContext

.. autoclass:: UserThroughBotOwnerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughDMChannelInitiatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughDMChannelInitiatorCacheContext

.. autoclass:: UserThroughDMChannelInitiatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageThroughDMChannelLastMessageCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageThroughDMChannelLastMessageCacheContext

.. autoclass:: MessageThroughDMChannelLastMessageCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ReadStateThroughDMChannelReadStateCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ReadStateThroughDMChannelReadStateCacheContext

.. autoclass:: ReadStateThroughDMChannelReadStateCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughDMChannelRecipientCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughDMChannelRecipientCacheContext

.. autoclass:: UserThroughDMChannelRecipientCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughDMChannelRecipientsCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughDMChannelRecipientsCacheContext

.. autoclass:: UserThroughDMChannelRecipientsCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageThroughGroupChannelLastMessageCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageThroughGroupChannelLastMessageCacheContext

.. autoclass:: MessageThroughGroupChannelLastMessageCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ReadStateThroughGroupChannelReadStateCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ReadStateThroughGroupChannelReadStateCacheContext

.. autoclass:: ReadStateThroughGroupChannelReadStateCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughGroupChannelOwnerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughGroupChannelOwnerCacheContext

.. autoclass:: UserThroughGroupChannelOwnerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughGroupChannelRecipientsCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughGroupChannelRecipientsCacheContext

.. autoclass:: UserThroughGroupChannelRecipientsCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughServerChannelMeCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughServerChannelMeCacheContext

.. autoclass:: MemberThroughServerChannelMeCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerThroughServerChannelServerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerThroughServerChannelServerCacheContext

.. autoclass:: ServerThroughServerChannelServerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageThroughTextChannelLastMessageCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageThroughTextChannelLastMessageCacheContext

.. autoclass:: MessageThroughTextChannelLastMessageCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughUserAddedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughUserAddedSystemEventUserCacheContext

.. autoclass:: UserThroughUserAddedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughUserAddedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughUserAddedSystemEventAuthorCacheContext

.. autoclass:: UserThroughUserAddedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughUserRemovedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughUserRemovedSystemEventUserCacheContext

.. autoclass:: UserThroughUserRemovedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughUserRemovedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughUserRemovedSystemEventAuthorCacheContext

.. autoclass:: UserThroughUserRemovedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughUserJoinedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughUserJoinedSystemEventUserCacheContext

.. autoclass:: MemberOrUserThroughUserJoinedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughUserJoinedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughUserJoinedSystemEventUserCacheContext

.. autoclass:: MemberThroughUserJoinedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughUserJoinedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughUserJoinedSystemEventUserCacheContext

.. autoclass:: UserThroughUserJoinedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughUserLeftSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughUserLeftSystemEventUserCacheContext

.. autoclass:: MemberOrUserThroughUserLeftSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughUserLeftSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughUserLeftSystemEventUserCacheContext

.. autoclass:: MemberThroughUserLeftSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughUserLeftSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughUserLeftSystemEventUserCacheContext

.. autoclass:: UserThroughUserLeftSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughUserKickedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughUserKickedSystemEventUserCacheContext

.. autoclass:: MemberOrUserThroughUserKickedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughUserKickedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughUserKickedSystemEventUserCacheContext

.. autoclass:: MemberThroughUserKickedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughUserKickedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughUserKickedSystemEventUserCacheContext

.. autoclass:: UserThroughUserKickedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughUserBannedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughUserBannedSystemEventUserCacheContext

.. autoclass:: MemberOrUserThroughUserBannedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughUserBannedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughUserBannedSystemEventUserCacheContext

.. autoclass:: MemberThroughUserBannedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughUserBannedSystemEventUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughUserBannedSystemEventUserCacheContext

.. autoclass:: UserThroughUserBannedSystemEventUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughChannelRenamedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughChannelRenamedSystemEventAuthorCacheContext

.. autoclass:: UserThroughChannelRenamedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughChannelDescriptionChangedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughChannelDescriptionChangedSystemEventAuthorCacheContext

.. autoclass:: UserThroughChannelDescriptionChangedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughChannelIconChangedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughChannelIconChangedSystemEventAuthorCacheContext

.. autoclass:: UserThroughChannelIconChangedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughChannelOwnershipChangedSystemEventFromCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughChannelOwnershipChangedSystemEventFromCacheContext

.. autoclass:: UserThroughChannelOwnershipChangedSystemEventFromCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughChannelOwnershipChangedSystemEventToCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughChannelOwnershipChangedSystemEventToCacheContext

.. autoclass:: UserThroughChannelOwnershipChangedSystemEventToCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageThroughMessagePinnedSystemEventPinnedMessageCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageThroughMessagePinnedSystemEventPinnedMessageCacheContext

.. autoclass:: MessageThroughMessagePinnedSystemEventPinnedMessageCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughMessagePinnedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughMessagePinnedSystemEventAuthorCacheContext

.. autoclass:: MemberOrUserThroughMessagePinnedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughMessagePinnedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughMessagePinnedSystemEventAuthorCacheContext

.. autoclass:: MemberThroughMessagePinnedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMessagePinnedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMessagePinnedSystemEventAuthorCacheContext

.. autoclass:: UserThroughMessagePinnedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MessageThroughMessageUnpinnedSystemEventUnpinnedMessageCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageThroughMessageUnpinnedSystemEventUnpinnedMessageCacheContext

.. autoclass:: MessageThroughMessageUnpinnedSystemEventUnpinnedMessageCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughMessageUnpinnedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughMessageUnpinnedSystemEventAuthorCacheContext

.. autoclass:: MemberOrUserThroughMessageUnpinnedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughMessageUnpinnedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughMessageUnpinnedSystemEventAuthorCacheContext

.. autoclass:: MemberThroughMessageUnpinnedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMessageUnpinnedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMessageUnpinnedSystemEventAuthorCacheContext

.. autoclass:: UserThroughMessageUnpinnedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughCallStartedSystemEventAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughCallStartedSystemEventAuthorCacheContext

.. autoclass:: UserThroughCallStartedSystemEventAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelThroughMessageChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelThroughMessageChannelCacheContext

.. autoclass:: ChannelThroughMessageChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerThroughMessageServerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerThroughMessageServerCacheContext

.. autoclass:: ServerThroughMessageServerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughMessageAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughMessageAuthorCacheContext

.. autoclass:: MemberOrUserThroughMessageAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughMessageAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughMessageAuthorCacheContext

.. autoclass:: MemberThroughMessageAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMessageAuthorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMessageAuthorCacheContext

.. autoclass:: UserThroughMessageAuthorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUsersThroughMessageMentionsCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUsersThroughMessageMentionsCacheContext

.. autoclass:: MemberOrUsersThroughMessageMentionsCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MembersThroughMessageMentionsCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MembersThroughMessageMentionsCacheContext

.. autoclass:: MembersThroughMessageMentionsCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UsersThroughMessageMentionsCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UsersThroughMessageMentionsCacheContext

.. autoclass:: UsersThroughMessageMentionsCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

RoleThroughMessageRoleMentionsCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: RoleThroughMessageRoleMentionsCacheContext

.. autoclass:: RoleThroughMessageRoleMentionsCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ReadStateThroughTextChannelReadStateCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ReadStateThroughTextChannelReadStateCacheContext

.. autoclass:: ReadStateThroughTextChannelReadStateCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MembersThroughRoleMembersCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MembersThroughRoleMembersCacheContext

.. autoclass:: MembersThroughRoleMembersCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerThroughRoleServerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerThroughRoleServerCacheContext

.. autoclass:: ServerThroughRoleServerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelVoiceStateContainerThroughTextChannelVoiceStatesCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelVoiceStateContainerThroughTextChannelVoiceStatesCacheContext

.. autoclass:: ChannelVoiceStateContainerThroughTextChannelVoiceStatesCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelVoiceStateContainerThroughVoiceChannelVoiceStatesCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelVoiceStateContainerThroughVoiceChannelVoiceStatesCacheContext

.. autoclass:: ChannelVoiceStateContainerThroughVoiceChannelVoiceStatesCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughServerEmojiCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughServerEmojiCreatorCacheContext

.. autoclass:: MemberOrUserThroughServerEmojiCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughServerEmojiCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughServerEmojiCreatorCacheContext

.. autoclass:: MemberThroughServerEmojiCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughServerEmojiCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughServerEmojiCreatorCacheContext

.. autoclass:: UserThroughServerEmojiCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughDetachedEmojiCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughDetachedEmojiCreatorCacheContext

.. autoclass:: UserThroughDetachedEmojiCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerThroughServerEmojiServerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerThroughServerEmojiServerCacheContext

.. autoclass:: ServerThroughServerEmojiServerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerThroughServerPublicInviteServerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerThroughServerPublicInviteServerCacheContext

.. autoclass:: ServerThroughServerPublicInviteServerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelThroughServerPublicInviteChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelThroughServerPublicInviteChannelCacheContext

.. autoclass:: ChannelThroughServerPublicInviteChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughServerPublicInviteUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughServerPublicInviteUserCacheContext

.. autoclass:: UserThroughServerPublicInviteUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelThroughGroupPublicInviteChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelThroughGroupPublicInviteChannelCacheContext

.. autoclass:: ChannelThroughGroupPublicInviteChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughGroupPublicInviteUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughGroupPublicInviteUserCacheContext

.. autoclass:: UserThroughGroupPublicInviteUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelThroughGroupInviteChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelThroughGroupInviteChannelCacheContext

.. autoclass:: ChannelThroughGroupInviteChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughGroupInviteCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughGroupInviteCreatorCacheContext

.. autoclass:: UserThroughGroupInviteCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerThroughServerInviteServerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerThroughServerInviteServerCacheContext

.. autoclass:: ServerThroughServerInviteServerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelThroughServerInviteChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelThroughServerInviteChannelCacheContext

.. autoclass:: ChannelThroughServerInviteChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughServerInviteCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughServerInviteCreatorCacheContext

.. autoclass:: MemberOrUserThroughServerInviteCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughServerInviteCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughServerInviteCreatorCacheContext

.. autoclass:: MemberThroughServerInviteCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughServerInviteCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughServerInviteCreatorCacheContext

.. autoclass:: UserThroughServerInviteCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:


ChannelThroughReadStateChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelThroughReadStateChannelCacheContext

.. autoclass:: ChannelThroughReadStateChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

EmojiThroughServerGetterCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: EmojiThroughServerGetterCacheContext

.. autoclass:: EmojiThroughServerGetterCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughServerGetterCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughServerGetterCacheContext

.. autoclass:: MemberThroughServerGetterCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

EmojisThroughServerGetterCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: EmojisThroughServerGetterCacheContext

.. autoclass:: EmojisThroughServerGetterCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MembersThroughServerGetterCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MembersThroughServerGetterCacheContext

.. autoclass:: MembersThroughServerGetterCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelThroughServerGetterCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelThroughServerGetterCacheContext

.. autoclass:: ChannelThroughServerGetterCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelsThroughServerGetterCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelsThroughServerGetterCacheContext

.. autoclass:: ChannelsThroughServerGetterCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughServerMeCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughServerMeCacheContext

.. autoclass:: MemberThroughServerMeCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughServerOwnerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughServerOwnerCacheContext

.. autoclass:: MemberOrUserThroughServerOwnerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughServerOwnerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughServerOwnerCacheContext

.. autoclass:: MemberThroughServerOwnerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughServerOwnerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughServerOwnerCacheContext

.. autoclass:: UserThroughServerOwnerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:


ServerThroughMemberServerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerThroughMemberServerCacheContext

.. autoclass:: ServerThroughMemberServerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberUserCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberUserCacheContext

.. autoclass:: UserThroughMemberUserCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberBotOwnerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberBotOwnerCacheContext

.. autoclass:: UserThroughMemberBotOwnerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelIDThroughMemberDMChannelIDCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelIDThroughMemberDMChannelIDCacheContext

.. autoclass:: ChannelIDThroughMemberDMChannelIDCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelThroughMemberDMChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelThroughMemberDMChannelCacheContext

.. autoclass:: ChannelThroughMemberDMChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberNameCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberNameCacheContext

.. autoclass:: UserThroughMemberNameCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberDiscriminatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberDiscriminatorCacheContext

.. autoclass:: UserThroughMemberDiscriminatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberDisplayNameCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberDisplayNameCacheContext

.. autoclass:: UserThroughMemberDisplayNameCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberInternalAvatarCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberInternalAvatarCacheContext

.. autoclass:: UserThroughMemberInternalAvatarCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberRawBadgesCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberRawBadgesCacheContext

.. autoclass:: UserThroughMemberRawBadgesCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberStatusCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberStatusCacheContext

.. autoclass:: UserThroughMemberStatusCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberRawFlagsCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberRawFlagsCacheContext

.. autoclass:: UserThroughMemberRawFlagsCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberPrivilegedCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberPrivilegedCacheContext

.. autoclass:: UserThroughMemberPrivilegedCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberBotCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberBotCacheContext

.. autoclass:: UserThroughMemberBotCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberRelationshipCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberRelationshipCacheContext

.. autoclass:: UserThroughMemberRelationshipCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberOnlineCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberOnlineCacheContext

.. autoclass:: UserThroughMemberOnlineCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughMemberTagCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughMemberTagCacheContext

.. autoclass:: UserThroughMemberTagCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerThroughMemberRolesCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerThroughMemberRolesCacheContext

.. autoclass:: ServerThroughMemberRolesCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerThroughMemberServerPermissionsCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerThroughMemberServerPermissionsCacheContext

.. autoclass:: ServerThroughMemberServerPermissionsCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ServerThroughMemberTopRoleCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerThroughMemberTopRoleCacheContext

.. autoclass:: ServerThroughMemberTopRoleCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughUserBotOwnerCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughUserBotOwnerCacheContext

.. autoclass:: UserThroughUserBotOwnerCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelIDThroughUserDMChannelIDCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelIDThroughUserDMChannelIDCacheContext

.. autoclass:: ChannelIDThroughUserDMChannelIDCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

ChannelThroughUserDMChannelIDCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelThroughUserDMChannelIDCacheContext

.. autoclass:: ChannelThroughUserDMChannelIDCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberOrUserThroughWebhookCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberOrUserThroughWebhookCreatorCacheContext

.. autoclass:: MemberOrUserThroughWebhookCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

MemberThroughWebhookCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberThroughWebhookCreatorCacheContext

.. autoclass:: MemberThroughWebhookCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:

UserThroughWebhookCreatorCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserThroughWebhookCreatorCacheContext

.. autoclass:: UserThroughWebhookCreatorCacheContext
    :show-inheritance:
    :members:
    :inherited-members:


ChannelThroughWebhookChannelCacheContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelThroughWebhookChannelCacheContext

.. autoclass:: ChannelThroughWebhookChannelCacheContext
    :show-inheritance:
    :members:
    :inherited-members:
