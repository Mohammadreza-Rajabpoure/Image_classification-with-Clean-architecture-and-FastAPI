from dataclasses import dataclass
from typing import Optional


@dataclass
class ImagePreprocesDto:
    # input
    image_path : str

    resize_size : tuple = (227,227)
    
    #output
    resized_image : Optional[object] = None

    tensor : Optional[list] = None 

