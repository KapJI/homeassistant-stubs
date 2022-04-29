from . import Image as Image
from _typeshed import Incomplete
from turbojpeg import TurboJPEG

SUPPORTED_SCALING_FACTORS: Incomplete
_LOGGER: Incomplete
JPEG_QUALITY: int

def find_supported_scaling_factor(current_width: int, current_height: int, target_width: int, target_height: int) -> Union[tuple[int, int], None]: ...
def scale_jpeg_camera_image(cam_image: Image, width: int, height: int) -> bytes: ...

class TurboJPEGSingleton:
    __instance: Incomplete
    @staticmethod
    def instance() -> TurboJPEG: ...
    def __init__(self) -> None: ...
