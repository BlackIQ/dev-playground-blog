# Datetime
from datetime import datetime

# BaseSchema
from database.base import BaseSchema


# Category Schema
class CategoryBase(BaseSchema):
    slug: str
    name: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime
