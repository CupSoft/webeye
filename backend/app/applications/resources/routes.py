from fastapi import BackgroundTasks

from app.core.auth.utils.contrib import get_current_active_superuser, send_new_account_email, get_current_active_user
from app.core.auth.utils.password import get_password_hash

from app.applications.users.models import User
from app.applications.users.schemas import BaseUserOut, BaseUserCreate, BaseUserUpdate

from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.applications.resources.models import Resource

from app.settings.config import settings

import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[BaseUserOut], status_code=200, tags=['resources'])
async def read_resources():
    """
    Get resource list.
    """
    users = await Resource.all()
    return users