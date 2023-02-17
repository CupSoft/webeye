import asyncio
import json
import logging
from asyncio import sleep
from os import getenv

import coloredlogs as coloredlogs
import redis.asyncio as redis
from dotenv import load_dotenv

from sender import sender

load_dotenv()
coloredlogs.install(level=logging.INFO)


async def reader(channel: redis.client.PubSub):
    while True:
        message = await channel.get_message(ignore_subscribe_messages=True)
        if message is not None:
            data = json.loads(message["data"])
            asyncio.create_task(sender(data["to"], data["event"], data["details"]))
        await sleep(0.1)


async def main():
    logging.info("Redis init")
    url = f"redis://:{getenv('REDIS_PASSWORD', '')}@{getenv('REDIS_HOST', 'localhost')}:{getenv('REDIS_PORT', 6379)}/1"
    r = redis.from_url(url)
    async with r.pubsub() as pubsub:
        await pubsub.subscribe("mail")
        logging.info(f"Launching a Message Broker")
        await asyncio.create_task(reader(pubsub))


if __name__ == "__main__":
    asyncio.run(main())
