import aiohttp

from app.my_errors import ApiError, TOKEN_ERROR
from app.schemas.resources_pdc import Resource
from app.services.restapi.URLS import URL_GET_JWT, URL_GET_MY_RESOURCES_UUIDS, URL_GET_RESOURCE, URL_DELETE_USER
from app.services.restapi.scripts import get_headers


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


async def api_get_my_resources_uuids(tg_id: int) -> list[str]:
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_GET_MY_RESOURCES_UUIDS, headers=await get_headers(tg_id)) as resp:
            if resp.status != 200:
                raise ApiError(TOKEN_ERROR)
            data = await resp.json()
            return [resource["resource_uuid"] for resource in data if resource["to_telegram"] is True]


async def api_get_resources(uuids: list) -> list[Resource]:
    async with aiohttp.ClientSession() as session:
        resources = []
        for uuid in uuids:
            async with session.get(f"{URL_GET_RESOURCE}{uuid}", headers=await get_headers()) as resp:
                if resp.status != 200:
                    raise ApiError(TOKEN_ERROR)
                data = await resp.json()
                resources.append(Resource(**data))
        return resources


async def api_delete_user(tg_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.delete(URL_DELETE_USER, headers=await get_headers(tg_id)) as resp:
            return True
