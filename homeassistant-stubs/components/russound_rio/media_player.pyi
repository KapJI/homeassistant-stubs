import datetime as dt
from . import RussoundConfigEntry as RussoundConfigEntry, media_browser as media_browser
from .const import DOMAIN as DOMAIN, RUSSOUND_MEDIA_TYPE_PRESET as RUSSOUND_MEDIA_TYPE_PRESET, SELECT_SOURCE_DELAY as SELECT_SOURCE_DELAY
from .entity import RussoundBaseEntity as RussoundBaseEntity, command as command
from _typeshed import Incomplete
from aiorussound.rio import Controller as Controller, Source as Source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: RussoundConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _parse_preset_source_id(media_id: str) -> tuple[int | None, int]: ...

class RussoundZoneDevice(RussoundBaseEntity, MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_media_content_type: Incomplete
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _sources: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, controller: Controller, zone_id: int, sources: dict[int, Source]) -> None: ...
    @property
    def _source(self) -> Source: ...
    @property
    @override
    def state(self) -> MediaPlayerState | None: ...
    @property
    @override
    def source(self) -> str: ...
    @property
    @override
    def source_list(self) -> list[str]: ...
    @property
    @override
    def media_title(self) -> str | None: ...
    @property
    @override
    def media_artist(self) -> str | None: ...
    @property
    @override
    def media_album_name(self) -> str | None: ...
    @property
    @override
    def media_image_url(self) -> str | None: ...
    @property
    @override
    def media_duration(self) -> int | None: ...
    @property
    @override
    def media_position(self) -> int | None: ...
    @property
    @override
    def media_position_updated_at(self) -> dt.datetime: ...
    @property
    @override
    def volume_level(self) -> float: ...
    @property
    @override
    def is_volume_muted(self) -> bool: ...
    @command
    @override
    async def async_turn_off(self) -> None: ...
    @command
    @override
    async def async_turn_on(self) -> None: ...
    @command
    @override
    async def async_set_volume_level(self, volume: float) -> None: ...
    @command
    @override
    async def async_select_source(self, source: str) -> None: ...
    @command
    @override
    async def async_volume_up(self) -> None: ...
    @command
    @override
    async def async_volume_down(self) -> None: ...
    @command
    @override
    async def async_mute_volume(self, mute: bool) -> None: ...
    @command
    @override
    async def async_media_seek(self, position: float) -> None: ...
    @command
    @override
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    @override
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
