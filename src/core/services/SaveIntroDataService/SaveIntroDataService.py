from src.core.services.SaveIntroDataService.contract.SaveIntroData import SaveintroData
from src.core.services.SaveIntroDataService.dto.SaveIntroDataDTO import SaveIntroDataDTO
import os
from src.core.services.SaveIntroDataService.execption.StoregFolderExistError import StoregFolderExistError
from src.core.services.SaveIntroDataService.execption.ImageExistError import ImageExistError


import os
import shutil
from PIL import Image
import pathlib




class SaveintroDataService(SaveintroData):

    def __init__(self, image) :
           
        self.image = image


    def save_to_storeg(self):

         if os.path.exists(os.path.abspath('storeg'))!=False:
             
            with open(os.path.join(os.path.abspath('storeg'), self.image.filename)  , 'wb') as buffer:
                shutil.copyfileobj(self.image.file, buffer)       
             
         else:
             raise StoregFolderExistError
                       
             
   
    def get_path(self):

        path = os.path.join(os.path.abspath('storeg'), self.image.filename)
        
        with Image.open(path) as x :
            x.verify()
        if not os.path.exists(path):
            raise ImageExistError

        return path