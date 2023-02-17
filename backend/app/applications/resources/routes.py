from app.applications.resources.models import Resource
from app.applications.resources.schemas import ResourceOut

from typing import List

from fastapi import APIRouter, HTTPException

from pydantic import UUID4

import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[ResourceOut], status_code=200, tags=['resources'])
async def read_resources():
    """
    Get resource list.
    """
    resources = await Resource.all()
    
    return resources


@router.get("/{id}", response_model=ResourceOut, status_code=200, tags=['resources'])
async def read_resources(id: UUID4):
    """
    Get resource by id.
    """
    resource = await Resource.filter(hashed_id=id).first()
    
    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this id does not exist in system",
        )
    
    return resource