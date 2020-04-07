
# WS server example

import asyncio
import websockets
import json
import matlab.engine


async def hello(websocket, path):
    raw = await websocket.recv()
    data = json.loads(raw)

    headerBitLength = data["headerBitLength"]
    payloadBitLength = data["payloadBitLength"]

    #
    # transmitter - IRadio pointer type, needs more investigation
    # macFrame - cPacket pointer type, needs more investigation
    # startTime - simtime_t type, needs PARSE
    # endTime - simtime_t type, needs PARSE
    # preambleDuration - simtime_t type, needs PARSE
    # headerDuration - simtime_t type, needs PARSE
    # dataDuration - simtime_t type, needs PARSE
    # startPosition - Coord type, needs PARSE
    # endPosition - Coord type, needs PARSE
    # startOrientation - EulerAngles type, needs PARSE
    # endOrientation - EulerAngles type, needs PARSE
    # modulation - UNKNOWN
    # headerBitLength - int type, DONE
    # payloadBitLength - int type, DONE
    # carrierFrequency - UNKNOWN
    # bandwidth - UNKNOWN
    # transmissionBitrate - bps type, needs PARSE
    # transmissionPower - W type, needs PARSE
    # transmissionMode - IIeee80211Mode pointer type, needs more investigation
    # transmissionChannel - IIeee80211Channel pointer type, needs more investigation
    #

    await websocket.send(message)


eng = matlab.engine.start_matlab()

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()