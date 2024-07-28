from dataclasses import dataclass
from typing import Optional

@dataclass
class ModelServicesDto:
   
   tensor : list 
   sess :  Optional[str] = None
   responce : Optional[int] = None
