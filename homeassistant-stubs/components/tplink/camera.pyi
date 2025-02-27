from . import TPLinkConfigEntry as TPLinkConfigEntry
from .const import CONF_CAMERA_CREDENTIALS as CONF_CAMERA_CREDENTIALS
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkModuleEntity as CoordinatedTPLinkModuleEntity, TPLinkModuleEntityDescription as TPLinkModuleEntityDescription
from _typeshed import Incomplete
from aiohttp import web as web
from dataclasses import dataclass
from homeassistant.components import ffmpeg as ffmpeg, stream as stream
from homeassistant.components.camera import Camera as Camera, CameraEntityDescription as CameraEntityDescription, CameraEntityFeature as CameraEntityFeature
from homeassistant.config_entries import ConfigFlowContext as ConfigFlowContext
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_stream as async_aiohttp_proxy_stream
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from kasa import Device as Device

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TPLinkCameraEntityDescription(CameraEntityDescription, TPLinkModuleEntityDescription): ...

CAMERA_DESCRIPTIONS: tuple[TPLinkCameraEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TPLinkCameraEntity(CoordinatedTPLinkModuleEntity, Camera):
    IMAGE_INTERVAL: Incomplete
    _attr_supported_features: Incomplete
    entity_description: TPLinkCameraEntityDescription
    _ffmpeg_manager: ffmpeg.FFmpegManager
    _camera_module: Incomplete
    _camera_credentials: Incomplete
    _video_url: Incomplete
    _image: bytes | None
    _image_lock: Incomplete
    _last_update: float
    _can_stream: bool
    _http_mpeg_stream_running: bool
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkCameraEntityDescription, *, parent: Device | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...
    async def stream_source(self) -> str | None: ...
    async def _async_check_stream_auth(self, video_url: str) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> web.StreamResponse | None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
