from pydantic import UUID4, BaseModel, Field


class ExampleBase(BaseModel):
    name: str = Field(max_length=100, nullable=False)
    age: int = Field(nullable=False)
    description: str = Field(max_length=255, nullable=True)


class ExampleOut(BaseModel):
    uuid: UUID4
