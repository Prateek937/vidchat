import socket
import threading
import pickle
import cv2
import numpy as np

socket1 = socket.socket()
socket2 = socket.socket()

socket1.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)
socket2.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

port1 = 1231
port2 = 1232

IP = "192.168.43.165"
print(IP)

socket1.bind((IP, port1))
socket2.bind((IP, port2))

socket1.listen()
conn1, addr1 = socket1.accept()
print(addr1)

socket2.listen()
conn2, addr2 = socket2.accept()
print(addr2)


while True:
    data1=conn1.recv(100000000)
    data2=conn2.recv(100000000)

    data1 = pickle.loads(data1)
    Data1 = cv2.imdecode(data1,cv2.IMREAD_COLOR)
    data2 = pickle.loads(data2)
    Data2 = cv2.imdecode(data2,cv2.IMREAD_COLOR)

    data1=Data1[:450,:450,:]
    data2=Data2[:450,:450,:]
  
    p = np.concatenate((data1,data2), axis=1)
    rphoto = cv2.rectangle(p, (0,0),(896,446), [0,0,255], 4 )
    ret, buffer = cv2.imencode('.jpg',rphoto)
    bytedata = pickle.dumps(buffer)
    conn1.send(bytedata)
    conn2.send(bytedata)
   
    
  

