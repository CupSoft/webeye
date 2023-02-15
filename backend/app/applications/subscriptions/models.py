from typing import Optional

from tortoise import fields
from tortoise.exceptions import DoesNotExist

from app.core.base.base_models import BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin, BaseDBModel

from app.applications.subscriptions.schemas import SubscriptionType


class Subscription(BaseDBModel, BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin):

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