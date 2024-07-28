from src.core.services.ModelServicesAppServices.dto.ModelServicesDto import ModelServicesDto
from src.core.services.ModelServicesAppServices.contract.ModelServices import ModelServices

import numpy as np
class ModelServicesAppServicesa(ModelServices):
    
    def __init__(self, model_service_dto:ModelServicesDto):
        self.tensor = model_service_dto.tensor
        self.model = model_service_dto.sess
        self.model_dto = model_service_dto
        
    def classifiy(self):

        input_name = self.model.get_inputs()[0].name

        output = self.model.run(None, {input_name: np.asarray(self.tensor.unsqueeze(dim=0)).astype(np.float32)})[0]

        predict = np.argmax(output)

        self.model_dto.responce = predict