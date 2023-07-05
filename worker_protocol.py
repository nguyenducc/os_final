class workerProtocol:

    def __init__(self,num_workers):
        self.num_workers=num_workers


    def compute(self,the_input):#Mỗi client sẽ tính toán một đóng góp phần cho tổng toàn cầu.
        print("input : ",the_input)
        split=the_input.split()      ##message là một chuỗi chứa id của worker và số bước.
        print(split)
        steps=int(split[0])
        myId=int(split[1])
        print("Worker "+str(myId)+ " calculates")

        partialSum=0      #initialize partial sum

        step=1.0/steps

        i=myId          #initialize i

        while(i<steps):                  #Phân phối tuần hoàn
            x = (i + 0.5) * step
            partialSum += 4.0 / (1.0 + x * x)
            i=i+self.num_workers

        myPi=step*partialSum
        the_output=str(myPi)

        return the_output            #Trả về giá trị pi phần tư dưới dạng chuỗi




