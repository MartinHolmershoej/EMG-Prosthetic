from abstract_factory import AbstractFactory
from simple_algorithm import SimpleAlgorithm
import few_sensors, few_queues

class SimpleFactory(AbstractFactory):
    #Overwrites the abstract method, to create the simple mode
    def create_mode(self):
        return SimpleAlgorithm

    #Overwrites the abstract method, to create many sensors
    def create_sensors(self):
        sensorList = few_sensors.createList()
        return sensorList
    
    #Overwrites the abstract method, to create many queues
    def create_queues(self):
        queueList = few_queues.createQueues()
        return queueList