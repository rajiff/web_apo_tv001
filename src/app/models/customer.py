"""Customer SQLAlchemy model definition for the database layer."""
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, declarative_base
import uuid
from datetime import datetime

# Base class for declarative setup
Base = declarative_base()


class Customer(Base):
    """Customer model representing customer records in the database."""

    __tablename__ = "customers"

    # Primary key - auto-generated UUID (using UUID.int as integer)
    id_column: Mapped[int] = Column(
        Integer, primary_key=True, default=lambda: uuid.uuid4().int
    )

    # Core customer information
    name: Mapped[str] = Column(String(255), nullable=False)
    email: Mapped[str] = Column(String(255), nullable=False, unique=True)
    phone: Mapped[str] = Column(String(50), nullable=False)

    # Audit trail - created at/by
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow)
    created_by: Mapped[int] = Column(Integer, nullable=False, default=1)

    # Audit trail - updated at/by
    updated_at: Mapped[datetime] = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    updated_by: Mapped[int] = Column(Integer, nullable=False, default=1)

    # Customer status
    is_active: Mapped[bool] = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}')>"
