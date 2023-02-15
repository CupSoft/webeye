from aiogram.fsm.state import StatesGroup, State


class RegistrationSG(StatesGroup):
    main = State()
    login = State()


class MenuSG(StatesGroup):
    main = State()


class InfoSG(StatesGroup):
    main = State()


class RemovalSG(StatesGroup):
    main = State()


class SubscriptionsSG(StatesGroup):
    main = State()
    info = State()


class ResourcesSG(StatesGroup):
    main = State()
