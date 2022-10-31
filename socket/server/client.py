import asyncio
from websockets import connect


async def listen():
    url = "ws://127.0.0.1:12344"

    async with connect(url) as ws:
        await ws.send(input())
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())
