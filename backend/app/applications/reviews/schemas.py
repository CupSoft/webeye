import datetime
import uuid
from typing import Optional

from pydantic import BaseModel, UUID4, validator


class BaseProperties(BaseModel):
    @validator("uuid", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()


class Review(BaseProperties):
    text: str
    stars: int


class ReviewCreate(Review):
    uuid: Optional[UUID4] = None
    resource_uuid: UUID4
    user_uuid: Optional[UUID4] = None

    class Config:
        schema_extra = {
            "example": {
                "text": "This is a review",
                "stars": 5,
                "resource_uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b",
            }
        }


class ReviewOut(Review):
    uuid: UUID4

    class Config:
        orm_mode = True
        
        schema_extra = {
            "example":  {
                "text": "This is a review",
                "stars": 4,
                "uuid": "f7b4c2c0-5b5a-4b4a-9c1c-8e1b0c1b0c1b"
            }
        }
