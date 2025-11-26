"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

import typing

from stoat import PyvoltException, utils

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from stoat import BaseChannel, Channel, BaseServerChannel, ServerChannel

    from .bot import Bot
    from .context import Context
    from .cooldown import BucketType, Cooldown
    from .converter import Converter
    from .core import Parameter


class CommandError(PyvoltException):
    r"""The base exception type for all command related errors.

    This inherits from :exc:`stoat.PyvoltException`.

    This exception and exceptions inherited from it are handled
    in a special way as they are caught and passed into a special event
    from :class:`.Bot`\, :class:`CommandErrorEvent`.
    """

    __slots__ = ()

    def __init__(self, *args: typing.Any, message: typing.Optional[str] = None) -> None:
        if message is not None:
            super().__init__(message, *args)
        else:
            super().__init__(*args)


class ConversionError(CommandError):
    """Exception raised when a Converter class raises non-CommandError.

    This inherits from :exc:`CommandError`.

    Attributes
    ----------
    converter: :class:`stoat.ext.commands.Converter`
        The converter that failed.
    original: :exc:`Exception`
        The original exception that was raised. You can also get this via
        the ``__cause__`` attribute.
    """

    def __init__(self, *, converter: Converter[typing.Any], original: Exception) -> None:
        self.converter: Converter[typing.Any] = converter
        self.original: Exception = original


class UserInputError(CommandError):
    """The base exception type for errors that involve errors
    regarding user input.

    This inherits from :exc:`.CommandError`.
    """

    __slots__ = ()


class MissingRequiredArgument(UserInputError):
    """Exception raised when parsing a command and a parameter
    that is required is not encountered.

    This inherits from :exc:`.UserInputError`.

    Attributes
    -----------
    parameter: :class:`.Parameter`
        The argument that is missing.
    """

    def __init__(self, *, parameter: Parameter) -> None:
        self.parameter: Parameter = parameter
        super().__init__(f'{parameter.displayed_name or parameter.name} is a required argument that is missing.')


class MissingRequiredAttachment(UserInputError):
    """Exception raised when parsing a command and a parameter
    that requires an attachment is not given.

    This inherits from :exc:`.UserInputError`.

    Attributes
    -----------
    parameter: :class:`.Parameter`
        The argument that is missing an attachment.
    """

    __slots__ = ('parameter',)

    def __init__(self, *, parameter: Parameter) -> None:
        self.parameter: Parameter = parameter
        super().__init__(
            f'{parameter.displayed_name or parameter.name} is a required argument that is missing an attachment.'
        )


class TooManyArguments(UserInputError):
    """Exception raised when the command was passed too many arguments and its
    :attr:`.Command.ignore_extra` attribute was not set to ``True``.

    This inherits from :exc:`.UserInputError`
    """

    __slots__ = ()


class BadArgument(UserInputError):
    """Exception raised when a parsing or conversion failure is encountered
    on an argument to pass into a command.

    This inherits from :exc:`.UserInputError`
    """

    __slots__ = ()


class CheckFailure(CommandError):
    """Exception raised when the predicates in :attr:`.Command.checks` have failed.

    This inherits from :exc:`.CommandError`
    """

    __slots__ = ()


class CheckAnyFailure(CheckFailure):
    """Exception raised when all predicates in :func:`check_any` fail.

    This inherits from :exc:`.CheckFailure`.

    Attributes
    ------------
    errors: List[:class:`.CheckFailure`]
        A list of errors that were caught during execution.
    checks: List[Callable[[:class:`.Context`], :class:`bool`]]
        A list of check predicates that failed.
    """

    __slots__ = (
        'checks',
        'errors',
    )

    def __init__(self, checks: list[Callable[[Context[Bot]], bool]], errors: list[CheckFailure]) -> None:
        self.checks: list[Callable[[Context[Bot]], bool]] = checks
        self.errors: list[CheckFailure] = errors
        super().__init__('You do not have permission to run this command.')


class PrivateMessageOnly(CheckFailure):
    """Exception raised when an operation does not work outside of private
    message contexts.

    This inherits from :exc:`.CheckFailure`.
    """

    __slots__ = ()

    def __init__(self, *, message: typing.Optional[str] = None) -> None:
        super().__init__(message or 'This command can only be used in private messages.')


class NoPrivateMessage(CheckFailure):
    """Exception raised when an operation does not work in private message
    contexts.

    This inherits from :exc:`.CheckFailure`.
    """

    __slots__ = ()

    def __init__(self, *, message: typing.Optional[str] = None) -> None:
        super().__init__(message or 'This command cannot be used in private messages.')


class NotOwner(CheckFailure):
    """Exception raised when the message author is not the owner of the bot.

    This inherits from :exc:`.CheckFailure`.
    """

    __slots__ = ()


class ObjectNotFound(BadArgument):
    """Exception raised when the argument provided did not match the format
    of an ID or a mention.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The argument supplied by the caller that was not matched.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'{argument!r} does not follow a valid ID or mention format.')


class MemberNotFound(BadArgument):
    """Exception raised when the member provided was not found in the bot's
    cache.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The member supplied by the caller that was not found.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'Member "{argument}" not found.')


class ServerNotFound(BadArgument):
    """Exception raised when the server provided was not found in the bot's cache.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The server supplied by the called that was not found.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'Server "{argument}" not found.')


class UserNotFound(BadArgument):
    """Exception raised when the user provided was not found in the bot's
    cache.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The user supplied by the caller that was not found.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'User "{argument}" not found.')


class MessageNotFound(BadArgument):
    """Exception raised when the message provided was not found in the channel.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The message supplied by the caller that was not found.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'Message "{argument}" not found.')


class ChannelIDNotReadable(BadArgument):
    """Exception raised when the bot does not have permission to read messages
    in the channel.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The channel supplied by the caller that was not readable.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f"Can't read messages in <#{argument}>.")


class ChannelNotReadable(BadArgument):
    """Exception raised when the bot does not have permission to read messages
    in the channel.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`.ServerChannel`
        The channel supplied by the caller that was not readable.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: ServerChannel) -> None:
        self.argument: ServerChannel = argument
        super().__init__(f"Can't read messages in {argument.mention}.")


class ChannelNotFound(BadArgument):
    """Exception raised when the bot can not find the channel.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The channel supplied by the caller that was not found.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'Channel "{argument}" not found.')


class InvalidChannelType(BadArgument):
    """Exception raised when the channel is of invalid type.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The channel supplied by the caller that had invalid type.
    channel: :class:`.BaseChannel`
        The channel object supplied by the caller that had invalid type.

    """

    __slots__ = ('argument', 'channel')

    def __init__(self, *, argument: str, channel: BaseChannel) -> None:
        self.argument: str = argument
        self.channel: BaseChannel = channel
        super().__init__(f'Channel "{argument}" has invalid type.')


class ChannelNotInServer(BadArgument):
    """Exception raised when the channel does not belong to the current server.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The channel supplied by the caller that didn't belong to the current server.
    """

    __slots__ = ('argument', 'channel')

    def __init__(self, *, argument: str, channel: BaseServerChannel) -> None:
        self.argument: str = argument
        self.channel: BaseServerChannel = channel
        super().__init__(f'Channel "{argument}" did not belong to the current server.')


class CategoryNotFound(BadArgument):
    """Exception raised when the bot can not find the category.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The category supplied by the caller that was not found.
    """

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'Channel "{argument}" not found.')


class BadColorArgument(BadArgument):
    """Exception raised when the color is not valid.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The color supplied by the caller that was not valid.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'Colour "{argument}" is invalid.')


class RoleNotFound(BadArgument):
    """Exception raised when the bot can not find the role.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The role supplied by the caller that was not found.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'Role "{argument}" not found.')


class BadInviteArgument(BadArgument):
    """Exception raised when the invite is invalid.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The invite supplied by the caller that was not valid.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'Invite "{argument}" is invalid.')


class EmojiNotFound(BadArgument):
    """Exception raised when the bot can not find the emoji.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The emoji supplied by the caller that was not found..
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'Emoji "{argument}" not found.')


# TODO: Investigate if partialemojis will exist in stoat.
# class PartialEmojiConversionFailure(BadArgument):
#     """Exception raised when the emoji provided does not match the correct
#     format.

#     This inherits from :exc:`.BadArgument`.

#     Attributes
#     -----------
#     argument: :class:`str`
#         The emoji supplied by the caller that did not match the regex.
#     """

#     def __init__(self, argument: str) -> None:
#         self.argument: str = argument
#         super().__init__(f'Couldn\'t convert "{argument}" to PartialEmoji.')


class BadBoolArgument(BadArgument):
    """Exception raised when a boolean argument was not convertable.

    This inherits from :exc:`.BadArgument`.

    Attributes
    -----------
    argument: :class:`str`
        The boolean argument supplied by the caller that is not in the predefined list.
    """

    __slots__ = ('argument',)

    def __init__(self, *, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'{argument} is not a recognised boolean option')


class RangeError(BadArgument):
    """Exception raised when an argument is out of range.

    This inherits from :exc:`.BadArgument`

    Attributes
    -----------
    minimum: Optional[Union[:class:`int`, :class:`float`]]
        The minimum value expected or ``None`` if there wasn't one
    maximum: Optional[Union[:class:`int`, :class:`float`]]
        The maximum value expected or ``None`` if there wasn't one
    value: Union[:class:`int`, :class:`float`, :class:`str`]
        The value that was out of range.
    """

    __slots__ = (
        'value',
        'minimum',
        'maximum',
    )

    def __init__(
        self,
        *,
        value: typing.Union[int, float, str],
        minimum: typing.Optional[typing.Union[float, int]],
        maximum: typing.Optional[typing.Union[float, int]],
    ) -> None:
        self.value: typing.Union[int, float, str] = value
        self.minimum: typing.Optional[typing.Union[float, int]] = minimum
        self.maximum: typing.Optional[typing.Union[float, int]] = maximum

        label: str = ''
        if minimum is None and maximum is not None:
            label = f'no more than {maximum}'
        elif minimum is not None and maximum is None:
            label = f'no less than {minimum}'
        elif maximum is not None and minimum is not None:
            label = f'between {minimum} and {maximum}'

        if label and isinstance(value, str):
            label += ' characters'
            count = len(value)
            if count == 1:
                value = '1 character'
            else:
                value = f'{count} characters'

        super().__init__(f'value must be {label} but received {value}')


class DisabledCommand(CommandError):
    """Exception raised when the command being invoked is disabled.

    This inherits from :exc:`.CommandError`.
    """

    __slots__ = ()


class CommandInvokeError(CommandError):
    """Exception raised when the command being invoked raised an exception.

    This inherits from :exc:`.CommandError`.

    Attributes
    -----------
    original: :exc:`Exception`
        The original exception that was raised. You can also get this via
        the ``__cause__`` attribute.
    """

    __slots__ = ('original',)

    def __init__(self, *, original: Exception) -> None:
        self.original: Exception = original
        super().__init__(f'Command raised an exception: {original.__class__.__name__}: {original}')


class CommandOnCooldown(CommandError):
    """Exception raised when the command being invoked is on cooldown.

    This inherits from :exc:`.CommandError`.

    Attributes
    -----------
    cooldown: :class:`~stoat.ext.commands.Cooldown`
        A class with attributes ``rate`` and ``per`` similar to the
        :func:`.cooldown` decorator.
    type: :class:`.BucketType`
        The type associated with the cooldown.
    retry_after: :class:`float`
        The amount of seconds to wait before you can retry again.
    """

    __slots__ = (
        'cooldown',
        'retry_after',
        'type',
    )

    def __init__(self, *, cooldown: Cooldown, retry_after: float, type: BucketType) -> None:
        self.cooldown: Cooldown = cooldown
        self.retry_after: float = retry_after
        self.type: BucketType = type
        super().__init__(f'You are on cooldown. Try again in {retry_after:.2f}s')


class MaxConcurrencyReached(CommandError):
    """Exception raised when the command being invoked has reached its maximum concurrency.

    This inherits from :exc:`.CommandError`.

    Attributes
    ------------
    number: :class:`int`
        The maximum number of concurrent invokers allowed.
    per: :class:`.BucketType`
        The bucket type passed to the :func:`.max_concurrency` decorator.
    """

    __slots__ = (
        'number',
        'per',
    )

    def __init__(self, *, number: int, per: BucketType) -> None:
        self.number: int = number
        self.per: BucketType = per
        name = per.name
        suffix = 'per %s' % name if per.name != 'default' else 'globally'
        plural = '%s times %s' if number > 1 else '%s time %s'
        fmt = plural % (number, suffix)
        super().__init__(f'Too many people are using this command. It can only be used {fmt} concurrently.')


class CommandNotFound(CommandError):
    """Exception raised when a command is attempted to be invoked
    but no command under that name is found.

    This is not raised for invalid subcommands, rather just the
    initial main command that is attempted to be invoked.

    This inherits from :exc:`.CommandError`.
    """

    __slots__ = ()


class MissingRole(CheckFailure):
    """Exception raised when the command invoker lacks a role to run a command.

    This inherits from :exc:`CheckFailure`.

    Attributes
    -----------
    missing_role: :class:`str`
        The required role that is missing.
        This is the parameter passed to :func:`~.commands.has_role`.
    """

    def __init__(self, *, missing_role: str) -> None:
        self.missing_role: str = missing_role
        message = f'Role {missing_role!r} is required to run this command.'
        super().__init__(message)


class BotMissingRole(CheckFailure):
    """Exception raised when the bot's member lacks a role to run a command.

    This inherits from :exc:`CheckFailure`.

    Attributes
    -----------
    missing_role: :class:`str`
        The required role that is missing.
        This is the parameter passed to :func:`~.commands.has_role`.
    """

    def __init__(self, *, missing_role: str) -> None:
        self.missing_role: str = missing_role
        message = f'Bot requires the role {missing_role!r} to run this command'
        super().__init__(message)


class MissingAnyRole(CheckFailure):
    """Exception raised when the command invoker lacks any of
    the roles specified to run a command.

    This inherits from :exc:`CheckFailure`.

    Attributes
    -----------
    missing_roles: List[:class:`str`]
        The roles that the invoker is missing.
        These are the parameters passed to :func:`~.commands.has_any_role`.
    """

    def __init__(self, *, missing_roles: list[str]) -> None:
        self.missing_roles: list[str] = missing_roles

        missing = [f"'{role}'" for role in missing_roles]
        fmt = utils.human_join(missing)
        message = f'You are missing at least one of the required roles: {fmt}'
        super().__init__(message)


class BotMissingAnyRole(CheckFailure):
    """Exception raised when the bot's member lacks any of
    the roles specified to run a command.

    This inherits from :exc:`CheckFailure`.

    Attributes
    -----------
    missing_roles: List[:class:`str`]
        The roles that the bot's member is missing.
        These are the parameters passed to :func:`~.commands.has_any_role`.

    """

    def __init__(self, *, missing_roles: list[str]) -> None:
        self.missing_roles: list[str] = missing_roles

        missing = [f"'{role}'" for role in missing_roles]
        fmt = utils.human_join(missing)
        message = f'Bot is missing at least one of the required roles: {fmt}'
        super().__init__(message)


class NSFWChannelRequired(CheckFailure):
    """Exception raised when a channel does not have the required NSFW setting.

    This inherits from :exc:`CheckFailure`.

    Attributes
    -----------
    channel: :class:`~stoat.Channel`
        The channel that does not have NSFW enabled.
    """

    def __init__(self, *, channel: Channel) -> None:
        self.channel: Channel = channel
        super().__init__(f"Channel '{channel}' needs to be NSFW for this command to work.")


class MissingPermissions(CheckFailure):
    """Exception raised when the command invoker lacks permissions to run a
    command.

    This inherits from :exc:`CheckFailure`.

    Attributes
    -----------
    missing_permissions: List[:class:`str`]
        The required permissions that are missing.
    """

    def __init__(self, /, *args: typing.Any, missing_permissions: list[str]) -> None:
        self.missing_permissions: list[str] = missing_permissions

        missing = [perm.replace('_', ' ').title() for perm in missing_permissions]
        fmt = utils.human_join(missing, final='and')
        message = f'You are missing {fmt} permission(s) to run this command.'
        super().__init__(message, *args)


class BotMissingPermissions(CheckFailure):
    """Exception raised when the bot's member lacks permissions to run a
    command.

    This inherits from :exc:`CheckFailure`.

    Attributes
    -----------
    missing_permissions: List[:class:`str`]
        The required permissions that are missing.
    """

    def __init__(self, /, *args: typing.Any, missing_permissions: list[str]) -> None:
        self.missing_permissions: list[str] = missing_permissions

        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in missing_permissions]

        fmt = utils.human_join(missing, final='and')
        message = f'Bot requires {fmt} permission(s) to run this command.'
        super().__init__(message, *args)


class BadUnionArgument(UserInputError):
    """Exception raised when a :data:`typing.Union` converter fails for all
    its associated types.

    This inherits from :exc:`.UserInputError`.

    Attributes
    -----------
    param: :class:`inspect.Parameter`
        The parameter that failed being converted.
    converters: Tuple[Type, ``...``]
        A tuple of converters attempted in conversion, in order of failure.
    errors: List[:class:`.CommandError`]
        A list of errors that were caught from failing the conversion.
    """

    __slots__ = (
        'param',
        'converters',
        'errors',
    )

    def __init__(self, *, param: Parameter, converters: tuple[type, ...], errors: list[CommandError]) -> None:
        self.param: Parameter = param
        self.converters: tuple[type, ...] = converters
        self.errors: list[CommandError] = errors

        def _get_name(x, /):
            try:
                return x.__name__
            except AttributeError:
                if hasattr(x, '__origin__'):
                    return repr(x)
                return x.__class__.__name__

        fmt = utils.human_join(list(map(_get_name, converters)))
        super().__init__(f'Could not convert "{param.displayed_name or param.name}" into {fmt}.')


class BadLiteralArgument(UserInputError):
    """Exception raised when a :data:`typing.Literal` converter fails for all
    its associated values.

    This inherits from :exc:`.UserInputError`.

    Attributes
    -----------
    param: :class:`inspect.Parameter`
        The parameter that failed being converted.
    literals: Tuple[Any, ``...``]
        A tuple of values compared against in conversion, in order of failure.
    errors: List[:class:`.CommandError`]
        A list of errors that were caught from failing the conversion.
    argument: :class:`str`
        The argument's value that failed to be converted. Defaults to an empty string.
    """

    __slots__ = (
        'param',
        'literals',
        'errors',
        'argument',
    )

    def __init__(
        self, *, param: Parameter, literals: tuple[typing.Any, ...], errors: list[CommandError], argument: str = ''
    ) -> None:
        self.param: Parameter = param
        self.literals: tuple[typing.Any, ...] = literals
        self.errors: list[CommandError] = errors
        self.argument: str = argument

        fmt = utils.human_join(list(map(repr, literals)))
        super().__init__(f'Could not convert "{param.displayed_name or param.name}" into the literal {fmt}.')


class ArgumentParsingError(UserInputError):
    """An exception raised when the parser fails to parse an user's input.

    This inherits from :exc:`.UserInputError`.

    There are child classes that implement more granular parsing errors for
    i18n purposes.
    """

    __slots__ = ()


class UnexpectedQuoteError(ArgumentParsingError):
    """An exception raised when the parser encounters a quote mark inside a non-quoted string.

    This inherits from :exc:`.ArgumentParsingError`.

    Attributes
    ------------
    quote: :class:`str`
        The quote mark that was found inside the non-quoted string.
    """

    __slots__ = ('quote',)

    def __init__(self, *, quote: str) -> None:
        self.quote: str = quote
        super().__init__(f'Unexpected quote mark, {quote!r}, in non-quoted string')


class InvalidEndOfQuotedStringError(ArgumentParsingError):
    """An exception raised when a space is expected after the closing quote in a string
    but a different character is found.

    This inherits from :exc:`.ArgumentParsingError`.

    Attributes
    -----------
    received: :class:`str`
        The character found instead of the expected string.
    """

    __slots__ = ('received',)

    def __init__(self, *, received: str) -> None:
        self.received: str = received
        super().__init__(f'Expected space after closing quotation but received {received!r}')


class ExpectedClosingQuoteError(ArgumentParsingError):
    """An exception raised when a quote character is expected but not found.

    This inherits from :exc:`.ArgumentParsingError`.

    Attributes
    -----------
    close_quote: :class:`str`
        The quote character expected.
    """

    __slots__ = ('close_quote',)

    def __init__(self, *, close_quote: str) -> None:
        self.close_quote: str = close_quote
        super().__init__(f'Expected closing {close_quote}.')


class ExtensionError(PyvoltException):
    """Base exception for extension related errors.

    This inherits from :exc:`~stoat.DiscordException`.

    Attributes
    ------------
    name: :class:`str`
        The extension that had an error.
    """

    __slots__ = ('name',)

    def __init__(self, /, *args: typing.Any, message: typing.Optional[str] = None, name: str) -> None:
        self.name: str = name
        message = f'Extension {name!r} had an error.' if message is None else message
        # clean-up @everyone and @online mentions
        m = message.replace('@everyone', '@\u200beveryone').replace('@online', '@\u200bonline')
        super().__init__(m, *args)


class ExtensionAlreadyLoaded(ExtensionError):
    """An exception raised when an extension has already been loaded.

    This inherits from :exc:`.ExtensionError`.
    """

    __slots__ = ()

    def __init__(self, *, name: str) -> None:
        super().__init__(f'Extension {name!r} is already loaded.', name=name)


class ExtensionNotLoaded(ExtensionError):
    """An exception raised when an extension was not loaded.

    This inherits from :exc:`.ExtensionError`.
    """

    __slots__ = ()

    def __init__(self, *, name: str) -> None:
        super().__init__(f'Extension {name!r} has not been loaded.', name=name)


class NoEntryPointError(ExtensionError):
    """An exception raised when an extension does not have a ``setup`` entry point function.

    This inherits from :exc:`.ExtensionError`.
    """

    __slots__ = ()

    def __init__(self, *, name: str) -> None:
        super().__init__(f"Extension {name!r} has no 'setup' function.", name=name)


class ExtensionFailed(ExtensionError):
    """An exception raised when an extension failed to load during execution of the module or ``setup`` entry point.

    This inherits from :exc:`.ExtensionError`.

    Attributes
    -----------
    name: :class:`str`
        The extension that had the error.
    original: :exc:`Exception`
        The original exception that was raised. You can also get this via
        the ``__cause__`` attribute.
    """

    __slots__ = ()

    def __init__(self, *, name: str, original: Exception) -> None:
        self.original: Exception = original
        msg = f'Extension {name!r} raised an error: {original.__class__.__name__}: {original}'
        super().__init__(msg, name=name)


class ExtensionNotFound(ExtensionError):
    """An exception raised when an extension is not found.

    This inherits from :exc:`.ExtensionError`.

    Attributes
    -----------
    name: :class:`str`
        The extension that had the error.
    """

    __slots__ = ()

    def __init__(self, *, name: str) -> None:
        msg = f'Extension {name!r} could not be loaded or found.'
        super().__init__(msg, name=name)


class CommandRegistrationError(PyvoltException):
    """An exception raised when the command can't be added
    because the name is already taken by a different command.

    This inherits from :exc:`stoat.PyvoltException`.

    Attributes
    ----------
    name: :class:`str`
        The command name that had the error.
    alias_conflict: :class:`bool`
        Whether the name that conflicts is an alias of the command we try to add.
    """

    __slots__ = (
        'name',
        'alias_conflict',
    )

    def __init__(self, *, name: str, alias_conflict: bool = False) -> None:
        self.name: str = name
        self.alias_conflict: bool = alias_conflict
        type_ = 'alias' if alias_conflict else 'command'
        super().__init__(f'The {type_} {name} is already an existing command or alias.')


__all__ = (
    'CommandError',
    'ConversionError',
    'UserInputError',
    'MissingRequiredArgument',
    'MissingRequiredAttachment',
    'TooManyArguments',
    'BadArgument',
    'CheckFailure',
    'CheckAnyFailure',
    'PrivateMessageOnly',
    'NoPrivateMessage',
    'NotOwner',
    'ObjectNotFound',
    'MemberNotFound',
    'ServerNotFound',
    'UserNotFound',
    'MessageNotFound',
    'ChannelIDNotReadable',
    'ChannelNotReadable',
    'ChannelNotFound',
    'InvalidChannelType',
    'ChannelNotInServer',
    'CategoryNotFound',
    'BadColorArgument',
    'RoleNotFound',
    'BadInviteArgument',
    'EmojiNotFound',
    # 'PartialEmojiConversionFailure',
    'BadBoolArgument',
    'RangeError',
    'DisabledCommand',
    'CommandInvokeError',
    'CommandOnCooldown',
    'MaxConcurrencyReached',
    'CommandNotFound',
    'MissingRole',
    'BotMissingRole',
    'MissingAnyRole',
    'BotMissingAnyRole',
    'NSFWChannelRequired',
    'MissingPermissions',
    'BotMissingPermissions',
    'BadUnionArgument',
    'BadLiteralArgument',
    'ArgumentParsingError',
    'UnexpectedQuoteError',
    'InvalidEndOfQuotedStringError',
    'ExpectedClosingQuoteError',
    'ExtensionError',
    'ExtensionAlreadyLoaded',
    'ExtensionNotLoaded',
    'NoEntryPointError',
    'ExtensionFailed',
    'ExtensionNotFound',
    'CommandRegistrationError',
)
