from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.models.example import ExampleModel
from app.repositories.base import BaseRepository


class ExampleRepository(BaseRepository):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_all(self) -> list[ExampleModel]:
        statement = select(ExampleModel.uuid).order_by(ExampleModel.uuid)
        result = await self.session.execute(statement=statement)
        return result.scalars().all()
