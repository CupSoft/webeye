from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button, Cancel
from aiogram_dialog.widgets.text import Const

from app.dialogs.states import RemovalSG
from app.dialogs.windows.removal_user.methods import delete_user

RemovalMainWin = Window(
    Const("Вы уверены, что хотите удалить свой аккаунт?"),
    Group(
        Button(Const("Да"), on_click=delete_user, id="yes"),
        Cancel(Const("Нет")),
    ),
    state=RemovalSG.main,
)
