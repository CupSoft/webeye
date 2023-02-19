from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.applications.reviews.schemas import ReviewCreate, ReviewOut
from app.applications.reviews.models import Review

from app.applications.users.models import User

from app.applications.resources.models import Resource
from app.core.auth.utils.contrib import get_current_admin, get_current_user

from app.core.base.utils import exclude_keys

from pydantic import UUID4

import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[ReviewOut], status_code=200)
async def read_reviews(skip: int = 0, limit: int = 100, current_user: User = Depends(get_current_admin)):
    """
    Get list of reviews.
    """
    reviews = await Review.all().limit(limit).offset(skip)

    return reviews


@router.get("/{uuid}", response_model=ReviewOut, status_code=200)
async def read_review(uuid: UUID4, current_user: User = Depends(get_current_admin)):
    """
    Get a review by uuid.
    """
    review = await Review.filter(uuid=uuid).first()

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="The review with this uuid does not exist",
        )

    return review


@router.post("/", response_model=ReviewOut, status_code=201)
async def create_review(review_in: ReviewCreate, current_user: User = Depends(get_current_user)):
    """
    Create a review
    """

    if review_in.stars < 1 or review_in.stars > 5:
        raise HTTPException(
            status_code=400,
            detail="The stars must be between 1 and 5",
        )

    review = await Review.filter(uuid=review_in.uuid).first()

    if review is not None:
        raise HTTPException(
            status_code=400,
            detail="The review with this uuid already exist",
        )

    if review_in.user_uuid:
        if (current_user.uuid != review_in.user_uuid) and (not current_user.is_admin):
            raise HTTPException(
                status_code=403,
                detail="You can't create a review for another user",
            )

        user = await User.filter(uuid=review_in.user_uuid).first()

        if user is None:
            raise HTTPException(
                status_code=400,
                detail="The user with this uuid does not exist",
            )
    else:
        user = current_user

    resource = await Resource.filter(uuid=review_in.resource_uuid).first()

    if resource is None:
        raise HTTPException(
            status_code=400,
            detail="The resource with this uuid does not exist",
        )

    created_review = await Review.create(
        **review_in.dict(exclude={"user_uuid", "resource_uuid"}),
        user=user,
        resource=resource,
    )

    return created_review


@router.delete("/{uuid}", status_code=200)
async def delete_review(uuid: UUID4, current_user: User = Depends(get_current_admin)):
    """
    Delete a review
    """

    review = await Review.filter(uuid=uuid).first()

    if review is None:
        raise HTTPException(
            status_code=400,
            detail="The review with this uuid does not exist",
        )

    await review.delete()

    return {"detail": "Review deleted"}
