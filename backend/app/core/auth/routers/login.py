from datetime import timedelta

from fastapi import APIRouter, HTTPException

from app.core.auth.schemas import JWTToken, CredentialsSchema
from app.core.auth.utils.contrib import authenticate
from app.core.auth.utils.jwt import create_access_token
from app.settings.config import settings


router = APIRouter()


@router.post("/access-token", response_model=JWTToken)
async def login_access_token(credentials: CredentialsSchema):
    user = await authenticate(credentials)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    
    return {
        "access_token": create_access_token(
            data={"user_uuid": str(user.uuid)}, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }