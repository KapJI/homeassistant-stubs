from .const import DATA_NEST as DATA_NEST, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow

_LOGGER: Incomplete
NEST_BRAND: str

async def async_setup_legacy_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NestCamera(Camera):
    _attr_should_poll: bool
    _attr_supported_features: Incomplete
    structure: Incomplete
    device: Incomplete
    _location: Incomplete
    _name: Incomplete
    _online: Incomplete
    _is_streaming: Incomplete
    _is_video_history_enabled: bool
    _time_between_snapshots: Incomplete
    _last_image: Incomplete
    _next_snapshot_at: Incomplete
    def __init__(self, structure, device) -> None: ...
    @property
    def name(self): ...
    @property
    def unique_id(self): ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def is_recording(self): ...
    @property
    def brand(self): ...
    @property
    def is_on(self): ...
    def turn_off(self) -> None: ...
    def turn_on(self) -> None: ...
    def update(self) -> None: ...
    def _ready_for_snapshot(self, now): ...
    def camera_image(self, width: int | None = ..., height: int | None = ...) -> bytes | None: ...
