from app.applications.resources.models import Resource
from app.applications.resources.schemas import ResourceOut

from app.core.auth.utils.contrib import get_current_admin, get_current_user

from app.applications.users.models import User

from typing import List

from fastapi import APIRouter, HTTPException, Depends

from pydantic import UUID4

import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[ResourceOut], status_code=200)
async def read_resources(
    skip: int = 0,
    limit: int = 100,
):
    """
    Get resource list.
    """
    resources = await Resource.all().limit(limit).offset(skip)
    
    return resources


@router.get("/{uuid}", response_model=ResourceOut, status_code=200)
async def read_resources(
    uuid: UUID4,
):
    """
    Get resource by uuid.
    """
    resource = await Resource.filter(uuid=uuid).first()
    
    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this id does not exist",
        )
    
    return resource