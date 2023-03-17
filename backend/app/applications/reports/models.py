from tortoise import fields

from app.core.base.base_models import BaseModel

from app.applications.resources.schemas import Status


class Report(BaseModel):
    status = fields.CharEnumField(Status)
    text = fields.CharField(max_length=255, default="")
    is_moderated = fields.BooleanField(default=False)
    resource: fields.ForeignKeyRelation["Resource"] = fields.ForeignKeyField(
        "models.Resource", related_name="reports", to_field="uuid", on_delete=fields.CASCADE
    )
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="reports", to_field="uuid", on_delete=fields.CASCADE
    )
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reports"
