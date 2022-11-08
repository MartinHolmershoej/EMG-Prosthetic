from multiprocessing import Queue
import Ialgorithm

baseline_1 = 0.600
baseline_2 = 0.600

class SimpleAlgorithm(Ialgorithm):

    def Analyse(queue1, queue2):
        
        #upper muscel active
        if (queue1.get()> baseline_1 and queue2.get()<baseline_2):
            return 1

        #lower muscel active
        if (queue2.get()>baseline_2 and queue1.get()<baseline_1):
            return 2

    def Baseline():
        #set baseline 1

        #set baseline 2
        None
