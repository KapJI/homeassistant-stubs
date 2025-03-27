import asyncio
from .bluetooth import async_connect_scanner as async_connect_scanner
from .const import ATTR_CHANNEL as ATTR_CHANNEL, ATTR_CLICK_TYPE as ATTR_CLICK_TYPE, ATTR_DEVICE as ATTR_DEVICE, ATTR_GENERATION as ATTR_GENERATION, BATTERY_DEVICES_WITH_PERMANENT_CONNECTION as BATTERY_DEVICES_WITH_PERMANENT_CONNECTION, BLEScannerMode as BLEScannerMode, CONF_BLE_SCANNER_MODE as CONF_BLE_SCANNER_MODE, CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DOMAIN as DOMAIN, DUAL_MODE_LIGHT_MODELS as DUAL_MODE_LIGHT_MODELS, ENTRY_RELOAD_COOLDOWN as ENTRY_RELOAD_COOLDOWN, EVENT_SHELLY_CLICK as EVENT_SHELLY_CLICK, INPUTS_EVENTS_DICT as INPUTS_EVENTS_DICT, LOGGER as LOGGER, MAX_PUSH_UPDATE_FAILURES as MAX_PUSH_UPDATE_FAILURES, MODELS_SUPPORTING_LIGHT_EFFECTS as MODELS_SUPPORTING_LIGHT_EFFECTS, OTA_BEGIN as OTA_BEGIN, OTA_ERROR as OTA_ERROR, OTA_PROGRESS as OTA_PROGRESS, OTA_SUCCESS as OTA_SUCCESS, PUSH_UPDATE_ISSUE_ID as PUSH_UPDATE_ISSUE_ID, REST_SENSORS_UPDATE_INTERVAL as REST_SENSORS_UPDATE_INTERVAL, RPC_INPUTS_EVENTS_TYPES as RPC_INPUTS_EVENTS_TYPES, RPC_RECONNECT_INTERVAL as RPC_RECONNECT_INTERVAL, RPC_SENSORS_POLLING_INTERVAL as RPC_SENSORS_POLLING_INTERVAL, SHBTN_MODELS as SHBTN_MODELS, UPDATE_PERIOD_MULTIPLIER as UPDATE_PERIOD_MULTIPLIER
from .utils import async_create_issue_unsupported_firmware as async_create_issue_unsupported_firmware, get_block_device_sleep_period as get_block_device_sleep_period, get_device_entry_gen as get_device_entry_gen, get_host as get_host, get_http_port as get_http_port, get_rpc_device_wakeup_period as get_rpc_device_wakeup_period, get_rpc_ws_url as get_rpc_ws_url, get_shelly_model_name as get_shelly_model_name, update_device_fw_info as update_device_fw_info
from _typeshed import Incomplete
from aioshelly.block_device import BlockDevice, BlockUpdateType
from aioshelly.rpc_device import RpcDevice, RpcUpdateType
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.bluetooth import async_remove_scanner as async_remove_scanner
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, format_mac as format_mac
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from propcache.api import cached_property
from typing import Any

@dataclass
class ShellyEntryData:
    platforms: list[Platform]
    block: ShellyBlockCoordinator | None = ...
    rest: ShellyRestCoordinator | None = ...
    rpc: ShellyRpcCoordinator | None = ...
    rpc_poll: ShellyRpcPollingCoordinator | None = ...
    rpc_script_events: dict[int, list[str]] | None = ...
    rpc_supports_scripts: bool | None = ...
type ShellyConfigEntry = ConfigEntry[ShellyEntryData]

class ShellyCoordinatorBase[_DeviceT: BlockDevice | RpcDevice](DataUpdateCoordinator[None]):
    config_entry: ShellyConfigEntry
    device: Incomplete
    device_id: str | None
    _pending_platforms: list[Platform] | None
    _came_online_once: bool
    _debounced_reload: Debouncer[Coroutine[Any, Any, None]]
    def __init__(self, hass: HomeAssistant, entry: ShellyConfigEntry, device: _DeviceT, update_interval: float) -> None: ...
    @cached_property
    def model(self) -> str: ...
    @cached_property
    def mac(self) -> str: ...
    @property
    def sw_version(self) -> str: ...
    @property
    def sleep_period(self) -> int: ...
    def async_setup(self, pending_platforms: list[Platform] | None = None) -> None: ...
    async def shutdown(self) -> None: ...
    async def _handle_ha_stop(self, _event: Event) -> None: ...
    async def _async_device_connect_task(self) -> bool: ...
    async def _async_reload_entry(self) -> None: ...
    last_update_success: bool
    async def async_shutdown_device_and_start_reauth(self) -> None: ...

class ShellyBlockCoordinator(ShellyCoordinatorBase[BlockDevice]):
    _last_cfg_changed: int | None
    _last_mode: str | None
    _last_effect: str | None
    _last_input_events_count: dict
    _last_target_temp: float | None
    _push_update_failures: int
    _input_event_listeners: list[Callable[[dict[str, Any]], None]]
    def __init__(self, hass: HomeAssistant, entry: ShellyConfigEntry, device: BlockDevice) -> None: ...
    @callback
    def async_subscribe_input_events(self, input_event_callback: Callable[[dict[str, Any]], None]) -> CALLBACK_TYPE: ...
    @callback
    def _async_device_updates_handler(self) -> None: ...
    async def _async_update_data(self) -> None: ...
    _came_online_once: bool
    @callback
    def _async_handle_update(self, device_: BlockDevice, update_type: BlockUpdateType) -> None: ...
    def async_setup(self, pending_platforms: list[Platform] | None = None) -> None: ...

class ShellyRestCoordinator(ShellyCoordinatorBase[BlockDevice]):
    def __init__(self, hass: HomeAssistant, device: BlockDevice, entry: ShellyConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...

class ShellyRpcCoordinator(ShellyCoordinatorBase[RpcDevice]):
    connected: bool
    _disconnected_callbacks: list[CALLBACK_TYPE]
    _connection_lock: Incomplete
    _event_listeners: list[Callable[[dict[str, Any]], None]]
    _ota_event_listeners: list[Callable[[dict[str, Any]], None]]
    _input_event_listeners: list[Callable[[dict[str, Any]], None]]
    _connect_task: asyncio.Task | None
    def __init__(self, hass: HomeAssistant, entry: ShellyConfigEntry, device: RpcDevice) -> None: ...
    @cached_property
    def bluetooth_source(self) -> str: ...
    async def async_device_online(self, source: str) -> None: ...
    update_interval: Incomplete
    def update_sleep_period(self) -> bool: ...
    @callback
    def async_subscribe_ota_events(self, ota_event_callback: Callable[[dict[str, Any]], None]) -> CALLBACK_TYPE: ...
    @callback
    def async_subscribe_input_events(self, input_event_callback: Callable[[dict[str, Any]], None]) -> CALLBACK_TYPE: ...
    @callback
    def async_subscribe_events(self, event_callback: Callable[[dict[str, Any]], None]) -> CALLBACK_TYPE: ...
    async def _async_update_listener(self, hass: HomeAssistant, entry: ShellyConfigEntry) -> None: ...
    @callback
    def _async_device_event_handler(self, event_data: dict[str, Any]) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _async_disconnected(self, reconnect: bool) -> None: ...
    @callback
    def _async_run_disconnected_events(self) -> None: ...
    last_update_success: bool
    async def _async_connected(self) -> None: ...
    async def _async_run_connected_events(self) -> None: ...
    async def _async_setup_outbound_websocket(self) -> None: ...
    async def _async_connect_ble_scanner(self) -> None: ...
    @callback
    def _async_handle_rpc_device_online(self) -> None: ...
    _came_online_once: bool
    @callback
    def _async_handle_update(self, device_: RpcDevice, update_type: RpcUpdateType) -> None: ...
    def async_setup(self, pending_platforms: list[Platform] | None = None) -> None: ...
    async def shutdown(self) -> None: ...

class ShellyRpcPollingCoordinator(ShellyCoordinatorBase[RpcDevice]):
    def __init__(self, hass: HomeAssistant, entry: ShellyConfigEntry, device: RpcDevice) -> None: ...
    async def _async_update_data(self) -> None: ...

def get_block_coordinator_by_device_id(hass: HomeAssistant, device_id: str) -> ShellyBlockCoordinator | None: ...
def get_rpc_coordinator_by_device_id(hass: HomeAssistant, device_id: str) -> ShellyRpcCoordinator | None: ...
async def async_reconnect_soon(hass: HomeAssistant, entry: ShellyConfigEntry) -> None: ...
