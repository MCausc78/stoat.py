:orphan:

.. currentmodule:: pyvolt

.. _server_subscriptions:

Server Subscriptions
====================

.. note::
    If you're not using user account, you may skip reading this. Otherwise, continue reading.

.. note::
    Subscriptions have no effect on bot accounts.

Server subscriptions were added and announced on `19 Jun 2024 because of official Revolt API instance kept going down <https://app.revolt.chat/server/01F7ZSBSFHQ8TA81725KQCSDDP/channel/01F9KATFHCAWGYG1NQ13MFDRAT/01J0RVAD25A56P65WPCH35B68Y>`_.

Since they don't appear to be changed, this page documents them in detail.

In essence, since library does not provide an automatic way to manage subscriptions, you'll need to do it manually through :meth:`~pyvolt.Server.subscribe` method.

Users are automatically subscribed to all friends, all recipients from all groups the user in, users who have friend request from the current users and users the current user sent friend request to.

Subscriptions are automatically expired within 15 minutes.

An single WebSocket connection can have only up to 5 active subscriptions.

.. note::
    This note is relevant only to client developers.

    You should subscribe only if the client is in focus.
    
    You should aim to subscribe at most every 10 minutes per server.
