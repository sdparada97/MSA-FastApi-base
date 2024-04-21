from typing import AsyncGenerator

import traceback
from loguru import logger
from app.database import AsyncSession, async_session
from fastapi import Depends, HTTPException


# DATABASE - SESSION DEPENDENCE
async def get_db() -> AsyncGenerator:
    async with async_session() as session:
        yield session


async def db_session(session: AsyncSession = Depends(get_db)):
    try:
        yield session
        await session.commit()
    except Exception as error:
        logger.critical(traceback.format_exc())
        await session.rollback()
        raise HTTPException(
            status_code=500, detail="Error al interactuar con la base de datos"
        )
    finally:
        await session.close()

