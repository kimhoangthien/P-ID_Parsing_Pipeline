from pathlib import Path

import pytest
from pydantic import ValidationError

from pid_parser.core.coordinates import BoundingBox, Point
from pid_parser.core.image import ImageMetadata
from pid_parser.core.transforms import ImageTransform


def test_image_metadata_and_independent_metadata_defaults():
    first = ImageMetadata(image_id="drawing-1", source_path="missing.png", width=640, height=480)
    second = ImageMetadata(image_id="drawing-2", source_path="other.png", width=1, height=1)
    assert first.source_path == Path("missing.png")
    first.metadata["page"] = 1
    assert second.metadata == {}


@pytest.mark.parametrize(
    "field,value",
    [
        ("width", 0),
        ("height", -1),
        ("width", 1.5),
        ("height", True),
        ("image_id", ""),
        ("image_id", "   "),
    ],
)
def test_invalid_metadata(field, value):
    values = dict(image_id="drawing", source_path="image.png", width=10, height=10)
    values[field] = value
    with pytest.raises(ValidationError):
        ImageMetadata(**values)


@pytest.mark.parametrize(
    "values",
    [
        (1, 0, 1, 3),
        (2, 0, 1, 3),
        (0, 3, 1, 2),
        (0, 0, 1, 0),
        (0, 0, float("inf"), 1),
        (float("nan"), 0, 1, 1),
    ],
)
def test_invalid_box(values):
    with pytest.raises(ValidationError):
        BoundingBox(**dict(zip(("x_min", "y_min", "x_max", "y_max"), values, strict=True)))


@pytest.mark.parametrize("value", [float("inf"), float("-inf"), float("nan")])
def test_point_must_be_finite(value):
    with pytest.raises(ValidationError):
        Point(x=value, y=0)


def test_negative_coordinates_are_allowed_without_implicit_clipping():
    assert Point(x=-1, y=-2).x == -1
    assert BoundingBox(x_min=-2, y_min=-1, x_max=5, y_max=4).x_min == -2


def test_identity_transform():
    point = Point(x=3, y=7)
    assert ImageTransform().to_processed(point) == point
    assert ImageTransform().to_original(point) == point


def test_crop_then_anisotropic_resize_and_inverse():
    transform = ImageTransform(scale_x=2, scale_y=0.5, offset_x=-20, offset_y=-10)
    original = Point(x=15, y=30)
    processed = transform.to_processed(original)
    assert processed == Point(x=10, y=5)
    assert transform.to_original(processed) == original
    box = BoundingBox(x_min=10, y_min=20, x_max=30, y_max=60)
    mapped = transform.box_to_processed(box)
    assert mapped == BoundingBox(x_min=0, y_min=0, x_max=40, y_max=20)
    assert transform.box_to_original(mapped) == box


@pytest.mark.parametrize(
    "field,value",
    [
        ("scale_x", 0),
        ("scale_y", -1),
        ("scale_x", float("inf")),
        ("offset_y", float("nan")),
    ],
)
def test_invalid_transform(field, value):
    with pytest.raises(ValidationError):
        ImageTransform(**{field: value})
