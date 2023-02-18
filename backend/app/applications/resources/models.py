from typing import Optional

from tortoise import fields
from tortoise.exceptions import DoesNotExist

from app.core.base.base_models import BaseModel
from app.applications.resources.schemas import Status


class Resource(BaseModel):
    name = fields.CharField(max_length=255, unique=True)
    status = fields.CharEnumField(Status)
    nodes: fields.ReverseRelation["ResourceNode"]
    reviews: fields.ReverseRelation["Review"]
    subscriptions: fields.ReverseRelation["Subscription"]
    reports: fields.ReverseRelation["Report"]
    social_network_resports: fields.ReverseRelation["SocialNetworkReport"]

    @classmethod
    async def get_by_name(cls, name: str) -> Optional["Resource"]:
        try:
            query = cls.get_or_none(name=name)
            resource = await query
            return resource
        except DoesNotExist:
            return None

    class Meta:
        table = "resources"


class ResourceNode(BaseModel):
    resource: fields.ForeignKeyRelation["Resource"] = fields.ForeignKeyField(
        "models.Resource", related_name="nodes", to_field="uuid", on_delete=fields.CASCADE
    )
    url = fields.CharField(max_length=255, unique=True)
    checks: fields.ReverseRelation["Check"]

    class Meta:
        table = "resource_nodes"
