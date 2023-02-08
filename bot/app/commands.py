from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault

from app.settings import settings

users_commands = {
    "help": "Показать список команд",
    "about": "Показать информацию о боте",
    "dialog": "Запустить тестовый диалог",
}

owner_commands = {**users_commands, "ping": "Check bot ping", "stats": "Show bot stats"}


async def setup_bot_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command=command, description=description)
            for command, description in owner_commands.items()
        ],
        scope=BotCommandScopeChat(chat_id=settings().ADMIN_ID),
    )

    await bot.set_my_commands(
        [
            BotCommand(command=command, description=description)
            for command, description in users_commands.items()
        ],
        scope=BotCommandScopeDefault(),
    )


async def remove_bot_commands(bot: Bot):
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    await bot.delete_my_commands(
        scope=BotCommandScopeChat(chat_id=settings().ADMIN_ID)
    )
