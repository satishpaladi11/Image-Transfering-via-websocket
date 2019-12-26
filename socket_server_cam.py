'''
This program acts as server which can be placed in your 
system or Controller where camera is available
'''

# above two libraries for websocket communication
import asyncio
import websockets
#Imageprocessing library
import cv2
#encoder and deccoder library
import base64

#Function which encodes the image to a string format
def convertImageToBase64():
    #copy the path in the Operate_soc() function to here
    with open("/home/sathish/Desktop/Machinevision/MV_prog/Kumdasamples/testing_sample.png", "rb") as image_file:
        encoded = base64.b64encode(image_file.read())
        return encoded
    
#these function called when the websocket server starts
async def Operate_soc(websocket, path):
    #starting a videocamera using opencv
    cap=cv2.VideoCapture(0)
    rect, frame = cap.read()
    
    while True:
        rect, frame = cap.read()
        resized=cv2.resize(frame,(350,300))
        #save the frame in your system location path and put the same path in convertImageToBase64() function
        cv2.imwrite("/home/sathish/Desktop/Machinevision/MV_prog/Kumdasamples/testing_sample.png",resized)
        i=convertImageToBase64()
        await websocket.send(i.decode('utf-8'))
        #BY pressing 'q' in keyboard streaming stops but server runs 
        if cv2.waitKey(1)==ord('q'):
            break
    cap.release
    cv2.destroyAllWindows()
    
#starting the server
#replace with your ipaddress and port num
start_server = websockets.serve(hello, "192.168.29.228", 4000)

#run the server untill the function complete
asyncio.get_event_loop().run_until_complete(start_server)

#run the server forever
asyncio.get_event_loop().run_forever()
