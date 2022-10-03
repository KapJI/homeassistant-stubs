from .const import CONF_DNSMASQ as CONF_DNSMASQ, CONF_INTERFACE as CONF_INTERFACE, CONF_REQUIRE_IP as CONF_REQUIRE_IP, CONF_SSH_KEY as CONF_SSH_KEY, CONF_TRACK_UNKNOWN as CONF_TRACK_UNKNOWN, DEFAULT_DNSMASQ as DEFAULT_DNSMASQ, DEFAULT_INTERFACE as DEFAULT_INTERFACE, DEFAULT_TRACK_UNKNOWN as DEFAULT_TRACK_UNKNOWN, DOMAIN as DOMAIN, PROTOCOL_TELNET as PROTOCOL_TELNET, SENSORS_BYTES as SENSORS_BYTES, SENSORS_CONNECTED_DEVICE as SENSORS_CONNECTED_DEVICE, SENSORS_LOAD_AVG as SENSORS_LOAD_AVG, SENSORS_RATES as SENSORS_RATES, SENSORS_TEMPERATURES as SENSORS_TEMPERATURES
from _typeshed import Incomplete
from aioasuswrt.asuswrt import AsusWrt, Device as WrtDevice
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.device_tracker import CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODE as CONF_MODE, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

CONF_REQ_RELOAD: Incomplete
DEFAULT_NAME: str
KEY_COORDINATOR: str
KEY_SENSORS: str
SCAN_INTERVAL: Incomplete
SENSORS_TYPE_BYTES: str
SENSORS_TYPE_COUNT: str
SENSORS_TYPE_LOAD_AVG: str
SENSORS_TYPE_RATES: str
SENSORS_TYPE_TEMPERATURES: str
_LOGGER: Incomplete

def _get_dict(keys: list, values: list) -> dict[str, Any]: ...

class AsusWrtSensorDataHandler:
    _hass: Incomplete
    _api: Incomplete
    _connected_devices: int
    def __init__(self, hass: HomeAssistant, api: AsusWrt) -> None: ...
    async def _get_connected_devices(self) -> dict[str, int]: ...
    async def _get_bytes(self) -> dict[str, Any]: ...
    async def _get_rates(self) -> dict[str, Any]: ...
    async def _get_load_avg(self) -> dict[str, Any]: ...
    async def _get_temperatures(self) -> dict[str, Any]: ...
    def update_device_count(self, conn_devices: int) -> bool: ...
    async def get_coordinator(self, sensor_type: str, should_poll: bool = ...) -> DataUpdateCoordinator: ...

class AsusWrtDevInfo:
    _mac: Incomplete
    _name: Incomplete
    _ip_address: Incomplete
    _last_activity: Incomplete
    _connected: bool
    def __init__(self, mac: str, name: Union[str, None] = ...) -> None: ...
    def update(self, dev_info: Union[WrtDevice, None] = ..., consider_home: int = ...) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def mac(self) -> str: ...
    @property
    def name(self) -> Union[str, None]: ...
    @property
    def ip_address(self) -> Union[str, None]: ...
    @property
    def last_activity(self) -> Union[datetime, None]: ...

class AsusWrtRouter:
    hass: Incomplete
    _entry: Incomplete
    _api: Incomplete
    _protocol: Incomplete
    _host: Incomplete
    _model: str
    _sw_v: Incomplete
    _devices: Incomplete
    _connected_devices: int
    _connect_error: bool
    _sensors_data_handler: Incomplete
    _sensors_coordinator: Incomplete
    _on_close: Incomplete
    _options: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def setup(self) -> None: ...
    async def update_all(self, now: Union[datetime, None] = ...) -> None: ...
    async def update_devices(self) -> None: ...
    async def init_sensors_coordinator(self) -> None: ...
    async def _update_unpolled_sensors(self) -> None: ...
    async def _get_available_temperature_sensors(self) -> list[str]: ...
    async def close(self) -> None: ...
    def async_on_close(self, func: CALLBACK_TYPE) -> None: ...
    def update_options(self, new_options: dict[str, Any]) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def signal_device_new(self) -> str: ...
    @property
    def signal_device_update(self) -> str: ...
    @property
    def host(self) -> str: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def name(self) -> str: ...
    @property
    def devices(self) -> dict[str, AsusWrtDevInfo]: ...
    @property
    def sensors_coordinator(self) -> dict[str, Any]: ...

async def get_nvram_info(api: AsusWrt, info_type: str) -> dict[str, Any]: ...
def get_api(conf: dict[str, Any], options: Union[dict[str, Any], None] = ...) -> AsusWrt: ...
