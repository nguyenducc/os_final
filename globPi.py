from threading import RLock

class Globpi:

    def __init__(self,steps):
        self.lock=RLock()
        self.steps=steps
        self.globPi=0.0

    def addToglobPi(self, threadPi):
        with self.lock:
            self.globPi+=threadPi

    def printPi(self):

        print("pi is "+str(self.globPi))

    def get_steps(self):
        return str(self.steps)
















