from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.applications.social_reports.schemas import SocialReportCreate, SocialReportOut
from app.applications.social_reports.models import SocialNetworks, SocialNetworkReport

from app.applications.users.models import User

from app.applications.resources.models import Resource
from app.core.auth.utils.contrib import get_current_admin, get_current_user

from app.core.base.utils import exclude_keys

from pydantic import UUID4

import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[SocialReportOut], status_code=200)
async def read_social_reports(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_admin),
):
    """
    Retrieve social reports.
    """
    social_reports = await SocialNetworkReport.all().limit(limit).offset(skip)
    return social_reports


@router.post("/", response_model=SocialReportOut, status_code=201)
async def create_social_report(
    *,
    social_report_in: SocialReportCreate,
    current_user: User = Depends(get_current_admin),
):
    """
    Create new social report.
    """
    resource = await Resource.filter(uuid=social_report_in.resource_uuid).first()
    if not resource:
        raise HTTPException(
            status_code=400,
            detail="The resource with this uuid does not exist",
        )

    created_social_report = await SocialNetworkReport.create(
        **social_report_in.dict(exclude={"resource_uuid"}), resource=resource
    )

    response_dict = await created_social_report.to_dict()

    return SocialReportOut(**response_dict, resource_uuid=resource.uuid)
