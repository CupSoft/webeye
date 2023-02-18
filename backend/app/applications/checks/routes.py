import datetime

from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.applications.checks.schemas import CheckOut, CheckUpdate, CheckCreate
from app.applications.checks.models import Check

from app.applications.resources.models import ResourceNode

from app.settings.config import settings

from app.core.base.utils import exclude_keys

import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[CheckOut], status_code=200)
async def read_checks(
    skip: int = 0,
    limit: int = 100,
):
    """
    Get check list.
    """
    checks = await Check.all().limit(limit).offset(skip)
    
    return checks


@router.post("/", response_model=CheckOut, status_code=201)
async def create_resource(
    check_in: CheckCreate
):
    """
    Create a check
    """
    
    print(check_in.dict())

    check = await Check.filter(uuid=check_in.uuid).first()

    if check is not None:
        raise HTTPException(
            status_code=400,
            detail="The check with this id allready exist",
        )
    
    resource_node = await ResourceNode.filter(uuid=check_in.resource_node_uuid).first()
    
    if resource_node is None:
        raise HTTPException(
            status_code=404,
            detail="The resource node with this id does not exist",
        )
    
    check = await Check.create(
        **exclude_keys(check_in.dict(), {'resource_node_uuid'}), resource_node=resource_node
    )
    
    return check

