from enum import Enum
import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4, validator


class RequestType(str, Enum):
    get = 'GET'
    post = 'POST'
    patch = 'PATCH'
    delete = 'DELETE'
    
    
class SocialNetworks(str, Enum):
    vk = 'VK'
    ok = 'OK'


class BaseProperties(BaseModel):
    @validator("hashed_id", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()

    def create_update_dict(self):
        return self.dict(
            exclude_unset=True,
            exclude={"id"},
        )


class BaseCheck(BaseProperties):
    name: str
    period: int
    expectation: str
    request_type: RequestType
    hashed_id: Optional[UUID4] = None
    created_at: Optional[datetime]


class BaseCheckCreate(BaseProperties):
    name: str
    period: int
    expectation: str
    request_type: RequestType
    hashed_id: Optional[UUID4] = None


class BaseCheckUpdate(BaseProperties):
    name: str
    period: int
    expectation: str
    request_type: RequestType


class BaseCheckDB(BaseCheck):
    id: int
    hashed_id: UUID4
    updated_at: datetime

    class Config:
        orm_mode = True


class BaseCheckOut(BaseCheck):
    id: int

    class Config:
        orm_mode = True
