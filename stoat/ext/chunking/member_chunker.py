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

import asyncio
import typing

from stoat import (
    BaseFlags,
    Forbidden,
    ReadyEvent,
    ServerCreateEvent,
    ServerDeleteEvent,
    ServerMemberJoinEvent,
    ServerMemberRemoveEvent,
    doc_flags,
    flag,
)

if typing.TYPE_CHECKING:
    from typing_extensions import Self

    from stoat import (
        BaseCacheContext,
        Cache,
        Client,
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
        """:class:`bool`: Whether to auto subscribe to :class:`~stoat.ReadyEvent`."""
        return 1 << 0

    @flag()
    def subscribe_to_server_create(self) -> int:
        """:class:`bool`: Whether to auto subscribe to :class:`~stoat.ServerCreateEvent`."""
        return 1 << 1

    @flag()
    def subscribe_to_server_delete(self) -> int:
        """:class:`bool`: Whether to auto subscribe to :class:`~stoat.ServerDeleteEvent`."""
        return 1 << 2

    @flag()
    def subscribe_to_server_member_join(self) -> int:
        """:class:`bool`: Whether to auto subscribe to :class:`~stoat.ServerMemberJoinEvent`."""
        return 1 << 3

    @flag()
    def subscribe_to_server_member_remove(self) -> int:
        """:class:`bool`: Whether to auto subscribe to :class:`~stoat.ServerMemberRemoveEvent`."""
        return 1 << 4

    @flag()
    def subscribe_to_events(self) -> int:
        """:class:`bool`: Whether to auto subscribe to :class:`~stoat.ReadyEvent`, :class:`~stoat.ServerCreateEvent`, :class:`~stoat.ServerDeleteEvent`, :class:`~stoat.ServerMemberJoinEvent` and :class:`~stoat.ServerMemberRemoveEvent`."""
        return (1 << 0) | (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4)

    @flag()
    def chunk_only_servers(self) -> int:
        """:class:`bool`: Whether to chunk only provided servers in constructor, not exclude them."""
        return 1 << 10

    @flag()
    def defer_prioritized(self) -> int:
        """:class:`bool`: Whether to defer prioritized servers for chunking."""
        return 1 << 11

    @flag()
    def asynchronously_chunk_prioritized_servers(self) -> int:
        """:class:`bool`: Whether to asynchronously chunk prioritized servers or not."""
        return 1 << 12

    @flag()
    def synchronously_chunk_unprioritized_servers(self) -> int:
        """:class:`bool`: Whether to synchronously chunk unprioritized servers or not."""
        return 1 << 13

    @flag()
    def keep_users_with_no_mutual_servers(self) -> int:
        """:class:`bool`: Whether to keep users cache if they no longer have mutual servers or not."""
        return 1 << 14


class MemberChunker:
    """Represents a member chunker.

    Parameters
    ----------
    client: :class:`~stoat.Client`
        The client.
    flags: Optional[:class:`MemberChunkerFlags`]
        The flags to use when chunking.
    prioritize: Optional[Dict[:class:`str`, :class:`int`]]
        The prioritized servers to chunk.
    servers: Optional[List[:class:`str`]]
        The list of servers to only chunk if :attr:`MemberChunkerFlags.chunk_only_servers` is ``True``,
        or exclude them otherwise.

    Attributes
    ----------
    client: :class:`~stoat.Client`
        The client.
    flags: :class:`MemberChunkerFlags`
        The flags to use when chunking.
    prioritize: Dict[:class:`str`, :class:`int`]
        The prioritized servers to chunk.
    servers: List[:class:`str`]
        The list of servers to only chunk if :attr:`MemberChunkerFlags.chunk_only_servers` is ``True``,
        or exclude them otherwise.
    """

    __slots__ = (
        '_tasks',
        'client',
        'flags',
        'priorities',
        'servers',
    )

    def __init__(
        self,
        client: Client,
        *,
        flags: typing.Optional[MemberChunkerFlags] = None,
        priorities: typing.Optional[dict[str, int]] = None,
        servers: typing.Optional[list[str]] = None,
    ) -> None:
        if flags is None:
            flags = MemberChunkerFlags.default()

        if priorities is None:
            priorities = {}

        if servers is None:
            servers = []

        self._tasks: dict[str, asyncio.Task] = {}
        self.client: Client = client
        self.flags: MemberChunkerFlags = flags
        self.priorities: dict[str, int] = priorities
        self.servers: list[str] = servers

        if self.flags.subscribe_to_ready:
            self.client.subscribe(ReadyEvent, self.process_ready)

        if self.flags.subscribe_to_server_create:
            self.client.subscribe(ServerCreateEvent, self.process_server_create)

        if self.flags.subscribe_to_server_delete:
            self.client.subscribe(ServerDeleteEvent, self.process_server_delete)

        if self.flags.subscribe_to_server_member_join:
            self.client.subscribe(ServerMemberJoinEvent, self.process_server_member_join)

        if self.flags.subscribe_to_server_member_remove:
            self.client.subscribe(ServerMemberRemoveEvent, self.process_server_member_remove)

    def is_chunking_completed(self) -> bool:
        """:class:`bool`: Returns whether chunking process was completed after receiving :class:`~stoat.ReadyEvent`."""

        if '' in self._tasks:
            return self._tasks[''].done()
        return True

    async def get_priorities(self) -> dict[str, int]:
        """Dict[:class:`str`, :class:`int`]: Retrieve server priorities."""

        return self.priorities

    async def can_chunk(self, server: Server, /) -> bool:
        """:class:`bool`: Whether the server should be chunked."""

        return (server.id not in self.servers) ^ self.flags.chunk_only_servers

    async def _chunk_servers(self, servers: list[Server], cache_context: BaseCacheContext, /) -> None:
        flags = self.flags

        priorities = await self.get_priorities()
        chunking_servers = sorted(
            [(server, priorities.get(server.id, 0)) for server in servers],
            key=lambda pair, /: pair[1],
        )

        prioritized = []
        servers = []

        excluded = False

        for server, priority in chunking_servers:
            excluded = (server.id in self.servers) ^ flags.chunk_only_servers
            if excluded:
                continue

            if priority > 0:
                prioritized.append(server)
            else:
                servers.append(server)

        groups = (
            [
                (servers, False),
                (prioritized, True),
            ]
            if flags.defer_prioritized
            else [
                (prioritized, True),
                (servers, False),
            ]
        )

        tasks = []
        for group, is_prioritized in groups:
            for server in group:
                can = await self.can_chunk(server)
                if not can:
                    continue

                task = asyncio.create_task(self.chunk(server, cache_context))
                self._tasks[server.id] = task
                if is_prioritized:
                    if flags.asynchronously_chunk_prioritized_servers:
                        tasks.append(task)
                    else:
                        await task
                elif flags.synchronously_chunk_unprioritized_servers:
                    await task
                else:
                    tasks.append(task)

        if tasks:
            await asyncio.gather(*tasks)

    async def process_ready(self, event: ReadyEvent, /) -> None:
        """Process a :class:`~stoat.ReadyEvent`.

        Parameters
        ----------
        event: :class:`~stoat.ReadyEvent`
            The event to process.
        """
        if '' in self._tasks:
            self._tasks[''].cancel()
        task = asyncio.create_task(self._chunk_servers(event.servers, event.cache_context))
        self._tasks[''] = task
        await task

    async def process_server_create(self, event: ServerCreateEvent, /) -> None:
        """Process a :class:`~stoat.ServerCreateEvent`.

        Parameters
        ----------
        event: :class:`~stoat.ServerCreateEvent`
            The event to process.
        """
        server = event.server

        if await self.can_chunk(server):
            await self.chunk(server, event.cache_context)

    async def process_server_delete(self, event: ServerDeleteEvent, /) -> None:
        """Process a :class:`~stoat.ServerDeleteEvent`.

        Parameters
        ----------
        event: :class:`~stoat.ServerDeleteEvent`
            The event to process.
        """
        task = self._tasks.pop(event.server_id, None)
        if task is not None:
            task.cancel()

    async def process_server_member_join(self, event: ServerMemberJoinEvent, /) -> None:
        """Process a :class:`~stoat.ServerMemberJoinEvent`.

        Parameters
        ----------
        event: :class:`~stoat.ServerMemberJoinEvent`
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

    async def process_server_member_remove(self, event: ServerMemberRemoveEvent, /) -> None:
        """Process a :class:`~stoat.ServerMemberRemoveEvent`.

        Parameters
        ----------
        event: :class:`~stoat.ServerMemberRemoveEvent`
            The event to process.
        """
        my_id = event.shard.state.my_id

        if event.user_id == my_id:
            task = self._tasks.pop(event.server_id, None)
            if task is not None:
                task.cancel()
            return

        if self.flags.keep_users_with_no_mutual_servers:
            return

        cache = event.shard.state.cache
        if cache is None:
            return

        server_ids = get_mutual_servers(cache, event.user_id, event.cache_context)

        if len(server_ids) == 0 or (len(server_ids) == 1 and server_ids[0] == event.server_id):
            cache.delete_user(event.user_id, event.cache_context)

        return

    async def chunk(self, server: Server, cache_context: BaseCacheContext, /) -> MemberList:
        """Chunks a server.

        Parameters
        ----------
        server: :class:`~stoat.Server`
            The server to chunk.
        cache_context: :class:`~stoat.BaseCacheContext`
            The cache context.

        Returns
        -------
        :class:`~stoat.MemberList`
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

        self._tasks.pop(server.id, None)

        return data


def get_mutual_servers(cache: Cache, user_id: str, cache_context: BaseCacheContext, /) -> list[str]:
    ret = []

    for server_id, members in cache.get_servers_member_mapping(cache_context).items():
        if user_id in members:
            ret.append(server_id)

    return ret


__all__ = (
    'MemberChunkerFlags',
    'MemberChunker',
    'get_mutual_servers',
)
