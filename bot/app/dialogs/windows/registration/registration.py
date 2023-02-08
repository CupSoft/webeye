from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Next, Back, Start
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import RegistrationSG, InfoSG
from app.dialogs.windows.registration.methods import handle_name

RegMainWin = Window(
    Const("📎 Регистрация"),
    Group(Next(Const("Войти")),
          Start(Const("Информация о боте"), state=InfoSG.main, id="info"),
          ),
    state=RegistrationSG.main,
)

RegLoginWin = Window(
    Format("Введите Имя:"),
    Group(Back(Const("Назад"))),
    MessageInput(handle_name),
    state=RegistrationSG.login,
)
