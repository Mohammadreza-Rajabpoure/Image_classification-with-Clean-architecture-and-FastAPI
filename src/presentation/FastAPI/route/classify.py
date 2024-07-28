from src.core.services.ImagePreprocesAppService.ImagePreprocesAppService import ImagePreprocesAppService
from src.core.services.ImagePreprocesAppService.Dto.ImagePreprocesDto import ImagePreprocesDto
from src.core.services.SaveIntroDataService.SaveIntroDataService import SaveintroDataService
from src.core.services.SaveIntroDataService.dto.SaveIntroDataDTO import SaveIntroDataDTO
from src.core.services.ModelLoadingAppServices.ModelLoadingAppServices import ModelLoadingAppServices
from src.core.services.ModelLoadingAppServices.dto.ModelLoadingDTO import ModelLoadingDTO
from src.presentation.FastAPI.config.ModelConfig import ModelConfig
from src.core.services.ModelServicesAppServices.ModelServicesAppServices import ModelServicesAppServicesa
from src.core.services.ModelServicesAppServices.dto.ModelServicesDto import ModelServicesDto
from src.infrastructure.mongodb import DBImpelemnt
from src.presentation.FastAPI.config.DbConfig import classifiyConfig
from src.presentation.FastAPI.APIexceptions.FileNotFoundError import FileNotFoundError
from src.core.services.SaveIntroDataService.execption.StoregFolderExistError import StoregFolderExistError
from src.core.services.SaveIntroDataService.execption.ImageExistError import ImageExistError
from src.core.services.ImagePreprocesAppService.exception.ImagePathError import ImagePathError
from src.core.services.ImagePreprocesAppService.exception.ImageShapeError import ImageShapeError
from src.core.services.ResponseStoregService.dto.ResponceStoregDTO import ResponceStoregDTO
from src.infrastructure.ResponseStoregService import ResponseStoregService
from src.presentation.FastAPI.config.DbConfig import classifiyConfig

from fastapi import HTTPException, UploadFile ,APIRouter
from pymongo import MongoClient
import os
import PIL
from PIL import Image

router_classify = APIRouter()

@router_classify.post('/classifiy')
def upload_image(image : UploadFile ):
    
    try:
        #get the file and save in storeg folder and return a path of image 
        save_service = SaveintroDataService(image=image)  
        save_service.save_to_storeg()
        save_service_dto = SaveIntroDataDTO(save_service.get_path())
        print(save_service_dto.image_path)
  
  
        #preprocess the image
  
        preproces_DTO = ImagePreprocesDto(image_path=save_service_dto.image_path)
     
        preproces = ImagePreprocesAppService(preproces_DTO)
         
        preproces.image_resize()
        preproces.image_to_tensor(preproces_DTO.resized_image)
     
        # load the model
        model_load_dto = ModelLoadingDTO(model_path=os.path.abspath(ModelConfig.MODEL_PATH))
        model_load_service = ModelLoadingAppServices(model_load_dto)
        model_load_service.load()
       
        # Inference 
  
        model_service_dto = ModelServicesDto(tensor=preproces_DTO.tensor,
                                             sess=model_load_dto.model_ready)
        
        model_service_service = ModelServicesAppServicesa(model_service_dto)
        model_service_service.classifiy()
        
        # save in Mongodb
        mongo_db = DBImpelemnt(LOCAL_HOSTE=classifiyConfig.LOCAL_HOSTE)      # create a DB
     
        
        collection = mongo_db.creat_db()
        
        responce_saver_dto = ResponceStoregDTO(responce=model_service_dto.responce,
                                               database=collection)
        responce_saver = ResponseStoregService(responce_saver_dto)
        
        responce = responce_saver.save_responce()
        
        return responce
        
    
    except (FileNotFoundError, PIL.UnidentifiedImageError, ValueError, TypeError):
         print('image file is empty')  

    except StoregFolderExistError as x :
         x.storeg_exist()
        
    except ImageExistError as x :
         x.image_exist()

    except ImagePathError as x:
         x.image_path()
    
    except ImageShapeError as x:
         x.file_Shape()


@router_classify.get('/classifiy')
def read_responce():

     connection = MongoClient(str(classifiyConfig.LOCAL_HOSTE))
     db = connection[str(classifiyConfig.DATABASE_NAME)]
     my_collection = db[str(classifiyConfig.COLLECTION_NAME)] 
     
     item_list = []

     for item in my_collection.find():
          d = {'id--{}'.format(item["_id"]): "responce : {}".format(item["responce"]) }
          item_list.append(d)
     
     

     if not item_list:
          raise HTTPException(status_code=404, detail='no item found')
     return item_list

