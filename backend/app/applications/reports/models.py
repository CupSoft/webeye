from tortoise import fields

from app.applications.resources.models import Resource
from app.applications.users.models import User
from app.core.base.base_models import BaseModel

from app.applications.resources.schemas import Status


class Report(BaseModel):
    status = fields.CharEnumField(Status)
    is_moderated = fields.BooleanField(default=False)
    resource: fields.ForeignKeyRelation["Resource"] = fields.ForeignKeyField(
        "models.Resource", related_name="reports", to_field="uuid", on_delete=fields.CASCADE
    )
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="reports", to_field="uuid", on_delete=fields.CASCADE
    )

    class Meta:
        table = "reports"
