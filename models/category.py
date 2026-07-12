# SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship

# BaseModel
from database.base import Base


# Category Model
class CategoryModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )
    slug: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        index=True
    )
    name: Mapped[str] = mapped_column(
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        nullable=False
    )
    posts: Mapped[list["PostModel"]] = relationship(
        back_populates="category"
    )
