from abc import ABC, abstractmethod

class ModelServices(ABC):
    
    @abstractmethod
    def classifiy(self):
        pass
