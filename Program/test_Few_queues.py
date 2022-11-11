import unittest
import few_queues

class TestFewQueues(unittest.TestCase):
    
    def test_createSensors(self):
        i = few_queues.createQueues()
        self.assertEqual(len(i), 2)

if __name__ == '__main__':
    unittest.main()
