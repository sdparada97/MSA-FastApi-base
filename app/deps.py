import traceback
from typing import AsyncGenerator

from fastapi import Depends, HTTPException
from loguru import logger

from app.database import AsyncSession, async_session


# DATABASE - SESSION DEPENDENCE
async def get_db() -> AsyncGenerator:
    async with async_session() as session:
        yield session


async def db_session(session: AsyncSession = Depends(get_db)):  # noqa: B008
    try:
        yield session
        await session.commit()
    except Exception:
        logger.critical(traceback.format_exc())
        await session.rollback()
        raise HTTPException(status_code=500, detail="Error al interactuar con la base de datos")  # noqa: B904
    finally:
        await session.close()
