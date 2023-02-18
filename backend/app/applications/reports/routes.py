from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.applications.reports.schemas import (
    ReportOut, ReportCreate
)
from app.applications.reports.models import Report

from app.applications.users.models import User

from app.applications.resources.models import Resource
from app.core.auth.utils.contrib import get_current_admin, get_current_user

from app.core.base.utils import exclude_keys

from pydantic import UUID4

import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[ReportOut], status_code=200)
async def read_reports(
        skip: int = 0,
        limit: int = 100,
        current_user: User = Depends(get_current_admin)
):
    """
    Get list of reports.
    """
    reports = await Report.all().limit(limit).offset(skip)

    return reports


@router.post("/", response_model=ReportOut, status_code=201)
async def create_report(
        report_in: ReportCreate,
        current_user: User = Depends(get_current_user)
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

    resource = await Resource.filter(uuid=report_in.resource_uuid).first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    report = await Report.create(
        **exclude_keys(report_in.dict(), {'resource_uuid', 'user_uuid'}), user=current_user, resource=resource
    )

    return report


@router.delete("/{uuid}", status_code=200)
async def delete_report(
        uuid: UUID4,
        current_user: User = Depends(get_current_admin)
):
    """
    Delete report by uuid.
    """
    report = await Report.filter(uuid=uuid).first()

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="The report with this uuid does not exist",
        )

    await report.delete()

    return "Successfully deleted"
