import asyncio
from . import OnkyoConfigEntry as OnkyoConfigEntry
from .const import DOMAIN as DOMAIN, InputSource as InputSource, ListeningMode as ListeningMode, OPTION_MAX_VOLUME as OPTION_MAX_VOLUME, OPTION_VOLUME_RESOLUTION as OPTION_VOLUME_RESOLUTION, PYEISCP_COMMANDS as PYEISCP_COMMANDS, VolumeResolution as VolumeResolution, ZONES as ZONES
from .receiver import Receiver as Receiver
from .services import DATA_MP_ENTITIES as DATA_MP_ENTITIES
from _typeshed import Incomplete
from enum import Enum as Enum
from functools import cache
from homeassistant.components.media_player import MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Literal

_LOGGER: Incomplete
SUPPORTED_FEATURES_BASE: Incomplete
SUPPORTED_FEATURES_VOLUME: Incomplete
PLAYABLE_SOURCES: Incomplete
ATTR_PRESET: str
ATTR_AUDIO_INFORMATION: str
ATTR_VIDEO_INFORMATION: str
ATTR_VIDEO_OUT: str
AUDIO_VIDEO_INFORMATION_UPDATE_WAIT_TIME: int
AUDIO_INFORMATION_MAPPING: Incomplete
VIDEO_INFORMATION_MAPPING: Incomplete
type LibValue = str | tuple[str, ...]

def _get_single_lib_value(value: LibValue) -> str: ...
def _get_lib_mapping[T: Enum](cmds: Any, cls: type[T]) -> dict[T, LibValue]: ...
@cache
def _input_source_lib_mappings(zone: str) -> dict[InputSource, LibValue]: ...
@cache
def _rev_input_source_lib_mappings(zone: str) -> dict[LibValue, InputSource]: ...
@cache
def _listening_mode_lib_mappings(zone: str) -> dict[ListeningMode, LibValue]: ...
@cache
def _rev_listening_mode_lib_mappings(zone: str) -> dict[LibValue, ListeningMode]: ...
async def async_setup_entry(hass: HomeAssistant, entry: OnkyoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OnkyoMediaPlayer(MediaPlayerEntity):
    _attr_should_poll: bool
    _supports_volume: bool
    _supports_sound_mode: bool
    _supports_audio_info: bool
    _supports_video_info: bool
    _query_timer: asyncio.TimerHandle | None
    _receiver: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _zone: Incomplete
    _volume_resolution: Incomplete
    _max_volume: Incomplete
    _options_sources: Incomplete
    _source_lib_mapping: Incomplete
    _rev_source_lib_mapping: Incomplete
    _source_mapping: Incomplete
    _rev_source_mapping: Incomplete
    _options_sound_modes: Incomplete
    _sound_mode_lib_mapping: Incomplete
    _rev_sound_mode_lib_mapping: Incomplete
    _sound_mode_mapping: Incomplete
    _rev_sound_mode_mapping: Incomplete
    _attr_source_list: Incomplete
    _attr_sound_mode_list: Incomplete
    _attr_supported_features: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, receiver: Receiver, zone: str, *, volume_resolution: VolumeResolution, max_volume: float, sources: dict[InputSource, str], sound_modes: dict[ListeningMode, str]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def _update_receiver(self, propname: str, value: Any) -> None: ...
    @callback
    def _query_receiver(self, propname: str) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    async def async_select_sound_mode(self, sound_mode: str) -> None: ...
    async def async_select_output(self, hdmi_output: str) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    @callback
    def backfill_state(self) -> None: ...
    _attr_state: Incomplete
    _attr_volume_level: Incomplete
    _attr_is_volume_muted: Incomplete
    @callback
    def process_update(self, update: tuple[str, str, Any]) -> None: ...
    _attr_source: Incomplete
    @callback
    def _parse_source(self, source_lib: LibValue) -> None: ...
    _attr_sound_mode: Incomplete
    @callback
    def _parse_sound_mode(self, mode_lib: LibValue) -> None: ...
    @callback
    def _parse_audio_information(self, audio_information: tuple[str] | Literal['N/A']) -> None: ...
    @callback
    def _parse_video_information(self, video_information: tuple[str] | Literal['N/A']) -> None: ...
    def _query_av_info_delayed(self) -> None: ...
