# Pydantic
from pydantic import BaseModel, ConfigDict

# SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Mixins
from database.mixins import TimestampMixin, SoftDeleteMixin


# Base Class: Model
class Base(TimestampMixin, SoftDeleteMixin, DeclarativeBase):
    pass


# Base Class: Schema
class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
