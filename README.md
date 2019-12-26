# Image-Transfering-via-websocket
Continuous transfer of images through websocket

It consists of 

1)Websocket sender(Socket_server_cam)

2)Websocket reciever(Socket_client_cam)

Websocket server

    The input image converted in to base64 format using base64 encoder
  
    The base64 format string is sent via websocket
  
    A user sets IPaddress and port number
  
  
Websocket client

    The base64 string format is recieved via websocket
  
    The base64 string is converted in to image using base64 decoder
  
    A user uses server ipaddress and port number to connect to server
  
