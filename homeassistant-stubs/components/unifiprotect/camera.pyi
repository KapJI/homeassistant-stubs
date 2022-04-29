from .const import ATTR_BITRATE as ATTR_BITRATE, ATTR_CHANNEL_ID as ATTR_CHANNEL_ID, ATTR_FPS as ATTR_FPS, ATTR_HEIGHT as ATTR_HEIGHT, ATTR_WIDTH as ATTR_WIDTH, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from _typeshed import Incomplete
from collections.abc import Generator
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.api import ProtectApiClient as ProtectApiClient
from pyunifiprotect.data import Camera as UFPCamera
from pyunifiprotect.data.devices import CameraChannel as CameraChannel

_LOGGER: Incomplete

def get_camera_channels(protect: ProtectApiClient) -> Generator[tuple[UFPCamera, CameraChannel, bool], None, None]: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectCamera(ProtectDeviceEntity, Camera):
    device: UFPCamera
    channel: Incomplete
    _secure: Incomplete
    _disable_stream: Incomplete
    _last_image: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, data: ProtectData, camera: UFPCamera, channel: CameraChannel, is_default: bool, secure: bool, disable_stream: bool) -> None: ...
    _stream_source: Incomplete
    _attr_supported_features: Incomplete
    def _async_set_stream_source(self) -> None: ...
    _attr_motion_detection_enabled: Incomplete
    _attr_is_recording: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _async_update_device_from_protect(self) -> None: ...
    async def async_camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    async def stream_source(self) -> Union[str, None]: ...
