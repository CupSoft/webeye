import redis.asyncio as redis
from app.settings import config
from app.applications.subscriptions.schemas import EmailNotification
import json


async def redis_publish_message(email: EmailNotification):
    data = json.dumps(email.dict())
    print(f"Publishing a message {data} to the channel 'mail'")
    r = redis.from_url(config.settings.REDIS_URL)

    res = r.publish("mail", data)
    print(res)
