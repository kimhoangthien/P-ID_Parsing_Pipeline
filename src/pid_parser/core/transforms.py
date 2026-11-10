"""Invertible axis-aligned resize/crop bookkeeping, without image processing."""

from pydantic import BaseModel, ConfigDict, Field

from pid_parser.core.coordinates import BoundingBox, Point


class ImageTransform(BaseModel):
    """Map original to processed coordinates: processed = original * scale + offset.

    For a crop at (left, top) followed by resize, offsets are
    (-left * scale_x, -top * scale_y). Padding adds to these offsets.
    Rotation/shear require a future affine representation; they are not supported here.
    """

    model_config = ConfigDict(frozen=True, extra="forbid", allow_inf_nan=False)

    scale_x: float = Field(default=1.0, gt=0)
    scale_y: float = Field(default=1.0, gt=0)
    offset_x: float = 0.0
    offset_y: float = 0.0

    def to_processed(self, point: Point) -> Point:
        return Point(
            x=point.x * self.scale_x + self.offset_x,
            y=point.y * self.scale_y + self.offset_y,
        )

    def to_original(self, point: Point) -> Point:
        return Point(
            x=(point.x - self.offset_x) / self.scale_x,
            y=(point.y - self.offset_y) / self.scale_y,
        )

    def box_to_processed(self, box: BoundingBox) -> BoundingBox:
        lower = self.to_processed(Point(x=box.x_min, y=box.y_min))
        upper = self.to_processed(Point(x=box.x_max, y=box.y_max))
        return BoundingBox(x_min=lower.x, y_min=lower.y, x_max=upper.x, y_max=upper.y)

    def box_to_original(self, box: BoundingBox) -> BoundingBox:
        lower = self.to_original(Point(x=box.x_min, y=box.y_min))
        upper = self.to_original(Point(x=box.x_max, y=box.y_max))
        return BoundingBox(x_min=lower.x, y_min=lower.y, x_max=upper.x, y_max=upper.y)
