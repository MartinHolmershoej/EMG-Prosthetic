from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def create_mode(self):
        pass
    
    @abstractmethod
    def create_sensors(self):
        pass
    
    #might need a queue creation
    @abstractmethod
    def create_queues(self):
        pass