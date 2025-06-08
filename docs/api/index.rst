.. currentmodule:: pyvolt

API Reference
=============

The following section outlines the API of pyvolt.

.. note::

    This module uses the Python logging module to log diagnostic and errors
    in an output independent way.  If the logging module is not configured,
    these logs will not be output anywhere.  See :ref:`logging_setup` for
    more information on how to set up and use the logging module with
    pyvolt.

Version Related Info
--------------------

There are two main ways to query version information about the library. There is no currently guarantees as Revolt API is still in beta.

.. For guarantees, check :ref:`version_guarantees`.

.. data:: version_info

    A named tuple that is similar to :obj:`py:sys.version_info`.

    Just like :obj:`py:sys.version_info` the valid values for ``releaselevel`` are
    'alpha', 'beta', 'candidate' and 'final'.

.. data:: __version__

    A string representation of the version. e.g. ``'1.0.0rc1'``. This is based
    off of :pep:`440`.

Documents
---------

.. toctree::
    :maxdepth: 1

    authentication
    bots
    cache
    channels
    clients
    discovery
    embeds
    emojis
    enums_and_flag_classes
    events
    invites
    messages
    roles
    server_members
    servers
    settings
    users
    webhooks

Shard
~~~~~

.. attributetable:: Shard

.. autoclass:: Shard
    :members:

ShardImpl
~~~~~~~~~

.. attributetable:: ShardImpl

.. autoclass:: ShardImpl
    :members:

EventHandler
~~~~~~~~~~~~

.. attributetable:: EventHandler

.. autoclass:: EventHandler
    :members:

State
~~~~~

.. attributetable:: State

.. autoclass:: State
    :members:

CDNClient
~~~~~~~~~

.. attributetable:: CDNClient

.. autoclass:: CDNClient
    :members:

Tag
~~~

.. class:: Tag
    
    An alias to :class:`typing.Literal` with available CDN tags.

Resource
~~~~~~~~

.. attributetable:: Resource

.. autoclass:: Resource
    :members:
    :inherited-members:

Upload
~~~~~~

.. attributetable:: Upload

.. autoclass:: Upload
    :members:
    :inherited-members:

Content
~~~~~~~

.. class:: Content

    An union of types that can be resolved into content.

    The following classes are included in this union:

    - :class:`bytes`
    - :class:`str`, as asset ID
    - :class:`bytearray`
    - :class:`io.IOBase`

.. autofunction:: resolve_content

ResolvableResource
~~~~~~~~~~~~~~~~~~

.. class:: ResolvableResource

    An union of types that can be resolved into resource.

    The following classes are included in this union:

    - :class:`.Resource`
    - :class:`str`
    - :class:`bytes`
    - Tuple[:class:`str`, :class:`.Content`]

.. autofunction:: resolve_resource

Parser
~~~~~~~

.. attributetable:: Parser

.. autoclass:: Parser
    :members:

.. _revolt-api-permissions-calculator:

Permissions Calculator
----------------------

.. autofunction:: calculate_saved_messages_channel_permissions

.. autofunction:: calculate_dm_channel_permissions

.. autofunction:: calculate_group_channel_permissions

.. autofunction:: calculate_server_channel_permissions

.. autofunction:: calculate_server_permissions

.. autofunction:: calculate_user_permissions

.. _revolt-api-utils:

Utility Functions
-----------------

.. autofunction:: ulid_new

.. autofunction:: ulid_timestamp

.. autofunction:: ulid_time

.. autofunction:: sort_member_roles

.. autofunction:: afind

.. autofunction:: find

.. autofunction:: aget

.. autofunction:: get

Abstract Base Classes
---------------------

Messageable
~~~~~~~~~~~

.. attributetable:: pyvolt.abc.Messageable

.. autoclass:: pyvolt.abc.Messageable()
    :members:
    :exclude-members: typing

    .. automethod:: pyvolt.abc.Messageable.typing
        :async-with:

Connectable
~~~~~~~~~~~

.. attributetable:: pyvolt.abc.Connectable

.. autoclass:: pyvolt.abc.Connectable
    :members:

.. _revolt-api-models:

Models
------

UndefinedOr
~~~~~~~~~~~

.. class:: UndefinedOr

    A generic union of either :data:`.UNDEFINED` or a ``T``.

.. data:: UNDEFINED

    A type-sentinel to mark something as undefined. Used to distinguish missing parameter from explicit ``None`` values.


StatelessAsset
~~~~~~~~~~~~~~

.. attributetable:: StatelessAsset

.. autoclass:: StatelessAsset
    :members:

Asset
~~~~~

.. attributetable:: Asset

.. autoclass:: Asset
    :show-inheritance:
    :members:
    :inherited-members:

.. attributetable:: AssetMetadata

.. autoclass:: AssetMetadata
    :members:

PermissionOverride
~~~~~~~~~~~~~~~~~~

.. attributetable:: PermissionOverride

.. autoclass:: PermissionOverride
    :members:

ReadState
~~~~~~~~~

.. attributetable:: ReadState

.. autoclass:: ReadState
    :members:
    :inherited-members:

InstanceCaptchaFeature
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: InstanceCaptchaFeature

.. autoclass:: InstanceCaptchaFeature
    :members:

InstanceGenericFeature
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: InstanceGenericFeature

.. autoclass:: InstanceGenericFeature
    :members:

InstanceVoiceFeature
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: InstanceVoiceFeature

.. autoclass:: InstanceVoiceFeature
    :members:

InstanceFeaturesConfig
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: InstanceFeaturesConfig

.. autoclass:: InstanceFeaturesConfig
    :members:

InstanceBuild
~~~~~~~~~~~~~

.. attributetable:: InstanceBuild

.. autoclass:: InstanceBuild
    :members:

Instance
~~~~~~~~

.. attributetable:: Instance

.. autoclass:: Instance
    :members:

PolicyChange
~~~~~~~~~~~~

.. attributetable:: PolicyChange

.. autoclass:: PolicyChange
    :members:

.. _revolt-api-exceptions:

Exceptions
----------

The following exceptions are thrown by the library.

.. autoexception:: PyvoltException
    :show-inheritance:
    :members:
    :inherited-members:
    :exclude-members: add_note, with_traceback

.. autoexception:: WebSocketConnectionFailure
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: HTTPException
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: NoEffect
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: Unauthorized
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: Forbidden
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: NotFound
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: Conflict
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: Ratelimited
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: InternalServerError
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: BadGateway
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: ShardError
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: ShardClosedError
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: AuthenticationError
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: ConnectError
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: DiscoverError
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: InvalidData
    :show-inheritance:
    :members:
    :inherited-members:

.. autoexception:: NoData
    :show-inheritance:
    :members:
    :inherited-members:

