"""
APIS for dialect identification task
"""


import logging
from typing import List
from fastapi import HTTPException
from fastapi import APIRouter, status
#from configuration.config import settings


dialect_id_route = APIRouter()
logger = logging.getLogger(__name__)



