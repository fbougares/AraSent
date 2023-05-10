from enum import Enum
from pydantic import BaseModel


class InputText(BaseModel):
    source_text : str


class Dialects(str, Enum):
    lyb = 'libyan'
    tun = 'tunisian'
    irq = 'iraqi'
    ksa = 'saudi'
    alg = 'algerian'
    egy = 'egyptian'
    leb = 'lebanon'
    pal = 'palestinian'
    syr = 'syrian'


    



