import asyncio
import websockets
import json


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")
        age = input("How old are you? ")
        city = input("Where do you live? ")

        x = {"name": name, "age": age, "city": city}

        y = json.dumps(x)
        print(x)
        print(y)

        await websocket.send(y)
        print(f"> {y}")

        greeting = await websocket.recv()
        print(f"< {greeting}")


asyncio.get_event_loop().run_until_complete(hello())
