from aiogram.types import Message
from aiogram_dialog import DialogManager, DialogProtocol

from app.dialogs.universal_methods import get_tg_id_from_manager
from app.services.restapi.restapi import api_get_my_resources_uuids, api_get_resources

tmp_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


async def getter_main_subscriptions(dialog_manager: DialogManager, **kwargs):
    tg_id = get_tg_id_from_manager(dialog_manager)
    uuids = await api_get_my_resources_uuids(tg_id)
    resources = await api_get_resources(uuids)
    return {"resources": resources}


async def getter_info_subscriptions(dialog_manager: DialogManager, **kwargs):
    resource_uuid = dialog_manager.dialog_data["resource_uuid"]
    resource = (await api_get_resources([resource_uuid]))[0]
    status = "все в порядке 🟢"
    # if not resource.is_active:
    #     status = "наблюдаются сбои 🔴"
    return {"res_name": resource.name, "res_url": tmp_url, "status": status}


async def start_resource_info(message: Message, dialog: DialogProtocol, manager: DialogManager, resource_uuid: int):
    manager.dialog_data["resource_uuid"] = resource_uuid
    await manager.next()
