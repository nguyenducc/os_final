from threading import RLock

class Globpi:

    def __init__(self,steps):
        self.lock=RLock()
        self.steps=steps
        self.globSum=0

    def addToglobSum(self, threadSum):
        with self.lock:
            self.globSum+=threadSum

    def calculatePi(self):
        step=1/self.steps
        pi=self.globSum*step        #sould pi be returned or simply printed?
        print("pi is "+str(pi))

    def get_steps(self):
        return str(self.steps)
















