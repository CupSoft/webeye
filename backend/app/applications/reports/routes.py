import datetime

from typing import List

from fastapi import APIRouter, HTTPException

from app.applications.reports.schemas import (
    ReportOut, ReportCreate
)
from app.applications.reports.models import Report

from app.applications.resources.models import ResourceNode

from app.core.base.utils import exclude_keys

from pydantic import UUID4

import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[ReportOut], status_code=200)
async def read_reports(
        skip: int = 0,
        limit: int = 100,
):
    """
    Get list of reports.
    """
    reports = await Report.all().limit(limit).offset(skip)

    return reports


@router.post("/", response_model=ReportOut, status_code=201)
async def create_check(
        report_in: ReportCreate
):
    """
    Create a report
    """

    report = await Report.filter(uuid=report_in.uuid).first()

    if report is not None:
        raise HTTPException(
            status_code=400,
            detail="The report with this uuid already exist",
        )

    resource_node = await ResourceNode.filter(uuid=report_in.resource_node_uuid).first()

    if resource_node is None:
        raise HTTPException(
            status_code=404,
            detail="The resource node with this id does not exist",
        )

    report = await Report.create(
        **exclude_keys(report_in.dict(), {'resource_node_uuid'}), resource_node=resource_node
    )

    return report


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
            detail="The check result with this uuid already exist",
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
