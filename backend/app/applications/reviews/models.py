from tortoise import fields

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
    datetime = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reviews"
