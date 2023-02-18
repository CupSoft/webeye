import uuid

from pydantic import BaseModel, UUID4, validator

from app.applications.resources.schemas import Status


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class Report(BaseProperties):
    status: Status
    is_moderated: bool = False


class ReportCreate(Report):
    uuid: UUID4 = None
    resource_uuid: UUID4


class ReportOut(Report):
    uuid: UUID4
    
    class Config:
        orm_mode = True
