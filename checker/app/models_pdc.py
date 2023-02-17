from typing import Literal

from pydantic import BaseModel


class Task(BaseModel):
    db_id: int
    method: Literal["get"]
    url: str
    expectation_code: int


class Answer(BaseModel):
    db_id: int
    status: Literal["ok", "partial", "critical"]
