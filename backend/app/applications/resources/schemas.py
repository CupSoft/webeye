from enum import Enum
import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4, validator


class Status(str, Enum):
    ok = 'OK'
    partial = 'partial'
    critical = 'critical'


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class BaseResource(BaseProperties):
    name: str
    status: Status = 'OK'


class ResourceCreate(BaseResource):
    uuid: Optional[UUID4] = None


class ResourceUpdate(BaseResource):
    name: str = None
    status: Status = None


class ResourceDB(BaseResource):
    uuid: UUID4
    
    class Config:
        orm_mode = True


class ResourceOut(BaseResource):
    uuid: UUID4
    
    class Config:
        orm_mode = True


class ResourceOutWithRating(BaseResource):
    uuid: UUID4
    rating: float
    
    class Config:
        orm_mode = True


class BaseResourceNode(BaseProperties):
    url: str


class ResourceNodeCreate(BaseResourceNode):    
    uuid: UUID4 = None
    resource_uuid: UUID4


class ResourceNodeOut(BaseResourceNode):
    uuid: UUID4
    
    class Config:
        orm_mode = True