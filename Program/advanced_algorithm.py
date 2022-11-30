from multiprocessing import Queue
import Ialgorithm
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from joblib import load

class AdvancedAlgorithm(Ialgorithm.ABC):

    def __init__(self) -> None:
        self.eMGList = []
        self.prediction = 0

    def AddToEMGList(self, queueList, eMGList):

        queue1 = queueList[0]
        queue2 = queueList[1]
        queue3 = queueList[2]
        queue4 = queueList[3]

        if len(eMGList) == 0:
            for i in range(8):
                queue1Value = queue1.get()
                queue2Value = queue2.get()
                queue3Value = queue3.get()
                queue4Value = queue4.get()
            

                eMGList.append(queue1Value)
                eMGList.append(queue2Value)
                eMGList.append(queue3Value)
                eMGList.append(queue4Value)
        
        elif len(eMGList) == 32:
            queue1Value = queue1.get()
            queue2Value = queue2.get()
            queue3Value = queue3.get()
            queue4Value = queue4.get()

            eMGList.append(queue1Value)
            eMGList.append(queue2Value)
            eMGList.append(queue3Value)
            eMGList.append(queue4Value)

            for i in range(4):
                eMGList.pop(0)

        else:
            eMGList.clear()

            for i in range(8):
                queue1Value = queue1.get()
                queue2Value = queue2.get()
                queue3Value = queue3.get()
                queue4Value = queue4.get()
            
                eMGList.append(queue1Value)
                eMGList.append(queue2Value)
                eMGList.append(queue3Value)
                eMGList.append(queue4Value)
                
        self.eMGList = eMGList
        return self.eMGList

    def predict(self, eMGList):
        clf = load(r"C:\Users\Vinni\OneDrive\Dokumenter\GitHub\EMG-Prosthetic\Program\RF_Minimalized.joblib")
        self.prediction = clf.predict(np.asarray(eMGList).reshape(1,-1))

        return self.prediction

# Skal køres i denne rækkefølge:
# test = AdvancedAlgorithm()
# test.AddToEMGList(test.eMGList)
# test.predict(test.eMGList)