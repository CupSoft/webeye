import datetime
import uuid

from pydantic import BaseModel, UUID4, validator


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class Review(BaseProperties):
    text: str
    stars: int
    date: datetime.datetime


class ReviewCreate(Review):
    uuid: UUID4 = None
    resource_id: UUID4
    user_id: UUID4


class ReviewOut(Review):
    uuid: UUID4

    class Config:
        orm_mode = True
