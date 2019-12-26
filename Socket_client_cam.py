# above two libraries for websocket communication
import asyncio
import websockets
#Imageprocessing library
import cv2
#encoder and deccoder library
import base64
#for converting bytes to array
import numpy as np

#Function which encodes the image to a string format
def convertImageToBase64(img_string):
    decoded=base64.decodestring(img_string)
    return decoded
    
#these function called when the websocket server starts
async def Operate_soc():
    #replace with your server ip address and port number
    uri = "ws://192.168.29.228:4000/ws"
    async with websockets.connect(uri) as websocket:
        while True:
            greeting = await websocket.recv()
            #decoding the string to image byte
            i=convertImageToBase64(greeting)
            #decoding the bytes to array
            decoded = cv2.imdecode(np.frombuffer(i, np.uint8), -1)
            #Showing the decoded image
            cv2.imshow('frame',decoded)
            #BY pressing 'q' in keyboard streaming stops but server runs 
            if cv2.waitKey(1)==ord('q'):
                break
    cv2.destroyAllWindows()

#run the client untill the function complete
asyncio.get_event_loop().run_until_complete(Operate_soc())

