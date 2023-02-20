from decouple import config


class Settings:
    REDIS_PASSWORD = config("REDIS_PASSWORD", default="")
    REDIS_HOST = config("REDIS_HOST", default="localhost")
    REDIS_PORT = config("REDIS_PORT", cast=int, default=6379)
    REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/1"

    SMTP_HOST = config("SMTP_HOST")
    SMTP_PORT = config("SMTP_PORT", cast=int, default=587)
    SMTP_USERNAME = config("SMTP_USERNAME")
    SMTP_PASSWORD = config("SMTP_PASSWORD")


settings = Settings()
