import os
from typing import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.sql import text
from contextlib import asynccontextmanager

# Environment Configuration
raw_url = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/dbname")

# Ensure the connection string uses the correct dialect for SQLAlchemy Async
if raw_url.startswith("postgresql://"):
    DATABASE_URL = raw_url.replace("postgresql://", "postgresql+asyncpg://", 1)
else:
    DATABASE_URL = raw_url

# We use a QueuePool for production-grade connection management
engine = create_async_engine(
    DATABASE_URL,
    pool_size=int(os.getenv("DB_POOL_SIZE", 10)),  # Minimum connections in pool
    max_overflow=int(os.getenv("DB_MAX_OVERFLOW", 20)),  # Extra connections allowed beyond pool size
    echo=os.getenv("SQL_ECHO", "false").lower() == "true",  # Set to False in production
)

# Session Factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)

# Dependency for FastAPI - ensures the session is closed after each request
async def get_db() -> AsyncIterator[AsyncSession]:
    async with AsyncSessionLocal() as session:
        yield session

# Helper to check connection health
async def check_connection() -> bool:
    try:
        async with AsyncSessionLocal() as session:
            await session.exec(text("SELECT 1"))
            return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False
