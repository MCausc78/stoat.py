.. currentmodule:: stoat

Messages
========

The following section documents everything related to messages. Messages are core part of Stoat and they are way
for users to communicate.

Models
------

BaseSystemEvent
~~~~~~~~~~~~~~~

.. attributetable:: BaseSystemEvent

.. autoclass:: BaseSystemEvent
    :members:

TextSystemEvent
~~~~~~~~~~~~~~~

.. attributetable:: TextSystemEvent

.. autoclass:: TextSystemEvent
    :members:
    :inherited-members:

StatelessUserAddedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessUserAddedSystemEvent

.. autoclass:: StatelessUserAddedSystemEvent
    :members:
    :inherited-members:

UserAddedSystemEvent
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserAddedSystemEvent

.. autoclass:: UserAddedSystemEvent
    :members:
    :inherited-members:

StatelessUserRemovedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessUserRemovedSystemEvent

.. autoclass:: StatelessUserRemovedSystemEvent
    :members:
    :inherited-members:

UserRemovedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserRemovedSystemEvent

.. autoclass:: UserRemovedSystemEvent
    :members:
    :inherited-members:

StatelessUserJoinedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessUserJoinedSystemEvent

.. autoclass:: StatelessUserJoinedSystemEvent
    :members:
    :inherited-members:

UserJoinedSystemEvent
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserJoinedSystemEvent

.. autoclass:: UserJoinedSystemEvent
    :members:
    :inherited-members:

StatelessUserLeftSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessUserLeftSystemEvent

.. autoclass:: StatelessUserLeftSystemEvent
    :members:
    :inherited-members:

UserLeftSystemEvent
~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserLeftSystemEvent

.. autoclass:: UserLeftSystemEvent
    :members:
    :inherited-members:

StatelessUserKickedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessUserKickedSystemEvent

.. autoclass:: StatelessUserKickedSystemEvent
    :members:
    :inherited-members:

UserKickedSystemEvent
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserKickedSystemEvent

.. autoclass:: UserKickedSystemEvent
    :members:
    :inherited-members:


StatelessUserBannedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessUserBannedSystemEvent

.. autoclass:: StatelessUserBannedSystemEvent
    :members:
    :inherited-members:


UserBannedSystemEvent
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UserBannedSystemEvent

.. autoclass:: UserBannedSystemEvent
    :members:
    :inherited-members:

StatelessChannelRenamedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessChannelRenamedSystemEvent

.. autoclass:: StatelessChannelRenamedSystemEvent
    :members:
    :inherited-members:

ChannelRenamedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelRenamedSystemEvent

.. autoclass:: ChannelRenamedSystemEvent
    :members:
    :inherited-members:

StatelessChannelDescriptionChangedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessChannelDescriptionChangedSystemEvent

.. autoclass:: StatelessChannelDescriptionChangedSystemEvent
    :members:
    :inherited-members:

ChannelDescriptionChangedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelDescriptionChangedSystemEvent

.. autoclass:: ChannelDescriptionChangedSystemEvent
    :members:
    :inherited-members:

StatelessChannelIconChangedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessChannelIconChangedSystemEvent

.. autoclass:: StatelessChannelIconChangedSystemEvent
    :members:
    :inherited-members:

ChannelIconChangedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelIconChangedSystemEvent

.. autoclass:: ChannelIconChangedSystemEvent
    :members:
    :inherited-members:

StatelessChannelOwnershipChangedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessChannelOwnershipChangedSystemEvent

.. autoclass:: StatelessChannelOwnershipChangedSystemEvent
    :members:
    :inherited-members:

ChannelOwnershipChangedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelOwnershipChangedSystemEvent

.. autoclass:: ChannelOwnershipChangedSystemEvent
    :members:
    :inherited-members:

StatelessMessagePinnedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessMessagePinnedSystemEvent

.. autoclass:: StatelessMessagePinnedSystemEvent
    :members:
    :inherited-members:

MessagePinnedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessagePinnedSystemEvent

.. autoclass:: MessagePinnedSystemEvent
    :members:
    :inherited-members:

StatelessMessageUnpinnedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessMessageUnpinnedSystemEvent

.. autoclass:: StatelessMessageUnpinnedSystemEvent
    :members:
    :inherited-members:

MessageUnpinnedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageUnpinnedSystemEvent

.. autoclass:: MessageUnpinnedSystemEvent
    :members:
    :inherited-members:

StatelessCallStartedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: StatelessCallStartedSystemEvent

.. autoclass:: StatelessCallStartedSystemEvent
    :members:
    :inherited-members:

CallStartedSystemEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: CallStartedSystemEvent

.. autoclass:: CallStartedSystemEvent
    :members:
    :inherited-members:

StatelessSystemEvent
~~~~~~~~~~~~~~~~~~~~

.. class:: StatelessSystemEvent

    An union of all stateless system events that message may hold.

    The following classes are included in this union:

    - :class:`.TextSystemEvent`
    - :class:`.StatelessUserAddedSystemEvent`
    - :class:`.StatelessUserRemovedSystemEvent`
    - :class:`.StatelessUserJoinedSystemEvent`
    - :class:`.StatelessUserLeftSystemEvent`
    - :class:`.StatelessUserKickedSystemEvent`
    - :class:`.StatelessUserBannedSystemEvent`
    - :class:`.StatelessChannelRenamedSystemEvent`
    - :class:`.StatelessChannelDescriptionChangedSystemEvent`
    - :class:`.StatelessChannelIconChangedSystemEvent`
    - :class:`.StatelessChannelOwnershipChangedSystemEvent`
    - :class:`.StatelessMessagePinnedSystemEvent`
    - :class:`.StatelessMessageUnpinnedSystemEvent`
    - :class:`.StatelessCallStartedSystemEvent`

SystemEvent
~~~~~~~~~~~

.. class:: SystemEvent

    An union of all system events that message may hold.

    The following classes are included in this union:

    - :class:`.TextSystemEvent`
    - :class:`.UserAddedSystemEvent`
    - :class:`.UserRemovedSystemEvent`
    - :class:`.UserJoinedSystemEvent`
    - :class:`.UserLeftSystemEvent`
    - :class:`.UserKickedSystemEvent`
    - :class:`.UserBannedSystemEvent`
    - :class:`.ChannelRenamedSystemEvent`
    - :class:`.ChannelDescriptionChangedSystemEvent`
    - :class:`.ChannelIconChangedSystemEvent`
    - :class:`.ChannelOwnershipChangedSystemEvent`
    - :class:`.MessagePinnedSystemEvent`
    - :class:`.MessageUnpinnedSystemEvent`
    - :class:`.CallStartedSystemEvent`

BaseMessage
~~~~~~~~~~~

.. attributetable:: BaseMessage

.. autoclass:: BaseMessage
    :members:

PartialMessage
~~~~~~~~~~~~~~

.. attributetable:: PartialMessage

.. autoclass:: PartialMessage
    :members:

MessageAppendData
~~~~~~~~~~~~~~~~~

.. attributetable:: MessageAppendData

.. autoclass:: MessageAppendData
    :members:

Message
~~~~~~~

.. attributetable:: Message

.. autoclass:: Message
    :members:
    :inherited-members:

Reply
~~~~~

.. attributetable:: Reply

.. autoclass:: Reply
    :members:

MessageMasquerade
~~~~~~~~~~~~~~~~~

.. attributetable:: MessageMasquerade

.. autoclass:: MessageMasquerade
    :members:

MessageInteractions
~~~~~~~~~~~~~~~~~~~

.. attributetable:: MessageInteractions

.. autoclass:: MessageInteractions
    :members:

MessageWebhook
~~~~~~~~~~~~~~

.. attributetable:: MessageWebhook

.. autoclass:: MessageWebhook
    :members: