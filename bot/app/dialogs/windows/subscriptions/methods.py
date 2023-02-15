from aiogram.types import Message
from aiogram_dialog import DialogManager, DialogProtocol


class TestResource:
    def __init__(self, id: int, name: str, is_active: bool):
        self.id = id
        self.name = name
        self.is_active = is_active
        self.status = "🟢" if is_active else "🔴"

    def __repr__(self):
        return f"TestResource(id={self.id}, name={self.name}, is_active={self.is_active})"


t_resources = [
    TestResource(1, "ВШЭ", True),
    TestResource(2, "ИТМО", False),
    TestResource(3, "МГУ", True),
    TestResource(4, "РГПУ Герцена", False),
]
for i in range(50):
    t_resources.append(TestResource(i + 5, str(i), True))

tmp_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


async def getter_main_subscriptions(dialog_manager: DialogManager, **kwargs):
    resources = t_resources
    return {"resources": resources}


async def getter_info_subscriptions(dialog_manager: DialogManager, **kwargs):
    resource_id = dialog_manager.dialog_data["current_resource"]
    resource = t_resources[int(resource_id) - 1]
    status = "все в порядке🟢"
    if not resource.is_active:
        status = "наблюдаются сбои🔴"
    return {"res_name": resource.name, "res_url": tmp_url, "status": status}


async def start_resource_info(message: Message, dialog: DialogProtocol, manager: DialogManager, resource_id: int):
    manager.dialog_data["current_resource"] = resource_id
    await manager.next()
