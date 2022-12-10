from motorController import MotorController



class SimpleAlgorithm():
    
    def __init__(self) -> None:
        self.baseline_1 = 0.600
        self.baseline_2 = 0.600
        self.result = 0        

    def Analyse(self, queueList, gripGroup):
        queue1 = queueList[0]
        queue2 = queueList[1]
        queue1Value = queue1.get()
        queue2Value = queue2.get()
        
        #upper muscel active
        if (queue1Value > self.baseline_1 and queue2Value < self.baseline_2):
            if gripGroup == 1:
                self.result = 1

            elif gripGroup == 2:
                self.result = 3
            
            elif gripGroup == 3:
                self.result = 5

        #lower muscel active
        elif (queue2Value > self.baseline_2 and queue1Value < self.baseline_1):
            if gripGroup == 1:
                self.result = 2

            elif gripGroup == 2:
                self.result = 4
            
            elif gripGroup == 3:
                self.result = 6
            
        else:
            self.result = 0
        

    def Baseline(self, queueList):
        value1 = 0
        value2 = 0
        queue1 = queueList[0]
        queue2 = queueList[1]
        
        # #set baseline 1 and 2
        for x in range(20):
             value1 += queue1.get()
             value2 += queue2.get()
            
        self.baseline_1 = (round((value1/10.0)*1.8,3))
        self.baseline_2 = (round((value2/10.0)*1.2,3))
        
        print(str(self.baseline_1))
        print(str(self.baseline_2))

    
        
