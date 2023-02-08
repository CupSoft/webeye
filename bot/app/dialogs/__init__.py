from aiogram_dialog import DialogRegistry

from app.dialogs.dialogs import RegistrationDLG, InfoDLG, MenuDLG


def register_dialogs(registry: DialogRegistry):
    registry.register(RegistrationDLG)
    registry.register(InfoDLG)
    registry.register(MenuDLG)

