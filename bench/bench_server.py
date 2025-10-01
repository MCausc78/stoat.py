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

async def bench_servers():
    with open('./tests/data/servers/server.json', 'r') as fp:
        payload = json.load(fp)

    state = stoat.State()
    parser = stoat.Parser(state=state)
    state.setup(parser=parser)

    def using_stoatpy():
        return parser.parse_server(payload, (True, payload['channels']))

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

    def using_revoltpy():
        return revolt.Server(data=payload, state=rpy_state)

    vpy_http = voltage.internals.http.HTTPHandler(session, '')
    vpy_cache = voltage.internals.cache.CacheHandler(vpy_http, asyncio.get_event_loop())

    def using_voltage():
        return voltage.Server(data=payload, cache=vpy_cache)

    time_stoatpy = timeit.timeit(using_stoatpy,     number=10000)
    time_revoltpy = timeit.timeit(using_revoltpy, number=10000)
    time_voltage = timeit.timeit(using_voltage,   number=10000)

    print(f"[Server] Time using stoat.py --: {time_stoatpy:.6f} seconds")
    print(f"[Server] Time using revolt.py -: {time_revoltpy:.6f} seconds")
    print(f"[Server] Time using voltage ---: {time_voltage:.6f} seconds")

    await session.close()

