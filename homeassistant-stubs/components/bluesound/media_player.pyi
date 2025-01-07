from . import BluesoundConfigEntry as BluesoundConfigEntry
from .const import ATTR_BLUESOUND_GROUP as ATTR_BLUESOUND_GROUP, ATTR_MASTER as ATTR_MASTER, DOMAIN as DOMAIN, INTEGRATION_TITLE as INTEGRATION_TITLE
from .utils import dispatcher_join_signal as dispatcher_join_signal, dispatcher_unjoin_signal as dispatcher_unjoin_signal, format_unique_id as format_unique_id
from _typeshed import Incomplete
from asyncio import Task
from datetime import datetime
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_HOSTS as CONF_HOSTS, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from pyblu import Input as Input, Player as Player, Preset as Preset, Status as Status, SyncStatus as SyncStatus
from typing import Any

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
DATA_BLUESOUND = DOMAIN
DEFAULT_PORT: int
SERVICE_CLEAR_TIMER: str
SERVICE_JOIN: str
SERVICE_SET_TIMER: str
SERVICE_UNJOIN: str
NODE_OFFLINE_CHECK_TIMEOUT: int
NODE_RETRY_INITIATION: Incomplete
SYNC_STATUS_INTERVAL: Incomplete
POLL_TIMEOUT: int
PLATFORM_SCHEMA: Incomplete

async def _async_import(hass: HomeAssistant, config: ConfigType) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: BluesoundConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None) -> None: ...

class BluesoundPlayer(MediaPlayerEntity):
    _attr_media_content_type: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    host: Incomplete
    port: Incomplete
    _poll_status_loop_task: Task[None] | None
    _poll_sync_status_loop_task: Task[None] | None
    _id: Incomplete
    _last_status_update: datetime | None
    _sync_status: Incomplete
    _status: Status | None
    _inputs: list[Input]
    _presets: list[Preset]
    _group_name: str | None
    _group_list: list[str]
    _bluesound_device_name: Incomplete
    _player: Incomplete
    _is_leader: bool
    _leader: BluesoundPlayer | None
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, host: str, port: int, player: Player, sync_status: SyncStatus) -> None: ...
    async def _poll_status_loop(self) -> None: ...
    async def _poll_sync_status_loop(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    _attr_available: bool
    async def async_update_status(self) -> None: ...
    async def update_sync_status(self) -> None: ...
    async def async_update_captures(self) -> None: ...
    async def async_update_presets(self) -> None: ...
    @property
    def state(self) -> MediaPlayerState: ...
    @property
    def media_title(self) -> str | None: ...
    @property
    def media_artist(self) -> str | None: ...
    @property
    def media_album_name(self) -> str | None: ...
    @property
    def media_image_url(self) -> str | None: ...
    @property
    def media_position(self) -> int | None: ...
    @property
    def media_duration(self) -> int | None: ...
    @property
    def media_position_updated_at(self) -> datetime | None: ...
    @property
    def volume_level(self) -> float | None: ...
    @property
    def is_volume_muted(self) -> bool: ...
    @property
    def id(self) -> str | None: ...
    @property
    def bluesound_device_name(self) -> str | None: ...
    @property
    def sync_status(self) -> SyncStatus: ...
    @property
    def source_list(self) -> list[str] | None: ...
    @property
    def source(self) -> str | None: ...
    @property
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    @property
    def is_leader(self) -> bool: ...
    @property
    def is_grouped(self) -> bool: ...
    @property
    def shuffle(self) -> bool: ...
    async def async_join(self, master: str) -> None: ...
    async def async_unjoin(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    def rebuild_bluesound_group(self) -> list[str]: ...
    async def async_add_follower(self, host: str, port: int) -> None: ...
    async def async_remove_follower(self, host: str, port: int) -> None: ...
    async def async_increase_timer(self) -> int: ...
    async def async_clear_timer(self) -> None: ...
    async def async_set_shuffle(self, shuffle: bool) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    async def async_clear_playlist(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_media_seek(self, position: float) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
