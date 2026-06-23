"""Pydantic schemas for Customer API - Input/Output models."""
from typing import Optional
from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    """Schema for creating a new customer - fields we can control at application level."""

    name: str
    email: EmailStr
    phone: str


class CustomerUpdate(BaseModel):
    """Schema for updating a customer - partial updates allowed."""

    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None


class CustomerResponse(BaseModel):
    """Schema for customer response - full record with all fields."""

    id: int
    name: str
    email: EmailStr
    phone: str
    created_at: str
    updated_at: str
    is_active: bool
