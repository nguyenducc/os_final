class workerProtocol:

    def __init__(self,num_workers):
        self.num_workers=num_workers


    def compute(self,the_input):         #each client will calculate a partial contribution for global sum

        print(the_input)
        split=the_input.split(' ')      #message is a string containg worker id and number of steps
        print(split)
        steps=int(split[0])
        myId=int(split[1])
        print("Worker "+str(myId)+ " calculates")

        partialSum=0      #initialize partial sum

        step=1.0/steps

        i=myId          #initialize i

        while(i<steps):                  #cyclic distribution
            x = (i + 0.5) * step
            partialSum += 4.0 / (1.0 + x * x)
            i=i+self.num_workers

        the_output=str(partialSum)

        return the_output            #returns partial sum as a string




