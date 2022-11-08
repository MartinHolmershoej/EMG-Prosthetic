from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def create_mode(self):
        pass
    
    @abstractmethod
    def create_sensors(self):
        pass