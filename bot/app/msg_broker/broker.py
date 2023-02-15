import asyncio
import json
import logging
from asyncio import sleep

import redis.asyncio as redis
from aiogram_dialog import DialogRegistry

from app.db.db_user.user_func import User


async def init_redis_sub(bot, registry, host, port, password):
    url = f"redis://:{password}@{host}:{port}/1"
    r = redis.from_url(url)
    async with r.pubsub() as pubsub:
        await pubsub.subscribe("channel1")
        logging.info(f"Launching a Message Broker")
        await asyncio.create_task(reader(pubsub, bot, registry))


async def send_notification(data, bot, registry: DialogRegistry):
    print(f"(Reader) Message Received: {data}")
    tg_ids = await User.get_all_tg_id()  # Потом будут получатся из data["tg_id"]
    for tg_id in tg_ids:
        status_icon = "🔴"
        if data["status"] == "warning":
            status_icon = "🟡"
        await bot.send_message(tg_id, f"У ресурса наблюдаются проблемы:\n{data['name']} {status_icon}")


async def reader(channel: redis.client.PubSub, bot, registry):
    while True:
        message = await channel.get_message(ignore_subscribe_messages=True)
        if message is not None:
            data = json.loads(message["data"])
            asyncio.create_task(send_notification(data, bot, registry))
        await sleep(0.1)
