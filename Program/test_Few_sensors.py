import unittest
import few_sensors

#can only be tested on the RPi, because for some imports
class TestFewSensors(unittest.TestCase):
    
    def test_createSensors(self):
        
        self.assertEqual(len(few_sensors.createList), 2)

if __name__ == '__main__':
    unittest.main()
      