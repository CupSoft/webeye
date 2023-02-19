import asyncio
import logging
from asyncio import sleep
import json

import redis.asyncio as redis
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram_dialog import DialogRegistry

from ..schemas import TelegramNotification, Status
from pydantic import parse_obj_as

from app.db.db_user.user_func import User


async def init_redis_sub(bot, registry, host, port, password):
    url = f"redis://:{password}@{host}:{port}/1"
    r = redis.from_url(url)
    async with r.pubsub() as pubsub:
        await pubsub.subscribe("telegram")
        logging.info(f"Launching a Message Broker")
        await asyncio.create_task(reader(pubsub, bot, registry))


async def send_notification(telegram_notification: TelegramNotification, bot, registry: DialogRegistry):
    print(telegram_notification)
    kb = [[KeyboardButton(text="Вызвать меню")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    status_icon = "🔴"
    if telegram_notification.resource_new_status == Status.partial:
        status_icon = "🟡"
    elif telegram_notification.resource_new_status == Status.ok:
        status_icon = "🟢"

    msg = await bot.send_message(
        telegram_notification.chat_id,
        f"{status_icon} Статус ресурса {telegram_notification.resource_name} изменился с"
        f" {telegram_notification.resource_old_status} на {telegram_notification.resource_new_status}",
        reply_markup=keyboard,
    )


async def reader(channel: redis.client.PubSub, bot, registry):
    while True:
        message = await channel.get_message(ignore_subscribe_messages=True)
        if message is not None:
            data = json.loads(message["data"])
            telegram_notification = parse_obj_as(TelegramNotification, data)
            asyncio.create_task(send_notification(telegram_notification, bot, registry))
        await sleep(0.1)
