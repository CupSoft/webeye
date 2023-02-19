from pydantic import BaseModel, UUID4


class Resource(BaseModel):
    name: str
    uuid: UUID4
