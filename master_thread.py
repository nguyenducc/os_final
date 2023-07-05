import threading
from master_protocol import MasterProtocol


class MasterThread(threading.Thread):

    def __init__(self, socket, id:int, globpi):
        super().__init__()
        self.socket=socket
        self.id=id
        self.globpi=globpi

    def run(self):
        app=MasterProtocol(self.globpi, self.id)  #create an instance of the class MasterProtocol
        outmsg=app.prepare_request()   #the outmsg contains a string with steps and worker id
        try:
            self.socket.sendall(outmsg.encode())  #server sends message(steps,id) to each worker
            inmsg=self.socket.recv(1024)           #server recieves partial pi from each worker
            app.process_reply(inmsg.decode())      #adds partial pi to global pi

        except:
            print("I/O Error")

        self.socket.close()
        print("Data socket closed")


