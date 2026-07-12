# Datetime
from datetime import datetime

# BaseSchema
from database.base import BaseSchema


# Tag Schema
class Tag(BaseSchema):
    name: str
    slug: str


class TagRead(Tag):
    id: int
    created_at: datetime
    updated_at: datetime
