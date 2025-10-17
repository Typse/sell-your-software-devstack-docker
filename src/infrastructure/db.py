from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import text
from .settings import settings

# engine und SessionMaker erstellen
engine = create_async_engine(
    settings.database_url,
    echo=True,
    pool_pre_ping=True
)

# async session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()

# FastAPI
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session