import redis.asyncio as redis
from app.settings import config
from app.applications.subscriptions.schemas import EmailNotification, TelegramNotification
import json


async def redis_publish_email(email: EmailNotification):
    data = email.dict()
    data["resource_uuid"] = str(email.resource_uuid)
    data = json.dumps(data)

    r = await redis.from_url(config.settings.REDIS_URL)
    await r.publish("mail", data)


async def redis_publish_telegram(telegram: TelegramNotification):
    data = telegram.dict()
    data["resource_uuid"] = str(telegram.resource_uuid)
    data = json.dumps(data)

    r = await redis.from_url(config.settings.REDIS_URL)
    await r.publish("telegram", data)
