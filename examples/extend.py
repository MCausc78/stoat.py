from __future__ import annotations

import typing

from attrs import define, field
import stoat
from stoat.ext import commands

# Of course, that's just a joke and that event (and route) doesn't actually exist. It's here only to illustrate capabilities of stoat.py
# how customizable it is :)


@define(slots=True)
class ReleaseBeesEvent(stoat.ShardEvent):
    """Dispatched when bees are released to an user."""

    by_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID who released bees."""

    user_id: str = field(repr=True, kw_only=True)
    """:class:`str`: The user's ID to release bees for."""


class ClientReleaseBeesEvent(typing.TypedDict):
    type: typing.Literal['ReleaseBees']
    by: str
    user: str


class MyClientEventHandler(stoat.ClientEventHandler):
    __slots__ = ()

    def __init__(self, client: stoat.Client) -> None:
        super().__init__(client)
        self.handlers['ReleaseBees'] = self.handle_release_bees

    def handle_release_bees(self, shard: stoat.Shard, payload: ClientReleaseBeesEvent, /) -> None:
        """Handle ``ReleaseBees`` WebSocket event.

        Parameters
        ----------
        shard: :class:`.Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload.
        """
        parser = self.state.parser
        if isinstance(parser, MyParser):
            event = parser.parse_release_bees_event(shard, payload)
            self.dispatch(event)


class MyParser(stoat.Parser):
    __slots__ = ()

    def parse_release_bees_event(self, shard: stoat.Shard, payload: ClientReleaseBeesEvent, /) -> ReleaseBeesEvent:
        """Parses a ReleaseBees event.

        Parameters
        ----------
        shard: :class:`Shard`
            The shard the event arrived on.
        payload: Dict[:class:`str`, Any]
            The event payload to parse.

        Returns
        -------
        :class:`ReleaseBeesEvent`
            The parsed release bees event object.
        """
        return ReleaseBeesEvent(
            shard=shard,
            by_id=payload['by'],
            user_id=payload['user'],
        )


# A stoat.routes.Route is a template; when you compile it, {user_id} will be replaced by user ID in actual API request
USERS_RELEASE_BEES: typing.Final[stoat.routes.Route] = stoat.routes.Route('POST', '/users/{user_id}/release_bees')

# If you are going to use stoat.Client, the only difference is removal of ``command_prefix``
bot = commands.Bot(
    command_prefix='!',
    # First argument is Client
    parser=lambda _, state, /: MyParser(state=state),
    # Second argument is State
    shard=lambda client, state, /: stoat.ShardImpl(
        token=client.token,
        bot=client.bot,
        handler=MyClientEventHandler(client),
        state=state,
    ),
)


@bot.listen()
async def on_release_bees(event: ReleaseBeesEvent) -> None:
    print('Bees have been released to user with', event.user_id, 'ID!')


@bot.command(name='release-bees')
async def release_bees(ctx: commands.Context[commands.Bot], user: stoat.User) -> None:
    """Release bees at specified user as bot."""

    # To call a route you must compile it.
    route = USERS_RELEASE_BEES.compile(user_id=user.id)
    await ctx.bot.http.request(route)
    await ctx.send(f'Released bees at {user.tag}.')


token = 'token'
bot.run(token)
