from typing import Optional

from tortoise import fields
from tortoise.exceptions import DoesNotExist

from app.applications.users.schemas import BaseUserCreate
from app.core.base.base_models import BaseCreatedUpdatedAtModel, UUIDDBModel, BaseDBModel
from app.core.auth.utils import password


class Resource(BaseDBModel, BaseCreatedUpdatedAtModel, UUIDDBModel):

    name = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    moderators = fields.ManyToManyField(
        "models.User", related_name="resources"
    )
    is_active = fields.BooleanField(default=True)

    class Meta:
        table = 'resources'


class ResourceNode(BaseDBModel, BaseCreatedUpdatedAtModel, UUIDDBModel):
    
    user: fields.ForeignKeyRelation['Resource'] = fields.OneToOneField(
        'models.Resource', on_delete=fields.CASCADE
    )
    
    class Meta:
        table = 'resource_nodes'
        
    