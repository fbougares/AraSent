"""
APIS for Arabic dialect sentiment analysis
input : text 
output : detected a sentiment of the input text
"""

import logging
from fastapi import APIRouter, status
from sources.datamodel.dialects import InputText, Dialects


dialect_sent_route = APIRouter()
logger = logging.getLogger(__name__)



@dialect_sent_route.post("/sentiment", status_code=status.HTTP_200_OK)
def get_dialect_sentiments(dialectal_text: InputText, dial: Dialects):
    return {'input': dialectal_text.source_text, 'dialect': dial, 'sent': None}

