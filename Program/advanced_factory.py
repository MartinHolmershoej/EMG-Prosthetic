from abstract_factory import AbstractFactory
from advanced_mode import AdvancedMode
from many_sensors import ManySensors
import many_queues

class AdvancedFactory(AbstractFactory):
    def __init__(self) -> None:
        self.manySensors = ManySensors()
        
    #Overwrites the abstract method, to create advanced mode
    def create_mode(self, motor):
        return AdvancedMode(motor)

    #Overwrites the abstract method, to create many sensors
    def create_channels(self):
        sensorList = self.manySensors.createChannelList()
        return sensorList
    
    #Overwrites the abstract method, to create many queuea
    def create_queues(self):
        queueList = many_queues.createQueues()
        return queueList