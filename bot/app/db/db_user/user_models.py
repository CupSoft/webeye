from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField()
    jwt_token = fields.CharField(max_length=255)
    name = fields.CharField(max_length=255)
    notifications = fields.BooleanField(default=True)
