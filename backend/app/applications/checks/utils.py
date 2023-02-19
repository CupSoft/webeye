import redis.asyncio as redis
from app.settings import config


async def redis_publish_message(msg):
    r = redis.from_url(config.REDIS_URL)
    r.publish('mail', msg)