import datetime

from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.applications.checks.schemas import (
    CheckOut, CheckCreate, CheckResultCreate, CheckResultOut, CheckOutWithUrl
)
from app.applications.checks.models import Check, CheckResult

from app.applications.resources.models import ResourceNode

from app.core.base.utils import exclude_keys

from pydantic import UUID4

import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[CheckOutWithUrl], status_code=200)
async def read_checks(
    skip: int = 0,
    limit: int = 100,
):
    """
    Get check list.
    """
    checks = await Check.all().limit(limit).offset(skip).prefetch_related('resource_node')
    
    res = []
    for check in checks:
        dict_check = await check.to_dict()
        dict_check['url'] =  check.resource_node.url
        res.append(dict_check)
    
    return res


@router.post("/", response_model=CheckOut, status_code=201)
async def create_check(
    check_in: CheckCreate
):
    """
    Create a check
    """

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


@router.delete("/{uuid}", status_code=200)
async def delete_check(
    uuid: UUID4,
):
    """
    Delete check by uuid.
    """
    check = await Check.filter(uuid=uuid).first()
    
    if check is None:
        raise HTTPException(
            status_code=404,
            detail="The check with this id does not exist",
        )
    
    await check.delete()

    return "Successfully deleted"


@router.post("/results/", response_model=CheckResultOut, status_code=201)
async def create_check_result(
    check_result_in: CheckResultCreate
):
    """
    Create a check result
    """

    check_result = await CheckResult.filter(uuid=check_result_in.uuid).first()

    if check_result is not None:
        raise HTTPException(
            status_code=400,
            detail="The check result with this id allready exist",
        )
    
    check = await Check.filter(uuid=check_result_in.check_uuid).first()
    
    if check is None:
        raise HTTPException(
            status_code=404,
            detail="The check with this id does not exist",
        )
    
    check_result = await CheckResult.create(
        **exclude_keys(check_result_in.dict(), {'check_uuid'}), parent_check=check
    )
    
    return check_result


@router.delete("/result/{uuid}", status_code=200)
async def delete_check(
    uuid: UUID4,
):
    """
    Delete check result by uuid.
    """
    check_result = await CheckResult.filter(uuid=uuid).first()
    
    if check_result is None:
        raise HTTPException(
            status_code=404,
            detail="The check result with this id does not exist",
        )
    
    await check_result.delete()

    return "Successfully deleted"
