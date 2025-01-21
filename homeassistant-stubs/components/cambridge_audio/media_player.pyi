from . import CambridgeAudioConfigEntry as CambridgeAudioConfigEntry, media_browser as media_browser
from .const import CAMBRIDGE_MEDIA_TYPE_AIRABLE as CAMBRIDGE_MEDIA_TYPE_AIRABLE, CAMBRIDGE_MEDIA_TYPE_INTERNET_RADIO as CAMBRIDGE_MEDIA_TYPE_INTERNET_RADIO, CAMBRIDGE_MEDIA_TYPE_PRESET as CAMBRIDGE_MEDIA_TYPE_PRESET, DOMAIN as DOMAIN
from .entity import CambridgeAudioEntity as CambridgeAudioEntity, command as command
from _typeshed import Incomplete
from aiostreammagic import StreamMagicClient as StreamMagicClient, TransportControl
from datetime import datetime
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, RepeatMode as RepeatMode
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

BASE_FEATURES: Incomplete
PREAMP_FEATURES: Incomplete
TRANSPORT_FEATURES: dict[TransportControl, MediaPlayerEntityFeature]
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: CambridgeAudioConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CambridgeAudioDevice(CambridgeAudioEntity, MediaPlayerEntity):
    _attr_name: Incomplete
    _attr_media_content_type: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, client: StreamMagicClient) -> None: ...
    @property
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    @property
    def state(self) -> MediaPlayerState: ...
    @property
    def source_list(self) -> list[str]: ...
    @property
    def source(self) -> str | None: ...
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
    def media_position_updated_at(self) -> datetime: ...
    @property
    def is_volume_muted(self) -> bool | None: ...
    @property
    def volume_level(self) -> float | None: ...
    @property
    def shuffle(self) -> bool: ...
    @property
    def repeat(self) -> RepeatMode | None: ...
    @command
    async def async_media_play_pause(self) -> None: ...
    @command
    async def async_media_pause(self) -> None: ...
    @command
    async def async_media_stop(self) -> None: ...
    @command
    async def async_media_play(self) -> None: ...
    @command
    async def async_media_next_track(self) -> None: ...
    @command
    async def async_media_previous_track(self) -> None: ...
    @command
    async def async_select_source(self, source: str) -> None: ...
    @command
    async def async_turn_on(self) -> None: ...
    @command
    async def async_turn_off(self) -> None: ...
    @command
    async def async_volume_up(self) -> None: ...
    @command
    async def async_volume_down(self) -> None: ...
    @command
    async def async_set_volume_level(self, volume: float) -> None: ...
    @command
    async def async_mute_volume(self, mute: bool) -> None: ...
    @command
    async def async_media_seek(self, position: float) -> None: ...
    @command
    async def async_set_shuffle(self, shuffle: bool) -> None: ...
    @command
    async def async_set_repeat(self, repeat: RepeatMode) -> None: ...
    @command
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
