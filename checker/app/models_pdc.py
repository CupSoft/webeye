from typing import Literal
from enum import Enum
from pydantic import BaseModel
from ipaddress import IPv4Address
import json


class ProxyTypeEnum(Enum):
   http = 'http'
   https = 'https'
   socks = 'socks'


class Proxy(BaseModel):
  ip: IPv4Address
  port: int
  proxy_type: ProxyTypeEnum
  country: str
  username: str
  password: str

  def __repr__(self) -> str:
     return f"{self.proxy_type}://{self.username}:{self.password}@{self.ip}:{self.port}"


class Task(BaseModel):
    db_id: int
    method: Literal["get"]
    url: str
    expectation_code: int


class Answer(BaseModel):
    db_id: int
    status: Literal["ok", "partial", "critical"]
