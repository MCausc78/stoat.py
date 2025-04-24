.. currentmodule:: pyvolt

Authentication
==============

The following section documents everything related to authentication.

PartialAccount
~~~~~~~~~~~~~~

.. attributetable:: PartialAccount

.. autoclass:: PartialAccount
    :members:

MFATicket
~~~~~~~~~

.. attributetable:: MFATicket

.. autoclass:: MFATicket
    :members:

WebPushSubscription
~~~~~~~~~~~~~~~~~~~

.. attributetable:: WebPushSubscription

.. autoclass:: WebPushSubscription
    :members:

PartialSession
~~~~~~~~~~~~~~

.. attributetable:: PartialSession

.. autoclass:: PartialSession
    :members:

Session
~~~~~~~

.. attributetable:: Session

.. autoclass:: Session
    :members:

MFARequired
~~~~~~~~~~~

.. attributetable:: MFARequired

.. autoclass:: MFARequired
    :members:

AccountDisabled
~~~~~~~~~~~~~~~

.. attributetable:: AccountDisabled

.. autoclass:: AccountDisabled
    :members:

MFAStatus
~~~~~~~~~

.. attributetable:: MFAStatus

.. autoclass:: MFAStatus
    :members:

BaseMFAResponse
~~~~~~~~~~~~~~~

.. attributetable:: BaseMFAResponse

.. autoclass:: BaseMFAResponse
    :members:

ByPassword
~~~~~~~~~~

.. attributetable:: ByPassword

.. autoclass:: ByPassword
    :members:

ByRecoveryCode
~~~~~~~~~~~~~~

.. attributetable:: ByRecoveryCode

.. autoclass:: ByRecoveryCode
    :members:

ByTOTP
~~~~~~

.. attributetable:: ByTOTP

.. autoclass:: ByTOTP
    :members:

MFAResponse
~~~~~~~~~~~

.. class:: MFAResponse

    An union of all possible MFA verification responses.
    
    The following classes are included in this union:

    - :class:`.ByPassword`
    - :class:`.ByRecoveryCode`
    - :class:`.ByTOTP`

LoginResult
~~~~~~~~~~~

.. class:: LoginResult

    An union of all login responses.
    
    The following classes are included in this union:

    - :class:`.Session`
    - :class:`.MFARequired`
    - :class:`.AccountDisabled`