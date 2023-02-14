from typing import Optional

from tortoise import fields
from tortoise.exceptions import DoesNotExist

from app.applications.users.schemas import BaseUserCreate
from app.core.base.base_models import BaseCreatedUpdatedAtModel, UUIDDBModel, BaseDBModel
from app.core.auth.utils import password


class Resource(BaseDBModel, BaseCreatedUpdatedAtModel, UUIDDBModel):

    name = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    moderators = fields.ManyToManyField(
        "users.models.User", related_name="resources"
    )
    is_active = fields.BooleanField(default=True)
    is_superuser = fields.BooleanField(default=False)

    def full_name(self) -> str:
        if self.first_name or self.last_name:
            return f"{self.first_name or ''} {self.last_name or ''}".strip()
        return self.username

    @classmethod
    async def get_by_email(cls, email: str) -> Optional["User"]:
        try:
            query = cls.get_or_none(email=email)
            user = await query
            return user
        except DoesNotExist:
            return None

    @classmethod
    async def get_by_username(cls, username: str) -> Optional["User"]:
        try:
            query = cls.get(username=username)
            user = await query
            return user
        except DoesNotExist:
            return None

    @classmethod
    async def create(cls, user: BaseUserCreate) -> "User":
        user_dict = user.dict()
        password_hash = password.get_password_hash(password=user.password)
        model = cls(**user_dict, password_hash=password_hash)
        await model.save()
        return model

    class Meta:
        table = 'users'

    class PydanticMeta:
        computed = ["full_name"]


class ResourceNode(BaseDBModel, BaseCreatedUpdatedAtModel, UUIDDBModel):
    
    user: fields.ForeignKeyRelation['User'] = fields.OneToOneField(
        'models.User', on_delete=fields.CASCADE
    )
    
    class Meta:
        table = 'admins'
        
    