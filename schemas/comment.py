# Datetime
from datetime import datetime

# BaseSchema
from database.base import BaseSchema


# Comment Schema
class CommentBase(BaseSchema):
    name: str
    content: str


class CommentRead(CommentBase):
    id: int
    created_at: datetime
    updated_at: datetime
