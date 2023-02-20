import contextlib
import logging

from aerich import Command
from click import Abort
from tortoise import Tortoise

from app.settings import settings

all_models = ["app.db.db_user.user_func", "aerich.models"]


def generate_config():
    connections = ""
    if settings().DB_PROTOCOL == "sqlite":
        connections = f"{settings().DB_PROTOCOL}://{settings().DB_SQLITE_DIR}"
    else:
        connections = f"{settings().DB_PROTOCOL}://{settings().DB_USERNAME}:{settings().DB_PASSWORD}" \
                      f"@{settings().DB_HOST}:{settings().DB_PORT}/{settings().DB_NAME}"
    return {
        "connections": {"default": connections},
        "apps": {
            "models": {
                "models": all_models,
                "default_connection": "default",
            },
        },
    }


async def create_models(tortoise_config: dict):
    command = Command(tortoise_config=tortoise_config, app="models")
    await command.init()
    await command.init_db(safe=True)
    await command.upgrade()


async def migrate_models(tortoise_config: dict):
    command = Command(tortoise_config=tortoise_config, app="models")
    await command.init()
    with contextlib.suppress(Abort):
        await command.migrate()
    await command.upgrade()


async def init_orm(tortoise_config: dict) -> None:
    await Tortoise.init(config=tortoise_config)
    logging.info(f"Tortoise-ORM started, {Tortoise.apps}")


async def close_orm() -> None:
    await Tortoise.close_connections()
    logging.info("Tortoise-ORM shutdown")
