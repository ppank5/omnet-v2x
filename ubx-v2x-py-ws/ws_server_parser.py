import asyncio
import json
import websockets
import matlab.engine

eng = matlab.engine.start_matlab()
print("Matlab Engine has started")

async def comm(websocket, path):

    raw = await websocket.recv()

    data = json.loads(raw)

    coord_a = matlab.double([data["coord_a_x"], data["coord_a_y"]])
    coord_b = matlab.double([data["coord_b_x"], data["coord_b_y"]])
    payload_len = matlab.double([data["payload_len"]])

    result = eng.batch_sim(coord_a, coord_b, payload_len)

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

    x = {"result": result}
    message = json.dumps(x)

    await websocket.send(message)
    print(message)

start_server = websockets.serve(comm, "localhost", 8765)
print("Server is running")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

