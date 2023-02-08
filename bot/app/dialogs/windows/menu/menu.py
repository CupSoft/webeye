from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Start
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import InfoSG, MenuSG
from app.dialogs.windows.menu.methods import get_name

MenuMainWin = Window(
    Format("Привет {name}"),
    Group(
        Start(Const("Информация о боте"), state=InfoSG.main, id="info"),
    ),
    getter=get_name,
    state=MenuSG.main,
)
