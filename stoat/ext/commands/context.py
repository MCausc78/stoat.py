"""
The MIT License (MIT)

Copyright (c) 2024-present MCausc78

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

import stoat
import typing

from ._types import BotT

if typing.TYPE_CHECKING:
    from .core import Command
    from .gear import Gear
    from .parameters import Parameter
    from .view import StringView


class Context(typing.Generic[BotT], stoat.abc.Messageable):
    r"""A invoking context for commands.

    These are not created manually, instead they are created via :meth:`Bot.get_context` method.

    Attributes
    -----------
    author: Union[:class:`~stoat.Member`, :class:`~stoat.User`]
        The user who created this context.
    author_id: :class:`str`
        The user's ID who created this context.
    bot: :class:`.Bot`
        The bot in this context.
    channel: Union[:class:`~stoat.TextableChannel`, :class:`~stoat.PartialMessageable`]
        The channel the context was created in.
    command: Optional[:class:`.Command`]
        The command used in this context.
    command_failed: :class:`bool`
        Whether invoking the command failed.
    label: :class:`str`
        The substring used to invoke the command. May be empty sometimes.
    me: Union[:class:`~stoat.Member`, :class:`~stoat.OwnUser`]
        The bot user in this context.
    message: :class:`~stoat.Message`
        The message that caused this context to be created.
    prefix: :class:`str`
        The prefix used to invoke command. May be empty sometimes.
    server: Optional[:class:`~stoat.Server`]
        The server this command invoked in.
    shard: :class:`~stoat.Shard`
        The shard the context was created on.
    view: :class:`.StringView`
        The string view, used to parse command parameters.
    """

    __slots__ = (
        'args',
        '_author',
        'author_id',
        'bot',
        'channel',
        'command',
        'command_failed',
        'current_argument',
        'current_parameter',
        'event',
        'kwargs',
        'invoked_parents',
        'invoked_subcommand',
        'label',
        'me',
        'message',
        'prefix',
        'server',
        'shard',
        'subcommand_passed',
        'view',
    )

    def __init__(
        self,
        *,
        args: typing.Optional[list[typing.Any]] = None,
        bot: BotT,
        command: typing.Optional[Command[typing.Any, ..., typing.Any]] = None,
        command_failed: bool = False,
        current_argument: typing.Optional[str] = None,
        current_parameter: typing.Optional[Parameter] = None,
        event: typing.Optional[stoat.MessageCreateEvent] = None,
        kwargs: typing.Optional[dict[str, typing.Any]] = None,
        invoked_parents: typing.Optional[list[str]] = None,
        invoked_subcommand: typing.Optional[Command[typing.Any, ..., typing.Any]] = None,
        label: str = '',
        message: stoat.Message,
        shard: stoat.Shard,
        subcommand_passed: typing.Optional[str] = None,
        view: StringView,
    ) -> None:
        channel = message.channel
        me: stoat.OwnUser = bot.me  # type: ignore
        server = getattr(channel, 'server', None)

        if args is None:
            args = []

        if kwargs is None:
            kwargs = {}

        if invoked_parents is None:
            invoked_parents = []

        self.args: list[typing.Any] = args
        self._author: typing.Optional[typing.Union[stoat.Member, stoat.User]] = message.get_author()
        self.author_id: str = message.author_id
        self.bot: BotT = bot
        self.channel: typing.Union[stoat.TextableChannel, stoat.PartialMessageable] = channel
        self.command: typing.Optional[Command[typing.Any, ..., typing.Any]] = command
        self.command_failed: bool = command_failed
        self.current_argument: typing.Optional[str] = current_argument
        self.current_parameter: typing.Optional[Parameter] = current_parameter
        self.event: typing.Optional[stoat.MessageCreateEvent] = event
        self.invoked_parents: list[str] = invoked_parents
        self.invoked_subcommand: typing.Optional[Command[typing.Any, ..., typing.Any]] = invoked_subcommand
        self.label: str = label
        self.me: typing.Union[stoat.Member, stoat.OwnUser] = server.get_member(me.id) or me if server else me
        self.message: stoat.Message = message
        self.prefix: str = ''
        self.server: typing.Optional[stoat.Server] = server
        self.shard: stoat.Shard = shard
        self.subcommand_passed: typing.Optional[str] = subcommand_passed
        self.view: StringView = view

    def _get_state(self) -> stoat.State:
        return self.bot.state

    @property
    def author(self) -> typing.Union[stoat.Member, stoat.User]:
        if self._author is None:
            raise stoat.NoData(self.author_id, 'message author')
        return self._author

    @property
    def channel_id(self) -> str:
        return self.channel.id

    @property
    def gear(self) -> typing.Optional[Gear]:
        """Optional[:class:`.Gear`]: Returns the gear associated with this context's command. None if it does not exist."""

        if self.command is None:
            return None
        return self.command.gear

    def get_author(self) -> typing.Optional[typing.Union[stoat.Member, stoat.User]]:
        return self._author

    def get_channel_id(self) -> str:
        return self.channel.id


__all__ = ('Context',)
