
# WS server example

import asyncio
import json

import websockets
import matlab.engine

eng = matlab.engine.start_matlab()


coord_a = [2, 2]
coord_b = [5, 6]
payload_len = 58
message = [coord_a, coord_b, payload_len]

raw = json.dumps(message)
data = json.loads(raw)

# data is a list.
# [0] is coord_a,
# [1] is coord_b,
# [3] is payload_len

o_coord_a = matlab.double(data[0])
o_coord_b = matlab.double(data[1])
o_payload_len = data[2]

output = eng.distance_calc(o_coord_a, o_coord_b)

print(output)



async def hello(websocket, path):

    aw = await websocket.recv()



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

    await websocket.send()

# start_server = websockets.serve(hello, "localhost", 8765)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

