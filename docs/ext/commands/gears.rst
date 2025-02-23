.. currentmodule:: pyvolt

.. _ext_commands_gears:

Gears
=====

There comes a point in your bot's development when you want to organize a collection of commands, listeners, and some state into one class. Gears allow you to do just that.

The gist:

- Each gear is a Python class that subclasses :class:`.commands.Gear`.
- Every command is marked with the :func:`.commands.command` decorator.
- Every listener is marked with the :meth:`.commands.Gear.listener` decorator.
- Gears are then registered with the :meth:`.Bot.add_gear` call.
- Gears are subsequently removed with the :meth:`.Bot.remove_gear` call.

It should be noted that gears are typically used alongside with :ref:`ext_commands_extensions`.

Quick Example
-------------

This example gear defines a ``Greetings`` category for your commands, with a single :ref:`command <ext_commands_commands>` named ``hello`` as well as a listener to listen to an :ref:`Event <pyvolt-api-events>`.

.. code-block:: python3

    class Greetings(commands.Gear):
        def __init__(self, bot):
            self.bot = bot
            self._last_member = None

        @commands.Gear.listener()
        async def on_member_join(self, event: pyvolt.ServerMemberJoinEvent):
            member = event.member
            server = member.server

            if server.system_messages is None:
                return
            
            channel = server.system_messages.user_joined
            
            if channel is None:
                return
            
            await member.state.http.send_message(channel, f'Welcome {member.mention}.')

        @commands.command()
        async def hello(self, ctx, *, member: typing.Optional[pyvolt.Member] = None):
            """Says hello"""
            member = member or ctx.author
            if self._last_member is None or self._last_member.id != member.id:
                await ctx.send(f'Hello {member.name}~')
            else:
                await ctx.send(f'Hello {member.name}... This feels familiar.')
            self._last_member = member

A couple of technical notes to take into consideration:

- All listeners must be explicitly marked via decorator, :meth:`~.commands.Gear.listener`.
- The name of the gear is automatically derived from the class name but can be overridden. See :ref:`ext_commands_gears_meta_options`.
- All commands must now take a ``self`` parameter to allow usage of instance attributes that can be used to maintain state.

Gear Registration
-----------------

Once you have defined your gear, you need to tell the bot to register the gears to be used. We do this via the :meth:`~.commands.Bot.add_gear` method.

.. code-block:: python3

    await bot.add_gear(Greetings(bot))

This binds the gear to the bot, adding all commands and listeners to the bot automatically.

Note that we reference the gear by name, which we can override through :ref:`ext_commands_gears_meta_options`. So if we ever want to remove the gear eventually, we would have to do the following.

.. code-block:: python3

    await bot.remove_gear('Greetings')

Using Gears
-----------

Just as we remove a gear by its name, we can also retrieve it by its name as well. This allows us to use a gear as an inter-command communication protocol to share data. For example:

.. code-block:: python3
    :emphasize-lines: 22,24

    class Economy(commands.Gear):
        ...

        async def withdraw_money(self, member, money):
            # implementation here
            ...

        async def deposit_money(self, member, money):
            # implementation here
            ...

    class Gambling(commands.Gear):
        def __init__(self, bot):
            self.bot = bot

        def coinflip(self):
            return random.randint(0, 1)

        @commands.command()
        async def gamble(self, ctx, money: int):
            """Gambles some money."""
            economy = self.bot.get_gear('Economy')
            if economy is not None:
                await economy.withdraw_money(ctx.author, money)
                if self.coinflip() == 1:
                    await economy.deposit_money(ctx.author, money * 1.5)

.. _ext_commands_gears_special_methods:

Special Methods
---------------

As gears get more complicated and have more commands, there comes a point where we want to customise the behaviour of the entire gear or bot.

They are as follows:

- :meth:`.Gear.gear_load`
- :meth:`.Gear.gear_unload`
- :meth:`.Gear.gear_check`
- :meth:`.Gear.gear_command_error`
- :meth:`.Gear.gear_before_invoke`
- :meth:`.Gear.gear_after_invoke`
- :meth:`.Gear.bot_check`
- :meth:`.Gear.bot_check_once`

You can visit the reference to get more detail.

.. _ext_commands_gears_meta_options:

Meta Options
------------

At the heart of a gear resides a metaclass, :class:`.commands.GearMeta`, which can take various options to customise some of the behaviour. To do this, we pass keyword arguments to the class definition line. For example, to change the gear name we can pass the ``name`` keyword argument as follows:

.. code-block:: python3

    class MyGear(commands.Gear, name='My Gear'):
        pass

To see more options that you can set, see the documentation of :class:`.commands.GearMeta`.

Inspection
----------

Since gears ultimately are classes, we have some tools to help us inspect certain properties of the gear.


To get a :class:`list` of commands, we can use :meth:`.Gear.get_commands`. ::

    >>> gear = bot.get_gear('Greetings')
    >>> commands = gear.get_commands()
    >>> print([c.name for c in commands])

If we want to get the subcommands as well, we can use the :meth:`.Gear.walk_commands` generator. ::

    >>> print([c.qualified_name for c in gear.walk_commands()])

To do the same with listeners, we can query them with :meth:`.Gear.get_listeners`. This returns a list of tuples -- the first element being the event class and the second one being the actual function itself. ::

    >>> for cls, func in gear.get_listeners():
    ...     print(cls, '->', func)