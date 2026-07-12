# SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

# BaseModel
from database.base import Base


# Comment Model
class CommentModel(Base):
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
