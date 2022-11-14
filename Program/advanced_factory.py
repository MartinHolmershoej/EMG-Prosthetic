from abstract_factory import AbstractFactory
from advanced_algorithm import AdvancedAlgorithm
import many_sensors, many_queues

class AdvancedFactory(AbstractFactory):
    #Overwrites the abstract method, to create advanced mode
    def create_mode():
        return AdvancedAlgorithm

    #Overwrites the abstract method, to create many sensors
    def create_sensors():
        sensorList = many_sensors.createList()
        return sensorList
    
    #Overwrites the abstract method, to create many queuea
    def create_queues(self):
        queueList = many_queues.createQueues()
        return queueList