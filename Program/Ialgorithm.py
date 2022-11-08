from abc import ABC, abstractmethod


class IAlgorithm(ABC):

    @abstractmethod
    def Analyse(queue, queue2):
        pass