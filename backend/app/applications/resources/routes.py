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
    ResourceStatsIn,
    ResourceStatsOut,
    Status,
)
from app.applications.reports.schemas import ReportOut
from app.applications.social_reports.schemas import SocialReportOut
from app.applications.reviews.schemas import ReviewOut
from app.core.auth.utils.contrib import get_current_admin, get_current_user

from app.applications.users.models import User

from typing import List

from fastapi import APIRouter, HTTPException, Depends

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
    res = []
    for resource in resources:
        resource_dict = await resource.to_dict()
        rating = await resource.rating
        status = await resource.status
        res.append(ResourceOutWithRating(**resource_dict, rating=rating, status=status))

    return res


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
    status = await resource.status
    return ResourceOut(**resource_dict, status=status)


@router.get("/{uuid}", response_model=ResourceOutWithRating, status_code=200)
async def read_resource(
    uuid: UUID4,
):
    """
    Get resource by uuid.
    """
    resource = await Resource.filter(uuid=uuid).first().prefetch_related("reviews")

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    resource_dict = await resource.to_dict()

    rating = await resource.rating
    status = await resource.status
    return ResourceOutWithRating(**resource_dict, rating=rating, status=status)


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
                    print(result)
                    result: CheckResult
                    if result.status == Status.ok:
                        ok_count += 1
                    elif result.status == Status.partial:
                        partial_count += 1
                    elif result.status == Status.critical:
                        critical_count += 1

        resource_checks_stats.append(
            ResourceStatsOut(end_datetime=end_datetime, ok=ok_count, partial=partial_count, critical=critical_count)
        )

    return resource_checks_stats


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
    status = await resource.status
    return ResourceOut(**resource_dict, status=status)


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
