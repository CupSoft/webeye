import asyncio
import json
import logging
from asyncio import sleep
from decouple import config

import coloredlogs as coloredlogs
import redis.asyncio as redis

from config import settings as s
from schemas import EmailNotification
from sender import sender

from pydantic import parse_obj_as

coloredlogs.install(level=logging.INFO)


async def reader(channel: redis.client.PubSub):
    while True:
        message = await channel.get_message(ignore_subscribe_messages=True)
        if message is not None:
            email = parse_obj_as(EmailNotification, json.loads(message["data"]))
            asyncio.create_task(sender(email))

        await sleep(0.1)


async def main():
    logging.info("Redis init")
    url = s.REDIS_URL
    r = redis.from_url(url)
    async with r.pubsub() as pubsub:
        await pubsub.subscribe("mail")
        logging.info(f"Launching a Message Broker")
        await asyncio.create_task(reader(pubsub))


if __name__ == "__main__":
    asyncio.run(main())
