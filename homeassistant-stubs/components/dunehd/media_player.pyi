from . import DuneHDConfigEntry as DuneHDConfigEntry
from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pdunehd import DuneHDPlayer as DuneHDPlayer
from typing import Any, Final

CONF_SOURCES: Final[str]
DUNEHD_PLAYER_SUPPORT: Final[MediaPlayerEntityFeature]

async def async_setup_entry(hass: HomeAssistant, entry: DuneHDConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DuneHDPlayerEntity(MediaPlayerEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _player: Incomplete
    _media_title: str | None
    _state: dict[str, Any]
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, player: DuneHDPlayer, name: str, unique_id: str) -> None: ...
    def update(self) -> None: ...
    @property
    def state(self) -> MediaPlayerState: ...
    @property
    def available(self) -> bool: ...
    @property
    def volume_level(self) -> float: ...
    @property
    def is_volume_muted(self) -> bool: ...
    @property
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    def volume_up(self) -> None: ...
    def volume_down(self) -> None: ...
    def mute_volume(self, mute: bool) -> None: ...
    def turn_off(self) -> None: ...
    def turn_on(self) -> None: ...
    def media_play(self) -> None: ...
    def media_pause(self) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    @property
    def media_title(self) -> str | None: ...
    def __update_title(self) -> None: ...
    def media_previous_track(self) -> None: ...
    def media_next_track(self) -> None: ...
