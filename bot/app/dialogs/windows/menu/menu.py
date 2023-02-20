from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Start, Button
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import InfoSG, MenuSG, RemovalSG, SubscriptionsSG, ResourcesSG
from app.dialogs.windows.menu.methods import getter_menu, change_notifications

MenuMainWin = Window(
    Format("Привет {name} {sticker}"),
    Group(
        Start(Const("Информация о боте"), state=InfoSG.main, id="info_btn"),
        Start(Const("Мои подписки"), state=SubscriptionsSG.main, id="subscriptions_btn"),
        # Start(Const("Популярные ресурсы"), state=ResourcesSG.main, id="resources_btn"),
        # Button(Format("{not_btn_text}"), on_click=change_notifications, id="notifications_btn"),
        Start(Const("Отключить телеграмм бота"), state=RemovalSG.main, id="removal_user_btn"),
        width=2,
    ),
    getter=getter_menu,
    state=MenuSG.main,
)
