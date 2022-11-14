import unittest
import many_queues

class TestFewQueues(unittest.TestCase):
    
    def test_createSensors(self):
        i = many_queues.createQueues()
        self.assertEqual(len(i), 4)

if __name__ == '__main__':
    unittest.main()
