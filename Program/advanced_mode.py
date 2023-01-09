from Icontroller import IController
from motorController import MotorController
from advanced_algorithm import AdvancedAlgorithm


class AdvancedMode(IController):
    
    def __init__(self, motor) -> None:
        self.motor = motor
        self.algorithm = AdvancedAlgorithm()
    
    def Analyse(self, queueList):
        self.algorithm.AddToEMGList(queueList)
        result = self.algorithm.Analyse()
        self.motor.MoveHand(result)