from tortoise import fields

from app.core.base.base_models import BaseModel
from app.applications.resources.schemas import Status


class Resource(BaseModel):

    name = fields.CharField(max_length=255, unique=True)
    status = fields.CharEnumField(Status)
    nodes: fields.ReverseRelation['ResourceNode']
    reviews: fields.ReverseRelation["Review"]

    class Meta:
        table = 'resources'


class ResourceNode(BaseModel):
    
    resource: fields.ForeignKeyRelation['Resource'] = fields.ForeignKeyField(
        'models.Resource', related_name='nodes', to_field='uuid', on_delete=fields.CASCADE
    )
    url = fields.CharField(max_length=255)
    checks: fields.ReverseRelation['Check']
    
    class Meta:
        table = 'resource_nodes'
