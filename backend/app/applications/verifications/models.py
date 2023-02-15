from typing import Optional

from tortoise import fields
from tortoise.exceptions import DoesNotExist

from app.core.base.base_models import BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin, BaseDBModel
from app.applications.verifications.schemas import RequestType


class Check(BaseDBModel, BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin):

    name = fields.CharField(max_length=255, unique=True)
    resource_node: fields.ForeignKeyRelation['ResourceNode'] = fields.ForeignKeyField(
        'models.ResourceNode', related_name='checks', to_field='hashed_id', on_delete=fields.CASCADE
    )
    results: fields.ReverseRelation['CheckResult']
    period = fields.IntField()
    expectation = fields.CharField(max_length=255)
    request_type = fields.CharEnumField(RequestType)
    
    class Meta:
        table = 'checks'


class CheckResult(BaseDBModel, BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin):
    
    Verification: fields.ForeignKeyRelation['Check'] = fields.ForeignKeyField(
        'models.Check', related_name='results', to_field='hashed_id', on_delete=fields.CASCADE
    )
    response = fields.CharField(max_length=255)
    result = fields.BooleanField(default=False)
    timestamp  = fields.DatetimeField()
    
    class Meta:
        table = 'check_results'
