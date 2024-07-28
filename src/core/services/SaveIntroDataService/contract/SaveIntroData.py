from abc import ABC, abstractmethod

class SaveintroData(ABC):

    @abstractmethod
    def save_to_storeg(self):
        
        pass

    @abstractmethod
    def get_path(self):

        pass