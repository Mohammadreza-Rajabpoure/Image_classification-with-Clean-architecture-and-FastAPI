from dataclasses import dataclass
from typing import Optional


@dataclass
class ResponceStoregDTO:

    responce : str

    database : Optional[str] = None