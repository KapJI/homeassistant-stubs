import asyncio
from . import OnkyoConfigEntry as OnkyoConfigEntry
from .const import DOMAIN as DOMAIN, InputSource as InputSource, LEGACY_HDMI_OUTPUT_MAPPING as LEGACY_HDMI_OUTPUT_MAPPING, LEGACY_REV_HDMI_OUTPUT_MAPPING as LEGACY_REV_HDMI_OUTPUT_MAPPING, ListeningMode as ListeningMode, OPTION_MAX_VOLUME as OPTION_MAX_VOLUME, OPTION_VOLUME_RESOLUTION as OPTION_VOLUME_RESOLUTION, VolumeResolution as VolumeResolution, ZONES as ZONES
from .receiver import ReceiverManager as ReceiverManager
from .services import DATA_MP_ENTITIES as DATA_MP_ENTITIES
from .util import get_meaning as get_meaning
from _typeshed import Incomplete
from aioonkyo import Status as Status, Zone, status
from homeassistant.components.media_player import MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

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

async def async_setup_entry(hass: HomeAssistant, entry: OnkyoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OnkyoMediaPlayer(MediaPlayerEntity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _supports_volume: bool
    _supports_sound_mode: bool | None
    _supports_audio_info: bool
    _supports_video_info: bool
    _query_task: asyncio.Task | None
    _manager: Incomplete
    _zone: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _volume_resolution: Incomplete
    _max_volume: Incomplete
    _source_mapping: Incomplete
    _rev_source_mapping: Incomplete
    _sound_mode_mapping: Incomplete
    _rev_sound_mode_mapping: Incomplete
    _hdmi_output_mapping: Incomplete
    _rev_hdmi_output_mapping: Incomplete
    _attr_source_list: Incomplete
    _attr_sound_mode_list: Incomplete
    _attr_supported_features: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, manager: ReceiverManager, zone: Zone, *, volume_resolution: VolumeResolution, max_volume: float, sources: dict[InputSource, str], sound_modes: dict[ListeningMode, str]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def backfill_state(self) -> None: ...
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
    _attr_state: Incomplete
    _attr_volume_level: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_source: Incomplete
    _attr_sound_mode: Incomplete
    def process_update(self, message: status.Known) -> None: ...
    def _query_av_info_delayed(self) -> None: ...
