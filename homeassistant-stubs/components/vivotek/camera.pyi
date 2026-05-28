from . import VivotekConfigEntry as VivotekConfigEntry
from .const import CONF_FRAMERATE as CONF_FRAMERATE, CONF_STREAM_PATH as CONF_STREAM_PATH, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from libpyvivotek.vivotek import VivotekCamera as VivotekCamera
from typing import Final

_LOGGER: Incomplete
DEFAULT_CAMERA_BRAND: str
DEFAULT_NAME: str
DEFAULT_EVENT_0_KEY: str
DEFAULT_FRAMERATE: int
DEFAULT_SECURITY_LEVEL: str
DEFAULT_STREAM_SOURCE: str
PLATFORM_SCHEMA: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: VivotekConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VivotekCam(Camera):
    _attr_brand = DEFAULT_CAMERA_BRAND
    _attr_supported_features: Incomplete
    _cam: Incomplete
    _attr_frame_interval: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _stream_source: Incomplete
    def __init__(self, cam_client: VivotekCamera, stream_source: str, unique_id: str, framerate: int, name: str) -> None: ...
    def camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def stream_source(self) -> str: ...
    _attr_motion_detection_enabled: Incomplete
    def disable_motion_detection(self) -> None: ...
    def enable_motion_detection(self) -> None: ...
    _attr_model: Incomplete
    _attr_available: Incomplete
    def update(self) -> None: ...
