from multiprocessing import Queue
import Ialgorithm

baseline_1 = 0.600 #default values
baseline_2 = 0.600 #default values

class SimpleAlgorithm(Ialgorithm):

    def Analyse(queue1, queue2):
            
            #upper muscel active
            if (queue1.get()> baseline_1 and queue2.get()<baseline_2):
                return 1

            #lower muscel active
            if (queue2.get()>baseline_2 and queue1.get()<baseline_1):
                return 2

    def Baseline(queue1, queue2):
            value1 = 0
            value2 = 0

            #set baseline 1 and 2
            for x in range(10):
                value1 += queue1.get()
                value2 += queue2.get()
            
            baseline_1 = (value1/10.0)
            baseline_2 = (value2/10.0)

            return baseline_1, baseline_2


        
