"""
ImaLink Schemas - Shared Pydantic models for the ImaLink ecosystem.

This package contains all data transfer schemas used by:
- imalink (backend API)
- imalink-core (image processing service)
- imalink-desktop (Rust client - uses generated types)
- imalink-web (TypeScript client - uses generated types)
"""

from imalink_schemas.version import SCHEMA_VERSION
from imalink_schemas.enums import VisibilityLevel, CategoryType
from imalink_schemas.photo import PhotoCreateSchema, PhotoUpdateSchema, PhotoResponse
from imalink_schemas.image_file import ImageFileCreateSchema, ImageFileResponse
from imalink_schemas.base import PaginatedResponse

__version__ = SCHEMA_VERSION

__all__ = [
    # Version
    "SCHEMA_VERSION",
    "__version__",
    
    # Enums
    "VisibilityLevel",
    "CategoryType",
    
    # Photo schemas
    "PhotoCreateSchema",
    "PhotoUpdateSchema",
    "PhotoResponse",
    
    # ImageFile schemas
    "ImageFileCreateSchema",
    "ImageFileResponse",
    
    # Common
    "PaginatedResponse",
]
