from src.core.services.ResponseStoregService.ResponceStoreg import ResponceStoreg
from src.core.services.ModelServicesAppServices.dto.ModelServicesDto import ModelServicesDto
from src.core.services.ResponseStoregService.dto.ResponceStoregDTO import ResponceStoregDTO

class ResponseStoregService(ResponceStoreg):
     
     def __init__(self, res : ResponceStoregDTO):
         self.responce = res.responce
         self.db = res.database
    


     def save_responce(self):

        
        item_dict ={'responce':str(self.responce)}
        result = self.db.insert_one(item_dict)
        item_dict["_id"] = str(result.inserted_id)
        return item_dict

