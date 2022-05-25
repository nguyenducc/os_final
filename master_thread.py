import threading
from master_protocol import MasterProtocol

class MasterThread(threading.Thread):

    def __init__self(self,socket,id,steps):
        super().__init__()
        self.socket=socket
        self.id=id
        self.steps=steps

    def run(self):
        app=MasterProtocol(self.steps,self.id)  #create an instance of the class MasterProtocol
        outmsg=app.prepare_request()   #the outmsg contains a string with steps and worker id
        self.socket.sendall(outmsg.encode())  #server sends message(steps,id) to each worker(clients)
        inmsg=self.socket.recv(1024)           #server recieves partial sum from each worker
        app.process_reply(inmsg.decode())      #adds partial sum to global sum
        self.socket.close()
        print("Data socket closed")

