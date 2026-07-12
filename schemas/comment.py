# Datetime
from datetime import datetime

# BaseSchema
from database.base import BaseSchema


# Comment Schema
class Comment(BaseSchema):
    name: str
    content: str


class CommentRead(Comment):
    id: int
    created_at: datetime
    updated_at: datetime
