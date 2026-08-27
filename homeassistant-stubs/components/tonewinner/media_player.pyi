from . import TonewinnerConfigEntry as TonewinnerConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from tonewinner_rs232 import ReceiverState as ReceiverState
from typing import override

_LOGGER: Incomplete
INPUT_SOURCES: Incomplete
SOUND_MODES: dict[str, str]
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: TonewinnerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TonewinnerMediaPlayer(MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_should_poll: bool
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _entry: Incomplete
    _receiver: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_available: bool
    _attr_state: Incomplete
    _attr_volume_level: float
    _attr_is_volume_muted: bool
    _attr_source: Incomplete
    _attr_sound_mode: Incomplete
    _attr_source_list: Incomplete
    _attr_sound_mode_list: Incomplete
    def __init__(self, entry: TonewinnerConfigEntry) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _on_state_change(self, state: ReceiverState | None) -> None: ...
    @callback
    def _apply_state(self, state: ReceiverState) -> None: ...
    def _resolve_source(self, source_name: str, audio_source: str | None) -> str | None: ...
    @override
    async def async_turn_on(self) -> None: ...
    @override
    async def async_turn_off(self) -> None: ...
    @override
    async def async_set_volume_level(self, volume: float) -> None: ...
    @override
    async def async_volume_up(self) -> None: ...
    @override
    async def async_volume_down(self) -> None: ...
    @override
    async def async_mute_volume(self, mute: bool) -> None: ...
    @override
    async def async_select_source(self, source: str) -> None: ...
    @override
    async def async_select_sound_mode(self, sound_mode: str) -> None: ...
