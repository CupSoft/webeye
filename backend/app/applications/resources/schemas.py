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
    @validator("hashed_id", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()

    def create_update_dict(self):
        return self.dict(
            exclude_unset=True,
            exclude={"id"},
        )


class BaseResource(BaseProperties):
    name: str
    status: Status = 'OK'


class ResourceCreate(BaseResource):
    hashed_id: Optional[UUID4] = None


class ResourceUpdate(BaseResource):
    pass


class ResourceDB(BaseResource):
    id: int
    hashed_id: UUID4
    updated_at: datetime

    class Config:
        orm_mode = True


class ResourceOut(BaseResource):
    id: int

    class Config:
        orm_mode = True
