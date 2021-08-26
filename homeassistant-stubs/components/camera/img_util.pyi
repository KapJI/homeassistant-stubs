from . import Image as Image
from turbojpeg import TurboJPEG
from typing import Any

SUPPORTED_SCALING_FACTORS: Any
_LOGGER: Any
JPEG_QUALITY: int

def find_supported_scaling_factor(current_width: int, current_height: int, target_width: int, target_height: int) -> Union[tuple[int, int], None]: ...
def scale_jpeg_camera_image(cam_image: Image, width: int, height: int) -> bytes: ...

class TurboJPEGSingleton:
    __instance: Any
    @staticmethod
    def instance() -> TurboJPEG: ...
    def __init__(self) -> None: ...
