# Datetime
from datetime import datetime

# BaseSchema
from database.base import BaseSchema


# Category Schema
class CategoryBase(BaseSchema):
    name: str
    slug: str
    description: str


class CategoryRead(CategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime
