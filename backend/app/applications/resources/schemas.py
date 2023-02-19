import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel, UUID4, validator


class Status(str, Enum):
    ok = "OK"
    partial = "partial"
    critical = "critical"


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class BaseResource(BaseProperties):
    name: str
    status: Status = "OK"


class ResourceCreate(BaseResource):
    uuid: Optional[UUID4] = None

    class Config:
        schema_extra = {"example": {"name": "HSE"}}


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
    rating: float = None

    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "name": "HSE",
                "status": "OK",
                "uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b",
                "rating": "4.76",
            }
        }


class BaseResourceNode(BaseProperties):
    url: str


class ResourceNodeCreate(BaseResourceNode):
    uuid: UUID4 = None
    resource_uuid: UUID4

    class Config:
        schema_extra = {
            "example": {
                "url": "https://www.hse.ru",
                "resource_uuid": "55f8663b-05be-421f-a409-6f8b31434a84",
            }
        }


class ResourceNodeOut(BaseResourceNode):
    uuid: UUID4

    class Config:
        orm_mode = True
