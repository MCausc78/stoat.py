stoat.py
========

A simple, flexible API wrapper for Stoat.

.. note::
    This is beta software. Please report bugs on GitHub issues if you will find any.

Key Features
------------

- Built on ``asyncio``.
- Sane rate limit handling that prevents 429s
- Fast. Really faster than Revolt.py and voltage.
- Low memory usage.
- Customizable architecture. Build object parser in Rust to achieve high speeds.
- Focuses on supporting both, bot and user accounts.

Installing
----------

**Python 3.10 or higher is required**

To install the library, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U stoat.py

    # Windows
    py -3 -m pip install -U stoat.py

Or to install alpha master (with all new features):

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U git+https://github.com/MCausc78/stoat.py@master

    # Windows
    py -3 -m pip install -U git+https://github.com/MCausc78/stoat.py@master

Quick Example
-------------

.. code:: py

    from stoat import Client

    class MyClient(Client):
        async def on_ready(self, _, /):
            print('Logged on as', self.me)

        async def on_message(self, message, /):
            # don't respond to ourselves
            if message.author_id == self.me.id:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    # You can pass `bot=False` to run as user account
    client = MyClient(token='token')
    client.run()

Bot Example
-----------

.. code:: py

    from stoat.ext import commands

    # Pass `self_bot=True` to make your bot listen only to you
    bot = commands.Bot(command_prefix='!')

    @bot.command()
    async def ping(ctx):
        await ctx.send('Pong!')

    token = 'token'

    # That's also allowed, just like in `discord.py`. Pass `bot=False` keyword argument if you want to run as user account.
    bot.run(token)

Links
------

- `Documentation <https://stoatpy.readthedocs.io/en/latest/index.html>`_
- `Official Stoat Server <https://stt.gg/ZZQb4sxx>`_
- `Stoat API <https://stoat.gg/API>`_

Why Not
-------

- `pyrevolt <https://github.com/GenericNerd/pyrevolt>`_ - Doesn't follow PEP8 and does a ton of requests on startup (not member list).
- `voltage <https://github.com/EnokiUN/voltage>`_ - Slow and simply copypasta from ``revolt.py``.
- `revolt.py <https://github.com/revoltchat/revolt.py>`_ - Slow and unable to disable member list loading.
- `luster <https://github.com/nerdguyahmad/luster>`_ - Unmaintained library.
