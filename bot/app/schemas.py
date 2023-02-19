from pydantic import BaseModel, UUID4, validator
from enum import Enum


class Status(str, Enum):
    ok = "OK"
    partial = "partial"
    critical = "critical"


class TelegramNotification(BaseModel):
    chat_id: str
    resource_name: str
    resource_old_status: Status
    resource_new_status: Status
    resource_uuid: UUID4
