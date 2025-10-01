import asyncio

import json
import stoat

import revolt
import revolt.http
import revolt.state

import timeit
import typing
import voltage
import voltage.internals

async def bench_messages():
    with open('./tests/data/channels/messages/rules.json', 'r') as fp:
        payload = json.load(fp)[0]

    with open('./tests/data/channels/rules_channel.json', 'r') as fp:
        channel_payload = json.load(fp)
    
    with open('./tests/data/servers/server.json', 'r') as fp:
        server_payload = json.load(fp)
    
    with open('./tests/data/users/user.json', 'r') as fp:
        user_payload = json.load(fp)

    with open('./tests/data/servers/member.json', 'r') as fp:
        member_payload = json.load(fp)
    
    payload['reactions'] = {}
    
    state = stoat.State()
    parser = stoat.Parser(state=state)
    state.setup(parser=parser)

    def using_stoatpy():
        return parser.parse_message(payload)

    import aiohttp
    session = aiohttp.ClientSession()

    api_info: typing.Any = {
        'features': {
            'autumn': {
                'url': 'https://autumn.revolt.chat/'
            }
        }
    }
    rpy_http = revolt.http.HttpClient(
        session,
        '',
        'https://api.revolt.chat/',
        api_info
    )
    rpy_state = revolt.state.State(rpy_http, api_info, 1000)
    rpy_state.add_user(user_payload)
    rpy_state.add_server(server_payload)
    rpy_state.add_member(server_payload['_id'], member_payload)
    rpy_state.add_channel(channel_payload)

    def using_revoltpy():
        return revolt.Message(data=payload, state=rpy_state)

    vpy_http = voltage.internals.http.HTTPHandler(session, '')
    vpy_cache = voltage.internals.cache.CacheHandler(vpy_http, asyncio.get_event_loop())
    vpy_cache.add_user(user_payload)

    server = voltage.Server(data=server_payload, cache=vpy_cache)
    vpy_cache.servers[server.id] = server

    vpy_cache.add_member(server_payload['_id'], member_payload)
    vpy_cache.add_channel(channel_payload)

    def using_voltage():
        return voltage.Message(data=payload, cache=vpy_cache)

    time_stoatpy = timeit.timeit(using_stoatpy,     number=10000)
    time_revoltpy = timeit.timeit(using_revoltpy, number=10000)
    time_voltage = timeit.timeit(using_voltage,   number=10000)

    print(f"[Message] Time using stoat.py --: {time_stoatpy:.6f} seconds")
    print(f"[Message] Time using revolt.py -: {time_revoltpy:.6f} seconds")
    print(f"[Message] Time using voltage ---: {time_voltage:.6f} seconds")

    await session.close()