.. currentmodule:: pyvolt

Clients
=======

The following section documents everything related to clients. Clients in this library are primary way to make bots and interact with Revolt API.

Clients
-------

Client
~~~~~~

.. attributetable:: Client

.. autoclass:: Client
    :members:
    :exclude-members: listen, on

    .. automethod:: Client.listen(event=None, /)
        :decorator:

    .. automethod:: Client.on(event=None, /)
        :decorator:

ClientEventHandler
~~~~~~~~~~~~~~~~~~

.. attributetable:: ClientEventHandler

.. autoclass:: ClientEventHandler
    :members:

EventSubscription
~~~~~~~~~~~~~~~~~

.. attributetable:: EventSubscription

.. autoclass:: EventSubscription()
    :members:

TemporarySubscription
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: TemporarySubscription

.. autoclass:: TemporarySubscription()
    :members:

TemporarySubscriptionList
~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: TemporarySubscriptionList

.. autoclass:: TemporarySubscriptionList()
    :members:

HTTPOverrideOptions
~~~~~~~~~~~~~~~~~~~

.. attributetable:: HTTPOverrideOptions

.. autoclass:: HTTPOverrideOptions
    :members:

HTTPClient
~~~~~~~~~~

.. attributetable:: HTTPClient

.. autoclass:: HTTPClient
    :members:

HTTPAdapter
~~~~~~~~~~~

.. attributetable:: HTTPAdapter

.. autoclass:: HTTPAdapter
    :members:

AIOHTTPAdapter
~~~~~~~~~~~~~~~

.. attributetable:: AIOHTTPAdapter

.. autoclass:: AIOHTTPAdapter
    :members:

HTTPResponse
~~~~~~~~~~~~

.. attributetable:: HTTPResponse

.. autoclass:: HTTPResponse
    :members:

AIOHTTPResponseWrapper
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: AIOHTTPResponseWrapper

.. autoclass:: AIOHTTPResponseWrapper
    :members:

HTTPWebSocket
~~~~~~~~~~~~~

.. attributetable:: HTTPWebSocket

.. autoclass:: HTTPWebSocket
    :members:

Route
~~~~~

.. attributetable:: pyvolt.routes.Route

.. autoclass:: pyvolt.routes.Route
    :members:

CompiledRoute
~~~~~~~~~~~~~

.. attributetable:: pyvolt.routes.CompiledRoute

.. autoclass:: pyvolt.routes.CompiledRoute
    :members:

RateLimit
~~~~~~~~~

.. attributetable:: RateLimit

.. autoclass:: RateLimit
    :members:

RateLimitBlocker
~~~~~~~~~~~~~~~~

.. attributetable:: RateLimitBlocker

.. autoclass:: RateLimitBlocker
    :members:

RateLimiter
~~~~~~~~~~~

.. attributetable:: RateLimiter

.. autoclass:: RateLimiter
    :members:

DefaultRateLimit
~~~~~~~~~~~~~~~~

.. attributetable:: DefaultRateLimit

.. autoclass:: DefaultRateLimit
    :members:

DefaultRateLimitBlocker
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: DefaultRateLimitBlocker

.. autoclass:: DefaultRateLimitBlocker
    :members:

DefaultRateLimiter
~~~~~~~~~~~~~~~~~~

.. attributetable:: DefaultRateLimiter

.. autoclass:: DefaultRateLimiter
    :members:
