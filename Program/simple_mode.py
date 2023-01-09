from Icontroller import IController
from simple_algorithm import SimpleAlgorithm
from motorController import MotorController


class SimpleMode(IController):
    
    def __init__(self, motor) -> None:
        self.algorithm = SimpleAlgorithm()
        self.motor = motor
        self.firstRun = True
        self.gripGroup = 1
        
    
    def Analyse(self, queueList):
        if self.firstRun:
            self.firstRun = False
            self.algorithm.Baseline(queueList)
            
        result = self.algorithm.Analyse(queueList, self.gripGroup)
        self.motor.MoveHand(result)
