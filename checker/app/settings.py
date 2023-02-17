from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_HOST: str
    API_PORT: int
    API_LOGIN: str
    API_PASSWORD: str


@lru_cache()
def settings():
    return Settings(
        _env_file=".env",
        _env_file_encoding="utf-8",
    )
