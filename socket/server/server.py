import websockets
import asyncio
import json
import traceback
from FileOperation import FileOperation

PORT = 0
record = FileOperation('server/record.txt')
showAll = False


async def echo(websocket, path):
    print("A client connected")
    try:
        async for msg in websocket:
            data: dict = json.loads(msg)
            if (data['query'] == 'getAll'):
                print(data)
                await websocket.send(json.dumps(record.prepareWallFile()))
            elif data['query'] == 'clear':
                record.clearFile()
                await websocket.send(msg)
            else:
                record.addRow(msg, data['title'], data['content'])
                await websocket.send(msg)

    except websockets.exceptions.ConnectionClosed as e:
        print("client disconnected")
    except Exception as e:
        print(traceback.format_exc())
        print("error occured ")


def main():
    global PORT
    f = open('./config.json', 'r')
    config = json.load(f)
    f.close()

    PORT = config['PORT']
    print(f"server started at {PORT}")

    start_server = websockets.serve(echo, "localhost", PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


main()
