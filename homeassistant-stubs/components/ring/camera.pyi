from . import RingConfigEntry as RingConfigEntry
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import RingEntity as RingEntity, exception_wrap as exception_wrap
from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant.components import ffmpeg as ffmpeg
from homeassistant.components.camera import Camera as Camera
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_stream as async_aiohttp_proxy_stream
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ring_doorbell import RingDoorBell
from typing import Any

FORCE_REFRESH_INTERVAL: Incomplete
MOTION_DETECTION_CAPABILITY: str
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingCam(RingEntity[RingDoorBell], Camera):
    _attr_name: Incomplete
    _ffmpeg_manager: Incomplete
    _last_event: Incomplete
    _last_video_id: Incomplete
    _video_url: Incomplete
    _image: Incomplete
    _expires_at: Incomplete
    _attr_unique_id: Incomplete
    _attr_motion_detection_enabled: Incomplete
    def __init__(self, device: RingDoorBell, coordinator: RingDataCoordinator, ffmpeg_manager: ffmpeg.FFmpegManager) -> None: ...
    _device: Incomplete
    def _handle_coordinator_update(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> web.StreamResponse | None: ...
    async def async_update(self) -> None: ...
    async def _async_get_video(self) -> str | None: ...
    async def _async_set_motion_detection_enabled(self, new_state: bool) -> None: ...
    async def async_enable_motion_detection(self) -> None: ...
    async def async_disable_motion_detection(self) -> None: ...
