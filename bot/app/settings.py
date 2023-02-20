from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    DB_PROTOCOL: str = "sqlite"  # sqlite / postgresql / mysql
    API_HOST: str = "http://localhost"
    API_PORT: int = 8000

    URL: str

    ADMIN_ID: int

    USE_REDIS: bool = True  # Without redis, the API connection does not work
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ""

    DB_USERNAME: str = "root"  # if sqlite is used, then it is not necessary
    DB_PASSWORD: str = "root"
    DB_HOST: str = "localhost"
    DB_NAME: str = "postgres"
    DB_PORT: int = 3306

    DB_SQLITE_DIR: str = "app/db/bot.db"


@lru_cache()
def settings():
    return Settings(
        _env_file=".env",
        _env_file_encoding="utf-8",
    )
