import unittest
from multiprocessing import Queue
import advanced_algorithm 

class TestAdvancedAlgorithm(unittest.TestCase):

    #help function for filling up the queue
    def fillQueueForAnalyse(self):
        self.queueList = []
        self.q1 = Queue(maxsize=0)
        self.q2 = Queue(maxsize=0)
        self.q3 = Queue(maxsize=0)
        self.q4 = Queue(maxsize=0)
        
        for i in range(4):
            self.q1.put(0.400)
            self.q2.put(0.400)
            self.q3.put(0.450)
            self.q4.put(0.400)
            self.q1.put(0.400)
            self.q2.put(0.400)
            self.q3.put(0.400)
            self.q4.put(0.400)
        
        self.queueList = [self.q1, self.q2, self.q3, self.q4]
        return self.queueList

    #help function for filling up eMGList
    def fillEMGListForAnalyse(self, x):
        self.eMGList = []

        self.l1 = [70, 50, 60, 80, 70, 50, 60, 80]
        self.l2 = [70, 55, 60, 80, 70, 50, 60, 80]
        self.l3 = [70, 65, 70, 75, 70, 50, 60, 80]
        self.l4 = [70, 60, 50, 70, 70, 50, 60, 80]
        
        for i in range(x):
            queue1Value = self.l1.pop(0)
            queue2Value = self.l2.pop(0)
            queue3Value = self.l3.pop(0)
            queue4Value = self.l4.pop(0)
            
            self.eMGList.append(queue1Value)
            self.eMGList.append(queue2Value)
            self.eMGList.append(queue3Value)
            self.eMGList.append(queue4Value)
        
        return self.eMGList

    def test_AddToEMGList_Empty_eMGList(self):
        advanced = advanced_algorithm.AdvancedAlgorithm()
        QList = self.fillQueueForAnalyse()
        EMGList = self.fillEMGListForAnalyse(0)
        advanced.AddToEMGList(QList, EMGList)
        self.assertEqual(advanced.eMGList, [0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400])

    def test_AddToEMGList_eMGList_not_lenght32(self):
        advanced = advanced_algorithm.AdvancedAlgorithm()
        QList = self.fillQueueForAnalyse()
        EMGList = self.fillEMGListForAnalyse(6)
        advanced.AddToEMGList(QList, EMGList)
        self.assertEqual(advanced.eMGList, [0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400])

    def test_AddToEMGList_eMGList_lenght32(self):
        advanced = advanced_algorithm.AdvancedAlgorithm()
        QList = self.fillQueueForAnalyse()
        EMGList = self.fillEMGListForAnalyse(8)
        advanced.AddToEMGList(QList, EMGList)
        self.assertEqual(advanced.eMGList, [70, 70, 70, 70, 50, 55, 65, 60, 60, 60, 70, 50, 80, 80, 75, 70, 70, 70, 70, 70, 50, 50, 50, 50, 60, 60, 60, 60, 0.400, 0.400, 0.400, 0.400])
        
        
if __name__ == '__main__':
    unittest.main()