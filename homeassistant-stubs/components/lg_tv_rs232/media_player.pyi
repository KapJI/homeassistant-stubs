from .const import DOMAIN as DOMAIN, LGTVRS232ConfigEntry as LGTVRS232ConfigEntry, QUERY_ATTRIBUTES as QUERY_ATTRIBUTES
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from lg_rs232_tv import InputSource, TVState as TVState
from typing import Any, override

SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int
INPUT_SOURCE_LG_TO_HA: dict[InputSource, str]
INPUT_SOURCE_HA_TO_LG: dict[str, InputSource]
_BASE_SUPPORTED_FEATURES: Incomplete

def catch_command_errors[**_P](func: Callable[_P, Coroutine[Any, Any, None]]) -> Callable[_P, Coroutine[Any, Any, None]]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: LGTVRS232ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LGTVRS232MediaPlayer(MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_source_list: Incomplete
    _tv: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry: LGTVRS232ConfigEntry) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    _attr_available: bool
    @callback
    def _async_on_state_update(self, state: TVState | None) -> None: ...
    _attr_state: Incomplete
    _attr_source: Incomplete
    _attr_volume_level: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_supported_features: Incomplete
    @callback
    def _async_update_from_state(self, state: TVState) -> None: ...
    @catch_command_errors
    @override
    async def async_turn_on(self) -> None: ...
    @catch_command_errors
    @override
    async def async_turn_off(self) -> None: ...
    @catch_command_errors
    @override
    async def async_set_volume_level(self, volume: float) -> None: ...
    @catch_command_errors
    @override
    async def async_mute_volume(self, mute: bool) -> None: ...
    @catch_command_errors
    @override
    async def async_select_source(self, source: str) -> None: ...
