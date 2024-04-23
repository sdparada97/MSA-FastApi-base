from sqlmodel import Field

from app.models.base import TimestampModel, UUIDModel


class ExampleModel(UUIDModel, TimestampModel, table=True):
    __tablename__ = "example_model"
    name: str = Field(max_length=100, nullable=False)
    age: int = Field(nullable=False)
    description: str = Field(max_length=255, nullable=True)
