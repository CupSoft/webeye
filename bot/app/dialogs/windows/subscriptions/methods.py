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
    t_resources.append(TestResource(i + 4, str(i), True))


async def getter_subscriptions(dialog_manager: DialogManager, **kwargs):
    resources = t_resources
    return {"resources": resources}


async def resource_info(message: Message, dialog: DialogProtocol, manager: DialogManager, resource_id: int):
    print(resource_id)
    pass
