from abc import ABC, abstractmethod

class ModelLoad (ABC):
    
    @abstractmethod
    def load(self):
        pass
    