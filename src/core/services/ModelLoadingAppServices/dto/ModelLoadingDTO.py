from dataclasses import dataclass
from typing import Optional

@dataclass
class ModelLoadingDTO:

    model_path : str

    model_ready : Optional[str] = None

