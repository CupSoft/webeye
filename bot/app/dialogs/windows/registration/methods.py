import asyncio

from aiogram.types import Message
from aiogram_dialog import DialogProtocol, DialogManager, ShowMode, StartMode

from app.dialogs.states import MenuSG
from app.dialogs.universal_methods import del_message_by, login_user


async def finish_registration(message: Message, dialog: DialogProtocol, manager: DialogManager):
    manager.show_mode = ShowMode.EDIT
    tg_id = message.from_user.id
    try:
        await login_user(tg_id, message.from_user.first_name, manager.dialog_data["short_jwt"])
    except Exception as e:
        print(e)
        warnings = await message.answer("❗️ Неверный токен")
        asyncio.create_task(del_message_by(warnings, 3))
        return
    await manager.start(MenuSG.main, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)


async def handle_token(message: Message, dialog: DialogProtocol, manager: DialogManager):
    manager.show_mode = ShowMode.EDIT
    await message.delete()
    manager.dialog_data["short_jwt"] = message.text
    await finish_registration(message, dialog, manager)
