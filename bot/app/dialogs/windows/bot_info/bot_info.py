from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Cancel
from aiogram_dialog.widgets.text import Const

from app.dialogs.states import InfoSG

InfoMainWin = Window(
    Const("Бот предназначен для получения уведомлений о недоступности сайтов вузов. "
          "Вы можете включить отслеживание интересующих вас вузов через сайт."),
    Group(Cancel(Const("Назад")),
          ),
    state=InfoSG.main,
)
