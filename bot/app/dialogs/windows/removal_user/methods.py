from aiogram.types import Message
from aiogram_dialog import DialogManager, DialogProtocol, ShowMode, StartMode

from app.db.db_user.user_func import User
from app.dialogs.states import RegistrationSG
from app.dialogs.universal_methods import get_tg_id_from_manager
from app.services.restapi.restapi import api_delete_user


async def delete_user(message: Message, dialog: DialogProtocol, manager: DialogManager):
    tg_id = get_tg_id_from_manager(manager)
    if await api_delete_user(tg_id) is True:
        user = await User.get_by_tg(tg_id)
        await user.delete()
        await manager.start(RegistrationSG.main, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
