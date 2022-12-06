from abstract_factory import AbstractFactory
from simple_controller import SimpleController
from few_sensors import FewSensors
import few_queues  

class SimpleFactory(AbstractFactory):
    
    def __init__(self) -> None:
        self.fewSensors = FewSensors()
        
    
    #Overwrites the abstract method, to create the simple mode
    def create_mode(self):
        return SimpleController()

    #Overwrites the abstract method, to create few sensors
    def create_channels(self):
        sensorList = self.fewSensors.createChannelList()
        return sensorList
    
    #Overwrites the abstract method, to create few queues
    def create_queues(self):
        queueList = few_queues.createQueues()
        return queueList