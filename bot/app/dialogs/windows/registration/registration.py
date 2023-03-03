from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Next, Back, Start, Url
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import RegistrationSG, InfoSG
from app.dialogs.windows.registration.methods import handle_token
from app.settings import settings

RegMainWin = Window(
    Const("📎 Привет! Я бот сервиса webeye. Отслеживайте состояние ваших любимых вузов 😍"),
    Group(Url(Const("Регистрация"), Const(f"{settings().URL}auth")),
          Next(Const("Авторизация")),
          Start(Const("Информация о боте"), state=InfoSG.main, id="info_btn"),
          width=2,
          ),
    state=RegistrationSG.main,
)
RegLoginWin = Window(
    Format("Введите код пользователя"),
    Group(Back(Const("Назад"))),
    MessageInput(handle_token),
    state=RegistrationSG.login,
)