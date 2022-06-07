from . import EsphomeEntity as EsphomeEntity, EsphomeEnumMapper as EsphomeEnumMapper, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import MediaPlayerEntityState, MediaPlayerInfo, MediaPlayerState
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity
from homeassistant.components.media_player.browse_media import BrowseMedia as BrowseMedia, async_process_play_media_url as async_process_play_media_url
from homeassistant.components.media_player.const import MediaPlayerEntityFeature as MediaPlayerEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_IDLE as STATE_IDLE, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_STATES: EsphomeEnumMapper[MediaPlayerState, str]

class EsphomeMediaPlayer(EsphomeEntity[MediaPlayerInfo, MediaPlayerEntityState], MediaPlayerEntity):
    _attr_device_class: Incomplete
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def is_volume_muted(self) -> bool: ...
    @property
    def volume_level(self) -> Union[float, None]: ...
    @property
    def supported_features(self) -> int: ...
    async def async_play_media(self, media_type: str, media_id: str, **kwargs: Any) -> None: ...
    async def async_browse_media(self, media_content_type: Union[str, None] = ..., media_content_id: Union[str, None] = ...) -> BrowseMedia: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...