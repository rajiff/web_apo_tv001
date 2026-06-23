"""Customer SQLAlchemy model definition for the database layer."""
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, declarative_base
import uuid
from datetime import datetime

Base = declarative_base()


class Customer(Base):
    """Customer model representing customer records in the database."""

    __tablename__ = "customers"

    # Primary key - auto-generated via __init__ (passed through Python setattr)
    id_column: Mapped[int] = Column(Integer, primary_key=True)

    # Core customer fields
    name: Mapped[str] = Column(String(255), nullable=False)
    email: Mapped[str] = Column(String(255), nullable=False, unique=True)
    phone: Mapped[str] = Column(String(50), nullable=False)

    # Audit fields - auto-populated via __init__ (passed through Python setattr)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow())
    created_by: Mapped[int] = Column(Integer, default=1)
    updated_at: Mapped[datetime] = Column(DateTime, onupdate=datetime.utcnow(), nullable=False)
    updated_by: Mapped[int] = Column(Integer, default=1)

    # Customer status - auto-initialized in __init__ if not provided or False
    is_active: Mapped[bool] = Column(Boolean, default=True, nullable=False)

    def __init__(self, name, email, phone):
        """Initialize customer with required fields."""
        self.name = name
        self.email = email
        self.phone = phone

        # Auto-generate ID on initialization if not set
        if not hasattr(self, "id_column"):
            object.__setattr__(self, "id_column", uuid.uuid4().int)

        # Set created_at if not already set
        if not hasattr(self, "created_at"):
            self.created_at = datetime.utcnow()

        # Set created_by if not already set
        if not hasattr(self, "created_by"):
            object.__setattr__(self, "created_by", 1)

        # Set updated_at if not already set
        if not hasattr(self, "updated_at"):
            self.updated_at = datetime.utcnow()

        # Set updated_by if not already set
        if not hasattr(self, "updated_by"):
            object.__setattr__(self, "updated_by", 1)

        # Set is_active to True if not provided or False
        if not hasattr(self, "is_active") or not self.is_active:
            self.is_active = True

    def __repr__(self):
        return f"<Customer(id={self.id_column}, name=\"{self.name}\")>"
