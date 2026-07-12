# SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

# BaseModel
from database.base import Base


# Post Model
class PostModel(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
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
