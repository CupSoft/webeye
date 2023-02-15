import asyncio
import json
from asyncio import sleep

import redis.asyncio as redis
from aiogram_dialog import DialogRegistry

from app.db.db_user.user_func import User


async def init_redis_sub(bot, registry):
    r = redis.Redis()
    async with r.pubsub() as pubsub:
        await pubsub.subscribe("channel1")
        print("broker start")
        await asyncio.create_task(reader(pubsub, bot, registry))


async def send_notification(data, bot, registry: DialogRegistry):
    print(f"(Reader) Message Received: {data}")
    tg_ids = await User.get_all_tg_id()
    for tg_id in tg_ids:
        await bot.send_message(tg_id, "test message")
        registry.dialogs["MenuSG.main"].bg().show(user=tg_id)
        print()


async def reader(channel: redis.client.PubSub, bot, registry):
    while True:
        message = await channel.get_message(ignore_subscribe_messages=True)
        if message is not None:
            data = json.loads(message["data"])
            asyncio.create_task(send_notification(data, bot, registry))
        await sleep(0.1)
