from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Cancel, ScrollingGroup, Select
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import SubscriptionsSG
from app.dialogs.windows.subscriptions.methods import getter_subscriptions, resource_info

SubscriptionsMainWin = Window(
    Const("Ваши подписки:"),
    Group(
        ScrollingGroup(
            Select(Format("{item.status} {item.name}"), "resource_btn", lambda res: res.id, "resources",
                   on_click=resource_info),
            width=3, height=5,
            id="resources_group"),
        Cancel(Const("Меню")),
    ),
    state=SubscriptionsSG.main,
    getter=getter_subscriptions,
)
