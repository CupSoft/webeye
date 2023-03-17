from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.applications.subscriptions.schemas import SubscriptionOut, SubscriptionIn, SubscriptionUpdate
from app.applications.subscriptions.models import Subscription

from app.applications.users.models import User

from app.applications.resources.models import Resource
from app.core.auth.utils.contrib import get_current_admin, get_current_user

from app.core.base.utils import exclude_keys

from pydantic import UUID4

import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[SubscriptionOut], status_code=200)
async def read_subscriptions(skip: int = 0, limit: int = 100, current_user: User = Depends(get_current_admin)):
    """
    Get list of subscriptions.
    """
    subscriptions = await Subscription.all().limit(limit).offset(skip)

    return subscriptions


@router.post("/", response_model=SubscriptionOut, status_code=201)
async def create_subscription(subscription_in: SubscriptionIn, current_user: User = Depends(get_current_user)):
    """
    Create a subscription
    """

    resource = await Resource.filter(uuid=subscription_in.resource_uuid).first()

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="The resource with this uuid does not exist",
        )

    subscription = await Subscription.filter(user=current_user, resource=resource).first()

    if subscription is not None:
        raise HTTPException(
            status_code=400,
            detail="The subscription already exist",
        )

    subscription = await Subscription.create(
        **exclude_keys(subscription_in.dict(), {"resource_uuid", "user_uuid"}), user=current_user, resource=resource
    )

    return subscription


@router.get("/{uuid}", response_model=SubscriptionOut, status_code=200)
async def read_subscription(uuid: UUID4, current_user: User = Depends(get_current_user)):
    """
    Get a subscription
    """

    subscription = await Subscription.filter(uuid=uuid).first()

    if subscription is None:
        raise HTTPException(
            status_code=404,
            detail="The subscription with this uuid does not exist",
        )

    if (subscription.user != current_user) and (not current_user.is_admin):
        raise HTTPException(
            status_code=403,
            detail="You do not have access to this subscription",
        )

    return subscription


@router.patch("/{uuid}", response_model=SubscriptionOut, status_code=200)
async def update_subscription(
    uuid: UUID4,
    subscribtion_in: SubscriptionUpdate,
    current_user: User = Depends(get_current_user),
):
    """
    Update a subscription
    """

    subscription = await Subscription.filter(uuid=uuid).first()

    if subscription is None:
        raise HTTPException(
            status_code=404,
            detail="The subscription with this uuid does not exist",
        )

    if (subscription.user_id != current_user.uuid) and (not current_user.is_admin):
        raise HTTPException(
            status_code=403,
            detail="You do not have access to this subscription",
        )

    if subscribtion_in.to_telegram is not None:
        subscription.to_telegram = subscribtion_in.to_telegram
    if subscribtion_in.to_email is not None:
        subscription.to_email = subscribtion_in.to_email

    await subscription.save()

    return subscription


@router.delete("/{uuid}", status_code=200)
async def delete_subscription(uuid: UUID4, current_user: User = Depends(get_current_user)):
    """
    Delete a subscription
    """

    subscription = await Subscription.filter(uuid=uuid).first()

    if subscription is None:
        raise HTTPException(
            status_code=404,
            detail="The subscription with this uuid does not exist",
        )

    if (subscription.user != current_user) and (not current_user.is_admin):
        raise HTTPException(
            status_code=403,
            detail="You do not have access to this subscription",
        )

    await subscription.delete()

    return "Successfully deleted"
