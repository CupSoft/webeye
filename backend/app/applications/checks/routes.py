import datetime

from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.applications.checks.schemas import CheckOut, CheckUpdate
from app.applications.checks.models import Check

from app.settings.config import settings

import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[CheckOut], status_code=200)
async def read_checks():
    """
    Get list of checks.
    """
    checks = await Check.all()
    
    return checks