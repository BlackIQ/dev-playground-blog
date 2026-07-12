# SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

# BaseModel
from database.base import Base


# Tag Model
class TagModel(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )
    name: Mapped[str] = mapped_column(
        nullable=False
    )
    slug: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        index=True
    )
    description: Mapped[str] = mapped_column(
        nullable=False
    )
