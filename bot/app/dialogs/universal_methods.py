from asyncio import sleep

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram_dialog import DialogManager

from app.db.db_user.user_func import User
from app.services.restapi.restapi import api_get_jwt, api_delete_user


def get_tg_id_from_manager(dialog_manager: DialogManager):
    return dialog_manager.middleware_data["event_from_user"].id


async def del_message_by(message, seconds):
    await sleep(seconds)
    await message.delete()


async def login_user(tg_id: int, name: str, short_jwt: str):
    print(f"login_user: {tg_id}, {name}, {short_jwt}")
    await api_delete_user(tg_id)
    jwt = await api_get_jwt(short_jwt, tg_id)
    await User.register(tg_id, name, jwt)


async def del_keyboard(message: Message):
    msg = await message.answer("1", reply_markup=ReplyKeyboardRemove())
    await msg.delete()
