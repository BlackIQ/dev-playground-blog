# Datetime
from datetime import datetime

# BaseSchema
from database.base import BaseSchema


# Tag Schema
class TagBase(BaseSchema):
    slug: str
    name: str
    description: str


class TagCreate(TagBase):
    pass


class TagRead(TagBase):
    id: int
    created_at: datetime
    updated_at: datetime
