from pid_parser.core.coordinates import Point
from pid_parser.core.image import ImageMetadata
from pid_parser.core.interfaces import InferenceModule
from pid_parser.core.transforms import ImageTransform


class ImageCenter:
    """Concrete metadata consumer to exercise the Protocol without an ML backend."""

    def infer(self, request: ImageMetadata, /) -> Point:
        return Point(x=request.width / 2, y=request.height / 2)


def test_metadata_service_and_coordinate_context():
    image = ImageMetadata(image_id="drawing", source_path="drawing.png", width=200, height=100)
    service: InferenceModule[ImageMetadata, Point] = ImageCenter()
    center = service.infer(image)
    transform = ImageTransform(scale_x=0.5, scale_y=0.5, offset_x=5, offset_y=10)
    assert transform.to_processed(center) == Point(x=55, y=35)
    assert transform.to_original(transform.to_processed(center)) == center
