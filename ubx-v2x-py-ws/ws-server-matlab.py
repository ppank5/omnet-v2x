
# WS server example

import asyncio
import websockets
import json
import matlab.engine


async def hello(websocket, path):
	eng = matlab.engine.start_matlab()
	
	raw = await websocket.recv()
	inp = json.loads(y)
	
	x = inp["x"]
	y = inp["y"]
	
	len = eng.triangulate(x,y)
	max = eng.max(x,y)
	
	dic = {"length": len, "max": max}
	message = json.dumps(dic)
	
    await websocket.send(message)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()