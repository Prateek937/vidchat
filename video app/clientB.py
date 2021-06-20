import socket, cv2, pickle
import urllib 
import numpy as np
url = "http://192.168.43.1:8080/shot.jpg"
client_socket = socket.socket()
client_socket.connect(("192.168.43.165", 1232))
while True:
    
    imgResp=urllib.request.urlopen(url)      #The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) 
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img = cv2.resize(img,(700,500))
    ret, buffer = cv2.imencode('.jpg',img)
    bytedata = pickle.dumps(buffer)
    client_socket.send(bytedata)
    client_socket.send(imgResp.read())
    
    recv_data = client_socket.recv(10000000)
    try:
        data = pickle.loads(recv_data)
        Data = cv2.imdecode(data,cv2.IMREAD_COLOR)
        if Data is not None :
            cv2.imshow("Friends on call...." , Data)
            if cv2.waitKey(10) == 13:
                break
    except: 
        print("Waiting for the network!")
        cv2.destroyWindow("Friends on call....")
        
cv2.destroyWindow("Friends on call....")
cap.release()