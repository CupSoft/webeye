from tortoise import fields

from app.core.base.base_models import BaseModel

from app.applications.resources.schemas import Status
from app.applications.social_reports.schemas import SocialNetworks


class SocialNetworkReport(BaseModel):
    resource: fields.ForeignKeyRelation["Resource"] = fields.ForeignKeyField(
        "models.Resource", related_name="social_network_reports", to_field="uuid", on_delete=fields.CASCADE
    )
    status = fields.CharEnumField(Status)
    is_moderated = fields.BooleanField(default=False)
    social_network = fields.CharEnumField(SocialNetworks)
    link = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "social_network_reports"
