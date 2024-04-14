from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import UUIDModel, TimestampModel


class ExampleModel(UUIDModel, TimestampModel):
    __tablename__ = "example_model"
    name: Mapped[String] = mapped_column(String(100), nullable=False)
    age: Mapped[Integer] = mapped_column(Integer, nullable=False)
    description: Mapped[String] = mapped_column(String(255), nullable=True)
