from tortoise import fields

from app.core.base.base_models import BaseModel
from app.applications.checks.schemas import RequestType


class Check(BaseModel):

    name = fields.CharField(max_length=255, unique=True)
    resource_node: fields.ForeignKeyRelation['ResourceNode'] = fields.ForeignKeyField(
        'models.ResourceNode', related_name='checks', to_field='uuid', on_delete=fields.CASCADE
    )
    results: fields.ReverseRelation['CheckResult']
    period = fields.IntField()
    expectation = fields.CharField(max_length=255)
    request_type = fields.CharEnumField(RequestType)
    
    class Meta:
        table = 'checks'


class CheckResult(BaseModel):
    
    verification: fields.ForeignKeyRelation['Check'] = fields.ForeignKeyField(
        'models.Check', related_name='results', to_field='uuid', on_delete=fields.CASCADE
    )
    response = fields.CharField(max_length=255)
    result = fields.BooleanField(default=False)
    timestamp  = fields.DatetimeField()
    
    class Meta:
        table = 'check_results'
