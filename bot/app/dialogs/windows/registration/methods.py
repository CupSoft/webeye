from aiogram.types import Message
from aiogram_dialog import DialogProtocol, DialogManager, ShowMode

from app.db.db_user.user_func import User
from app.dialogs.states import MenuSG
from app.dialogs.universal_methods import get_tg_id_from_manager, del_message_by


async def finish_registration(message: Message, dialog: DialogProtocol, manager: DialogManager):
    manager.show_mode = ShowMode.EDIT
    tg_id = message.from_user.id
    await message.delete()
    username = manager.dialog_data["name"]
    if username == "admin":
        warnings = await message.answer("❗️ Не используйте имя admin")
        await del_message_by(warnings, 3)
        return

    await User.register(tg_id, username)
    await manager.done()
    await manager.start(MenuSG.main, show_mode=ShowMode.EDIT)


async def handle_name(message: Message, dialog: DialogProtocol, manager: DialogManager):
    manager.dialog_data["name"] = message.text
    await finish_registration(message, dialog, manager)
