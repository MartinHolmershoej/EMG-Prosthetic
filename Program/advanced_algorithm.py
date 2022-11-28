from multiprocessing import Queue
import Ialgorithm

eMGList = []

class AdvancedAlgorithm(Ialgorithm.ABC):

    def Analyse(queueList):

        queue1 = queueList[0]
        queue2 = queueList[1]
        queue3 = queueList[2]
        queue4 = queueList[3]

        for i in range(32):
            queue1Value = queue1.get()
            queue2Value = queue2.get()
            queue3Value = queue3.get()
            queue4Value = queue4.get()
        
            eMGList.insert(i,queue1Value)
            eMGList.insert(i,queue2Value)
            eMGList.insert(i,queue3Value)
            eMGList.insert(i,queue4Value)
            i += 1
        return eMGList

