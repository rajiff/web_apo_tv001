from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncIterator
import os

# This is the base class for all models
class Base(DeclarativeBase):
    pass
