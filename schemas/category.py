# Datetime
from datetime import datetime

# BaseSchema
from database.base import BaseSchema


# Category Schema
class Category(BaseSchema):
    name: str
    slug: str


class CategoryRead(Category):
    id: int
    created_at: datetime
    updated_at: datetime
