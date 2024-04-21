from sqlalchemy import AsyncAdaptedQueuePool, NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from .settings import settings, ModeEnum


DATABASE_URL = settings.DATABASE_URL
DB_POOL_SIZE = 83
WEB_CONCURRENCY = 9
POOL_SIZE = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)

Base = declarative_base()

async_engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    poolclass=NullPool
    if settings.MODE == ModeEnum.testing
    else AsyncAdaptedQueuePool,  # Asincio pytest works with NullPool
    # pool_size=POOL_SIZE,
    # max_overflow=64,
)

async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
