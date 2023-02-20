import datetime

from enum import Enum
import uuid

from pydantic import BaseModel, UUID4, validator

from app.applications.resources.schemas import Status


class SocialNetworks(str, Enum):
    vk = "VK"
    ok = "OK"


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class SocialReport(BaseProperties):
    status: Status
    snippet: str
    social_network: SocialNetworks
    link: str
    resource_uuid: UUID4


class SocialReportCreate(SocialReport):
    uuid: UUID4 = None

    class Config:
        schema_extra = {
            "example": {
                "status": "OK",
                "social_network": "VK",
                "snippet": "Игорь К: Только у меня упал сайт вышки??",
                "link": "https://vk.com/club123456789",
                "resource_uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b",
            }
        }


class SocialReportOut(SocialReport):
    uuid: UUID4
    is_moderated: bool = False
    created_at: datetime.datetime

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "status": "OK",
                "social_network": "VK",
                "snippet": "Игорь К: Только у меня упал сайт вышки??",
                "link": "https://vk.com/club123456789",
                "resource_uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b",
                "uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b",
                "is_moderated": False,
                "created_at": "2023-02-19T09:50:41.783Z",
            }
        }
