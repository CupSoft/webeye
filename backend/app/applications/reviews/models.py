from typing import Optional

from tortoise import fields
from tortoise.exceptions import DoesNotExist

from app.core.base.base_models import BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin, BaseDBModel


class Review(BaseDBModel, BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin):
    resource: fields.ForeignKeyRelation['Resource'] = fields.ForeignKeyField(
        'models.Resource', related_name='reviews', to_field='hashed_id', on_delete=fields.CASCADE
    )
    user: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User', related_name='reviews', to_field='hashed_id', on_delete=fields.CASCADE
    )
    text = fields.CharField(max_length=150)
    stars = fields.IntField()
    date = fields.DatetimeField()

    class Meta:
        table = 'reviews'