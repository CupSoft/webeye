from fastapi import FastAPI
from app.core.exceptions import SettingNotFound
from app.core.init_app import (
    configure_logging,
    init_middlewares,
    register_db,
    register_exceptions,
    register_routers,
)

try:
    from app.settings.config import settings
except ImportError:
    raise SettingNotFound("Can not import settings. Create settings file from template.config.py")

app = FastAPI(title=settings.APP_TITLE, description=settings.APP_DESCRIPTION, version=settings.VERSION)

configure_logging()
init_middlewares(app)
register_db(app)
register_exceptions(app)
register_routers(app)
from fastapi_admin.app import app as admin_app

app.mount("/admin", admin_app)

from fastapi_admin.providers.login import UsernamePasswordProvider
import aioredis
import os


# login_provider = UsernamePasswordProvider(login_logo_url="https://preview.tabler.io/static/logo.svg")


@app.on_event("startup")
async def startup():
    print(settings.REDIS_HOST)
    redis = await aioredis.create_redis_pool(f"redis://{settings.REDIS_HOST}", encoding="utf8")
    admin_app.configure(
        logo_url="https://preview.tabler.io/static/logo-white.svg",
        template_folders=[os.path.join(".", "templates")],
        # providers=[login_provider],
        redis=redis,
    )
