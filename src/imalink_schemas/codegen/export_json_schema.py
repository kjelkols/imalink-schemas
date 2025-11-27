"""Export schemas to JSON Schema format for code generation."""

import json
from pathlib import Path
from pydantic.json_schema import models_json_schema

from imalink_schemas.photo import PhotoCreateSchema, PhotoUpdateSchema, PhotoResponse
from imalink_schemas.image_file import ImageFileCreateSchema, ImageFileResponse


def export_json_schema(output_file: str = "schemas.json"):
    """Export all schemas to JSON Schema format.
    
    This can be used to generate types for Rust (quicktype) or TypeScript.
    
    Usage:
        python -m imalink_schemas.codegen.export_json_schema
    """
    
    # List all schemas to export
    schemas_to_export = [
        (PhotoCreateSchema, 'validation'),
        (PhotoUpdateSchema, 'validation'),
        (PhotoResponse, 'validation'),
        (ImageFileCreateSchema, 'validation'),
        (ImageFileResponse, 'validation'),
    ]
    
    # Generate JSON Schema
    _, top_level_schema = models_json_schema(
        schemas_to_export,
        title="ImaLink Schemas",
        description="Shared data schemas for ImaLink ecosystem"
    )
    
    # Write to file
    output_path = Path(output_file)
    with output_path.open('w') as f:
        json.dump(top_level_schema, f, indent=2)
    
    print(f"✅ Exported schemas to {output_path.absolute()}")
    print(f"📦 {len(schemas_to_export)} schemas exported")
    print("\nGenerate Rust types:")
    print(f"  quicktype {output_file} --lang rust -o schemas.rs")
    print("\nGenerate TypeScript types:")
    print(f"  quicktype {output_file} --lang typescript -o schemas.ts")


if __name__ == '__main__':
    export_json_schema()
