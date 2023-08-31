import datetime
from .const import DOMAIN as DOMAIN
from .entity import DoorBirdEntity as DoorBirdEntity
from .models import DoorBirdData as DoorBirdData
from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LAST_VISITOR_INTERVAL: Incomplete
_LAST_MOTION_INTERVAL: Incomplete
_LIVE_INTERVAL: Incomplete
_LOGGER: Incomplete
_TIMEOUT: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DoorBirdCamera(DoorBirdEntity, Camera):
    _url: Incomplete
    _stream_url: Incomplete
    _attr_translation_key: Incomplete
    _last_image: Incomplete
    _attr_supported_features: Incomplete
    _interval: Incomplete
    _last_update: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, door_bird_data: DoorBirdData, url: str, camera_id: str, translation_key: str, interval: datetime.timedelta, stream_url: str | None = ...) -> None: ...
    async def stream_source(self) -> str | None: ...
    async def async_camera_image(self, width: int | None = ..., height: int | None = ...) -> bytes | None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
