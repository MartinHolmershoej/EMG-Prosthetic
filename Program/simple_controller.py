from Icontroller import IController
from simple_algorithm import SimpleAlgorithm
from motorController import MotorController


class SimpleController(IController):
    
    def __init__(self) -> None:
        self.algorithm = SimpleAlgorithm()
        self.motor = MotorController()
        self.firstRun = True
        
    
    def Analyse(self, queueList, gripGroup):
        if self.firstRun:
            self.firstRun = False
            self.algorithm.Baseline()
            
        result = self.algorithm.Analyse(queueList, gripGroup)
        self.motor.MoveHand(result)
