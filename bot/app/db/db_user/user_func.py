from typing import Union

from tortoise.exceptions import DoesNotExist

from app.db.db_user import user_models


class User(user_models.User):
    @classmethod
    async def is_registered(cls, telegram_id: int) -> Union[user_models.User, bool]:
        try:
            return await cls.get(telegram_id=telegram_id)
        except DoesNotExist:
            return False

    @classmethod
    async def register(cls, telegram_id: int, name: str, jwt_token: str):
        await User(telegram_id=telegram_id, name=name, jwt_token=jwt_token).save()

    @classmethod
    async def get_by_tg(cls, telegram_id: int) -> Union[user_models.User, bool]:
        try:
            return await cls.get(telegram_id=telegram_id)
        except DoesNotExist:
            return False

    @classmethod
    async def get_all_tg_id(cls):
        return await cls.all().values_list("telegram_id", flat=True)

    @classmethod
    async def get_count(cls) -> int:
        return await cls.all().count()
