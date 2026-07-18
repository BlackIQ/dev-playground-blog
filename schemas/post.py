# Datetime
from datetime import datetime

# BaseSchema
from database.base import BaseSchema


# Post Schema
class PostBase(BaseSchema):
    slug: str
    title: str
    content: str
    description: str
    category_id: int
    # tag_ids: list[int]


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime
    likes_count: int
    views_count: int
