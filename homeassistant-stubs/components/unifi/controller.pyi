import aiounifi
from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, CONF_ALLOW_BANDWIDTH_SENSORS as CONF_ALLOW_BANDWIDTH_SENSORS, CONF_ALLOW_UPTIME_SENSORS as CONF_ALLOW_UPTIME_SENSORS, CONF_BLOCK_CLIENT as CONF_BLOCK_CLIENT, CONF_CLIENT_SOURCE as CONF_CLIENT_SOURCE, CONF_DETECTION_TIME as CONF_DETECTION_TIME, CONF_DPI_RESTRICTIONS as CONF_DPI_RESTRICTIONS, CONF_IGNORE_WIRED_BUG as CONF_IGNORE_WIRED_BUG, CONF_SITE_ID as CONF_SITE_ID, CONF_SSID_FILTER as CONF_SSID_FILTER, CONF_TRACK_CLIENTS as CONF_TRACK_CLIENTS, CONF_TRACK_DEVICES as CONF_TRACK_DEVICES, CONF_TRACK_WIRED_CLIENTS as CONF_TRACK_WIRED_CLIENTS, DEFAULT_ALLOW_BANDWIDTH_SENSORS as DEFAULT_ALLOW_BANDWIDTH_SENSORS, DEFAULT_ALLOW_UPTIME_SENSORS as DEFAULT_ALLOW_UPTIME_SENSORS, DEFAULT_DETECTION_TIME as DEFAULT_DETECTION_TIME, DEFAULT_DPI_RESTRICTIONS as DEFAULT_DPI_RESTRICTIONS, DEFAULT_IGNORE_WIRED_BUG as DEFAULT_IGNORE_WIRED_BUG, DEFAULT_TRACK_CLIENTS as DEFAULT_TRACK_CLIENTS, DEFAULT_TRACK_DEVICES as DEFAULT_TRACK_DEVICES, DEFAULT_TRACK_WIRED_CLIENTS as DEFAULT_TRACK_WIRED_CLIENTS, LOGGER as LOGGER, PLATFORMS as PLATFORMS, UNIFI_WIRELESS_CLIENTS as UNIFI_WIRELESS_CLIENTS
from .entity import UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry, DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.entity_registry import async_entries_for_config_entry as async_entries_for_config_entry
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_time_interval as async_track_time_interval
from types import MappingProxyType
from typing import Any

RETRY_TIMER: int
CHECK_HEARTBEAT_INTERVAL: Incomplete

class UniFiController:
    hass: Incomplete
    config_entry: Incomplete
    api: Incomplete
    ws_task: Incomplete
    available: bool
    wireless_clients: Incomplete
    site: Incomplete
    is_admin: bool
    _cancel_heartbeat_check: Incomplete
    _heartbeat_time: Incomplete
    entities: Incomplete
    known_objects: Incomplete
    poe_command_queue: Incomplete
    _cancel_poe_command: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, api: aiounifi.Controller) -> None: ...
    option_supported_clients: Incomplete
    option_track_clients: Incomplete
    option_track_wired_clients: Incomplete
    option_track_devices: Incomplete
    option_ssid_filter: Incomplete
    option_detection_time: Incomplete
    option_ignore_wired_bug: Incomplete
    option_block_clients: Incomplete
    option_dpi_restrictions: Incomplete
    option_allow_bandwidth_sensors: Incomplete
    option_allow_uptime_sensors: Incomplete
    def load_config_entry_options(self) -> None: ...
    @property
    def host(self) -> str: ...
    @staticmethod
    def register_platform(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, entity_class: type[UnifiEntity], descriptions: tuple[UnifiEntityDescription, ...], requires_admin: bool = ...) -> None: ...
    def register_platform_add_entities(self, unifi_platform_entity: type[UnifiEntity], descriptions: tuple[UnifiEntityDescription, ...], async_add_entities: AddEntitiesCallback) -> None: ...
    @property
    def signal_reachable(self) -> str: ...
    @property
    def signal_options_update(self) -> str: ...
    @property
    def signal_heartbeat_missed(self) -> str: ...
    async def initialize(self) -> None: ...
    def async_heartbeat(self, unique_id: str, heartbeat_expire_time: datetime | None = ...) -> None: ...
    def _async_check_for_stale(self, *_: datetime) -> None: ...
    def async_queue_poe_port_command(self, device_id: str, port_idx: int, poe_mode: str) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    def async_update_device_registry(self) -> DeviceEntry: ...
    @staticmethod
    async def async_config_entry_updated(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    def start_websocket(self) -> None: ...
    def reconnect(self, log: bool = ...) -> None: ...
    async def async_reconnect(self) -> None: ...
    def shutdown(self, event: Event) -> None: ...
    async def async_reset(self) -> bool: ...

async def get_unifi_controller(hass: HomeAssistant, config: MappingProxyType[str, Any]) -> aiounifi.Controller: ...
