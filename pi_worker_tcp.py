import socket
from worker_protocol import workerProtocol

HOST='localhost'
PORT=1024
WORKERS=4

if __name__ == '__main__':             #Client recieves steps and worker id for partial computation of integral sum from Server

    server = (HOST, PORT)                     #host and port from server
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #create  instance of socket
    data_socket.connect(server)                                        #request connection to server
    print("Connection to " + HOST + " established")

    app = workerProtocol(WORKERS)           #create an instance of worker protocol

    try:
        inmsg = data_socket.recv(1024)            #Nhận số bước và id từ máy chủ
        outmsg = app.compute(inmsg.decode())      #compute partial contribution to pi
        data_socket.send(outmsg.encode())        #partial pi of worker thread is sent to server
    except:
        print("I/O Error")

    data_socket.close()

