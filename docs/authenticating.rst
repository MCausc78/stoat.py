:orphan:

.. _tokens:

Tokens
======

Tokens are how we authenticate with Stoat.

Regular (and bot) tokens are exactly 64 characters long and generated with `nanoid <https://docs.rs/nanoid/latest/nanoid/>`_
and contain only ``_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`` characters.

How do I obtain mine?
---------------------

Although the library does support authenticating traditionally, it's fairly easier to obtain your token manually.

To obtain your token from the Stoat client, the easiest way is pasting this into the developer console (CTRL+SHIFT+I):

.. code:: js

    controllers.client.getReadyClient().api.authentication.revolt.token

Or, you can do it manually:

1. Open developer tools (CTRL+SHIFT+I).
2. Click the Network tab.
3. Click the XHR tab.
4. Select a request and go to the Headers section.
5. Copy-paste the value from the X-Session-Token header.

Traditional Authentication
--------------------------

To manually authenticate via having email and password, you'll need to call :meth:`stoat.HTTPClient.login_with_email` method.

Example:

.. code-block:: python3

    try:
        result = await http.login_with_email(
            email='mcausc78@gmail.com',
            password='myverysecretpassword',
            friendly_name='My Stoat client (for testing)',
        )
    except stoat.Unauthorized as exc:
        if exc.type == 'InvalidCredentials':
            raise IncorrectPassword()
        raise exc from None
    except stoat.Forbidden as exc:
        if exc.type == 'LockedOut':
            raise AccountIsLockedOut()
        raise exc from None

    if isinstance(result, stoat.MFARequired):
        # The user has 2FA enabled.
        
        # You can use ``use_totp`` for usual ``123456`` 2FA codes, or ``use_recovery_code`` for recovery ones (``xxxx-yyyy``).
        # If you have MFA secret key and you wish to skip asking TOTP/recovery code from user, you might want to use pyotp here.
        result = await result.use_totp('123456')
    
    if isinstance(result, stoat.AccountDisabled):
        raise AccountIsDisabled()

    # result is Session here
    token = result.token

    http.with_credentials(token, bot=False)

    # Retrieve logged in user.
    me = await http.get_me()
    print(f'You was logged in as {me.tag} (ID: {me.id}).')
