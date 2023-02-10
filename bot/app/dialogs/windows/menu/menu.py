from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Start, Button
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import InfoSG, MenuSG, RemovalSG
from app.dialogs.windows.menu.methods import getter_menu, change_notifications

MenuMainWin = Window(
    Format("Привет {name}\n{not_text}"),
    Group(
        Start(Const("Информация о боте"), state=InfoSG.main, id="info"),
        Button(Format("{not_btn_text}"), on_click=change_notifications, id="notifications"),
        Start(Const("Удалить аккаунт"), state=RemovalSG.main, id="removal"),
    ),
    getter=getter_menu,
    state=MenuSG.main,
)
