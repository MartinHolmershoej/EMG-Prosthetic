from multiprocessing import Queue
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from joblib import load

class AdvancedAlgorithm():

    def __init__(self) -> None:
        self.eMGList = []
        self.prediction = 0

    def AddToEMGList(self, queueList):

        queue1 = queueList[0]
        queue2 = queueList[1]
        queue3 = queueList[2]
        queue4 = queueList[3]

        if len(self.eMGList) == 0:
            for i in range(8):
                queue1Value = queue1.get()
                queue2Value = queue2.get()
                queue3Value = queue3.get()
                queue4Value = queue4.get()
            

                self.eMGList.append(queue1Value)
                self.eMGList.append(queue2Value)
                self.eMGList.append(queue3Value)
                self.eMGList.append(queue4Value)
        
        elif len(self.eMGList) == 32:
            queue1Value = queue1.get()
            queue2Value = queue2.get()
            queue3Value = queue3.get()
            queue4Value = queue4.get()

            self.eMGList.append(queue1Value)
            self.eMGList.append(queue2Value)
            self.eMGList.append(queue3Value)
            self.eMGList.append(queue4Value)

            for i in range(4):
                self.eMGList.pop(0)

        else:
            self.eMGList.clear()

            for i in range(8):
                queue1Value = queue1.get()
                queue2Value = queue2.get()
                queue3Value = queue3.get()
                queue4Value = queue4.get()
            
                self.eMGList.append(queue1Value)
                self.eMGList.append(queue2Value)
                self.eMGList.append(queue3Value)
                self.eMGList.append(queue4Value)
                
    def Analyse(self):
        clf = load(r"/home/pi/Documents/EMG-Prosthetic/Program/RF_Minimalized.joblib")
        self.prediction = clf.predict(np.asarray(self.eMGList).reshape(1,-1))

        return self.prediction
