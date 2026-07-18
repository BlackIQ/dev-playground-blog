from datetime import datetime

from database.base import BaseSchema

from schemas.tag import TagRead
from schemas.category import CategoryRead
from schemas.comment import CommentRead


class PostBase(BaseSchema):
    slug: str
    title: str
    content: str
    description: str
    category_id: int


class PostCreate(PostBase):
    tag_ids: list[int]


class PostUpdate(PostBase):
    tag_ids: list[int]


class PostRead(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime
    likes_count: int
    views_count: int

    category: CategoryRead
    tags: list[TagRead]
    comments: list[CommentRead]
