"""Tests for photo schemas."""

import pytest
from datetime import datetime

from imalink_schemas import PhotoCreateSchema, ImageFileCreateSchema, VisibilityLevel


def test_photo_create_schema_minimal():
    """Test creating a minimal PhotoCreateSchema."""
    
    photo = PhotoCreateSchema(
        hothash="a" * 64,
        hotpreview_base64="base64encodedimage",
        width=4000,
        height=3000,
        user_id=1,
        image_file_list=[
            ImageFileCreateSchema(
                filename="IMG_001.jpg",
                file_size=1024000
            )
        ]
    )
    
    assert photo.hothash == "a" * 64
    assert photo.width == 4000
    assert photo.rating == 0
    assert photo.visibility == "private"
    assert len(photo.image_file_list) == 1


def test_photo_create_schema_full():
    """Test creating a complete PhotoCreateSchema."""
    
    photo = PhotoCreateSchema(
        hothash="b" * 64,
        hotpreview_base64="base64encodedimage",
        exif_dict={
            "camera_make": "Canon",
            "camera_model": "EOS R5",
            "iso": 400,
            "aperture": 2.8,
        },
        width=8192,
        height=5464,
        taken_at=datetime(2024, 11, 27, 12, 30, 0),
        gps_latitude=59.9139,
        gps_longitude=10.7522,
        user_id=1,
        rating=4,
        category="photo",
        visibility="public",
        image_file_list=[
            ImageFileCreateSchema(filename="IMG_001.CR3", file_size=30000000),
            ImageFileCreateSchema(filename="IMG_001.jpg", file_size=5000000),
        ]
    )
    
    assert photo.rating == 4
    assert photo.visibility == "public"
    assert photo.exif_dict["camera_make"] == "Canon"
    assert len(photo.image_file_list) == 2


def test_photo_create_schema_validation():
    """Test that invalid data raises validation errors."""
    
    with pytest.raises(ValueError):
        PhotoCreateSchema(
            hothash="tooshort",
            hotpreview="base64",
            width=100,
            height=100,
            user_id=1,
            rating=10,  # Invalid: must be 0-5
            image_file_list=[]
        )


def test_image_file_create_schema():
    """Test ImageFileCreateSchema."""
    
    image_file = ImageFileCreateSchema(
        filename="test.jpg",
        file_size=1024,
        imported_info={"source": "/photos/test.jpg"}
    )
    
    assert image_file.filename == "test.jpg"
    assert image_file.file_size == 1024
    assert image_file.imported_info["source"] == "/photos/test.jpg"


def test_schema_serialization():
    """Test that schemas can be serialized to JSON."""
    
    photo = PhotoCreateSchema(
        hothash="c" * 64,
        hotpreview_base64="base64",
        width=100,
        height=100,
        user_id=1,
        image_file_list=[
            ImageFileCreateSchema(filename="test.jpg", file_size=1024)
        ]
    )
    
    json_data = photo.model_dump_json()
    assert isinstance(json_data, str)
    assert "hothash" in json_data
    
    # Deserialize back
    photo2 = PhotoCreateSchema.model_validate_json(json_data)
    assert photo2.hothash == photo.hothash
