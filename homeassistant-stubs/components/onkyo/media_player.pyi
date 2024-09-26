import asyncio
from .receiver import Receiver as Receiver, ReceiverInfo as ReceiverInfo
from _typeshed import Incomplete
from homeassistant.components.media_player import MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Literal

_LOGGER: Incomplete
DOMAIN: str
DATA_MP_ENTITIES: HassKey[list[dict[str, OnkyoMediaPlayer]]]
CONF_SOURCES: str
CONF_MAX_VOLUME: str
CONF_RECEIVER_MAX_VOLUME: str
DEFAULT_NAME: str
SUPPORTED_MAX_VOLUME: int
DEFAULT_RECEIVER_MAX_VOLUME: int
ZONES: Incomplete
SUPPORT_ONKYO_WO_VOLUME: Incomplete
SUPPORT_ONKYO: Incomplete
KNOWN_HOSTS: list[str]
DEFAULT_SOURCES: Incomplete
DEFAULT_PLAYABLE_SOURCES: Incomplete
PLATFORM_SCHEMA: Incomplete
ATTR_HDMI_OUTPUT: str
ATTR_PRESET: str
ATTR_AUDIO_INFORMATION: str
ATTR_VIDEO_INFORMATION: str
ATTR_VIDEO_OUT: str
AUDIO_VIDEO_INFORMATION_UPDATE_WAIT_TIME: int
AUDIO_INFORMATION_MAPPING: Incomplete
VIDEO_INFORMATION_MAPPING: Incomplete
ACCEPTED_VALUES: Incomplete
ONKYO_SELECT_OUTPUT_SCHEMA: Incomplete
SERVICE_SELECT_HDMI_OUTPUT: str

async def async_register_services(hass: HomeAssistant) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class OnkyoMediaPlayer(MediaPlayerEntity):
    _attr_should_poll: bool
    _supports_volume: bool
    _supports_audio_info: bool
    _supports_video_info: bool
    _query_timer: asyncio.TimerHandle | None
    _receiver: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _zone: Incomplete
    _source_mapping: Incomplete
    _reverse_mapping: Incomplete
    _max_volume: Incomplete
    _volume_resolution: Incomplete
    _attr_source_list: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, receiver: Receiver, sources: dict[str, str], zone: str, max_volume: int, volume_resolution: int) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    def _update_receiver(self, propname: str, value: Any) -> None: ...
    def _query_receiver(self, propname: str) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    async def async_select_output(self, hdmi_output: str) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    def backfill_state(self) -> None: ...
    _attr_state: Incomplete
    _attr_volume_level: Incomplete
    _attr_is_volume_muted: Incomplete
    def process_update(self, update: tuple[str, str, Any]) -> None: ...
    _attr_source: Incomplete
    def _parse_source(self, source_raw: str | int | tuple[str]) -> None: ...
    def _parse_audio_information(self, audio_information: tuple[str] | Literal['N/A']) -> None: ...
    def _parse_video_information(self, video_information: tuple[str] | Literal['N/A']) -> None: ...
    def _query_av_info_delayed(self) -> None: ...
