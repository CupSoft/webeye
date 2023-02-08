from aiogram_dialog import DialogManager

from app.db.db_user.user_func import User
from app.dialogs.universal_methods import get_tg_id_from_manager


async def get_name(dialog_manager: DialogManager, **kwargs):
    tg_id = get_tg_id_from_manager(dialog_manager)
    user = await User.get_by_tg(tg_id)
    return {
        "name": user.name
    }
