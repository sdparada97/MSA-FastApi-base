from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.deps import db_session
from app.log_config import logger
from app.services.examples import ExampleService

router = APIRouter()


@router.get("/examples/", tags=["examples"])
async def get_all_examples(session: AsyncSession = Depends(db_session)):  # noqa: B008
    logger.info("Inicia endpoint de ejemplo con log")
    return await ExampleService.get_all_examples(session)
