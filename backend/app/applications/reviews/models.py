from tortoise import fields

from app.applications.resources.models import Resource
from app.applications.users.models import User
from app.core.base.base_models import BaseModel


class Review(BaseModel):
    resource: fields.ForeignKeyRelation["Resource"] = fields.ForeignKeyField(
        "models.Resource", related_name="reviews", to_field="uuid", on_delete=fields.CASCADE
    )
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="reviews", to_field="uuid", on_delete=fields.CASCADE
    )
    text = fields.CharField(max_length=150)
    stars = fields.IntField()
    date = fields.DatetimeField()

    class Meta:
        table = "reviews"
