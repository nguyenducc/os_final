from globPi import Globpi
import socket
from master_thread import MasterThread

port=1024
workers=4
st=Globpi(1000)    #instance of the class Globpi(steps)
binds=("localhost",port)

if __name__=='__main__':
    connectionSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #create socket instance
    connectionSocket.bind(binds)    #bind socket to port
    connectionSocket.listen(10)     #listen new connection requests

    mthread=[]

    for i in range(workers):

        conn,addr=connectionSocket.accept() #accept connection to ip address
        print('Master thread ',addr,' started')
        master=MasterThread(conn, i, st)
        master.start()
        mthread.append(master)

    print("All workers started")

    for i in range(workers):
        try:
            mthread[i].join()
        except InterruptedError as e:
            pass
    st.calculatePi()



