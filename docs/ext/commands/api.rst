.. currentmodule:: stoat

API Reference
=============

The following section outlines the API of stoat.py's command extension module.

.. _ext_commands_api_bot:

Bots
----

Bot
~~~

.. attributetable:: stoat.ext.commands.Bot

.. autoclass:: stoat.ext.commands.Bot
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, check, check_once, command, group, listen, on

    .. automethod:: Bot.after_invoke()
        :decorator:

    .. automethod:: Bot.before_invoke()
        :decorator:

    .. automethod:: Bot.check()
        :decorator:

    .. automethod:: Bot.check_once()
        :decorator:

    .. automethod:: Bot.command(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.group(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.listen(event=None, /)
        :decorator:

    .. automethod:: Bot.on(event=None, /)
        :decorator:


Prefix Helpers
--------------

.. autofunction:: stoat.ext.commands.when_mentioned

.. autofunction:: stoat.ext.commands.when_mentioned_or

.. _ext_commands_api_events:

Event Reference
---------------

CommandErrorEvent
~~~~~~~~~~~~~~~~~

.. attributetable:: stoat.ext.commands.CommandErrorEvent

.. autoclass:: stoat.ext.commands.CommandErrorEvent
    :members:
    :inherited-members:

CommandEvent
~~~~~~~~~~~~

.. attributetable:: stoat.ext.commands.CommandEvent

.. autoclass:: stoat.ext.commands.CommandEvent
    :members:
    :inherited-members:

CommandCompletionEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: stoat.ext.commands.CommandCompletionEvent

.. autoclass:: stoat.ext.commands.CommandCompletionEvent
    :members:
    :inherited-members:

.. _ext_commands_api_command:

Commands
--------

Decorators
~~~~~~~~~~

.. autofunction:: stoat.ext.commands.command
    :decorator:

.. autofunction:: stoat.ext.commands.group
    :decorator:

Command
~~~~~~~

.. attributetable:: stoat.ext.commands.Command

.. autoclass:: stoat.ext.commands.Command
    :members:
    :special-members: __call__
    :exclude-members: after_invoke, before_invoke, error

    .. automethod:: Command.after_invoke()
        :decorator:

    .. automethod:: Command.before_invoke()
        :decorator:

    .. automethod:: Command.error()
        :decorator:

Group
~~~~~

.. attributetable:: stoat.ext.commands.Group

.. autoclass:: stoat.ext.commands.Group
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, command, error, group

    .. automethod:: Group.after_invoke()
        :decorator:

    .. automethod:: Group.before_invoke()
        :decorator:

    .. automethod:: Group.command(*args, **kwargs)
        :decorator:

    .. automethod:: Group.error()
        :decorator:

    .. automethod:: Group.group(*args, **kwargs)
        :decorator:

GroupMixin
~~~~~~~~~~

.. attributetable:: stoat.ext.commands.GroupMixin

.. autoclass:: stoat.ext.commands.GroupMixin
    :members:
    :exclude-members: command, group

    .. automethod:: GroupMixin.command(*args, **kwargs)
        :decorator:

    .. automethod:: GroupMixin.group(*args, **kwargs)
        :decorator:

.. _ext_commands_api_gears:

Gears
-----

Gear
~~~~

.. attributetable:: stoat.ext.commands.Gear

.. autoclass:: stoat.ext.commands.Gear
    :members:

GearMeta
~~~~~~~~

.. attributetable:: stoat.ext.commands.GearMeta

.. autoclass:: stoat.ext.commands.GearMeta
    :members:

Enums
-----

.. class:: BucketType
    :module: stoat.ext.commands

    Specifies a type of bucket for, e.g. a cooldown.

    .. attribute:: default

        The default bucket operates on a global basis.
    .. attribute:: user

        The user bucket operates on a per-user basis.
    .. attribute:: server

        The server bucket operates on a per-server basis.
    .. attribute:: channel

        The channel bucket operates on a per-channel basis.
    .. attribute:: member

        The member bucket operates on a per-member basis.
    .. attribute:: category

        The category bucket operates on a per-category basis.
    .. attribute:: role

        The role bucket operates on a per-role basis.

.. _ext_commands_api_checks:

Checks
------

.. autofunction:: stoat.ext.commands.check(predicate)
    :decorator:

.. autofunction:: stoat.ext.commands.check_any(*checks)
    :decorator:

.. autofunction:: stoat.ext.commands.has_role(item)
    :decorator:

.. autofunction:: stoat.ext.commands.has_permissions(**perms)
    :decorator:

.. autofunction:: stoat.ext.commands.has_server_permissions(**perms)
    :decorator:

.. autofunction:: stoat.ext.commands.has_any_role(*items)
    :decorator:

.. autofunction:: stoat.ext.commands.bot_has_role(item)
    :decorator:

.. autofunction:: stoat.ext.commands.bot_has_permissions(**perms)
    :decorator:

.. autofunction:: stoat.ext.commands.bot_has_server_permissions(**perms)
    :decorator:

.. autofunction:: stoat.ext.commands.bot_has_any_role(*items)
    :decorator:

.. autofunction:: stoat.ext.commands.cooldown(rate, per, type=stoat.ext.commands.BucketType.default)
    :decorator:

.. autofunction:: stoat.ext.commands.dynamic_cooldown(cooldown, type)
    :decorator:

.. autofunction:: stoat.ext.commands.max_concurrency(number, per=stoat.ext.commands.BucketType.default, *, wait=False)
    :decorator:

.. autofunction:: stoat.ext.commands.before_invoke(coro)
    :decorator:

.. autofunction:: stoat.ext.commands.after_invoke(coro)
    :decorator:

.. autofunction:: stoat.ext.commands.server_only(,)
    :decorator:

.. autofunction:: stoat.ext.commands.dm_only(,)
    :decorator:

.. autofunction:: stoat.ext.commands.is_owner(,)
    :decorator:

.. autofunction:: stoat.ext.commands.is_nsfw(,)
    :decorator:

.. _ext_commands_api_context:

Context
-------

.. attributetable:: stoat.ext.commands.Context

.. autoclass:: stoat.ext.commands.Context
    :members:
    :inherited-members:
    :exclude-members: typing

    .. automethod:: stoat.ext.commands.Context.typing
        :async-with:

.. _ext_commands_api_converters:

Converters
----------

.. attributetable:: stoat.ext.commands.Converter

.. autoclass:: stoat.ext.commands.Converter
    :members:

.. attributetable:: stoat.ext.commands.BaseConverter

.. autoclass:: stoat.ext.commands.BaseConverter
    :members:

.. attributetable:: stoat.ext.commands.MemberConverter

.. autoclass:: stoat.ext.commands.MemberConverter
    :members:

.. attributetable:: stoat.ext.commands.UserConverter

.. autoclass:: stoat.ext.commands.UserConverter
    :members:

.. attributetable:: stoat.ext.commands.MessageConverter

.. autoclass:: stoat.ext.commands.MessageConverter
    :members:

.. attributetable:: stoat.ext.commands.BaseMessageConverter

.. autoclass:: stoat.ext.commands.BaseMessageConverter
    :members:

.. attributetable:: stoat.ext.commands.ServerChannelConverter

.. autoclass:: stoat.ext.commands.ServerChannelConverter
    :members:

.. attributetable:: stoat.ext.commands.TextChannelConverter

.. autoclass:: stoat.ext.commands.TextChannelConverter
    :members:

.. attributetable:: stoat.ext.commands.VoiceChannelConverter

.. autoclass:: stoat.ext.commands.VoiceChannelConverter
    :members:

.. attributetable:: stoat.ext.commands.CategoryConverter

.. autoclass:: stoat.ext.commands.CategoryConverter
    :members:

.. attributetable:: stoat.ext.commands.InviteConverter

.. autoclass:: stoat.ext.commands.InviteConverter
    :members:

.. attributetable:: stoat.ext.commands.ServerConverter

.. autoclass:: stoat.ext.commands.ServerConverter
    :members:

.. attributetable:: stoat.ext.commands.RoleConverter

.. autoclass:: stoat.ext.commands.RoleConverter
    :members:

.. attributetable:: stoat.ext.commands.EmojiConverter

.. autoclass:: stoat.ext.commands.EmojiConverter
    :members:

.. attributetable:: stoat.ext.commands.Greedy

.. autoclass:: stoat.ext.commands.Greedy()

.. autofunction:: stoat.ext.commands.run_converters

Defaults
--------

.. attributetable:: stoat.ext.commands.Parameter

.. autoclass:: stoat.ext.commands.Parameter()
    :members:

.. autofunction:: stoat.ext.commands.parameter

.. autofunction:: stoat.ext.commands.param

.. data:: stoat.ext.commands.Author

    A default :class:`Parameter` which returns the :attr:`~.Context.author` for this context.

.. data:: stoat.ext.commands.CurrentChannel

    A default :class:`Parameter` which returns the :attr:`~.Context.channel` for this context.

.. data:: stoat.ext.commands.CurrentServer

    A default :class:`Parameter` which returns the :attr:`~.Context.server` for this context. This will never be ``None``. If the command is called in a DM context then :exc:`~stoat.ext.commands.NoPrivateMessage` is raised to the error handlers.


.. _ext_commands_api_cooldowns:

Cooldowns
---------

.. attributetable:: stoat.ext.commands.MaxConcurrency

.. autoclass:: stoat.ext.commands.MaxConcurrency
    :members:

.. attributetable:: stoat.ext.commands.Cooldown

.. autoclass:: stoat.ext.commands.Cooldown
    :members:

.. _ext_commands_api_errors:

Exceptions
----------

.. autoexception:: stoat.ext.commands.CommandError
    :members:

.. autoexception:: stoat.ext.commands.ConversionError
    :members:

.. autoexception:: stoat.ext.commands.MissingRequiredArgument
    :members:

.. autoexception:: stoat.ext.commands.MissingRequiredAttachment
    :members:

.. autoexception:: stoat.ext.commands.ArgumentParsingError
    :members:

.. autoexception:: stoat.ext.commands.UnexpectedQuoteError
    :members:

.. autoexception:: stoat.ext.commands.InvalidEndOfQuotedStringError
    :members:

.. autoexception:: stoat.ext.commands.ExpectedClosingQuoteError
    :members:

.. autoexception:: stoat.ext.commands.BadArgument
    :members:

.. autoexception:: stoat.ext.commands.BadUnionArgument
    :members:

.. autoexception:: stoat.ext.commands.BadLiteralArgument
    :members:

.. autoexception:: stoat.ext.commands.PrivateMessageOnly
    :members:

.. autoexception:: stoat.ext.commands.NoPrivateMessage
    :members:

.. autoexception:: stoat.ext.commands.CheckFailure
    :members:

.. autoexception:: stoat.ext.commands.CheckAnyFailure
    :members:

.. autoexception:: stoat.ext.commands.CommandNotFound
    :members:

.. autoexception:: stoat.ext.commands.DisabledCommand
    :members:

.. autoexception:: stoat.ext.commands.CommandInvokeError
    :members:

.. autoexception:: stoat.ext.commands.TooManyArguments
    :members:

.. autoexception:: stoat.ext.commands.UserInputError
    :members:

.. autoexception:: stoat.ext.commands.CommandOnCooldown
    :members:

.. autoexception:: stoat.ext.commands.MaxConcurrencyReached
    :members:

.. autoexception:: stoat.ext.commands.NotOwner
    :members:

.. autoexception:: stoat.ext.commands.MessageNotFound
    :members:

.. autoexception:: stoat.ext.commands.MemberNotFound
    :members:

.. autoexception:: stoat.ext.commands.ServerNotFound
    :members:

.. autoexception:: stoat.ext.commands.UserNotFound
    :members:

.. autoexception:: stoat.ext.commands.ChannelNotFound
    :members:

.. autoexception:: stoat.ext.commands.ChannelNotReadable
    :members:

.. autoexception:: stoat.ext.commands.RoleNotFound
    :members:

.. autoexception:: stoat.ext.commands.BadInviteArgument
    :members:

.. autoexception:: stoat.ext.commands.EmojiNotFound
    :members:

.. autoexception:: stoat.ext.commands.BadBoolArgument
    :members:

.. autoexception:: stoat.ext.commands.RangeError
    :members:

.. autoexception:: stoat.ext.commands.MissingPermissions
    :members:

.. autoexception:: stoat.ext.commands.BotMissingPermissions
    :members:

.. autoexception:: stoat.ext.commands.MissingRole
    :members:

.. autoexception:: stoat.ext.commands.BotMissingRole
    :members:

.. autoexception:: stoat.ext.commands.MissingAnyRole
    :members:

.. autoexception:: stoat.ext.commands.BotMissingAnyRole
    :members:

.. autoexception:: stoat.ext.commands.NSFWChannelRequired
    :members:

.. autoexception:: stoat.ext.commands.ExtensionError
    :members:

.. autoexception:: stoat.ext.commands.ExtensionAlreadyLoaded
    :members:

.. autoexception:: stoat.ext.commands.ExtensionNotLoaded
    :members:

.. autoexception:: stoat.ext.commands.NoEntryPointError
    :members:

.. autoexception:: stoat.ext.commands.ExtensionFailed
    :members:

.. autoexception:: stoat.ext.commands.ExtensionNotFound
    :members:

.. autoexception:: stoat.ext.commands.CommandRegistrationError
    :members:

Exception Hierarchy
~~~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`~.PyvoltException`
        - :exc:`~.commands.CommandError`
            - :exc:`~.commands.ConversionError`
            - :exc:`~.commands.UserInputError`
                - :exc:`~.commands.MissingRequiredArgument`
                - :exc:`~.commands.MissingRequiredAttachment`
                - :exc:`~.commands.TooManyArguments`
                - :exc:`~.commands.BadArgument`
                    - :exc:`~.commands.MessageNotFound`
                    - :exc:`~.commands.MemberNotFound`
                    - :exc:`~.commands.ServerNotFound`
                    - :exc:`~.commands.UserNotFound`
                    - :exc:`~.commands.ChannelNotFound`
                    - :exc:`~.commands.ChannelNotReadable`
                    - :exc:`~.commands.BadColourArgument`
                    - :exc:`~.commands.RoleNotFound`
                    - :exc:`~.commands.BadInviteArgument`
                    - :exc:`~.commands.EmojiNotFound`
                    - :exc:`~.commands.BadBoolArgument`
                    - :exc:`~.commands.RangeError`
                - :exc:`~.commands.BadUnionArgument`
                - :exc:`~.commands.BadLiteralArgument`
                - :exc:`~.commands.ArgumentParsingError`
                    - :exc:`~.commands.UnexpectedQuoteError`
                    - :exc:`~.commands.InvalidEndOfQuotedStringError`
                    - :exc:`~.commands.ExpectedClosingQuoteError`
            - :exc:`~.commands.CommandNotFound`
            - :exc:`~.commands.CheckFailure`
                - :exc:`~.commands.CheckAnyFailure`
                - :exc:`~.commands.PrivateMessageOnly`
                - :exc:`~.commands.NoPrivateMessage`
                - :exc:`~.commands.NotOwner`
                - :exc:`~.commands.MissingPermissions`
                - :exc:`~.commands.BotMissingPermissions`
                - :exc:`~.commands.MissingRole`
                - :exc:`~.commands.BotMissingRole`
                - :exc:`~.commands.MissingAnyRole`
                - :exc:`~.commands.BotMissingAnyRole`
                - :exc:`~.commands.NSFWChannelRequired`
            - :exc:`~.commands.DisabledCommand`
            - :exc:`~.commands.CommandInvokeError`
            - :exc:`~.commands.CommandOnCooldown`
            - :exc:`~.commands.MaxConcurrencyReached`
        - :exc:`~.commands.ExtensionError`
            - :exc:`~.commands.ExtensionAlreadyLoaded`
            - :exc:`~.commands.ExtensionNotLoaded`
            - :exc:`~.commands.NoEntryPointError`
            - :exc:`~.commands.ExtensionFailed`
            - :exc:`~.commands.ExtensionNotFound`
    - :exc:`~.ClientException`
        - :exc:`~.commands.CommandRegistrationError`