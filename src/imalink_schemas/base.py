"""Base schemas and common utilities."""

from typing import Generic, TypeVar, Optional
from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """Base class for all ImaLink schemas."""
    
    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True,
        validate_assignment=True,
    )


T = TypeVar('T')


class PaginatedResponse(BaseModel, Generic[T]):
    """Standard paginated response wrapper."""
    
    items: list[T]
    total: int
    page: int
    page_size: int
    pages: Optional[int] = None
    
    model_config = ConfigDict(from_attributes=True)
