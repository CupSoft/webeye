import redis.asyncio as redis
from app.settings import config
from app.applications.subscriptions.schemas import EmailNotification
import json


async def redis_publish_message(email: EmailNotification):
    data = email.dict()
    data["resource_uuid"] = str(email.resource_uuid)
    data = json.dumps(data)

    r = await redis.from_url(config.settings.REDIS_URL)
    res = await r.publish("mail", data)
