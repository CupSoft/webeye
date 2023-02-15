import asyncio

from aiogram import Router
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode
from aiogram_dialog.api.exceptions import UnknownIntent

from app.db.db_user.user_func import User
from app.dialogs.states import RegistrationSG, MenuSG
from app.dialogs.universal_methods import login_user, del_message_by, del_keyboard
from app.dialogs.windows.bot_info.bot_info import InfoMainWin
from app.dialogs.windows.menu.menu import MenuMainWin
from app.dialogs.windows.registration.registration import RegMainWin, RegLoginWin
from app.dialogs.windows.removal_user.removal import RemovalMainWin
from app.dialogs.windows.subscriptions.subscriptions import SubscriptionsMainWin

dlg_router = Router()


@dlg_router.message(CommandStart())
async def handle_start_query(message: Message, dialog_manager: DialogManager):
    await del_keyboard(message)
    user_id = message.from_user.id
    if "text" in message and len(message.text.split()) > 1:
        try:
            await login_user(user_id, message.from_user.first_name, message.text.split()[1])
        except Exception as e:
            print(e)
            warnings = await message.answer("❗️ Неверный токен")
            asyncio.create_task(del_message_by(warnings, 20))

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
    if isinstance(event.exception, UnknownIntent):
        # Ловим ошибку устаревшего callback
        await handle_start_query(event.update.callback_query, dialog_manager)
    else:
        return UNHANDLED


RegistrationDLG = Dialog(RegMainWin, RegLoginWin)
InfoDLG = Dialog(InfoMainWin)
MenuDLG = Dialog(MenuMainWin)
RemovalDLG = Dialog(RemovalMainWin)
SubscriptionsDLG = Dialog(SubscriptionsMainWin)
