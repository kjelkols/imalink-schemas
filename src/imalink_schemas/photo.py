"""Photo schemas - the core of ImaLink."""

from typing import Optional, Any
from datetime import datetime
from pydantic import Field

from imalink_schemas.base import BaseSchema
from imalink_schemas.enums import VisibilityLevel, CategoryType
from imalink_schemas.image_file import ImageFileCreateSchema


class PhotoCreateSchema(BaseSchema):
    """Schema for creating a Photo.
    
    Created by imalink-core from image file(s).
    Frontend adds user organization fields before sending to backend.
    
    Key principles:
    - hothash is unique identifier (SHA256 of hotpreview)
    - exif_dict contains ALL EXIF metadata (flexible JSON)
    - Only taken_at, gps_latitude, gps_longitude copied to root for DB indexing
    - image_file_list contains one or more source files (JPEG + RAW companions)
    """
    
    # Identity - created by imalink-core
    hothash: str = Field(..., description="SHA256 hash of hotpreview (unique ID)")
    hotpreview: str = Field(..., description="Base64 encoded JPEG preview (~200px)")
    
    # Complete EXIF metadata (readonly DNA)
    exif_dict: Optional[dict[str, Any]] = Field(
        None,
        description="Complete EXIF data (camera_make, iso, etc. - flexible schema)"
    )
    
    # Dimensions
    width: int = Field(..., description="Image width in pixels")
    height: int = Field(..., description="Image height in pixels")
    
    # Time & Location (indexed copies from exif_dict)
    taken_at: Optional[datetime] = Field(
        None,
        description="When photo was taken (for timeline queries)"
    )
    gps_latitude: Optional[float] = Field(
        None,
        description="GPS latitude (for map queries)"
    )
    gps_longitude: Optional[float] = Field(
        None,
        description="GPS longitude (for map queries)"
    )
    
    # User organization (set by frontend)
    user_id: int = Field(..., description="Owner user ID")
    rating: int = Field(default=0, ge=0, le=5, description="Star rating (0-5)")
    category: Optional[str] = Field(
        default=None,
        description="Category type (photo, screenshot, video, etc.)"
    )
    import_session_id: Optional[int] = Field(
        None,
        description="Import batch this photo belongs to"
    )
    author_id: Optional[int] = Field(
        None,
        description="Photographer/creator ID"
    )
    stack_id: Optional[int] = Field(
        None,
        description="Photo stack ID (for related images)"
    )
    
    # Corrections (user-editable overrides)
    timeloc_correction: Optional[dict[str, Any]] = Field(
        None,
        description="Time/location corrections (timezone fix, GPS override, etc.)"
    )
    view_correction: Optional[dict[str, Any]] = Field(
        None,
        description="Visual adjustments (rotation, crop hints for frontend)"
    )
    
    # Privacy
    visibility: str = Field(
        default="private",
        description="Visibility level (private/space/authenticated/public)"
    )
    
    # Optional larger preview
    coldpreview: Optional[str] = Field(
        None,
        description="Base64 encoded larger preview (~1000px) - optional"
    )
    coldpreview_path: Optional[str] = Field(
        None,
        description="Filesystem path to coldpreview if stored separately"
    )
    
    # Source files
    image_file_list: list[ImageFileCreateSchema] = Field(
        ...,
        description="One or more source image files (JPEG, RAW, etc.)"
    )


class PhotoUpdateSchema(BaseSchema):
    """Schema for updating a Photo's user-editable fields."""
    
    rating: Optional[int] = Field(None, ge=0, le=5)
    category: Optional[str] = None
    author_id: Optional[int] = None
    stack_id: Optional[int] = None
    timeloc_correction: Optional[dict[str, Any]] = None
    view_correction: Optional[dict[str, Any]] = None
    visibility: Optional[str] = None


class PhotoResponse(BaseSchema):
    """Response schema for Photo."""
    
    id: int
    user_id: int
    hothash: str
    
    # Note: hotpreview is binary BLOB, not included in JSON response
    # Use separate endpoint: GET /photos/{hothash}/hotpreview
    
    exif_dict: Optional[dict[str, Any]] = None
    width: int
    height: int
    
    taken_at: Optional[datetime] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    
    rating: int
    category: Optional[str] = None
    
    import_session_id: Optional[int] = None
    author_id: Optional[int] = None
    stack_id: Optional[int] = None
    coldpreview_path: Optional[str] = None
    
    timeloc_correction: Optional[dict[str, Any]] = None
    view_correction: Optional[dict[str, Any]] = None
    
    visibility: str
    
    # Relationships (optional, depending on query params)
    image_files: Optional[list] = None
    tags: Optional[list] = None
