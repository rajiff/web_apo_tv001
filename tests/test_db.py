import pytest
# from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from src.app.db.database import get_db, engine, DATABASE_URL
# from typing import AsyncIterator
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# @TODO currently had to run this test case with the env var, we need to fix it
#  DATABASE_URL="postgresql+asyncpg://fs_dev_admin:dev%40123@localhost:5432/fs_dev_db" python -m pytest tests/test_db.py

# Note: This test requires a running PostgreSQL instance
# to successfully establish a connection.
@pytest.mark.asyncio
async def test_engine_creation():
    """Verify that the engine is created with the correct URL."""
    print(DATABASE_URL)
    assert "postgresql+asyncpg" in DATABASE_URL

@pytest.mark.asyncio
async def test_get_db_yields_session():
    """Verify that get_db yields an AsyncSession."""
    generator = get_db()
    session = await anext(generator)
    assert isinstance(session, AsyncSession)

@pytest.mark.asyncio
async def test_database_connection():
    """Verifies if the database is reachable.
    Note: This will fail without a real DB, but we want to see it run.
    """
    # This verifies that the engine exists and doesn't error out on construction.
    assert engine is not None

@pytest.mark.asyncio
async def test_db_connection():
    """Verifies if the database is reachable by executing a simple query."""
    # This verifies that the engine exists and doesn't error out on construction.
    assert engine is not None
    
    # We use the engine to connect and execute a dummy query
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        # If we reach this line, the connection was successful
        assert result.scalar() == 1
    
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT NOW()"))
        current_date_time = result.scalar()
        assert current_date_time is not None