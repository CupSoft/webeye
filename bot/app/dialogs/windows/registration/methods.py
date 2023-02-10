from aiogram.types import Message
from aiogram_dialog import DialogProtocol, DialogManager, ShowMode, StartMode

from app.db.db_user.user_func import User
from app.dialogs.states import MenuSG, RegistrationSG
from app.dialogs.universal_methods import del_message_by
from app.services.restapi.restapi import api_login_user


async def finish_registration(message: Message, dialog: DialogProtocol, manager: DialogManager):
    manager.show_mode = ShowMode.EDIT
    tg_id = message.from_user.id
    name, jwt_token = await api_login_user(tg_id, manager.dialog_data["email"], manager.dialog_data["password"])
    if name == "error":
        warnings = await message.answer("❗️ Пароль 123 для дебилов, попробуй снова")
        await del_message_by(warnings, 3)
        return
    await User.register(tg_id, name, manager.dialog_data["email"], jwt_token)
    await manager.start(MenuSG.main, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)


async def handle_email(message: Message, dialog: DialogProtocol, manager: DialogManager):
    manager.show_mode = ShowMode.EDIT
    await message.delete()
    manager.dialog_data["email"] = message.text
    await manager.switch_to(RegistrationSG.password)


async def handle_password(message: Message, dialog: DialogProtocol, manager: DialogManager):
    manager.show_mode = ShowMode.EDIT
    await message.delete()
    manager.dialog_data["password"] = message.text
    await finish_registration(message, dialog, manager)


async def getter_email(dialog_manager: DialogManager, **kwargs):
    return {"email": dialog_manager.dialog_data.get("email", "")}
