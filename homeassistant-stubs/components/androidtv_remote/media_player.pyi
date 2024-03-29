from .const import DOMAIN as DOMAIN
from .entity import AndroidTVRemoteBaseEntity as AndroidTVRemoteBaseEntity
from _typeshed import Incomplete
from androidtvremote2 import AndroidTVRemote as AndroidTVRemote
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AndroidTVRemoteMediaPlayerEntity(AndroidTVRemoteBaseEntity, MediaPlayerEntity):
    _attr_assumed_state: bool
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _channel_set_task: Incomplete
    def __init__(self, api: AndroidTVRemote, config_entry: ConfigEntry) -> None: ...
    _attr_app_id: Incomplete
    _attr_app_name: Incomplete
    def _update_current_app(self, current_app: str) -> None: ...
    _attr_volume_level: Incomplete
    _attr_is_volume_muted: Incomplete
    def _update_volume_info(self, volume_info: dict[str, str | bool]) -> None: ...
    def _current_app_updated(self, current_app: str) -> None: ...
    def _volume_info_updated(self, volume_info: dict[str, str | bool]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def state(self) -> MediaPlayerState: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_play_pause(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def _send_key_commands(self, key_codes: list[str], delay_secs: float = 0.1) -> None: ...
