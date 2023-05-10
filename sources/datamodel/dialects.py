from enum import Enum
from pydantic import BaseModel


class InputText(BaseModel):
    source_text : str


class Dialects(str, Enum):
    libyan = 'libyan'
    tunisian = 'tunisian'
    iraqi = 'iraqi'
    saudi = 'saudi'
    algerian = 'algerian'
    egyptian = 'egyptian'
    lebanon = 'lebanon'
    palestinian = 'palestinian'
    syrian = 'syrian'


    



