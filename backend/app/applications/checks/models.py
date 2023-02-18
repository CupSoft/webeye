from tortoise import fields

from app.core.base.base_models import BaseModel
from app.applications.checks.schemas import RequestType, SocialNetworks

from app.applications.resources.schemas import Status


class Check(BaseModel):

    name = fields.CharField(max_length=255, unique=True)
    resource_node: fields.ForeignKeyRelation['ResourceNode'] = fields.ForeignKeyField(
        'models.ResourceNode', related_name='checks', to_field='uuid', on_delete=fields.CASCADE
    )
    results: fields.ReverseRelation['CheckResult']
    expectation = fields.CharField(max_length=255)
    request_type = fields.CharEnumField(RequestType)
    
    class Meta:
        table = 'checks'


class CheckResult(BaseModel):
    
    parent_check: fields.ForeignKeyRelation['Check'] = fields.ForeignKeyField(
        'models.Check', related_name='results', to_field='uuid', on_delete=fields.CASCADE
    )
    response = fields.CharField(max_length=255)
    result = fields.BooleanField(default=False)
    timestamp  = fields.DatetimeField()
    location = fields.CharField(max_length=255)
    
    class Meta:
        table = 'check_results'


class Report(BaseModel):

    status = fields.CharEnumField(Status)
    is_moderated = fields.BooleanField(default=False)
    resource: fields.ForeignKeyRelation['Resource'] = fields.ForeignKeyField(
        'models.Resource', related_name='reports', to_field='uuid', on_delete=fields.CASCADE
    )
    user: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User', related_name='reports', to_field='uuid', on_delete=fields.CASCADE
    )

    class Meta:
        table = 'reports'


class SocialNetworkReport(BaseModel):
    
    resource: fields.ForeignKeyRelation['Resource'] = fields.ForeignKeyField(
        'models.Resource', related_name='social_network_resports', to_field='uuid', on_delete=fields.CASCADE
    )
    status = fields.CharEnumField(Status)
    is_moderated = fields.BooleanField(default=False)
    social_network = fields.CharEnumField(SocialNetworks)
    
    class Meta:
        table = 'social_network_reports'
