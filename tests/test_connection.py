import pytest
import asyncio
import os
# from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
# from sqlalchemy.pool import QueuePool
from sqlalchemy.sql import text

# Simulate the app environment
os.environ["DATABASE_URL"] = "postgresql+asyncpg://fs_dev_admin:dev%40123@localhost:5432/fs_dev_db"
os.environ["DB_POOL_SIZE"] = "10"
os.environ["DB_MAX_OVERFLOW"] = "20"
os.environ["SQL_ECHO"] = "false"

# from src.app.db.database import engine, AsyncSessionLocal
from src.app.db.database import AsyncSessionLocal

@pytest.mark.asyncio
async def test_verify():
    print("Checking DB Connection...")
    try:
        async with AsyncSessionLocal() as session:
            result = await session.execute(text("SELECT 1"))
            await result.fetchall()
            print("Successfully connected to the database!")
    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == "__main__":
    asyncio.run(test_verify())
