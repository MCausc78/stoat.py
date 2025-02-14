.. currentmodule:: pyvolt

API Reference
===============

The following section outlines the API of pyvolt's command extension module.

.. _ext_commands_api_bot:

Bots
----

Bot
~~~

.. attributetable:: pyvolt.ext.commands.Bot

.. autoclass:: pyvolt.ext.commands.Bot
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

.. autofunction:: pyvolt.ext.commands.when_mentioned

.. autofunction:: pyvolt.ext.commands.when_mentioned_or

.. _ext_commands_api_events:

Event Reference
---------------

CommandErrorEvent
~~~~~~~~~~~~~~~~~

.. attributetable:: CommandErrorEvent

.. autoclass:: CommandErrorEvent
    :members:
    :inherited-members:

CommandEvent
~~~~~~~~~~~~

.. attributetable:: CommandEvent

.. autoclass:: CommandEvent
    :members:
    :inherited-members:

CommandCompletionEvent
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: CommandCompletionEvent

.. autoclass:: CommandCompletionEvent
    :members:
    :inherited-members:

.. _ext_commands_api_command:

Commands
--------

Decorators
~~~~~~~~~~

.. autofunction:: pyvolt.ext.commands.command
    :decorator:

.. autofunction:: pyvolt.ext.commands.group
    :decorator:

.. autofunction:: pyvolt.ext.commands.hybrid_command
    :decorator:

.. autofunction:: pyvolt.ext.commands.hybrid_group
    :decorator:


Command
~~~~~~~

.. attributetable:: pyvolt.ext.commands.Command

.. autoclass:: pyvolt.ext.commands.Command
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

.. attributetable:: pyvolt.ext.commands.Group

.. autoclass:: pyvolt.ext.commands.Group
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

.. attributetable:: pyvolt.ext.commands.GroupMixin

.. autoclass:: pyvolt.ext.commands.GroupMixin
    :members:
    :exclude-members: command, group

    .. automethod:: GroupMixin.command(*args, **kwargs)
        :decorator:

    .. automethod:: GroupMixin.group(*args, **kwargs)
        :decorator:

HybridCommand
~~~~~~~~~~~~~

.. attributetable:: pyvolt.ext.commands.HybridCommand

.. autoclass:: pyvolt.ext.commands.HybridCommand
    :members:
    :special-members: __call__
    :exclude-members: after_invoke, autocomplete, before_invoke, error

    .. automethod:: HybridCommand.after_invoke()
        :decorator:

    .. automethod:: HybridCommand.autocomplete(name)
        :decorator:

    .. automethod:: HybridCommand.before_invoke()
        :decorator:

    .. automethod:: HybridCommand.error()
        :decorator:

HybridGroup
~~~~~~~~~~~~

.. attributetable:: pyvolt.ext.commands.HybridGroup

.. autoclass:: pyvolt.ext.commands.HybridGroup
    :members:
    :inherited-members:
    :exclude-members: after_invoke, autocomplete, before_invoke, command, error, group

    .. automethod:: HybridGroup.after_invoke()
        :decorator:

    .. automethod:: HybridGroup.autocomplete(name)
        :decorator:

    .. automethod:: HybridGroup.before_invoke()
        :decorator:

    .. automethod:: HybridGroup.command(*args, **kwargs)
        :decorator:

    .. automethod:: HybridGroup.error()
        :decorator:

    .. automethod:: HybridGroup.group(*args, **kwargs)
        :decorator:


.. _ext_commands_api_gears:

Gears
-----

Gear
~~~~

.. attributetable:: pyvolt.ext.commands.Gear

.. autoclass:: pyvolt.ext.commands.Gear
    :members:

GearMeta
~~~~~~~~

.. attributetable:: pyvolt.ext.commands.GearMeta

.. autoclass:: pyvolt.ext.commands.GearMeta
    :members:

Enums
-----

.. class:: BucketType
    :module: pyvolt.ext.commands

    Specifies a type of bucket for, e.g. a cooldown.

    .. attribute:: default

        The default bucket operates on a global basis.
    .. attribute:: user

        The user bucket operates on a per-user basis.
    .. attribute:: guild

        The guild bucket operates on a per-guild basis.
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
-------

.. autofunction:: pyvolt.ext.commands.check(predicate)
    :decorator:

.. autofunction:: pyvolt.ext.commands.check_any(*checks)
    :decorator:

.. autofunction:: pyvolt.ext.commands.has_role(item)
    :decorator:

.. autofunction:: pyvolt.ext.commands.has_permissions(**perms)
    :decorator:

.. autofunction:: pyvolt.ext.commands.has_guild_permissions(**perms)
    :decorator:

.. autofunction:: pyvolt.ext.commands.has_any_role(*items)
    :decorator:

.. autofunction:: pyvolt.ext.commands.bot_has_role(item)
    :decorator:

.. autofunction:: pyvolt.ext.commands.bot_has_permissions(**perms)
    :decorator:

.. autofunction:: pyvolt.ext.commands.bot_has_guild_permissions(**perms)
    :decorator:

.. autofunction:: pyvolt.ext.commands.bot_has_any_role(*items)
    :decorator:

.. autofunction:: pyvolt.ext.commands.cooldown(rate, per, type=pyvolt.ext.commands.BucketType.default)
    :decorator:

.. autofunction:: pyvolt.ext.commands.dynamic_cooldown(cooldown, type)
    :decorator:

.. autofunction:: pyvolt.ext.commands.max_concurrency(number, per=pyvolt.ext.commands.BucketType.default, *, wait=False)
    :decorator:

.. autofunction:: pyvolt.ext.commands.before_invoke(coro)
    :decorator:

.. autofunction:: pyvolt.ext.commands.after_invoke(coro)
    :decorator:

.. autofunction:: pyvolt.ext.commands.guild_only(,)
    :decorator:

.. autofunction:: pyvolt.ext.commands.dm_only(,)
    :decorator:

.. autofunction:: pyvolt.ext.commands.is_owner(,)
    :decorator:

.. autofunction:: pyvolt.ext.commands.is_nsfw(,)
    :decorator:

.. _ext_commands_api_context:

Context
-------

.. attributetable:: pyvolt.ext.commands.Context

.. autoclass:: pyvolt.ext.commands.Context
    :members:
    :inherited-members:
    :exclude-members: typing

    .. automethod:: pyvolt.ext.commands.Context.typing
        :async-with:

.. _ext_commands_api_converters:

Converters
----------

.. attributetable:: pyvolt.ext.commands.Converter

.. autoclass:: pyvolt.ext.commands.Converter
    :members:

.. attributetable:: pyvolt.ext.commands.ObjectConverter

.. autoclass:: pyvolt.ext.commands.ObjectConverter
    :members:

.. attributetable:: pyvolt.ext.commands.MemberConverter

.. autoclass:: pyvolt.ext.commands.MemberConverter
    :members:

.. attributetable:: pyvolt.ext.commands.UserConverter

.. autoclass:: pyvolt.ext.commands.UserConverter
    :members:

.. attributetable:: pyvolt.ext.commands.MessageConverter

.. autoclass:: pyvolt.ext.commands.MessageConverter
    :members:

.. attributetable:: pyvolt.ext.commands.PartialMessageConverter

.. autoclass:: pyvolt.ext.commands.PartialMessageConverter
    :members:

.. attributetable:: pyvolt.ext.commands.ServerChannelConverter

.. autoclass:: pyvolt.ext.commands.ServerChannelConverter
    :members:

.. attributetable:: pyvolt.ext.commands.TextChannelConverter

.. autoclass:: pyvolt.ext.commands.TextChannelConverter
    :members:

.. attributetable:: pyvolt.ext.commands.VoiceChannelConverter

.. autoclass:: pyvolt.ext.commands.VoiceChannelConverter
    :members:

.. attributetable:: pyvolt.ext.commands.CategoryConverter

.. autoclass:: pyvolt.ext.commands.CategoryConverter
    :members:

.. attributetable:: pyvolt.ext.commands.InviteConverter

.. autoclass:: pyvolt.ext.commands.InviteConverter
    :members:

.. attributetable:: pyvolt.ext.commands.ServerConverter

.. autoclass:: pyvolt.ext.commands.ServerConverter
    :members:

.. attributetable:: pyvolt.ext.commands.RoleConverter

.. autoclass:: pyvolt.ext.commands.RoleConverter
    :members:

.. attributetable:: pyvolt.ext.commands.EmojiConverter

.. autoclass:: pyvolt.ext.commands.EmojiConverter
    :members:

.. attributetable:: pyvolt.ext.commands.Greedy

.. autoclass:: pyvolt.ext.commands.Greedy()

.. autofunction:: pyvolt.ext.commands.run_converters

Defaults
--------

.. attributetable:: pyvolt.ext.commands.Parameter

.. autoclass:: pyvolt.ext.commands.Parameter()
    :members:

.. autofunction:: pyvolt.ext.commands.parameter

.. autofunction:: pyvolt.ext.commands.param

.. data:: pyvolt.ext.commands.Author

    A default :class:`Parameter` which returns the :attr:`~.Context.author` for this context.

.. data:: pyvolt.ext.commands.CurrentChannel

    A default :class:`Parameter` which returns the :attr:`~.Context.channel` for this context.

.. data:: pyvolt.ext.commands.CurrentServer

    A default :class:`Parameter` which returns the :attr:`~.Context.server` for this context. This will never be ``None``. If the command is called in a DM context then :exc:`~pyvolt.ext.commands.NoPrivateMessage` is raised to the error handlers.


.. _ext_commands_api_errors:

Exceptions
-----------

.. autoexception:: pyvolt.ext.commands.CommandError
    :members:

.. autoexception:: pyvolt.ext.commands.ConversionError
    :members:

.. autoexception:: pyvolt.ext.commands.MissingRequiredArgument
    :members:

.. autoexception:: pyvolt.ext.commands.MissingRequiredAttachment
    :members:

.. autoexception:: pyvolt.ext.commands.ArgumentParsingError
    :members:

.. autoexception:: pyvolt.ext.commands.UnexpectedQuoteError
    :members:

.. autoexception:: pyvolt.ext.commands.InvalidEndOfQuotedStringError
    :members:

.. autoexception:: pyvolt.ext.commands.ExpectedClosingQuoteError
    :members:

.. autoexception:: pyvolt.ext.commands.BadArgument
    :members:

.. autoexception:: pyvolt.ext.commands.BadUnionArgument
    :members:

.. autoexception:: pyvolt.ext.commands.BadLiteralArgument
    :members:

.. autoexception:: pyvolt.ext.commands.PrivateMessageOnly
    :members:

.. autoexception:: pyvolt.ext.commands.NoPrivateMessage
    :members:

.. autoexception:: pyvolt.ext.commands.CheckFailure
    :members:

.. autoexception:: pyvolt.ext.commands.CheckAnyFailure
    :members:

.. autoexception:: pyvolt.ext.commands.CommandNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.DisabledCommand
    :members:

.. autoexception:: pyvolt.ext.commands.CommandInvokeError
    :members:

.. autoexception:: pyvolt.ext.commands.TooManyArguments
    :members:

.. autoexception:: pyvolt.ext.commands.UserInputError
    :members:

.. autoexception:: pyvolt.ext.commands.CommandOnCooldown
    :members:

.. autoexception:: pyvolt.ext.commands.MaxConcurrencyReached
    :members:

.. autoexception:: pyvolt.ext.commands.NotOwner
    :members:

.. autoexception:: pyvolt.ext.commands.MessageNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.MemberNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.GuildNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.UserNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.ChannelNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.ChannelNotReadable
    :members:

.. autoexception:: pyvolt.ext.commands.ThreadNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.BadColourArgument
    :members:

.. autoexception:: pyvolt.ext.commands.RoleNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.BadInviteArgument
    :members:

.. autoexception:: pyvolt.ext.commands.EmojiNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.PartialEmojiConversionFailure
    :members:

.. autoexception:: pyvolt.ext.commands.GuildStickerNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.ScheduledEventNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.SoundboardSoundNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.BadBoolArgument
    :members:

.. autoexception:: pyvolt.ext.commands.RangeError
    :members:

.. autoexception:: pyvolt.ext.commands.MissingPermissions
    :members:

.. autoexception:: pyvolt.ext.commands.BotMissingPermissions
    :members:

.. autoexception:: pyvolt.ext.commands.MissingRole
    :members:

.. autoexception:: pyvolt.ext.commands.BotMissingRole
    :members:

.. autoexception:: pyvolt.ext.commands.MissingAnyRole
    :members:

.. autoexception:: pyvolt.ext.commands.BotMissingAnyRole
    :members:

.. autoexception:: pyvolt.ext.commands.NSFWChannelRequired
    :members:

.. autoexception:: pyvolt.ext.commands.FlagError
    :members:

.. autoexception:: pyvolt.ext.commands.BadFlagArgument
    :members:

.. autoexception:: pyvolt.ext.commands.MissingFlagArgument
    :members:

.. autoexception:: pyvolt.ext.commands.TooManyFlags
    :members:

.. autoexception:: pyvolt.ext.commands.MissingRequiredFlag
    :members:

.. autoexception:: pyvolt.ext.commands.ExtensionError
    :members:

.. autoexception:: pyvolt.ext.commands.ExtensionAlreadyLoaded
    :members:

.. autoexception:: pyvolt.ext.commands.ExtensionNotLoaded
    :members:

.. autoexception:: pyvolt.ext.commands.NoEntryPointError
    :members:

.. autoexception:: pyvolt.ext.commands.ExtensionFailed
    :members:

.. autoexception:: pyvolt.ext.commands.ExtensionNotFound
    :members:

.. autoexception:: pyvolt.ext.commands.CommandRegistrationError
    :members:

.. autoexception:: pyvolt.ext.commands.HybridCommandError
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
            - :exc:`~.commands.HybridCommandError`
        - :exc:`~.commands.ExtensionError`
            - :exc:`~.commands.ExtensionAlreadyLoaded`
            - :exc:`~.commands.ExtensionNotLoaded`
            - :exc:`~.commands.NoEntryPointError`
            - :exc:`~.commands.ExtensionFailed`
            - :exc:`~.commands.ExtensionNotFound`
    - :exc:`~.ClientException`
        - :exc:`~.commands.CommandRegistrationError`