from multiprocessing import Queue
import Ialgorithm
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import load
import numpy as np

class AdAlgoLists():

    def __init__(self) -> None:
        self.prediction = 0
        self.eMGList = []

    def FillEMGList(self, eMGList):
        queue1 = [70, 50, 60, 80, 70, 50, 60, 80]
        queue2 = [70, 55, 60, 80, 70, 50, 60, 80]
        queue3 = [70, 65, 70, 75, 70, 50, 60, 80]
        queue4 = [70, 60, 50, 70, 70, 50, 60, 80]
        
        for i in range(8):
            queue1Value = queue1.pop(0)
            queue2Value = queue2.pop(0)
            queue3Value = queue3.pop(0)
            queue4Value = queue4.pop(0)
            
            self.eMGList.append(queue1Value)
            self.eMGList.append(queue2Value)
            self.eMGList.append(queue3Value)
            self.eMGList.append(queue4Value)
        
        print(eMGList)
        print(len(eMGList))

    def AddToEMGList(self, eMGList):

        queue1_1 = [40, 40, 45, 40, 40, 40, 40, 40]
        queue2_1 = [40, 40, 45, 40, 40, 40, 40, 40]
        queue3_1 = [40, 40, 45, 40, 40, 40, 40, 40]
        queue4_1 = [40, 40, 45, 40, 40, 40, 40, 40]

        if len(eMGList) == 0:
            for i in range(8):
                queue1Value = queue1_1.pop(0)
                queue2Value = queue2_1.pop(0)
                queue3Value = queue3_1.pop(0)
                queue4Value = queue4_1.pop(0)
            
                self.eMGList.append(queue1Value)
                self.eMGList.append(queue2Value)
                self.eMGList.append(queue3Value)
                self.eMGList.append(queue4Value)
        
        elif len(eMGList) == 32:
            queue1Value = queue1_1.pop(0)
            queue2Value = queue2_1.pop(0)
            queue3Value = queue3_1.pop(0)
            queue4Value = queue4_1.pop(0)

            self.eMGList.append(queue1Value)
            self.eMGList.append(queue2Value)
            self.eMGList.append(queue3Value)
            self.eMGList.append(queue4Value)

            for i in range(4):
                self.eMGList.pop(0)

        else:
            self.eMGList.clear()
            for i in range(8):
                queue1Value = queue1_1.pop(0)
                queue2Value = queue2_1.pop(0)
                queue3Value = queue3_1.pop(0)
                queue4Value = queue4_1.pop(0)
            
                self.eMGList.append(queue1Value)
                self.eMGList.append(queue2Value)
                self.eMGList.append(queue3Value)
                self.eMGList.append(queue4Value)


        return self.eMGList


test1 = AdAlgoLists()

test1.FillEMGList(test1.eMGList)

class MAL():

    def __init__(self) -> None:
        self.eMGList = []
        self.prediction = 0

    def predict(self, eMGList):
        clf = load(r"C:\Users\Vinni\OneDrive\Dokumenter\GitHub\EMG-Prosthetic\Program\RF_Minimalized.joblib")
        self.prediction = clf.predict(np.asarray(eMGList).reshape(1,-1))

        return self.prediction

test2 = MAL()
test1.AddToEMGList(test1.eMGList)
print(test2.predict(test1.eMGList))
