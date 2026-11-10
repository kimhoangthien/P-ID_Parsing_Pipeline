# Data and integration contracts

Keep three distinct layers:

| Layer | Owner | Purpose |
| --- | --- | --- |
| Dataset schema | Each research module | Native annotations, provenance, splits and conversions |
| Internal schema | Each research module | Algorithm-specific requests, predictions and postprocessing |
| Integration contract | Collaboratively agreed | Stable artifacts used for association and graph construction |

There is no universal Prediction class. Text can have polygons and transcription;
lines can have polylines and junctions; symbols can have class labels and boxes.
None of these tentative structures is a committed schema yet.

## Shared conventions

`ImageMetadata.image_id` is a nonblank stable identifier for an original drawing;
its source path is provenance, not identity, and need not exist during validation.
Assign IDs at ingestion; all modules must reuse the same ID for the same drawing.
Width and height are positive integer pixel dimensions of that original image.
Optional metadata is caller-owned; nested values are not recursively frozen or
restricted to JSON types, so exporters must validate serialization themselves.

Coordinates use continuous pixels, origin top-left, x rightward, y downward.
Bounding boxes are `(x_min, y_min, x_max, y_max)` with exclusive maximum edges
and positive area. A whole-image box is `(0, 0, width, height)`. Points and boxes
must be finite. Geometry may be out of bounds before clipping; checking image
bounds and clipping are explicit caller responsibilities. No normalized coordinates
cross an adapter boundary without conversion.

`ImageTransform` maps original to processed with `p = original * scale + offset`,
independently per axis. For crop-then-resize, offset is minus the crop origin times
the scale. Padding adds to offset. Store the transform with module outputs, and
invert it in adapters. Multiple stages must be accounted for by the module;
composition, rotation and shear are future work.

## Adapter responsibilities (future)

Validate image identity, convert geometry to original-image coordinates, preserve
provenance, distinguish missing from empty results, and document units and any
confidence semantics. Do not invent confidence for artifacts that do not have it.
Negotiate versioning and detailed schemas when real integration needs emerge.

Illustrative conceptual outputs only, not models or actual predictions:

- Symbol artifact: image identity, equipment category, source-space region.
- Text artifact: image identity, source-space polygon, transcription.
- Line artifact: image identity, source-space polyline, junction references.

Do not serialize these examples as if a supported interchange format exists.
