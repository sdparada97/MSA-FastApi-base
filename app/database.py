from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from fastapi import Depends
from .settings import settings


DATABASE_URL = settings.DATABASE_URL

async_engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

Base = declarative_base()

async_session = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with async_session() as session:
        yield session


def db_session(session: AsyncSession = Depends(get_db)):
    try:
        yield session
    finally:
        session.close()
