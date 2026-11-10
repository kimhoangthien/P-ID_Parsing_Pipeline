"""Continuous pixel coordinates, origin top-left, x rightward, y downward."""

from typing import Self

from pydantic import BaseModel, ConfigDict, model_validator


class Point(BaseModel):
    """A finite location; negative coordinates can occur before clipping."""

    model_config = ConfigDict(frozen=True, extra="forbid", allow_inf_nan=False)

    x: float
    y: float


class BoundingBox(BaseModel):
    """Positive-area xyxy box with exclusive maximum edges.

    Boxes may extend outside an image. Bounds checks and clipping are caller-owned.
    A full-image box is (0, 0, width, height).
    """

    model_config = ConfigDict(frozen=True, extra="forbid", allow_inf_nan=False)

    x_min: float
    y_min: float
    x_max: float
    y_max: float

    @model_validator(mode="after")
    def validate_extent(self) -> Self:
        if self.x_max <= self.x_min or self.y_max <= self.y_min:
            raise ValueError("Bounding boxes must have positive width and height")
        return self
