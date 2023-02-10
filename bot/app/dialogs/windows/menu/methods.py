from aiogram.types import Message
from aiogram_dialog import DialogManager, DialogProtocol, ShowMode, StartMode

from app.db.db_user.user_func import User
from app.dialogs.states import RegistrationSG
from app.dialogs.universal_methods import get_tg_id_from_manager
from app.services.restapi.restapi import api_delete_user


async def getter_menu(dialog_manager: DialogManager, **kwargs):
    tg_id = get_tg_id_from_manager(dialog_manager)
    user = await User.get_by_tg(tg_id)
    return {"name": user.name,
            "not_btn_text": "Отключить уведомления" if user.notifications else "Включить уведомления",
            "not_text": "Уведомления включены ✅" if user.notifications else "Уведомления отключены ❌"}


async def change_notifications(message: Message, dialog: DialogProtocol, manager: DialogManager):
    tg_id = get_tg_id_from_manager(manager)
    user = await User.get_by_tg(tg_id)
    user.notifications = not user.notifications
    await user.save()

