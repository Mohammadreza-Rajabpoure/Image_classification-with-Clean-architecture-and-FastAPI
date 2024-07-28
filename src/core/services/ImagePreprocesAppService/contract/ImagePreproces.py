from abc import ABC, abstractmethod




class ImagePreproces(ABC):
    
    @abstractmethod
    
    def image_resize(self):
        pass
    
    @abstractmethod
    
    def image_to_tensor(self):
        pass