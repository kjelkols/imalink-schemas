# Changelog

All notable changes to imalink-schemas will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2025-12-01

### BREAKING CHANGES
- **Renamed field**: `import_session_id` → `input_channel_id` in PhotoCreateSchema
  - Better reflects the purpose: user-defined channels for organizing uploads
  - Backend refactored: ImportSession → InputChannel
  - API endpoint changed: `/api/v1/import-sessions` → `/api/v1/input-channels`
  - Default channel name: "Quick Add" → "Quick Channel"

### Migration Guide

**Backend (imalink):**
- Update all references from `import_session_id` to `input_channel_id`
- Update model field: `Photo.import_session_id` → `Photo.input_channel_id`
- Update API calls to `/api/v1/input-channels`
- Database: Fresh start recommended (drop and recreate with input_channels table)

**Clients (imalink-web, imalink-desktop, imalink-core):**
- Update PhotoCreateSchema usage to use `input_channel_id` field
- Update API calls from `/api/v1/import-sessions` to `/api/v1/input-channels`
- No other changes required - backward compatible field type (Optional[int])

## [2.1.0] - 2025-11-27

### Added
- Removed `user_id` field from PhotoCreateSchema for security
- Backend now sets user_id from JWT token (not from client request)

## [2.0.1] - 2025-11-27

### Added
- Added `_base64` suffix to preview fields for clarity
- `hotpreview_base64` and `coldpreview_base64` clearly indicate base64 encoding

## [2.0.0] - 2025-11-26

### BREAKING CHANGES
- Renamed PhotoEgg → PhotoCreateSchema
- Complete restructure of schema design

## [1.0.0] - 2025-11-20

### Added
- Initial release with PhotoEgg schema
