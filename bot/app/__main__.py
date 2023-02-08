import asyncio
import logging
import platform

import coloredlogs
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram_dialog import DialogRegistry
from redis import Redis

from app import db
from app.settings import settings
from app.commands import setup_bot_commands, remove_bot_commands
from app.db import init_orm, close_orm
from app.dialogs import register_dialogs
from app.dialogs.dialogs import dlg_router, error_handler



async def on_startup(dispatcher: Dispatcher, bot: Bot):
    bot_info = await bot.get_me()

    logging.info(f"Name - {bot_info.full_name}")
    logging.info(f"Username - @{bot_info.username}")
    logging.info(f"ID - {bot_info.id}")

    states = {
        True: "Enabled",
        False: "Disabled",
    }
    logging.debug(f"Groups Mode - {states[bot_info.can_join_groups]}")
    logging.debug(f"Privacy Mode - {states[not bot_info.can_read_all_group_messages]}")
    logging.debug(f"Inline Mode - {states[bot_info.supports_inline_queries]}")
    logging.error("Bot started!")


async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    logging.warning("Stopping bot...")
    await remove_bot_commands(bot)
    await dispatcher.fsm.storage.close()
    await bot.session.close()
    await close_orm()


async def main():
    coloredlogs.install(level=logging.INFO)
    logging.warning("Starting bot...")

    # Инициализация БД
    tortoise_config = db.generate_config()
    try:
        await db.create_models(tortoise_config)
    except FileExistsError:
        await db.migrate_models(tortoise_config)
    await init_orm(tortoise_config)

    # Инициализация REDIS
    if settings().USE_REDIS:
        storage = RedisStorage(
            redis=Redis(host=settings().REDIS_HOST, port=settings().REDIS_PORT, db=0,
                        password=settings().REDIS_PASSWORD),
            key_builder=DefaultKeyBuilder(with_destiny=True),
        )
    else:
        storage = MemoryStorage()

    # Инициализация диспетчера
    bot = Bot(token=settings().TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=storage)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.errors.register(error_handler)

    # Регистрация роутов
    dp.include_router(dlg_router)
    registry = DialogRegistry(dp)
    register_dialogs(registry)
    await setup_bot_commands(bot)

    await dp.start_polling(bot, on_shutdown=on_shutdown, on_startup=on_startup)


if __name__ == "__main__":
    try:
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
