import asyncio
import websockets
import json


async def comm():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        coord_a_x = 1
        coord_a_y = 2
        coord_b_x = 4
        coord_b_y = 6
        payload_len = 200
        x = {
            "coord_a_x": coord_a_x,
            "coord_a_y": coord_a_y,
            "coord_b_x": coord_b_x,
            "coord_b_y": coord_b_y,
            "payload_len": payload_len
        }

        message = json.dumps(x)

        await websocket.send(message)
        print(message)

        response = await websocket.recv()
        print (response)

asyncio.get_event_loop().run_until_complete(comm())
