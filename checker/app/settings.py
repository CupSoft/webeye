import json
from functools import lru_cache
from typing import List

from pydantic import BaseSettings
from pydantic.tools import parse_obj_as

from app.models_pdc import Proxy


class Settings(BaseSettings):
    CHECK_TIMEOUT: int = 120
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


@lru_cache()
def proxy_settings():
    with open('proxy.json') as f:
        return parse_obj_as(List[Proxy], json.load(f))
