from tortoise import fields

from app.core.base.base_models import BaseModel

from app.applications.subscriptions.schemas import SubscriptionType


class Subscription(BaseModel):

    to_telegram = fields.BooleanField(default=False)
    to_email = fields.BooleanField(default=False)
    notification_level = fields.IntEnumField(SubscriptionType)
    resource: fields.ForeignKeyRelation['Resource'] = fields.ForeignKeyField(
        'models.Resource', related_name='subscriptions', to_field='uuid', on_delete=fields.CASCADE
    )
    user: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User', related_name='subscriptions', to_field='uuid', on_delete=fields.CASCADE
    )

    class Meta:
        table = 'subscriptions'