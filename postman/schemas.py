from enum import Enum
from pydantic import BaseModel, UUID4


class Status(str, Enum):
    ok = "OK"
    partial = "partial"
    critical = "critical"


class EmailNotification(BaseModel):
    recipient: str
    subject: str
    body: str
    resource_status: Status
    resource_uuid: UUID4
