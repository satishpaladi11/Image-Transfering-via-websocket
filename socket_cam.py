import asyncio
import websockets
import cv2
import loading_object_video as lov
import base64
import time
import numpy as np

def convertImageToBase64():
    with open("/home/sathish/Desktop/Machinevision/MV_prog/Kumdasamples/testing_sample.png", "rb") as image_file:
        encoded = base64.b64encode(image_file.read())
        return encoded
    

async def hello(websocket, path):
    cap=cv2.VideoCapture(0)
    rect, frame = cap.read()
    while True:
        rect, frame = cap.read()
        resized=cv2.resize(frame,(350,300))
        cv2.imwrite("/home/sathish/Desktop/Machinevision/MV_prog/Kumdasamples/testing_sample.png",resized)
        i=convertImageToBase64()
        #print(i)
        await websocket.send(i.decode('utf-8'))

        if cv2.waitKey(1)==ord('q'):
            break
    cap.release
    cv2.destroyAllWindows()
    

start_server = websockets.serve(hello, "192.168.29.228", 4000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
