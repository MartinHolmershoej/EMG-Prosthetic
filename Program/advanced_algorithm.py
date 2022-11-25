from multiprocessing import Queue
import Ialgorithm


class AdvancedAlgorithm(Ialgorithm.ABC):

    def Analyse(queueList):

        queue1 = queueList[0]
        queue2 = queueList[1]
        queue3 = queueList[2]
        queue4 = queueList[3]

        eMGList = range(24)

        for i in range(8):
            queue1Value = queue1.get()
            queue2Value = queue2.get()
            queue3Value = queue3.get()
            queue4Value = queue4.get()
        
            eMGList.append(queue1Value)
            eMGList.append(queue2Value)
            eMGList.append(queue3Value)
            eMGList.append(queue4Value)
            i += 1
        return eMGList

