# SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

# BaseModel
from database.base import Base


# Post-Tag Model
class PostTagModel(Base):
    __tablename__ = "posts_tags"

    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id"),
        primary_key=True,
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tags.id"),
        primary_key=True
    )
