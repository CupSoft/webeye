import logging

from asyncio import sleep

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.core.exceptions import APIException, on_api_exception
from app.settings.config import settings
from app.settings.log import DEFAULT_LOGGING
from app.core.auth.utils.contrib import get_current_admin, get_current_user
from app.applications.users.models import User
from app.applications.users.schemas import BaseUserCreate
from app.core.auth.utils.password import get_password_hash

from app.core.auth.routers.login import router as login_router
from app.applications.users.routes import router as users_router
from app.applications.checks.routes import router as checks_routes
from app.applications.resources.routes import router as resources_routes
from app.applications.reports.routes import router as reports_routes
from app.applications.subscriptions.routes import router as subscriptions_routes
from app.applications.social_reports.routes import router as social_reports_routes
from app.applications.reviews.routes import router as reviews_routes

from aerich import Command


def configure_logging(log_settings: dict = None):
    log_settings = log_settings or DEFAULT_LOGGING
    logging.config.dictConfig(log_settings)


def init_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )


def get_app_list():
    app_list = [f"{settings.APPLICATIONS_MODULE}.{app}.models" for app in settings.APPLICATIONS]
    return app_list


def get_tortoise_config() -> dict:
    app_list = get_app_list()
    app_list.append("aerich.models")
    config = {
        "connections": settings.DB_CONNECTIONS,
        "apps": {
            "models": {
                "models": app_list,
                "default_connection": "default",
            }
        },
    }
    return config


TORTOISE_ORM = get_tortoise_config()


async def create_default_admin_user():
    await sleep(3)
    user = await User.get_by_email(email=settings.ROOT_ADMIN_EMAIL)
    if user:
        return

    hashed_password = get_password_hash(settings.ROOT_ADMIN_PASSWORD)

    admin_user = User()
    admin_user.email = settings.ROOT_ADMIN_EMAIL
    admin_user.password_hash = hashed_password
    admin_user.is_admin = True
    await admin_user.save()
    return admin_user


def register_db(app: FastAPI, db_url: str = None):
    db_url = db_url or settings.DB_URL
    app_list = get_app_list()
    app_list.append("aerich.models")
    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": app_list},
        generate_schemas=True,
        add_exception_handlers=True,
    )


async def upgrade_db(app: FastAPI, db_url: str = None):
    command = Command(tortoise_config=TORTOISE_ORM, app="models")
    await command.init()
    await command.upgrade()


def register_exceptions(app: FastAPI):
    app.add_exception_handler(APIException, on_api_exception)


def register_routers(app: FastAPI):
    app.include_router(login_router, prefix="/api/auth/login", tags=["login"])
    app.include_router(users_router, prefix="/api/auth/users", tags=["users"])
    app.include_router(resources_routes, prefix="/api/resources", tags=["resources"])
    app.include_router(
        checks_routes,
        prefix="/api/checks",
        tags=["checks"],
        dependencies=[Depends(get_current_admin)],
    )
    app.include_router(subscriptions_routes, prefix="/api/subscriptions", tags=["subscriptions"])
    app.include_router(reports_routes, prefix="/api/reports", tags=["reports"])
    app.include_router(social_reports_routes, prefix="/api/social_reports", tags=["social_reports"])
    app.include_router(reviews_routes, prefix="/api/reviews", tags=["reviews"])
