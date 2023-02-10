from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Next, Back, Start, Url
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import RegistrationSG, InfoSG
from app.dialogs.windows.registration.methods import handle_email, handle_password, getter_email

RegMainWin = Window(
    Const("📎 Привет! Я бот сервиса ..."),
    Group(Url(Const("Регистрация"), Const("https://www.youtube.com/watch?v=dQw4w9WgXcQ")),
          Next(Const("Авторизация")),
          Start(Const("Информация о боте"), state=InfoSG.main, id="info"),
          width=2,
          ),
    state=RegistrationSG.main,
)
RegLoginWin = Window(
    Format("Введите mail"),
    Group(Back(Const("Назад"))),
    MessageInput(handle_email),
    state=RegistrationSG.login,
)
RegPasswordWin = Window(
    Format("Введите пароль:\nВход в {email}"),
    Group(Back(Const("Назад"))),
    MessageInput(handle_password),
    state=RegistrationSG.password,
    getter=getter_email,
)
