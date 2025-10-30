from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature
from homeassistant.const import CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, HTTP_BASIC_AUTHENTICATION as HTTP_BASIC_AUTHENTICATION, HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from libpyvivotek import VivotekCamera

CONF_FRAMERATE: str
CONF_SECURITY_LEVEL: str
CONF_STREAM_PATH: str
DEFAULT_CAMERA_BRAND: str
DEFAULT_NAME: str
DEFAULT_EVENT_0_KEY: str
DEFAULT_SECURITY_LEVEL: str
DEFAULT_STREAM_SOURCE: str
PLATFORM_SCHEMA: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class VivotekCam(Camera):
    _attr_brand = DEFAULT_CAMERA_BRAND
    _attr_supported_features: Incomplete
    _cam: Incomplete
    _attr_frame_interval: Incomplete
    _attr_name: Incomplete
    _stream_source: Incomplete
    def __init__(self, config: ConfigType, cam: VivotekCamera, stream_source: str) -> None: ...
    def camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def stream_source(self) -> str: ...
    _attr_motion_detection_enabled: Incomplete
    def disable_motion_detection(self) -> None: ...
    def enable_motion_detection(self) -> None: ...
    _attr_model: Incomplete
    def update(self) -> None: ...
