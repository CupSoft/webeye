from app.core.auth.utils.contrib import get_current_active_admin, get_current_active_user
from app.core.auth.utils.password import get_password_hash

from app.applications.users.models import User
from app.applications.users.schemas import BaseUserOut, BaseUserCreate, BaseUserUpdate

from typing import List

from fastapi import APIRouter, Depends, HTTPException

import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[BaseUserOut], status_code=200, tags=['users'])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_admin),
):
    """
    Retrieve users.
    """
    users = await User.all().limit(limit).offset(skip)
    return users


@router.post("/", response_model=BaseUserOut, status_code=201, tags=['users'])
async def create_user(
    *,
    user_in: BaseUserCreate,
    current_user: User = Depends(get_current_active_admin),
):
    """
    Create new user.
    """
    user = await User.get_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists",
        )

    hashed_password = get_password_hash(user_in.password)
    db_user = BaseUserCreate(
        **user_in.dict(), hashed_password=hashed_password
    )
    created_user = await User.create(db_user)

    return created_user


@router.put("/me", response_model=BaseUserOut, status_code=200, tags=['users'])
async def update_user_me(
    user_in: BaseUserUpdate,
    current_user: User = Depends(get_current_active_user)
):
    """
    Update own user.
    """
    if user_in.password is not None:
        hashed_password = get_password_hash(user_in.password)
        current_user.hashed_password = hashed_password
    if user_in.email is not None:
        current_user.email = user_in.email
    await current_user.save()
    return current_user


@router.get("/me", response_model=BaseUserOut, status_code=200, tags=['users'])
def read_user_me(
    current_user: User = Depends(get_current_active_user),
):
    """
    Get current user.
    """
    return current_user


@router.get("/{uuid}", response_model=BaseUserOut, status_code=200, tags=['users'])
async def read_user_by_id(
    user_id: int,
    current_user: User = Depends(get_current_active_user),
):
    """
    Get a specific user by id.
    """
    user = await User.get(id=user_id)
    if user == current_user:
        return user
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user


@router.put("/{uuid}", response_model=BaseUserOut, status_code=200, tags=['users'])
async def update_user(
    uuid: int,
    user_in: BaseUserUpdate,
    current_user: User = Depends(get_current_active_admin),
):
    """
    Update a user.
    """
    user = await User.get(uuid=uuid)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist",
        )
    user = await user.update_from_dict(user_in.dict())
    await user.save()

    return user
