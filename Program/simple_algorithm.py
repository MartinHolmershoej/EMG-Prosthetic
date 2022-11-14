from multiprocessing import Queue
import Ialgorithm

baseline_1 = 0.600 #default values
baseline_2 = 0.600 #default values
 

class SimpleAlgorithm(Ialgorithm.ABC):

    def Analyse(queueList, gripGroup):
        queue1 = queueList[0]
        queue2 = queueList[1]
        queue1Value = queue1.get()
        queue2Value = queue2.get()
        
        #upper muscel active
        if (queue1Value > baseline_1 and queue2Value < baseline_2):
            if gripGroup == 1:
                return 1

            elif gripGroup == 2:
                return 3
            
            elif gripGroup == 3:
                return 5

        #lower muscel active
        elif (queue2Value > baseline_2 and queue1Value < baseline_1):
            if gripGroup == 1:
                return 2

            elif gripGroup == 2:
                return 4
            
            elif gripGroup == 3:
                return 6
            
        else:
            return 0

    def Baseline(queueList):
        value1 = 0
        value2 = 0
        queue1 = queueList[0]
        queue2 = queueList[1]
        
        #set baseline 1 and 2
        for x in range(10):
            value1 += queue1.get()
            value2 += queue2.get()
            
        baseline_1 = round(value1/10.0,2)
        baseline_2 = round(value2/10.0,2)
        
    
        
