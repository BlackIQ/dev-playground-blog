# SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

# BaseModel
from database.base import Base


# Category Model
class CategoryModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )
    name: Mapped[str] = mapped_column(
        nullable=False
    )
    slug: Mapped[str] = mapped_column(
        nullable=False
    )
