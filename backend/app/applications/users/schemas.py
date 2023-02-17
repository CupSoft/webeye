import uuid
from datetime import datetime
from typing import Optional, TypeVar

from pydantic import BaseModel, EmailStr, UUID4, validator


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class BaseUser(BaseProperties):
    uuid: Optional[UUID4] = None
    email: Optional[EmailStr] = None
    is_superuser: Optional[bool] = False


class BaseUserCreate(BaseProperties):
    uuid: Optional[UUID4] = None
    email: EmailStr
    username: Optional[str]
    password: str


class BaseUserUpdate(BaseProperties):
    password: Optional[str]
    email: Optional[EmailStr]


class BaseUserDB(BaseUser):
    uuid: UUID4
    password_hash: str
    
    class Config:
        orm_mode = True


class BaseUserOut(BaseUser):
    uuid: UUID4
    
    class Config:
        orm_mode = True
