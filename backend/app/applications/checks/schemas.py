import datetime
from enum import Enum
import uuid
from typing import Optional
from app.applications.resources.schemas import Status

from pydantic import BaseModel, UUID4, validator


class RequestType(str, Enum):
    get = "GET"
    post = "POST"
    head = "HEAD"
    put = "PUT"


class Location(str, Enum):
    russia = "RUSSIA"
    austria = "AUSTRIA"
    germany = "GERMANY"


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class Check(BaseProperties):
    expectation: str
    request_type: RequestType


class CheckCreate(BaseProperties):
    uuid: Optional[UUID4] = None
    expectation: str
    request_type: RequestType
    resource_node_uuid: UUID4

    class Config:
        schema_extra = {
            "example": {
                "expectation": "200",
                "request_type": "GET",
                "resource_node_uuid": "fb7c10eb-0a5d-4bab-b769-713d93088c54",
            }
        }


class CheckUpdate(BaseProperties):
    expectation: str = None
    request_type: RequestType = None


class CheckOut(Check):
    uuid: UUID4

    class Config:
        orm_mode = True


class CheckOutWithUrl(Check):
    uuid: UUID4
    url: str

    class Config:
        orm_mode = True


class CheckResult(BaseProperties):
    response: str
    location: Location
    datetime: Optional[datetime.datetime]
    check_uuid: UUID4


class CheckResultCreate(CheckResult):
    uuid: Optional[UUID4] = None
    status: Status

    class Config:
        schema_extra = {
            "example": {
                "response": "200",
                "location": "RUSSIA",
                "datetime": "2021-09-01T00:00:00",
                "status": "OK",
                "check_uuid": "fb7c10eb-0a5d-4bab-b769-713d93088c54",
            }
        }


class CheckResultOut(CheckResult):
    uuid: UUID4

    class Config:
        orm_mode = True
