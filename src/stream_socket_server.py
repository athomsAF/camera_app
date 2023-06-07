import asyncio
import websockets
import cv2
import numpy as np
import base64

async def video_stream(websocket, path) -> None:
    """Generate a video stream from the webcam and send it to the client.

    Args:
        websocket (_type_): websocket from lib websockets
        path (str): path necessary for websocket.serve()
    """
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        _, buffer = cv2.imencode('.jpg', frame)
        frame_base64 = base64.b64encode(buffer)

        await websocket.send(frame_base64)

        await asyncio.sleep(0.1)

    cap.release()

start_server = websockets.serve(video_stream, '10.3.141.1', 9000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

