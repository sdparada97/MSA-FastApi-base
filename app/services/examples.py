from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.example import ExampleOut
from app.repositories import example


class ExampleService:
    @staticmethod
    async def get_all_examples(session: AsyncSession) -> list[ExampleOut]:
        list_examples = await example.ExampleRepository(session).get_all()
        return [ExampleOut(uuid=uuid) for uuid in list_examples]
