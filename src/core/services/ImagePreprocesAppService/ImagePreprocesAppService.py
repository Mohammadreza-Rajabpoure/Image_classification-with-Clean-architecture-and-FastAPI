from src.core.services.ImagePreprocesAppService.contract.ImagePreproces import ImagePreproces
from src.core.services.ImagePreprocesAppService.Dto.ImagePreprocesDto import ImagePreprocesDto
from src.core.services.ImagePreprocesAppService.exception.ImagePathError import ImagePathError
from src.core.services.ImagePreprocesAppService.exception.ImageShapeError import ImageShapeError

from torchvision import transforms
import os
from PIL import Image


class ImagePreprocesAppService(ImagePreproces):
    
    def __init__(self,image_preproces_dto:ImagePreprocesDto) :
        self.image = image_preproces_dto.image_path
        self.resize = image_preproces_dto.resize_size
        self.dto = image_preproces_dto

        if not os.path.exists(self.image):
            raise ImagePathError
          

    def image_resize(self):
        load_image = Image.open(self.image)

        if load_image.mode != 'L':
            raise ImageShapeError

        T = transforms.Compose([transforms.Resize(self.resize)])
        resized_image = T(load_image)
        self.dto.resized_image = resized_image
    

    def image_to_tensor(self,image):
      
      T = transforms.Compose([transforms.ToTensor()])
      tensor = T(image)

      self.dto.tensor = tensor

    