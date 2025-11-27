"""ImageFile schemas for source file metadata."""

from typing import Optional, Any
from datetime import datetime
from pydantic import Field

from imalink_schemas.base import BaseSchema


class ImageFileCreateSchema(BaseSchema):
    """Schema for creating an ImageFile record.
    
    Represents metadata about a source image file (JPEG, RAW, etc.)
    that belongs to a Photo.
    """
    
    filename: str = Field(..., description="Original filename")
    file_size: int = Field(..., description="File size in bytes")
    imported_time: Optional[datetime] = Field(
        None, 
        description="When the file was imported"
    )
    imported_info: Optional[dict[str, Any]] = Field(
        None,
        description="Additional import metadata (source path, user, etc.)"
    )
    local_storage_info: Optional[dict[str, Any]] = Field(
        None,
        description="Local filesystem storage details"
    )
    cloud_storage_info: Optional[dict[str, Any]] = Field(
        None,
        description="Cloud storage details (S3, etc.)"
    )


class ImageFileResponse(BaseSchema):
    """Response schema for ImageFile."""
    
    id: int
    filename: str
    file_size: int
    photo_id: Optional[int] = None
    imported_time: Optional[datetime] = None
    imported_info: Optional[dict[str, Any]] = None
    local_storage_info: Optional[dict[str, Any]] = None
    cloud_storage_info: Optional[dict[str, Any]] = None
