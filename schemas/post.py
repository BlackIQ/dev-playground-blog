# Datetime
from datetime import datetime

# BaseSchema
from database.base import BaseSchema


# Post Schema
class Post(BaseSchema):
    title: str
    content: str
    description: str


class PostRead(Post):
    id: int
    created_at: datetime
    updated_at: datetime
    likes_count: int
    views_count: int
