import datetime as dt
from . import RussoundConfigEntry as RussoundConfigEntry
from .entity import RussoundBaseEntity as RussoundBaseEntity, command as command
from _typeshed import Incomplete
from aiorussound import Controller as Controller
from aiorussound.models import Source as Source
from aiorussound.rio import ZoneControlSurface as ZoneControlSurface
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: RussoundConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RussoundZoneDevice(RussoundBaseEntity, MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_media_content_type: Incomplete
    _attr_supported_features: Incomplete
    _zone_id: Incomplete
    _sources: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, controller: Controller, zone_id: int, sources: dict[int, Source]) -> None: ...
    @property
    def _zone(self) -> ZoneControlSurface: ...
    @property
    def _source(self) -> Source: ...
    @property
    def state(self) -> MediaPlayerState | None: ...
    @property
    def source(self) -> str: ...
    @property
    def source_list(self) -> list[str]: ...
    @property
    def media_title(self) -> str | None: ...
    @property
    def media_artist(self) -> str | None: ...
    @property
    def media_album_name(self) -> str | None: ...
    @property
    def media_image_url(self) -> str | None: ...
    @property
    def media_duration(self) -> int | None: ...
    @property
    def media_position(self) -> int | None: ...
    @property
    def media_position_updated_at(self) -> dt.datetime: ...
    @property
    def volume_level(self) -> float: ...
    @property
    def is_volume_muted(self) -> bool: ...
    @command
    async def async_turn_off(self) -> None: ...
    @command
    async def async_turn_on(self) -> None: ...
    @command
    async def async_set_volume_level(self, volume: float) -> None: ...
    @command
    async def async_select_source(self, source: str) -> None: ...
    @command
    async def async_volume_up(self) -> None: ...
    @command
    async def async_volume_down(self) -> None: ...
    @command
    async def async_mute_volume(self, mute: bool) -> None: ...
    @command
    async def async_media_seek(self, position: float) -> None: ...
