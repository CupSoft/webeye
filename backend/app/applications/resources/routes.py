import datetime

from app.applications.checks.models import Check, CheckResult
from app.applications.resources.models import Resource, ResourceNode
from app.applications.resources.schemas import (
    ResourceOut,
    ResourceCreate,
    ResourceUpdate,
    ResourceNodeOut,
    ResourceNodeCreate,
    ResourceOutWithRating,
    ResourceNodeOutWithResourceUUID,
    ResourceStatsOut,
    Status,
    IsDDOS,
)
from app.applications.reports.schemas import ReportOut
from app.applications.social_reports.schemas import SocialReportOut
from app.applications.reviews.schemas import ReviewOut
from app.core.auth.utils.contrib import get_current_admin, get_current_user

from app.applications.users.models import User

from typing import List

import pandas as pd
import io

from fastapi import APIRouter, HTTPException, Depends, Response

from pydantic import UUID4

import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[ResourceOutWithRating], status_code=200)
async def read_resources(skip: int = 0, limit: int = 100):
    """
    Get resource list.
    """
    resources = await Resource.all().prefetch_related("reviews").limit(limit).offset(skip)
    resources = sorted(resources, key=lambda r: len(r.reviews), reverse=True)
    res = []
    for resource in resources:
        resource_dict = await resource.to_dict()
        rating = await resource.rating
        url = await resource.url
        res.append(ResourceOutWithRating(**resource_dict, rating=rating, url=url))

    return res


@router.get("/is_ddos", response_model=IsDDOS, status_code=200)
async def is_ddos_handler():
    try:
        return IsDDOS(is_ddos=(await Resource.exclude(status=Status.ok).count() / await Resource.all().count()) > 0.5)
    except:
        return IsDDOS(is_ddos=False)


@router.post("/", response_model=ResourceOut, status_code=201)
async def create_resource(
    resource_in: ResourceCreate,
    current_user: User = Depends(get_current_admin),
):
    """
    Create a resource
    """
    resource = await Resource.get_by_name(name=resource_in.name)

    if resource is not None:
        raise HTTPException(
            status_code=400,
            detail="The resource with this name already exist",
        )

    resource = await Resource.create(**resource_in.dict())

    resource_dict = await resource.to_dict()
    return ResourceOut(**resource_dict)


@router.get("/{uuid}", response_model=ResourceOutWithRating, status_code=200)
async def read_resource(
    uuid: UUID4,
):
    """
    Get resource by uuid.
    """
    resource: Resource = await Resource.filter(uuid=uuid).first().prefetch_related("reviews")

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    resource_dict = await resource.to_dict()

    rating = await resource.rating
    url = await resource.url

    return ResourceOutWithRating(**resource_dict, rating=rating, url=url)


@router.get("/{uuid}/stats/checks", response_model=List[ResourceStatsOut], status_code=200)
async def read_resource_checks_stats(uuid: UUID4, timedelta: datetime.timedelta, max_count: int = 10):
    """
    Get resource checks stats.
    """
    resource = await Resource.filter(uuid=uuid).first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    resource_checks_stats = []

    for i in range(max_count):
        end_datetime = datetime.datetime.now() - timedelta * i
        start_datetime = end_datetime - timedelta

        ok_count = 0
        partial_count = 0
        critical_count = 0

        for node in await resource.nodes.all():
            for check in await node.checks.all():
                check: Check
                for result in await check.results.filter(datetime__gte=start_datetime, datetime__lt=end_datetime).all():
                    result: CheckResult
                    if result.status == Status.ok:
                        ok_count += 1
                    elif result.status == Status.partial:
                        partial_count += 1
                    elif result.status == Status.critical:
                        critical_count += 1

        resource_checks_stats.append(
            ResourceStatsOut(
                end_datetime=end_datetime,
                ok=ok_count,
                partial=partial_count,
                critical=critical_count,
            )
        )

    return resource_checks_stats[::-1]


@router.get("/{uuid}/stats/reports", response_model=List[ResourceStatsOut], status_code=200)
async def read_resource_reports_stats(uuid: UUID4, timedelta: datetime.timedelta, max_count: int = 10):
    """
    Get resource reports stats.
    """
    resource = await Resource.filter(uuid=uuid).first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    resource_reports_stats = []

    for i in range(max_count):
        end_datetime = datetime.datetime.now() - timedelta * i
        start_datetime = end_datetime - timedelta

        ok_count = 0
        partial_count = 0
        critical_count = 0

        for report in await resource.reports.filter(datetime__gte=start_datetime, datetime__lt=end_datetime).all():
            report: ReportOut
            if report.status == Status.ok:
                ok_count += 1
            elif report.status == Status.partial:
                partial_count += 1
            elif report.status == Status.critical:
                critical_count += 1

        resource_reports_stats.append(
            ResourceStatsOut(
                end_datetime=end_datetime,
                ok=ok_count,
                partial=partial_count,
                critical=critical_count,
            )
        )

    return resource_reports_stats[::-1]


@router.patch("/{uuid}", response_model=ResourceOut, status_code=201)
async def update_resource(
    uuid: UUID4,
    resource_in: ResourceUpdate,
    current_user: User = Depends(get_current_admin),
):
    """
    Update a resource
    """
    resource = await Resource.filter(uuid=uuid).first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this name does not exist",
        )

    if resource_in.name is not None:
        resource_name = await Resource.get_by_name(name=resource_in.name)

        if resource_name is not None:
            raise HTTPException(
                status_code=400,
                detail="The resource with this name already exist",
            )

        resource.name = resource_in.name

    await resource.save()

    resource_dict = await resource.to_dict()
    return ResourceOut(**resource_dict)


@router.delete("/{uuid}", status_code=200)
async def delete_resource(
    uuid: UUID4,
    current_user: User = Depends(get_current_admin),
):
    """
    Delete resource by uuid.
    """
    resource = await Resource.filter(uuid=uuid).first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    await resource.delete()

    return "Successfully deleted"


@router.get("/{uuid}/nodes", response_model=List[ResourceNodeOut], status_code=200)
async def read_resource_nodes(
    uuid: UUID4,
    current_user: User = Depends(get_current_admin),
):
    """
    Get resource nodes by uuid.
    """
    resource = await Resource.filter(uuid=uuid).prefetch_related("nodes").first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    return list(resource.nodes)


@router.get("/{uuid}/reports", response_model=List[ReportOut], status_code=200)
async def read_resource_reports(
    uuid: UUID4,
):
    """
    Get resource reports by uuid.
    """
    resource = await Resource.filter(uuid=uuid).prefetch_related("reports").first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    return list(resource.reports)


@router.get("/{uuid}/social_reports", response_model=List[SocialReportOut], status_code=200)
async def read_resource_social_reports(
    uuid: UUID4,
    is_moderated: bool = False,
):
    """
    Get resource social reports by uuid.
    """
    resource = await Resource.filter(uuid=uuid).prefetch_related("social_network_reports").first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    res = []
    social_reports = await resource.social_network_reports.filter(is_moderated=is_moderated).all()
    for social_report in social_reports:
        report_dict = await social_report.to_dict()
        res.append(SocialReportOut(**report_dict, resource_uuid=resource.uuid))

    return res


@router.get("/{uuid}/reviews", response_model=List[ReviewOut], status_code=200)
async def read_resource_reviews(
    uuid: UUID4,
):
    """
    Get resource reviews by uuid.
    """
    resource = await Resource.filter(uuid=uuid).prefetch_related("reviews").first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    res = []
    for review in resource.reviews:
        review_dict = await review.to_dict()
        res.append(ReviewOut(**review_dict, resource_uuid=resource.uuid))

    return res


@router.get("/{uuid}/stats/export", status_code=200)
async def read_resource_reviews(
    uuid: UUID4,
):
    """
    Export resource recent checks by uuid.
    """
    resource = await Resource.filter(uuid=uuid).first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    results = (
        await CheckResult.filter(parent_check__resource_node__resource__uuid=uuid).order_by("-datetime").limit(3000)
    )
    # TODO: rewrite shitcode below

    prev_result = results[0]
    prev_changed_result = results[0]

    prev_changed_datetime = datetime.datetime.now()
    data = {"status": [], "time_from": [], "time_to": []}

    for result in results[1:]:
        result: CheckResult
        if result.status != prev_result.status:
            data["status"].append(str(prev_result.status).split(".")[1])
            data["time_from"].append(result.datetime.strftime("%m/%d/%Y, %H:%M:%S"))
            data["time_to"].append(prev_changed_datetime.strftime("%m/%d/%Y, %H:%M:%S"))
            prev_changed_result = result
            prev_changed_datetime = result.datetime

        prev_result = result

    pr_st = None
    if len(data["status"]) > 0:
        pr_st = data["status"][-1]

    if str(result.status).split(".")[1] != pr_st:
        data["status"].append(str(prev_result.status).split(".")[1])
        data["time_from"].append(result.datetime.strftime("%m/%d/%Y, %H:%M:%S"))
        data["time_to"].append(prev_changed_result.datetime.strftime("%m/%d/%Y, %H:%M:%S"))

    df = pd.DataFrame(data)
    sheet_name = resource.name.lower().strip() or "export"

    bio = io.BytesIO()
    writer = pd.ExcelWriter(bio, engine="xlsxwriter")

    df.to_excel(writer, sheet_name=sheet_name, index=False, na_rep="NaN")

    for column in df:
        column_length = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets[sheet_name].set_column(col_idx, col_idx, column_length)

    writer.close()
    bio.seek(0)

    bytes_data = bio.read()

    return Response(content=bytes_data, media_type="application/vnd.ms-excel")


@router.get("/nodes/", response_model=List[ResourceNodeOutWithResourceUUID], status_code=200)
async def read_resources_nodes(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_admin),
):
    """
    Get resource nodes list.
    """
    resources_nodes = await ResourceNode.all().limit(limit).offset(skip).prefetch_related("resource")

    res = []
    for resource_node in resources_nodes:
        resource_node_dict = await resource_node.to_dict()
        res.append(ResourceNodeOutWithResourceUUID(**resource_node_dict, resource_uuid=resource_node.resource.uuid))

    return res


@router.post("/nodes/", response_model=ResourceNodeOut, status_code=201)
async def create_node(
    resource_node_in: ResourceNodeCreate,
    current_user: User = Depends(get_current_admin),
):
    """
    Create a resource node
    """
    resource_node = await ResourceNode.filter(url=resource_node_in.url).first()

    if resource_node is not None:
        raise HTTPException(
            status_code=400,
            detail="The resource node with this url already exist",
        )

    resource = await Resource.filter(uuid=resource_node_in.resource_uuid).first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    resource_node = await ResourceNode.create(url=resource_node_in.url, uuid=resource_node_in.uuid, resource=resource)

    return resource_node


@router.delete("/nodes/{uuid}", status_code=200)
async def delete_node(
    uuid: UUID4,
    current_user: User = Depends(get_current_admin),
):
    """
    Delete a resource node
    """
    resource_node = await ResourceNode.filter(uuid=uuid).first()

    if resource_node is None:
        raise HTTPException(
            status_code=404,
            detail="The resource node with this uuid does not exist",
        )

    await resource_node.delete()

    return "Successfully deleted"
