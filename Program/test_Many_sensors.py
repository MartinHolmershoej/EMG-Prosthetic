import unittest
import many_sensors

#can only be tested on the RPi, because of some of the imports
class TestFewSensors(unittest.TestCase):
    
    def test_createSensors(self):
        
        self.assertEqual(len(many_sensors.createList), 4)

if __name__ == '__main__':
    unittest.main()