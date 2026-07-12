# SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# BaseModel
from database.base import Base


# Post Model
class PostModel(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )
    slug: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        index=True
    )
    title: Mapped[str] = mapped_column(
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        nullable=False
    )
    content: Mapped[str] = mapped_column(
        nullable=False
    )
    likes_count: Mapped[int] = mapped_column(
        nullable=False,
        default=0
    )
    views_count: Mapped[int] = mapped_column(
        nullable=False,
        default=0
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )
    tags: Mapped[list["TagModel"]] = relationship(
        secondary="posts_tags",
        back_populates="posts"
    )
    category: Mapped["CategoryModel"] = relationship(
        back_populates="posts"
    )
    comments: Mapped[list["CommentModel"]] = relationship(
        back_populates="post"
    )
