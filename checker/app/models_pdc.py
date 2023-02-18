from typing import Literal
from pydantic import BaseModel
from ipaddress import IPv4Address


class Proxy(BaseModel):
  ip: IPv4Address
  port: int
  protocol: Literal["http", "https"]
  country: str
  username: str
  password: str

  def __repr__(self) -> str:
    if self.username == '':
        return  f"{self.protocol}://{self.ip}:{self.port}"
    return f"{self.protocol}://{self.username}:{self.password}@{self.ip}:{self.port}"


class Task(BaseModel):
    db_id: int
    method: Literal["get", "post", "head"]
    url: str
    expectation_code: int


class Answer(BaseModel):
    db_id: int
    status: Literal["ok", "partial", "critical"]
