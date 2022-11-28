import unittest
from multiprocessing import Queue
import simple_algorithm 

class TestSimpleAlgorithm(unittest.TestCase):
    
    #help function for filling up the queue
    def fillQueueForAnalyse(self, value1, value2):
        self.queueList = []
        self.q1 = Queue(maxsize=0)
        self.q2 = Queue(maxsize=0)
        
        self.q1.put(value1)
        self.q2.put(value2)
        
        self.queueList = [self.q1, self.q2]
        return self.queueList
    
    #help function for filling up the queue
    def fillQueueForBaseline(self):
        self.queueList = []
        self.q1 = Queue(maxsize=0)
        self.q2 = Queue(maxsize=0)
        
        for x in range(10):
            self.q1.put(0.600)
            self.q2.put(0.700)
            self.q1.put(0.700)
            self.q2.put(0.800)
        
        self.queueList = [self.q1, self.q2]
        return self.queueList


    def test_Baseline(self):
        simple = simple_algorithm.SimpleAlgorithm()
        QList = self.fillQueueForBaseline()
        simple.Baseline(QList)
        self.assertEqual((simple.baseline_1, simple.baseline_2), (1.17, 0.9))


    def test_Analyse_Upper_gripGroup_1(self):
        gripGroup = 1
        simple = simple_algorithm.SimpleAlgorithm()
        QList = self.fillQueueForAnalyse(1.3, 0.500)
        simple.Analyse(QList, gripGroup)
        self.assertEqual(simple.result, 1)
    
    def test_Analyse_Upper_gripGroup_2(self):
        gripGroup = 2
        simple = simple_algorithm.SimpleAlgorithm()
        QList = self.fillQueueForAnalyse(1.3, 0.500)
        simple.Analyse(QList, gripGroup)
        self.assertEqual(simple.result, 3)
    
    def test_Analyse_Upper_gripGroup_3(self):
        gripGroup = 3
        simple = simple_algorithm.SimpleAlgorithm()
        QList = self.fillQueueForAnalyse(1.3, 0.500)
        simple.Analyse(QList, gripGroup)
        self.assertEqual(simple.result, 5)
        
    def test_Analyse_Lower_gripGroup_1(self):
        gripGroup = 1
        simple = simple_algorithm.SimpleAlgorithm()
        QList = self.fillQueueForAnalyse(1, 1)
        simple.Analyse(QList, gripGroup)
        self.assertEqual(simple.result, 2)
    
    def test_Analyse_Lower_gripGroup_2(self):
        gripGroup = 2
        simple = simple_algorithm.SimpleAlgorithm()
        QList = self.fillQueueForAnalyse(1, 1)
        simple.Analyse(QList, gripGroup)
        self.assertEqual(simple.result, 4)
    
    def test_Analyse_Lower_gripGroup_3(self):
        gripGroup = 3
        simple = simple_algorithm.SimpleAlgorithm()
        QList = self.fillQueueForAnalyse(1, 1)
        simple.Analyse(QList, gripGroup)
        self.assertEqual(simple.result, 6)

        
    def test_Analyse_return0_value1_True(self):
        gripGroup = 1
        simple = simple_algorithm.SimpleAlgorithm()
        QList = self.fillQueueForAnalyse(1.3, 1)
        simple.Analyse(QList, gripGroup)      
        self.assertEqual(simple.result, 0)
    
    
    def test_Analyse_return0_value2_True(self):
        gripGroup = 1
        simple = simple_algorithm.SimpleAlgorithm()
        QList = self.fillQueueForAnalyse(1.3, 1)
        simple.Analyse(QList, gripGroup)      
        self.assertEqual(simple.result, 0)
        
    
    
    
if __name__ == '__main__':
    unittest.main()
