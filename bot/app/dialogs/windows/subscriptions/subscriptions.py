from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Cancel, ScrollingGroup, Select, Back, Url
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import SubscriptionsSG
from app.dialogs.windows.subscriptions.methods import getter_main_subscriptions, start_resource_info, \
    getter_info_subscriptions

SubscriptionsMainWin = Window(
    Const("Ваши подписки:"),
    Group(
        ScrollingGroup(
            Select(Format("{item.status} {item.name}"), "resource_btn", lambda res: res.id, "resources",
                   on_click=start_resource_info),
            width=3, height=5,
            id="resources_group"),
        Cancel(Const("Меню")),
    ),
    state=SubscriptionsSG.main,
    getter=getter_main_subscriptions,
)

SubscriptionsInfoWin = Window(
    Format("{res_name}\nСтатус: {status}"),
    Group(
        Url(Const("Открыть на сайте"), Format("{res_url}")),
        Back(Const("Назад")),
    ),
    state=SubscriptionsSG.info,
    getter=getter_info_subscriptions,
)

