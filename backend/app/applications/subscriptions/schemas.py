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

        schema_extra = {
            "example": {
                "to_email": False,
                "to_telegram": False,
                "uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b",
            }
        }


class SubscriptionOutWithResourceUUID(Subscription):
    resource_uuid: UUID4

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "to_email": False,
                "to_telegram": False,
                "uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b",
                "resource_uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b",
            }
        }


class SubscriptionIn(Subscription):
    resource_uuid: UUID4

    class Config:
        schema_extra = {
            "example": {
                "to_email": False,
                "to_telegram": False,
                "resource_uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b",
            }
        }


class EmailNotification(BaseModel):
    recipient: str
    subject: str
    body: str
    resource_status: Status
    resource_uuid: UUID4


class TelegramNotification(BaseModel):
    chat_id: str
    resource_status: Status
    resource_uuid: UUID4
