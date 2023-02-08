from aiogram import Router
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode
from aiogram_dialog.api.exceptions import UnknownIntent

from app.db.db_user.user_func import User
from app.dialogs.states import RegistrationSG, MenuSG
from app.dialogs.windows.bot_info.bot_info import InfoMainWin
from app.dialogs.windows.menu.menu import MenuMainWin
from app.dialogs.windows.registration.registration import RegMainWin, RegLoginWin

dlg_router = Router()


@dlg_router.message(CommandStart())
async def handle_start_query(message: Message, dialog_manager: DialogManager):
    user_id = message.from_user.id
    if not await User.is_registered(user_id):
        await dialog_manager.start(RegistrationSG.main, mode=StartMode.RESET_STACK)
    else:
        await dialog_manager.start(MenuSG.main, mode=StartMode.RESET_STACK)


async def error_handler(event, dialog_manager: DialogManager):
    """Example of handling UnknownIntent Error and starting new dialog"""
    if isinstance(event.exception, UnknownIntent):
        await handle_start_query(event.update.callback_query, dialog_manager)
    else:
        return UNHANDLED


RegistrationDLG = Dialog(RegMainWin, RegLoginWin)
InfoDLG = Dialog(InfoMainWin)
MenuDLG = Dialog(MenuMainWin)
