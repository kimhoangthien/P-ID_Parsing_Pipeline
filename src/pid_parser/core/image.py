"""Image identity and dimensions shared across research modules."""

from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ImageMetadata(BaseModel):
    """Metadata only: constructing this object does not read an image from disk."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    image_id: str = Field(min_length=1, pattern=r"\S")
    source_path: Path
    width: int = Field(gt=0, strict=True)
    height: int = Field(gt=0, strict=True)
    metadata: dict[str, Any] = Field(default_factory=dict)
