import datetime
from enum import Enum
import uuid
from typing import Optional

from pydantic import BaseModel, UUID4, validator


class RequestType(str, Enum):
    get = 'GET'
    post = 'POST'
    head = 'HEAD'
    put = 'PUT'


class Location(str, Enum):
    russia = 'RUSSIA'
    austria = 'AUSTRIA'
    germany = 'GERMANY'


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
    timestamp: datetime.datetime
    result: bool = False
    

class CheckResultCreate(CheckResult):
    uuid: Optional[UUID4] = None
    check_uuid: UUID4


class CheckResultOut(CheckResult):
    uuid: UUID4

    class Config:
        orm_mode = True
