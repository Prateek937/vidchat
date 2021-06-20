import socket, cv2, pickle
import numpy as np
cap = cv2.VideoCapture(0)
client_socket = socket.socket()
client_socket.connect(("192.168.43.165", 1231))
while True:
    ret, photo = cap.read()
    if ret:
        ret, buffer = cv2.imencode('.jpg',photo)
        bytedata = pickle.dumps(buffer)
        client_socket.send(bytedata)
        
    recv_data = client_socket.recv(100000000)
    try:
        data = pickle.loads(recv_data)
        Data = cv2.imdecode(data,cv2.IMREAD_COLOR)
        if Data is not None :
            cv2.imshow("friends on call...." , Data)
            if cv2.waitKey(10) == 13:
                break
    except: 
        print("Waiting for the network!")
        cv2.destroyWindow("friends on call....")
        
cv2.destroyWindow("friends on call....")
cap.release()  