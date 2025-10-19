from sqlalchemy import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text
from settings import settings

# uber settings dann die env und die werte pasrsen

engine = create_async_engine(
    f"mariadb+aiomysql://" \
    "{settings.DATABASE_USER}:" \
    "{settings.DATABASE_PASSWORD}@" \
    "{settings.DATABASE_HOST}/" \
    "{settings.DATABASE_NAME}", 
    echo=True, 
    pool_pre_ping=True
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
