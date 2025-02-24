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

import typing

from pyvolt import BaseFlags, Forbidden, ReadyEvent, ServerCreateEvent, ServerMemberJoinEvent, doc_flags, flag

if typing.TYPE_CHECKING:
    from typing_extensions import Self

    from pyvolt import (
        Client,
        BaseCacheContext,
        MemberList,
        Server,
    )


@doc_flags('Wraps up a member chunker flag value.')
class MemberChunkerFlags(BaseFlags):
    __slots__ = ()

    @classmethod
    def default(cls) -> Self:
        return cls(
            subscribe_to_events=True,
        )

    @flag()
    def subscribe_to_ready(self) -> int:
        return 1 << 0

    @flag()
    def subscribe_to_server_create(self) -> int:
        return 1 << 1

    @flag()
    def subscribe_to_server_member_join(self) -> int:
        return 1 << 2

    @flag()
    def subscribe_to_events(self) -> int:
        return (1 << 0) | (1 << 1) | (1 << 2)


class MemberChunker:
    """Represents a member chunker."""

    __slots__ = (
        'client',
        'flags',
        'priorities',
    )

    def __init__(
        self,
        client: Client,
        *,
        flags: typing.Optional[MemberChunkerFlags] = None,
        priorities: typing.Optional[dict[str, int]] = None,
    ) -> None:
        if flags is None:
            flags = MemberChunkerFlags.default()

        if priorities is None:
            priorities = {}

        self.client: Client = client
        self.flags: MemberChunkerFlags = flags
        self.priorities: dict[str, int] = priorities

        if self.flags.subscribe_to_ready:
            client.subscribe(ReadyEvent, self.process_ready)

        if self.flags.subscribe_to_server_create:
            client.subscribe(ServerCreateEvent, self.process_server_create)

        if self.flags.subscribe_to_server_member_join:
            client.subscribe(ServerMemberJoinEvent, self.process_server_member_join)

    async def process_ready(self, event: ReadyEvent, /) -> None:
        """Process a :class:`.ReadyEvent`.

        Parameters
        ----------
        event: :class:`.ReadyEvent`
            The event to process.
        """
        pass

    async def process_server_create(self, event: ServerCreateEvent, /) -> None:
        """Process a :class:`.ServerCreateEvent`.

        Parameters
        ----------
        event: :class:`.ServerCreateEvent`
            The event to process.
        """
        await self.chunk(event.server, event.cache_context)

    async def process_server_member_join(self, event: ServerMemberJoinEvent, /) -> None:
        """Process a :class:`.ServerMemberJoinEvent`.

        Parameters
        ----------
        event: :class:`.ServerMemberJoinEvent`
            The event to process.
        """
        state = event.shard.state
        cache = state.cache

        if cache is None:
            # Do not bother fetching user
            return

        cache_context = event.cache_context
        user_id = event.member.id

        if cache.get_user(user_id, cache_context) is None:
            http = state.http

            try:
                user = await http.get_user(user_id)
            except Forbidden:
                # User blocked us; cache might be outdated.
                pass
            else:
                cache.store_user(user, cache_context)

    async def chunk(self, server: Server, cache_context: BaseCacheContext, /) -> MemberList:
        """Chunks a server.

        Parameters
        ----------
        server: :class:`~pyvolt.Server`
            The server to chunk.
        cache_context: :class:`~pyvolt.BaseCacheContext`
            The cache context.

        Returns
        -------
        :class:`~pyvolt.MemberList`
            The member list.
        """
        state = server.state

        http = state.http
        cache = state.cache

        if cache is None:
            raise TypeError('Cannot chunk without cache.')

        data = await http.get_member_list(server.id, exclude_offline=False)

        users = {user.id: user for user in data.users}
        members = {member.id: member for member in data.members}

        cache.bulk_store_server_members(server.id, members, cache_context)
        cache.bulk_store_users(users, cache_context)

        return data
