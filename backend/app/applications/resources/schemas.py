import uuid
from enum import Enum
from typing import Optional

import datetime as datetime
from pydantic import BaseModel, UUID4, validator


class Status(str, Enum):
    ok = "OK"
    partial = "partial"
    critical = "critical"
    ddos = "ddos"


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class BaseResource(BaseProperties):
    name: str


class ResourceCreate(BaseResource):
    uuid: Optional[UUID4] = None

    class Config:
        schema_extra = {"example": {"name": "HSE"}}


class ResourceUpdate(BaseResource):
    name: str = None


class ResourceDB(BaseResource):
    uuid: UUID4

    class Config:
        orm_mode = True


class ResourceStatsIn(BaseProperties):
    timedelta: datetime.timedelta
    max_count: int


class ResourceStatsOut(BaseProperties):
    end_datetime: datetime.datetime
    ok: int
    partial: int
    critical: int


class ResourceOut(BaseResource):
    uuid: UUID4
    status: Status

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "name": "HSE",
                "status": "OK",
                "uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b",
            }
        }


class ResourceOutWithRating(ResourceOut):
    rating: float = None
    url: str = None

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "name": "HSE",
                "url": "https://hse.ru",
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

        schema_extra = {
            "example": {
                "url": "https://www.hse.ru",
                "uuid": "55440d60-bc79-449e-9708-d967b5da5dcd",
            }
        }


class ResourceNodeOutWithResourceUUID(BaseResourceNode):
    uuid: UUID4
    resource_uuid: UUID4

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "url": "https://www.hse.ru",
                "uuid": "55440d60-bc79-449e-9708-d967b5da5dcd",
                "resource_uuid": "55f8663b-05be-421f-a409-6f8b31434a84",
            }
        }
