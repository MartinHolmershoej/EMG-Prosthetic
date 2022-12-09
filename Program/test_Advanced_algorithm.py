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


    def test_AddToEMGList_Empty_eMGList(self):
        advanced = advanced_algorithm.AdvancedAlgorithm()
        QList = self.fillQueueForAnalyse()
        advanced.eMGList = []
        advanced.AddToEMGList(QList)
        self.assertEqual(advanced.eMGList, [0.400, 0.400, 0.450, 0.400, 0.400, 
        0.400, 0.400, 0.400, 0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 
        0.400, 0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 
        0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400])

    def test_AddToEMGList_eMGList_not_lenght32(self):
        advanced = advanced_algorithm.AdvancedAlgorithm()
        QList = self.fillQueueForAnalyse()
        advanced.eMGList = [70, 70, 70, 70, 50, 55, 65, 60, 60, 60, 70, 50, 80, 80]
        advanced.AddToEMGList(QList)
        self.assertEqual(advanced.eMGList, [0.400, 0.400, 0.450, 0.400, 0.400, 
        0.400, 0.400, 0.400, 0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 
        0.400, 0.400, 0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 
        0.400, 0.450, 0.400, 0.400, 0.400, 0.400, 0.400])

    def test_AddToEMGList_eMGList_lenght32(self):
        advanced = advanced_algorithm.AdvancedAlgorithm()
        QList = self.fillQueueForAnalyse()
        advanced.eMGList = [70, 70, 70, 70, 50, 55, 65, 60, 60, 60, 70, 50, 80, 
        80, 75, 70, 70, 70, 70, 70, 50, 50, 50, 50, 60, 60, 60, 60, 70, 60, 90, 70]
        advanced.AddToEMGList(QList)
        self.assertEqual(advanced.eMGList, [50, 55, 65, 60, 60, 60, 70, 50, 80, 
        80, 75, 70, 70, 70, 70, 70, 50, 50, 50, 50, 60, 60, 60, 60, 70, 60, 90, 
        70, 0.400, 0.400, 0.450, 0.400])
        
        
if __name__ == '__main__':
    unittest.main()