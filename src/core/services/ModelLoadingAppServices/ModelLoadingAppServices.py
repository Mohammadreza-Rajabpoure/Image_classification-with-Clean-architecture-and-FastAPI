from src.core.services.ModelLoadingAppServices.contract.ModelLoading import ModelLoad
from src.core.services.ModelLoadingAppServices.dto.ModelLoadingDTO import ModelLoadingDTO


import onnxruntime as ort


class ModelLoadingAppServices(ModelLoad):
    
    def __init__(self, model_loading_dto :ModelLoadingDTO) :
        self.path = model_loading_dto.model_path
        self.model_dto = model_loading_dto
        
        
    def load(self):
        
       sess = ort.InferenceSession(self.path, providers=['CPUExecutionProvider'])
       
       self.model_dto.model_ready = sess