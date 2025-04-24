.. currentmodule:: pyvolt

Events
======

The following section documents everything related to events.

Models
------

.. _revolt-api-events:

Events
------

BaseEvent
~~~~~~~~~

.. attributetable:: BaseEvent

.. autoclass:: BaseEvent
    :members:
    :inherited-members:

ShardEvent
~~~~~~~~~~

.. attributetable:: ShardEvent

.. autoclass:: ShardEvent
    :members:
    :inherited-members:

.. attributetable:: ReadyEvent

.. autoclass:: ReadyEvent
    :members:
    :inherited-members:

BaseChannelCreateEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: BaseChannelCreateEvent

.. autoclass:: BaseChannelCreateEvent
    :members:
    :inherited-members:

PrivateChannelCreateEvent
~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: PrivateChannelCreateEvent

.. autoclass:: PrivateChannelCreateEvent
    :show-inheritance:
    :members:
    :inherited-members:

ServerChannelCreateEvent
~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerChannelCreateEvent

.. autoclass:: ServerChannelCreateEvent
    :show-inheritance:
    :members:
    :inherited-members:

ChannelCreateEvent
~~~~~~~~~~~~~~~~~~

.. class:: ChannelCreateEvent

    An union of private/server channel create events.
    
    The following classes are included in this union:

    - :class:`.PrivateChannelCreateEvent`
    - :class:`.ServerChannelCreateEvent`

ChannelUpdateEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelUpdateEvent

.. autoclass:: ChannelUpdateEvent
    :members:
    :inherited-members:

ChannelDeleteEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelDeleteEvent

.. autoclass:: ChannelDeleteEvent
    :members:
    :inherited-members:

GroupRecipientAddEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: GroupRecipientAddEvent

.. autoclass:: GroupRecipientAddEvent
    :members:
    :inherited-members:

GroupRecipientRemoveEvent
~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: GroupRecipientRemoveEvent

.. autoclass:: GroupRecipientRemoveEvent
    :members:
    :inherited-members:

ChannelStartTypingEvent
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelStartTypingEvent

.. autoclass:: ChannelStartTypingEvent
    :members:
    :inherited-members:

ChannelStopTypingEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelStopTypingEvent

.. autoclass:: ChannelStopTypingEvent
    :members:
    :inherited-members:

MessageStartEditingEvent
~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageStartEditingEvent

.. autoclass:: MessageStartEditingEvent
    :members:
    :inherited-members:

MessageStopEditingEvent
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageStopEditingEvent

.. autoclass:: MessageStopEditingEvent
    :members:
    :inherited-members:

MessageAckEvent
~~~~~~~~~~~~~~~

.. attributetable:: MessageAckEvent

.. autoclass:: MessageAckEvent
    :members:
    :inherited-members:

MessageCreateEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageCreateEvent

.. autoclass:: MessageCreateEvent
    :members:
    :inherited-members:

MessageUpdateEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageUpdateEvent

.. autoclass:: MessageUpdateEvent
    :members:
    :inherited-members:

MessageAppendEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageAppendEvent

.. autoclass:: MessageAppendEvent
    :members:
    :inherited-members:

MessageDeleteEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageDeleteEvent

.. autoclass:: MessageDeleteEvent
    :members:
    :inherited-members:

MessageReactEvent
~~~~~~~~~~~~~~~~~

.. attributetable:: MessageReactEvent

.. autoclass:: MessageReactEvent
    :members:
    :inherited-members:

MessageUnreactEvent
~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageUnreactEvent

.. autoclass:: MessageUnreactEvent
    :members:
    :inherited-members:

MessageClearReactionEvent
~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageClearReactionEvent

.. autoclass:: MessageClearReactionEvent
    :members:
    :inherited-members:

MessageDeleteBulkEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageDeleteBulkEvent

.. autoclass:: MessageDeleteBulkEvent
    :members:
    :inherited-members:

ServerCreateEvent
~~~~~~~~~~~~~~~~~

.. attributetable:: ServerCreateEvent

.. autoclass:: ServerCreateEvent
    :members:
    :inherited-members:

ServerEmojiCreateEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerEmojiCreateEvent

.. autoclass:: ServerEmojiCreateEvent
    :members:
    :inherited-members:

ServerEmojiDeleteEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerEmojiDeleteEvent

.. autoclass:: ServerEmojiDeleteEvent
    :members:
    :inherited-members:

ServerUpdateEvent
~~~~~~~~~~~~~~~~~

.. attributetable:: ServerUpdateEvent

.. autoclass:: ServerUpdateEvent
    :members:
    :inherited-members:

ServerDeleteEvent
~~~~~~~~~~~~~~~~~

.. attributetable:: ServerDeleteEvent

.. autoclass:: ServerDeleteEvent
    :members:
    :inherited-members:

ServerMemberJoinEvent
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerMemberJoinEvent

.. autoclass:: ServerMemberJoinEvent
    :members:
    :inherited-members:

ServerMemberUpdateEvent
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerMemberUpdateEvent

.. autoclass:: ServerMemberUpdateEvent
    :members:
    :inherited-members:

ServerMemberRemoveEvent
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerMemberRemoveEvent

.. autoclass:: ServerMemberRemoveEvent
    :members:
    :inherited-members:

RawServerRoleUpdateEvent
~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: RawServerRoleUpdateEvent

.. autoclass:: RawServerRoleUpdateEvent
    :members:
    :inherited-members:

ServerRoleDeleteEvent
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ServerRoleDeleteEvent

.. autoclass:: ServerRoleDeleteEvent
    :members:
    :inherited-members:

ReportCreateEvent
~~~~~~~~~~~~~~~~~

.. attributetable:: ReportCreateEvent

.. autoclass:: ReportCreateEvent
    :members:
    :inherited-members:

UserUpdateEvent
~~~~~~~~~~~~~~~

.. attributetable:: UserUpdateEvent

.. autoclass:: UserUpdateEvent
    :members:
    :inherited-members:

UserRelationshipUpdateEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserRelationshipUpdateEvent

.. autoclass:: UserRelationshipUpdateEvent
    :members:
    :inherited-members:

UserSettingsUpdateEvent
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserSettingsUpdateEvent

.. autoclass:: UserSettingsUpdateEvent
    :members:
    :inherited-members:

UserPlatformWipeEvent
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserPlatformWipeEvent

.. autoclass:: UserPlatformWipeEvent
    :members:
    :inherited-members:

WebhookCreateEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: WebhookCreateEvent

.. autoclass:: WebhookCreateEvent
    :members:
    :inherited-members:

WebhookUpdateEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: WebhookUpdateEvent

.. autoclass:: WebhookUpdateEvent
    :members:
    :inherited-members:

WebhookDeleteEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: WebhookDeleteEvent

.. autoclass:: WebhookDeleteEvent
    :members:
    :inherited-members:

AuthifierEvent
~~~~~~~~~~~~~~

.. attributetable:: AuthifierEvent

.. autoclass:: AuthifierEvent
    :members:
    :inherited-members:

SessionCreateEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: SessionCreateEvent

.. autoclass:: SessionCreateEvent
    :show-inheritance:
    :members:
    :inherited-members:

SessionDeleteEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: SessionDeleteEvent

.. autoclass:: SessionDeleteEvent
    :show-inheritance:
    :members:
    :inherited-members:

SessionDeleteAllEvent
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: SessionDeleteAllEvent

.. autoclass:: SessionDeleteAllEvent
    :show-inheritance:
    :members:
    :inherited-members:

LogoutEvent
~~~~~~~~~~~

.. attributetable:: LogoutEvent

.. autoclass:: LogoutEvent
    :members:
    :inherited-members:

VoiceChannelJoinEvent
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: VoiceChannelJoinEvent

.. autoclass:: VoiceChannelJoinEvent
    :members:
    :inherited-members:

VoiceChannelLeaveEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: VoiceChannelLeaveEvent

.. autoclass:: VoiceChannelLeaveEvent
    :members:
    :inherited-members:

VoiceChannelMoveEvent
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: VoiceChannelMoveEvent

.. autoclass:: VoiceChannelMoveEvent
    :members:
    :inherited-members:

UserVoiceStateUpdateEvent
~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserVoiceStateUpdateEvent

.. autoclass:: UserVoiceStateUpdateEvent
    :members:
    :inherited-members:

UserMoveVoiceChannelEvent
~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserMoveVoiceChannelEvent

.. autoclass:: UserMoveVoiceChannelEvent
    :members:
    :inherited-members:

AuthenticatedEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: AuthenticatedEvent

.. autoclass:: AuthenticatedEvent
    :members:
    :inherited-members:

BeforeConnectEvent
~~~~~~~~~~~~~~~~~~

.. attributetable:: BeforeConnectEvent

.. autoclass:: BeforeConnectEvent
    :members:
    :inherited-members:

AfterConnectEvent
~~~~~~~~~~~~~~~~~

.. attributetable:: AfterConnectEvent

.. autoclass:: AfterConnectEvent
    :members:
    :inherited-members: