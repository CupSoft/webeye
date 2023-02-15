import os

from decouple import config


class Settings:
    VERSION = '0.1.0'
    APP_TITLE = 'Preprof'
    PROJECT_NAME = 'Name'
    APP_DESCRIPTION = 'Project for preprof'

    SERVER_HOST = 'localhost'

    DEBUG = True

    APPLICATIONS = [
        'users',
        'resources',
        'checks',
        'reviews',
        'subscriptions',
    ]

    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
    LOGS_ROOT = os.path.join(BASE_DIR, "app/logs")
    EMAIL_TEMPLATES_DIR = os.path.join(BASE_DIR, "app/templates/emails/build/")

    DB_USER = config('DB_USER')
    DB_NAME = config('DB_NAME')
    DB_PASS = config('DB_PASS')
    DB_HOST = config('DB_HOST')
    DB_PORT = config('DB_PORT')

    DB_URL = f"postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    DB_CONNECTIONS = {
            'default': {
                'credentials': {
                    "engine": "tortoise.backends.asyncpg",
                    'host': DB_HOST,
                    'port': DB_PORT,
                    'user': DB_USER,
                    'password': DB_PASS,
                    'database': DB_NAME,
                }
            },
        }

    SECRET_KEY = '3488a63e1765035d386f05409663f55c83bfae3b3c61a932744b20ad14244dcf'  # openssl rand -hex 32
    JWT_ALGORITHM = 'HS25'
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 day

    EMAILS_FROM_NAME = ''
    EMAILS_FROM_EMAIL = ''
    SMTP_USER = ''
    SMTP_HOST = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_TLS = True
    SMTP_PASSWORD = ''
    EMAIL_RESET_TOKEN_EXPIRE_HOURS = 1
    EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL
    LOGIN_URL = SERVER_HOST + '/api/auth/login/access-token'

    RABBIT_LOGIN = config('RABBIT_HOST')
    RABBIT_PASSWORD = config('RABBIT_PASSWORD')
    RABBIT_HOST = config('RABBIT_HOST')

    REDIS_URL = config('REDIS_HOST')

    APPLICATIONS_MODULE = 'app.applications'

    CORS_ORIGINS = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:5000",
        "http://localhost:3000",
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_METHODS = ["*"]
    CORS_ALLOW_HEADERS = ["*"]


settings = Settings()
