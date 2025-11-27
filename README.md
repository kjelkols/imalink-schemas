# imalink-schemas

Shared Pydantic schemas for the ImaLink ecosystem.

## Purpose

This package contains all data schemas (Pydantic models) shared between ImaLink modules:

- **imalink** - Backend API (Python/FastAPI)
- **imalink-core** - Image processing service (Python/FastAPI)
- **imalink-desktop** - Desktop application (Rust) - uses generated types
- **imalink-web** - Web application (TypeScript) - uses generated types

## Installation

### For Python projects (imalink, imalink-core)

```bash
# From GitHub
pip install git+https://github.com/kjelkols/imalink-schemas.git@v2.0.0

# Or with uv
uv add "imalink-schemas @ git+https://github.com/kjelkols/imalink-schemas.git@v2.0.0"

# For local development (editable)
pip install -e /path/to/imalink-schemas
```

### For Rust projects (imalink-desktop)

Generate Rust types from JSON Schema:

```bash
# Export schemas to JSON
python -m imalink_schemas.codegen.export_json_schema

# Generate Rust types with quicktype
quicktype schemas.json --lang rust -o src/schemas.rs
```

### For TypeScript projects (imalink-web)

Generate TypeScript types:

```bash
datamodel-code-generator \
  --input src/imalink_schemas \
  --input-file-type python \
  --output src/types/schemas.ts
```

## Usage

### Python

```python
from imalink_schemas import (
    PhotoCreateSchema,
    ImageFileCreateSchema,
    PhotoResponse,
    VisibilityLevel,
    SCHEMA_VERSION
)

# Create a photo schema
photo = PhotoCreateSchema(
    hothash="abc123...",
    hotpreview="base64...",
    width=4000,
    height=3000,
    image_file_list=[
        ImageFileCreateSchema(filename="IMG_001.jpg", file_size=1024000)
    ],
    visibility=VisibilityLevel.PRIVATE
)

# Validate and serialize
photo_json = photo.model_dump_json()
```

### Rust

```rust
use crate::schemas::{PhotoCreateSchema, ImageFileCreateSchema};

// Deserialize from imalink-core response
let photo: PhotoCreateSchema = serde_json::from_str(&json_string)?;

// Send to imalink backend
let response = client.post("https://api.example.com/photos/create")
    .json(&photo)
    .send()
    .await?;
```

### TypeScript

```typescript
import { PhotoCreateSchema, PhotoResponse } from '@/types/schemas';

const photo: PhotoCreateSchema = {
  hothash: "abc123...",
  hotpreview: "base64...",
  width: 4000,
  height: 3000,
  image_file_list: [
    { filename: "IMG_001.jpg", file_size: 1024000 }
  ],
  visibility: "private"
};

const response = await fetch('/api/v1/photos/create', {
  method: 'POST',
  body: JSON.stringify(photo)
});
```

## Schema Organization

- `photo.py` - Photo schemas (create, update, response)
- `image_file.py` - ImageFile schemas
- `author.py` - Author schemas
- `tag.py` - Tag schemas
- `import_session.py` - Import session schemas
- `photo_stack.py` - Photo stack schemas
- `timeline.py` - Timeline query and response schemas
- `user.py` - User schemas (without sensitive data)
- `enums.py` - Shared enums (VisibilityLevel, CategoryType, etc.)
- `base.py` - Base classes and common validators
- `errors.py` - Error response schemas

## Versioning

This package follows [Semantic Versioning](https://semver.org/):

- **Major (X.0.0)**: Breaking changes (field removed/renamed, type changed)
- **Minor (1.X.0)**: New optional fields, backward compatible
- **Patch (1.0.X)**: Bug fixes, documentation, validation tweaks

Check `SCHEMA_VERSION` constant to verify compatibility:

```python
from imalink_schemas import SCHEMA_VERSION
print(SCHEMA_VERSION)  # "2.0.0"
```

## Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
ruff check src/

# Format code
ruff format src/
```

## License

MIT
