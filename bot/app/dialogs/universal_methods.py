from asyncio import sleep

from aiogram_dialog import DialogManager


def get_tg_id_from_manager(dialog_manager: DialogManager):
    return dialog_manager.middleware_data["event_from_user"].id


async def del_message_by(message, seconds):
    await sleep(seconds)
    await message.delete()
