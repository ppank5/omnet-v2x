
# WS server example

import asyncio
import websockets
import json

async def hello(websocket, path):
    y = await websocket.recv()
    z = json.loads(y)

    name = z["name"]
    age = z["age"]
    city = z["city"]

    greeting = f"Hello {name}, aged {age} living in {city}! Welcome here"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()