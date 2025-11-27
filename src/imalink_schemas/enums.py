"""Shared enums used across ImaLink schemas."""

from enum import Enum


class VisibilityLevel(str, Enum):
    """Photo visibility levels."""
    PRIVATE = "private"
    SPACE = "space"
    AUTHENTICATED = "authenticated"
    PUBLIC = "public"


class CategoryType(str, Enum):
    """Photo category types."""
    PHOTO = "photo"
    SCREENSHOT = "screenshot"
    VIDEO = "video"
    COLLAGE = "collage"
    STORY = "story"
