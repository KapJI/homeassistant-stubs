from .const import CONF_FFMPEG_ARGUMENTS as CONF_FFMPEG_ARGUMENTS, DATA_COORDINATOR as DATA_COORDINATOR, DEFAULT_FFMPEG_ARGUMENTS as DEFAULT_FFMPEG_ARGUMENTS, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import CanaryDataUpdateCoordinator as CanaryDataUpdateCoordinator
from aiohttp.web import Request as Request, StreamResponse as StreamResponse
from canary.api import Device as Device, Location as Location
from canary.live_stream_api import LiveStreamSession as LiveStreamSession
from homeassistant.components.camera import Camera as Camera
from homeassistant.components.ffmpeg import DATA_FFMPEG as DATA_FFMPEG, FFmpegManager as FFmpegManager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_stream as async_aiohttp_proxy_stream
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import Throttle as Throttle
from typing import Any, Final

MIN_TIME_BETWEEN_SESSION_RENEW: Final[Any]
PLATFORM_SCHEMA: Final[Any]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CanaryCamera(CoordinatorEntity, Camera):
    coordinator: CanaryDataUpdateCoordinator
    _ffmpeg: Any
    _ffmpeg_arguments: Any
    _location_id: Any
    _device: Any
    _live_stream_session: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, hass: HomeAssistant, coordinator: CanaryDataUpdateCoordinator, location_id: str, device: Device, ffmpeg_args: str) -> None: ...
    @property
    def location(self) -> Location: ...
    @property
    def is_recording(self) -> bool: ...
    @property
    def motion_detection_enabled(self) -> bool: ...
    async def async_camera_image(self) -> Union[bytes, None]: ...
    async def handle_async_mjpeg_stream(self, request: Request) -> Union[StreamResponse, None]: ...
    def renew_live_stream_session(self) -> None: ...
