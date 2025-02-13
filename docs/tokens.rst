:orphan:

.. _tokens:

Tokens
=======

Tokens are how we authenticate with Revolt.

Regular (and bot) tokens are exactly 64 characters long and generated with `nanoid <https://docs.rs/nanoid/latest/nanoid/>`_`
and contain only ``_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`` characters.

How do I obtain mine?
----------------------
While the library does support authenticating traditionally, it's fairly easier to obtain your token manually.

To obtain your token from the Revolt client, the easiest way is pasting this into the developer console (CTRL+SHIFT+I):

.. code:: js

    controllers.client.getReadyClient().api.authentication.revolt.token

Or, you can do it manually:

1. Open developer tools (CTRL+SHIFT+I).
2. Click the Network tab.
3. Click the XHR tab.
4. Select a request and go to the Headers section.
5. Copy-paste the value from the X-Session-Token header.
