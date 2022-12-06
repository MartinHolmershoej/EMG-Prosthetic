from abc import ABC, abstractmethod

class IController(ABC):
    
    @abstractmethod
    def Analyse(self):
        pass