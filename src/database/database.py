from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from src.database.base import Base

from typing import AsyncGenerator
from dotenv import load_dotenv
load_dotenv()
import os


DB_URL = f"postgresql+asyncpg://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWD')}@localhost/{os.getenv('DB_NAME')}"
engine = create_async_engine(DB_URL, echo=False)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Use connection
async def async_main():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
