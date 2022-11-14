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


    def test_Baseline(self):
        self.fillQueueForBaseline()
        simple_algorithm.SimpleAlgorithm.Baseline(self.queueList)
        self.assertEqual(simple_algorithm.baseline_1, simple_algorithm.baseline_2, (0.65, 0.750))


    def test_Analyse_Upper_gripGroup_1(self):
        gripGroup = 1
        self.fillQueueForAnalyse(0.700, 0.500)
        self. assertEqual(simple_algorithm.SimpleAlgorithm.Analyse(self.queueList, gripGroup),1)
    
    def test_Analyse_Upper_gripGroup_2(self):
        gripGroup = 2
        self.fillQueueForAnalyse(0.700, 0.500)
        self. assertEqual(simple_algorithm.SimpleAlgorithm.Analyse(self.queueList, gripGroup),3)
    
    def test_Analyse_Upper_gripGroup_3(self):
        gripGroup = 3
        self.fillQueueForAnalyse(0.700, 0.500)
        self. assertEqual(simple_algorithm.SimpleAlgorithm.Analyse(self.queueList, gripGroup),5) 
        
    def test_Analyse_Lower_gripGroup_1(self):
        gripGroup = 1
        self.fillQueueForAnalyse(0.500, 0.800)
        self. assertEqual(simple_algorithm.SimpleAlgorithm.Analyse(self.queueList, gripGroup),2)
    
    def test_Analyse_Lower_gripGroup_2(self):
        gripGroup = 2
        self.fillQueueForAnalyse(0.500, 0.800)
        self. assertEqual(simple_algorithm.SimpleAlgorithm.Analyse(self.queueList, gripGroup),4)
    
    def test_Analyse_Lower_gripGroup_3(self):
        gripGroup = 3
        self.fillQueueForAnalyse(0.500, 0.800)
        self. assertEqual(simple_algorithm.SimpleAlgorithm.Analyse(self.queueList, gripGroup),6)

        
    def test_Analyse_return0_value1_True(self):
        gripGroup = 1
        self.fillQueueForAnalyse(0.700, 0.800)        
        self. assertEqual(simple_algorithm.SimpleAlgorithm.Analyse(self.queueList, gripGroup),0)
    
    
    def test_Analyse_return0_value2_True(self):
        gripGroup = 1
        self.fillQueueForAnalyse(0.700, 0.800)        
        self. assertEqual(simple_algorithm.SimpleAlgorithm.Analyse(self.queueList, gripGroup),0)
        
    
    
    
if __name__ == '__main__':
    unittest.main()
