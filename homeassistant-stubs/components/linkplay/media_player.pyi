from . import LinkPlayConfigEntry as LinkPlayConfigEntry, SHARED_DATA as SHARED_DATA
from .const import DOMAIN as DOMAIN
from .entity import LinkPlayBaseEntity as LinkPlayBaseEntity, exception_wrap as exception_wrap
from _typeshed import Incomplete
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, RepeatMode as RepeatMode, async_process_play_media_url as async_process_play_media_url
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from linkplay.bridge import LinkPlayBridge as LinkPlayBridge
from linkplay.consts import EqualizerMode, LoopMode, PlayingMode, PlayingStatus
from linkplay.controller import LinkPlayController as LinkPlayController
from typing import Any

_LOGGER: Incomplete
STATE_MAP: dict[PlayingStatus, MediaPlayerState]
SOURCE_MAP: dict[PlayingMode, str]
SOURCE_MAP_INV: dict[str, PlayingMode]
REPEAT_MAP: dict[LoopMode, RepeatMode]
REPEAT_MAP_INV: dict[RepeatMode, LoopMode]
EQUALIZER_MAP_INV: dict[str, EqualizerMode]
DEFAULT_FEATURES: MediaPlayerEntityFeature
SEEKABLE_FEATURES: MediaPlayerEntityFeature
SERVICE_PLAY_PRESET: str
ATTR_PRESET_NUMBER: str
SERVICE_PLAY_PRESET_SCHEMA: Incomplete
RETRY_POLL_MAXIMUM: int
SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: LinkPlayConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LinkPlayMediaPlayerEntity(LinkPlayBaseEntity, MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_media_content_type: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _retry_count: int
    _attr_source_list: Incomplete
    _attr_sound_mode_list: Incomplete
    def __init__(self, bridge: LinkPlayBridge) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_available: bool
    @exception_wrap
    async def async_update(self) -> None: ...
    @exception_wrap
    async def async_select_source(self, source: str) -> None: ...
    @exception_wrap
    async def async_select_sound_mode(self, sound_mode: str) -> None: ...
    @exception_wrap
    async def async_mute_volume(self, mute: bool) -> None: ...
    @exception_wrap
    async def async_set_volume_level(self, volume: float) -> None: ...
    @exception_wrap
    async def async_media_pause(self) -> None: ...
    @exception_wrap
    async def async_media_play(self) -> None: ...
    @exception_wrap
    async def async_media_stop(self) -> None: ...
    @exception_wrap
    async def async_media_next_track(self) -> None: ...
    @exception_wrap
    async def async_media_previous_track(self) -> None: ...
    @exception_wrap
    async def async_set_repeat(self, repeat: RepeatMode) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    @exception_wrap
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    @exception_wrap
    async def async_play_preset(self, preset_number: int) -> None: ...
    @exception_wrap
    async def async_media_seek(self, position: float) -> None: ...
    @exception_wrap
    async def async_join_players(self, group_members: list[str]) -> None: ...
    async def _get_linkplay_bridge(self, entity_id: str) -> LinkPlayBridge: ...
    @property
    def group_members(self) -> list[str]: ...
    @property
    def media_image_url(self) -> str | None: ...
    @exception_wrap
    async def async_unjoin_player(self) -> None: ...
    _attr_state: Incomplete
    _attr_volume_level: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_repeat: Incomplete
    _attr_shuffle: Incomplete
    _attr_sound_mode: Incomplete
    _attr_supported_features: Incomplete
    _attr_source: Incomplete
    _attr_media_position: Incomplete
    _attr_media_position_updated_at: Incomplete
    _attr_media_duration: Incomplete
    _attr_media_artist: Incomplete
    _attr_media_title: Incomplete
    _attr_media_album_name: Incomplete
    def _update_properties(self) -> None: ...
