from typing import Optional

from tortoise import fields
from tortoise.exceptions import DoesNotExist

from app.core.base.base_models import BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin, BaseDBModel
from app.applications.resources.schemas import Status


class Resource(BaseDBModel, BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin):

    name = fields.CharField(max_length=255, unique=True)
    status = fields.CharEnumField(Status)
    nodes: fields.ReverseRelation['ResourceNode']
    reviews: fields.ReverseRelation["Review"]

    class Meta:
        table = 'resources'


class ResourceNode(BaseDBModel, BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin):
    
    resource: fields.ForeignKeyRelation['Resource'] = fields.ForeignKeyField(
        'models.Resource', related_name='nodes', to_field='hashed_id', on_delete=fields.CASCADE
    )
    url = fields.CharField(max_length=255)
    checks: fields.ReverseRelation['Check']
    
    class Meta:
        table = 'resource_nodes'
