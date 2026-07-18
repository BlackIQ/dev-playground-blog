# SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# BaseModel
from database.base import Base


# Post Model
class Post(Base):
    __tablename__ = "posts"

    # Columns
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )
    slug: Mapped[str] = mapped_column(
        unique=True,
        index=True,
        nullable=False,
    )
    title: Mapped[str] = mapped_column(
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        nullable=False,
    )
    content: Mapped[str] = mapped_column(
        nullable=False,
    )
    likes_count: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
    )
    views_count: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
    )

    # Foreign Keys
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
    )

    # Relationships
    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="posts",
    )
    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="post",
    )
    tags: Mapped[list["Tag"]] = relationship(
        "Tag",
        secondary="posts_tags",
        back_populates="posts",
    )
