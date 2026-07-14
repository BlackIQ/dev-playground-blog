# SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# BaseModel
from database.base import Base


# Comment Model
class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )
    name: Mapped[str] = mapped_column(
        nullable=False
    )
    content: Mapped[str] = mapped_column(
        nullable=False
    )
    post_id: Mapped[int] = mapped_column(
        ForeignKey(
            column="posts.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    post: Mapped["Post"] = relationship(
        back_populates="comments"
    )
