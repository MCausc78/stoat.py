.. currentmodule:: stoat

Channels
========

The following section documents everything related to channels.

Models
------

BaseChannel
~~~~~~~~~~~

.. attributetable:: BaseChannel

.. autoclass:: BaseChannel
    :members:

PartialChannel
~~~~~~~~~~~~~~

.. attributetable:: PartialChannel

.. autoclass:: PartialChannel
    :members:
    :inherited-members:

SavedMessagesChannel
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: SavedMessagesChannel

.. autoclass:: SavedMessagesChannel
    :members:
    :inherited-members:

DMChannel
~~~~~~~~~

.. attributetable:: DMChannel

.. autoclass:: DMChannel
    :members:
    :inherited-members:

GroupChannel
~~~~~~~~~~~~

.. attributetable:: GroupChannel

.. autoclass:: GroupChannel
    :members:
    :inherited-members:

UnknownPrivateChannel
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UnknownPrivateChannel

.. autoclass:: UnknownPrivateChannel
    :members:
    :inherited-members:

BaseServerChannel
~~~~~~~~~~~~~~~~~

.. attributetable:: BaseServerChannel

.. autoclass:: BaseServerChannel
    :members:
    :inherited-members:

ChannelVoiceMetadata
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelVoiceMetadata

.. autoclass:: ChannelVoiceMetadata
    :members:

TextChannel
~~~~~~~~~~~

.. attributetable:: TextChannel

.. autoclass:: TextChannel
    :members:
    :inherited-members:

VoiceChannel
~~~~~~~~~~~~

.. attributetable:: VoiceChannel

.. autoclass:: VoiceChannel
    :members:
    :inherited-members:

UnknownServerChannel
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: UnknownServerChannel

.. autoclass:: UnknownServerChannel
    :members:
    :inherited-members:

PrivateChannel
~~~~~~~~~~~~~~

.. class:: PrivateChannel
    
    An union of all channels that do not belong to a server.
    
    The following classes are included in this union:

    - :class:`.SavedMessagesChannel`
    - :class:`.DMChannel`
    - :class:`.GroupChannel`

ServerChannel
~~~~~~~~~~~~~
    
.. class:: ServerChannel

    An union of all channels that belong to a server.
    
    The following classes are included in this union:

    - :class:`.TextChannel`
    - :class:`.VoiceChannel`

TextableChannel
~~~~~~~~~~~~~~~

.. class:: TextableChannel

    An union of all channels that can have messages in them.
    
    The following classes are included in this union:
    
    - :class:`.SavedMessagesChannel`
    - :class:`.DMChannel`
    - :class:`.GroupChannel`
    - :class:`.TextChannel`
    - :class:`.VoiceChannel`

UnknownChannel
~~~~~~~~~~~~~~

.. class:: UnknownChannel

    An union of all channels that are not recognized by library.
    
    The following classes are included in this union:
    
    - :class:`.UnknownPrivateChannel`
    - :class:`.UnknownServerChannel`

Channel
~~~~~~~

.. class:: Channel

    An union of all channels.

    Union types such as this exist to help determine which exact channel type has some field during development.

    The following classes are included in this union:
    
    - :class:`.SavedMessagesChannel`
    - :class:`.DMChannel`
    - :class:`.GroupChannel`
    - :class:`.UnknownPrivateChannel`
    - :class:`.TextChannel`
    - :class:`.VoiceChannel`
    - :class:`.UnknownServerChannel`

ChannelVoiceStateContainer
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: ChannelVoiceStateContainer

.. autoclass:: ChannelVoiceStateContainer
    :members:

PartialMessageable
~~~~~~~~~~~~~~~~~~

.. attributetable:: PartialMessageable

.. autoclass:: PartialMessageable
    :members: