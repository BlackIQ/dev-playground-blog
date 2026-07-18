# SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship

# BaseModel
from database.base import Base


# Tag Model
class Tag(Base):
    __tablename__ = "tags"

    # Columns
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )
    slug: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        nullable=False,
    )

    # Relationships
    posts: Mapped[list["Post"]] = relationship(
        "Post",
        secondary="posts_tags",
        back_populates="tags",
    )
