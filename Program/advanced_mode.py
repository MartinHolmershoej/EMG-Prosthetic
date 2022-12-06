from Icontroller import IController
from motorController import MotorController
from advanced_algorithm import AdvancedAlgorithm


class AdvancedMode(IController):
    
    def __init__(self) -> None:
        self.motor = MotorController()
        self.algorithm = AdvancedAlgorithm()
    
    def Analyse(self, queueList, eMGList):
        self.algorithm.AddToEMGList(queueList, eMGList)
        result = self.algorithm.Analyse()
        self.motor.MoveHand(result)