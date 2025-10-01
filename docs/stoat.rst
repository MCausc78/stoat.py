:orphan:

.. _stoat-intro:

Creating a Bot Account
=======================

In order to work with the library and the Stoat API in general, we should first create a Stoat bot account.

.. note::
    If you wish to use user account, please visit :doc:`authenticating` instead.

Creating a Bot account is a pretty straightforward process.

1. Make sure you're logged on to the `Stoat website <https://app.stoat.chat>`_.
2. Navigate to the bots page.
3. Click on the "CREATE A BOT" button.

    .. image:: /images/stoat_create_bot_button.png
        :alt: The "CREATE A BOT" button.

4. Give the bot a name and click "Create".

    .. image:: /images/stoat_create_bot_form.png
        :alt: The new bot form filled in.

5. Click on the "Edit" button to configure bot's profile.
6. Make sure that **Public Bot** is ticked if you want others to invite your bot.

    .. image:: /images/stoat_bot_user_options.png
        :alt: How the Bot User options should look like for most people.

7. Copy the token using the "Copy" button.

    .. warning::

        It should be worth noting that this token is essentially your bot's
        password. You should **never** share this with someone else. In doing so,
        someone can log in to your bot and do malicious things, such as leaving
        servers, ban all members inside a server, or pinging all members maliciously.

        The possibilities are endless, so **do not share this token.**

        If you accidentally leaked your token, click the "Regenerate" button as soon
        as possible. This revokes your old token and re-generates a new one.
        Now you need to use the new token to login.

And that's it. You now have a bot account and you can login with that token.

.. _stoat_invite_bot:

Inviting Your Bot
-----------------

So, you've made a bot account, but it's not actually in any server.

If you want to invite your bot, you must create an invite URL for it.

1. Make sure you're logged on to the `Stoat website <https://stoat.chat/app>`_.
2. Navigate to the bots page in user settings.
3. Click on your bot.
4. Click on the "Copy Invite Link" button.

    .. image:: /images/stoat_invite_bot.png
        :alt: How the bot invite page should look like.

5. The copied URL can be used to add your bot to a server or group. Copy and paste the URL into your browser, choose a destination to invite the bot to, and click "ADD".

.. note::

    The person adding the bot needs "Manage Server" or "Invite Others" (in groups) permissions to do so.
