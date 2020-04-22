
# WS server example

import asyncio
import json

import websockets
import matlab.engine

eng = matlab.engine.start_matlab()

async def hello(websocket, path):

    raw = await websocket.recv()
    data = json.loads(raw)

    headerBitLength = data["headerBitLength"]
    payloadBitLength = data["payloadBitLength"]
    transmissionPower = data["transmissionPower"]
    transmissionBitrate = data["transmissionBitrate"]
    startOrientation = data["startOrientation"]
    endOrientation = data["endOrientation"]
    startPosition = data["startPosition"]
    endPosition = data["endPosition"]



    #
    # transmitter - IRadio pointer type, needs more investigation
    # macFrame - cPacket pointer type, needs more investigation
    # startTime - simtime_t type, needs PARSE
    # endTime - simtime_t type, needs PARSE
    # preambleDuration - simtime_t type, needs PARSE
    # headerDuration - simtime_t type, needs PARSE
    # dataDuration - simtime_t type, needs PARSE
    # startPosition - Coord type, has 3 double var (x, y, z)
    # endPosition - Coord type, has 3 double var (x, y, z)
    # startOrientation - EulerAngles type, has 3 double var (alpha, beta, gamma)
    # endOrientation - EulerAngles type, has 3 double var (alpha, beta, gamma)
    # modulation - UNKNOWN
    # headerBitLength - int type, DONE
    # payloadBitLength - int type, DONE
    # carrierFrequency - UNKNOWN
    # bandwidth - UNKNOWN
    # transmissionBitrate - bps type, needs PARSE
    # transmissionPower - W type, needs PARSE
    # transmissionMode - IIeee80211Mode pointer type, needs more investigation
    # transmissionChannel - IIeee80211Channel pointer type, needs more investigation

    message = "OK"

    print(eng.doubler(2))

    await websocket.send(message)


start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

