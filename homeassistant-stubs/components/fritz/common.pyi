from .const import DEFAULT_DEVICE_NAME as DEFAULT_DEVICE_NAME, DEFAULT_HOST as DEFAULT_HOST, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN, SERVICE_REBOOT as SERVICE_REBOOT, SERVICE_RECONNECT as SERVICE_RECONNECT, TRACKER_SCAN_INTERVAL as TRACKER_SCAN_INTERVAL
from datetime import datetime
from homeassistant.components.device_tracker.const import CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, dispatcher_send as dispatcher_send
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from types import MappingProxyType
from typing import Any, Callable, TypedDict

_LOGGER: Any

class ClassSetupMissing(Exception):
    def __init__(self) -> None: ...

class Device:
    mac: str
    ip_address: str
    name: str

class HostInfo(TypedDict):
    mac: str
    name: str
    ip: str
    status: bool

class FritzBoxTools:
    _cancel_scan: Any
    _devices: Any
    _options: Any
    _unique_id: Any
    connection: Any
    fritz_hosts: Any
    fritz_status: Any
    hass: Any
    host: Any
    password: Any
    port: Any
    username: Any
    _mac: Any
    _model: Any
    _sw_version: Any
    def __init__(self, hass: HomeAssistant, password: str, username: str = ..., host: str = ..., port: int = ...) -> None: ...
    async def async_setup(self) -> None: ...
    def setup(self) -> None: ...
    async def async_start(self, options: MappingProxyType[str, Any]) -> None: ...
    def async_unload(self) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def model(self) -> str: ...
    @property
    def sw_version(self) -> str: ...
    @property
    def mac(self) -> str: ...
    @property
    def devices(self) -> dict[str, Any]: ...
    @property
    def signal_device_new(self) -> str: ...
    @property
    def signal_device_update(self) -> str: ...
    def _update_info(self) -> list[HostInfo]: ...
    def scan_devices(self, now: Union[datetime, None] = ...) -> None: ...
    async def service_fritzbox(self, service: str) -> None: ...

class FritzData:
    tracked: dict
    profile_switches: dict

class FritzDeviceBase(Entity):
    _router: Any
    _mac: Any
    _name: Any
    def __init__(self, router: FritzBoxTools, device: FritzDevice) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def ip_address(self) -> Union[str, None]: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def hostname(self) -> Union[str, None]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    async def async_process_update(self) -> None: ...
    async def async_on_demand_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class FritzDevice:
    _mac: Any
    _name: Any
    _ip_address: Any
    _last_activity: Any
    _connected: bool
    def __init__(self, mac: str, name: str) -> None: ...
    def update(self, dev_info: Device, dev_home: bool, consider_home: float) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def hostname(self) -> str: ...
    @property
    def ip_address(self) -> Union[str, None]: ...
    @property
    def last_activity(self) -> Union[datetime, None]: ...

class SwitchInfo(TypedDict):
    description: str
    friendly_name: str
    icon: str
    type: str
    callback_update: Callable
    callback_switch: Callable

class FritzBoxBaseEntity:
    _fritzbox_tools: Any
    _device_name: Any
    def __init__(self, fritzbox_tools: FritzBoxTools, device_name: str) -> None: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
