from aiogram.fsm.state import StatesGroup, State


class RegistrationSG(StatesGroup):
    main = State()
    login = State()
    password = State()


class MenuSG(StatesGroup):
    main = State()


class InfoSG(StatesGroup):
    main = State()
