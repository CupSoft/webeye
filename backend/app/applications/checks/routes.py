import datetime
import json

from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.applications.checks.schemas import CheckOut, CheckCreate, CheckResultCreate, CheckResultOut, CheckOutWithUrl
from app.applications.checks.models import Check, CheckResult
from app.applications.checks.utils import redis_publish_email, redis_publish_telegram

from app.applications.resources.models import ResourceNode
from app.applications.subscriptions.models import Subscription
from app.applications.subscriptions.schemas import EmailNotification, TelegramNotification

from app.core.base.utils import exclude_keys

from pydantic import UUID4

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter()


@router.get("/", response_model=List[CheckOutWithUrl], status_code=200)
async def read_checks(
    skip: int = 0,
    limit: int = 100,
):
    """
    Get check list.
    """
    checks = await Check.all().limit(limit).offset(skip).prefetch_related("resource_node")

    res = []
    for check in checks:
        dict_check = await check.to_dict()
        dict_check["url"] = check.resource_node.url
        res.append(dict_check)

    return res


@router.post("/", response_model=CheckOut, status_code=201)
async def create_check(check_in: CheckCreate):
    """
    Create a check
    """

    check = await Check.filter(uuid=check_in.uuid).first()

    if check is not None:
        raise HTTPException(
            status_code=400,
            detail="The check with this uuid already exist",
        )

    resource_node = await ResourceNode.filter(uuid=check_in.resource_node_uuid).first()

    if resource_node is None:
        raise HTTPException(
            status_code=404,
            detail="The resource node with this uuid does not exist",
        )

    check = await Check.create(**exclude_keys(check_in.dict(), {"resource_node_uuid"}), resource_node=resource_node)

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
            detail="The check with this uuid does not exist",
        )

    await check.delete()

    return "Successfully deleted"


@router.post("/results/", response_model=CheckResultOut, status_code=201)
async def create_check_result(check_result_in: CheckResultCreate):
    """
    Create a check result
    """

    check_result = await CheckResult.filter(uuid=check_result_in.uuid).first()

    if check_result is not None:
        raise HTTPException(
            status_code=400,
            detail="The check result with this uuid already exist",
        )

    check = (
        await Check.filter(uuid=check_result_in.check_uuid)
        .prefetch_related("resource_node__resource__subscriptions__user")
        .first()
    )
    if check is None:
        raise HTTPException(
            status_code=404,
            detail="The check with this uuid does not exist",
        )

    check_result = await CheckResult.create(**exclude_keys(check_result_in.dict(), {"check_uuid"}), parent_check=check)

    last_status = await check.resource_node.resource.status

    if last_status != check_result_in.status:
        for subscription in check.resource_node.resource.subscriptions:
            subscription: Subscription
            if subscription.to_email:
                email = EmailNotification(
                    recipient=subscription.user.email,
                    subject=f"Resource {check.resource_node.resource.name} status changed",
                    body=(
                        f"Resource {check.resource_node.resource.name} status changed from {last_status} to"
                        f" {check_result_in.status}"
                    ),
                    resource_status=check_result_in.status,
                    resource_uuid=check.resource_node.resource.uuid,
                )
                await redis_publish_email(email)

            if subscription.to_telegram:
                telegram_notification = TelegramNotification(
                    chat_id=str(subscription.user.tg_id),
                    resource_name=check.resource_node.resource.name,
                    resource_old_status=last_status,
                    resource_new_status=check_result_in.status,
                    resource_uuid=check.resource_node.resource.uuid,
                )
                await redis_publish_telegram(telegram_notification)

    check_result_dict = await check_result.to_dict()

    return CheckResultOut(**check_result_dict, check_uuid=check.uuid)


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
            detail="The check result with this uuid does not exist",
        )

    await check_result.delete()

    return "Successfully deleted"
