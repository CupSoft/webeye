import aiohttp

from app.my_errors import ApiError, TOKEN_ERROR
from app.services.restapi.URLS import URL_GET_JWT


async def api_get_jwt(short_jwt: str, tg_id: int):
    async with aiohttp.ClientSession() as session:
        body = {
            "token": short_jwt,
            "id": str(tg_id),
        }
        async with session.post(URL_GET_JWT, json=body) as resp:
            if resp.status != 200:
                raise ApiError(TOKEN_ERROR)
            data = await resp.json()
            return data["access_token"]


async def api_delete_user(tg_id: int):
    return True
