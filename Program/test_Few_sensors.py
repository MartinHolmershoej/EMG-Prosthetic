import unittest
import few_sensors

#can only be tested on the RPi, because of some of the imports
class TestFewSensors(unittest.TestCase):
    
    def test_createSensors(self):
        
        sensor = few_sensors.FewSensors()  
        clist = sensor.createChannelList()      
        self.assertEqual(len(clist), 2)

if __name__ == '__main__':
    unittest.main()
      