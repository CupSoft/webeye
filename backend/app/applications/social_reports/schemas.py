from enum import Enum
import uuid

from pydantic import BaseModel, UUID4, validator

from app.applications.resources.schemas import Status


class SocialNetworks(str, Enum):
    vk = 'VK'
    ok = 'OK'


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class SocialReport(BaseProperties):
    status: Status
    is_moderated: bool = False
    social_network: SocialNetworks
    link: str


class SocialReportCreate(SocialReport):
    uuid: UUID4 = None
    resource_id: UUID4


class SocialReportOut(SocialReport):
    uuid: UUID4
    
    class Config:
        orm_mode = True
