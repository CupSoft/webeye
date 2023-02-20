from aiogram.types import Message
from aiogram_dialog import DialogManager, DialogProtocol

from app.dialogs.universal_methods import get_tg_id_from_manager
from app.schemas.broker_pdc import Status
from app.services.restapi.restapi import api_get_my_resources_uuids, api_get_resources
from app.settings import settings

tmp_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


async def getter_main_subscriptions(dialog_manager: DialogManager, **kwargs):
    tg_id = get_tg_id_from_manager(dialog_manager)
    uuids = await api_get_my_resources_uuids(tg_id)
    resources = await api_get_resources(uuids)
    for resource in resources:
        point = "🟢"
        if resource.status == Status.partial:
            point = "🟡"
        elif resource.status == Status.critical:
            point = "🔴"
        resource.name = f"{point} {resource.name}"
    return {"resources": resources}


async def getter_info_subscriptions(dialog_manager: DialogManager, **kwargs):
    resource_uuid = dialog_manager.dialog_data["resource_uuid"]
    resource = (await api_get_resources([resource_uuid]))[0]
    sub_url = settings().URL
    if sub_url[-1] != "/":
        sub_url = f"{sub_url}/"
    sub_url = f"{sub_url}sources/{resource.uuid}"
    status = "все в порядке 🟢"
    if resource.status == Status.partial:
        status = "Сервис работает нестабильно 🟡"
    elif resource.status == Status.critical:
        status = "Сервис не работает 🔴"

    return {"res_name": resource.name, "res_url": sub_url, "status": status,
            "rating": "Недостаточно отзывов" if resource.rating is None else resource.rating}


async def start_resource_info(message: Message, dialog: DialogProtocol, manager: DialogManager, resource_uuid: int):
    manager.dialog_data["resource_uuid"] = resource_uuid
    await manager.next()
