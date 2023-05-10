"""
APIS for Arabic dialect identification
input : text 
output : detected dialect of the input text
"""

import logging
from typing import List
from fastapi import HTTPException
from fastapi import APIRouter, status
from sources.datamodel.dialects import InputText, Dialects


dialect_id_route = APIRouter()
logger = logging.getLogger(__name__)



@dialect_id_route.get("/dialects", status_code=status.HTTP_200_OK)
def get_list_dialects():
    return [dial.value for dial in Dialects]


@dialect_id_route.post("/dialect_id", status_code=status.HTTP_200_OK)
def dialect_identification(dialectal_text: InputText):
    return len(dialectal_text.source_text)



