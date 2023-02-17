from functools import lru_cache
from typing import List
from pydantic import BaseSettings
from models_pdc import Proxy
from pydantic.tools import parse_obj_as


class ProxySettings(BaseSettings):
    proxies: List[Proxy]


class Settings(BaseSettings):
    API_HOST: str
    API_PORT: int
    API_LOGIN: str
    API_PASSWORD: str


@lru_cache()
def settings():
    return Settings(
        _env_file=".env",
        _env_file_encoding="utf-8"
    )
