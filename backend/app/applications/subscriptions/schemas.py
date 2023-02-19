from enum import Enum
import uuid
from typing import Optional

from pydantic import BaseModel, UUID4, validator

from app.applications.resources.schemas import Status


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class Subscription(BaseProperties):
    uuid: Optional[UUID4] = None
    to_telegram: bool = False
    to_email: bool = False


class SubscriptionOut(Subscription):
    class Config:
        orm_mode = True


class SubscriptionIn(Subscription):
    resource_uuid: UUID4
