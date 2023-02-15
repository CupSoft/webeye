from aiogram_dialog import DialogRegistry

from app.dialogs.dialogs import RegistrationDLG, InfoDLG, MenuDLG, RemovalDLG, SubscriptionsDLG


def register_dialogs(registry: DialogRegistry):
    registry.register(RegistrationDLG)
    registry.register(InfoDLG)
    registry.register(MenuDLG)
    registry.register(RemovalDLG)
    registry.register(SubscriptionsDLG)

