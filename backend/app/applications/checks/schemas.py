from enum import Enum
import uuid
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
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class Check(BaseProperties):
    expectation: str
    request_type: RequestType


class CheckCreate(BaseProperties):
    expectation: str
    request_type: RequestType
    uuid: Optional[UUID4] = None


class CheckUpdate(BaseProperties):
    expectation: str
    request_type: RequestType


class CheckDB(Check):
    uuid: UUID4

    class Config:
        orm_mode = True


class CheckOut(Check):
    uuid: UUID4

    class Config:
        orm_mode = True
