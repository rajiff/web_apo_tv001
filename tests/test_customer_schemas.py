"""Test cases for Customer Pydantic Schemas - TDD Step 2.1"""

import sys
sys.path.insert(0, '/Users/basavarajkn/py_devbox/web_apo_tv001/src')

import pytest
from datetime import datetime
from pydantic import ValidationError

from app.schemas.customer import CustomerCreate, CustomerUpdate, CustomerResponse


class TestCustomerSchemas:
    """Test suite for Customer schema validation."""

    def test_customer_create_schema_valid(self):
        """Test that valid customer creation data is accepted."""
        customer_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1-234-567-8900",
        }

        customer_create = CustomerCreate(**customer_data)

        assert customer_create.name == "John Doe"
        assert customer_create.email == "john.doe@example.com"
        assert customer_create.phone == "+1-234-567-8900"

    def test_customer_update_schema_valid(self):
        """Test that valid customer update data is accepted."""
        update_data = {
            "name": "John Smith Updated",
            "phone": "+1-999-888-7777",
        }

        customer_update = CustomerUpdate(**update_data)

        assert customer_update.name == "John Smith Updated"
        assert customer_update.phone == "+1-999-888-7777"
        assert customer_update.email is None, "email should be None (not provided)"

    def test_customer_response_schema_valid(self):
        """Test that valid customer response data is accepted."""
        response_data = {
            "id": 12345,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1-234-567-8900",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "is_active": True,
        }

        customer_response = CustomerResponse(**response_data)

        assert customer_response.id == 12345
        assert customer_response.name == "John Doe"
        assert customer_response.email == "john.doe@example.com"
        assert customer_response.phone == "+1-234-567-8900"
        assert customer_response.created_at is not None
        assert customer_response.updated_at is not None
        assert customer_response.is_active is True

    def test_customer_create_validation_invalid_email(self):
        """Test that invalid email format is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            CustomerCreate(
                name="John Doe",
                email="not-an-email",  # Invalid email format
                phone="+1-234-567-8900",
            )

        assert "value is not a valid email address" in str(exc_info.value).lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
