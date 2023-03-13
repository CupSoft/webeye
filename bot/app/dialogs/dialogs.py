import asyncio
import logging

from aiogram import Router
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode
from aiogram_dialog.api.exceptions import UnknownIntent
from aiohttp import ClientConnectorError

from app.db.db_user.user_func import User
from app.dialogs.states import RegistrationSG, MenuSG
from app.dialogs.universal_methods import login_user, del_message_by, del_keyboard
from app.dialogs.windows.bot_info.bot_info import InfoMainWin
from app.dialogs.windows.menu.menu import MenuMainWin
from app.dialogs.windows.registration.registration import RegMainWin, RegLoginWin
from app.dialogs.windows.removal_user.removal import RemovalMainWin
from app.dialogs.windows.subscriptions.subscriptions import SubscriptionsMainWin, SubscriptionsInfoWin
from app.my_errors import ApiError

dlg_router = Router()


@dlg_router.message(CommandStart())
async def handle_start_query(message: Message, dialog_manager: DialogManager):
    await del_keyboard(message)
    user_id = message.from_user.id
    if len(message.text.split()) > 1 and not await User.is_registered(user_id):
        try:
            await login_user(user_id, message.from_user.first_name, message.text.split()[1])
        except Exception as e:
            logging.error(e)
            warnings = await message.answer("❗️ Неверный токен")
            asyncio.create_task(del_message_by(warnings, 20))
    await starting_dispatcher(message, dialog_manager)


async def starting_dispatcher(message: Message, dialog_manager: DialogManager):
    user_id = message.from_user.id
    if not await User.is_registered(user_id):
        await dialog_manager.start(RegistrationSG.main, mode=StartMode.RESET_STACK)
    else:
        await dialog_manager.start(MenuSG.main, mode=StartMode.RESET_STACK)


@dlg_router.message(Text(text="Вызвать меню"))
async def update_menu(message: Message, dialog_manager: DialogManager):
    await del_keyboard(message)
    await message.delete()
    await dialog_manager.show()


@dlg_router.message(Command("ping"))
async def handle_ping(message: Message):
    await message.reply("pong🟢")


async def error_handler(event, dialog_manager: DialogManager):
    logging.error(event.exception)
    if isinstance(event.exception, UnknownIntent):
        # Handling an error related to an outdated callback
        await handle_start_query(event.update.callback_query, dialog_manager)
    elif isinstance(event.exception, ApiError):
        await starting_dispatcher(event.update.callback_query, dialog_manager)
        await event.update.callback_query.answer(
            "Ошибка сервера\n"
            "Вероятное решение проблемы - удаление аккаунта в боте и повторная авторизация", show_alert=True)
    elif isinstance(event.exception, ClientConnectorError):
        await event.update.callback_query.answer("Сервер недоступен", show_alert=True)
    else:
        return UNHANDLED


RegistrationDLG = Dialog(RegMainWin, RegLoginWin)
InfoDLG = Dialog(InfoMainWin)
MenuDLG = Dialog(MenuMainWin)
RemovalDLG = Dialog(RemovalMainWin)
SubscriptionsDLG = Dialog(SubscriptionsMainWin, SubscriptionsInfoWin)
