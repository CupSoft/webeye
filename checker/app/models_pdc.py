from datetime import datetime
from enum import Enum
from ipaddress import IPv4Address
from typing import Literal

from pydantic import BaseModel, UUID4


class Proxy(BaseModel):
    ip: IPv4Address
    port: int
    protocol: Literal["http", "https"]
    country: str
    username: str
    password: str

    def __repr__(self) -> str:
        if self.username == '':
            return f"{self.protocol}://{self.ip}:{self.port}"
        return f"{self.protocol}://{self.username}:{self.password}@{self.ip}:{self.port}"


class Status(str, Enum):
    ok = "OK"
    partial = "partial"
    critical = "critical"


class Task(BaseModel):
    uuid: str
    request_type: Literal["GET", "POST", "HEAD"]
    url: str
    expectation: int


class Answer(BaseModel):
    response: str
    location: str
    datetime: datetime
    status: Status
    check_uuid: UUID4
