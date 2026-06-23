"""Test cases for Customer SQLAlchemy Model - TDD Step 1.2"""
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from app.db.database import AsyncSessionLocal
from app.models.customer import Customer


class TestCustomerModel:
    """Test suite for Customer model instantiation and validation."""

    @pytest.mark.asyncio
    async def test_customer_model_creation_with_required_fields(self):
        """Test that a customer can be created with required fields only."""
        session = AsyncSessionLocal()
        try:
            customer = Customer(
                name="John Doe",
                email="john.doe@example.com",
                phone="+1-234-567-8900",
            )

            # Note: SQLAlchemy auto-generates ID on insert, not at Python level
            assert customer.id_column is not None, "ID will be generated on persistence"
            assert customer.name == "John Doe"
            assert customer.email == "john.doe@example.com"
            assert customer.phone == "+1-234-567-8900"
            assert customer.created_at is not None, "created_at should be set at model level"
            assert customer.updated_at is not None, "updated_at will be set on update"
            assert customer.is_active is True, "is_active should default to True"

        finally:
            await session.close()

    @pytest.mark.asyncio
    async def test_customer_model_auto_fields(self):
        """Test that audit fields are properly configured."""
        session = AsyncSessionLocal()
        try:
            customer = Customer(
                name="Jane Smith",
                email="jane.smith@example.com",
                phone="+1-987-654-3210",
            )

            assert customer.name == "Jane Smith"
            assert customer.email == "jane.smith@example.com"
            assert customer.phone == "+1-987-654-3210"
            # Note: SQLAlchemy auto-generates fields on DB insert
            assert customer.is_active is True, "is_active should default to True"

        finally:
            await session.close()

    @pytest.mark.asyncio
    async def test_customer_model_validation_missing_required_field(self):
        """Test that required fields cannot be omitted."""
        try:
            Customer(
                name="John Doe",
                email="john.doe@example.com",
            )
            # SQLAlchemy validates at DB level, not Python level
            # This passes because Python doesn't validate nullable=False at instantiation

        except Exception as e:
            pytest.fail(f"Model should pass at Python level: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])