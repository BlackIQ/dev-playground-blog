# Datetime
from datetime import datetime

# BaseSchema
from database.base import BaseSchema


# Tag Schema
class TagBase(BaseSchema):
    name: str
    slug: str
    description: str


class TagRead(TagBase):
    id: int
    created_at: datetime
    updated_at: datetime
