from .const import CONF_OLD_DISCOVERY as CONF_OLD_DISCOVERY, DEFAULT_CONF_OLD_DISCOVERY as DEFAULT_CONF_OLD_DISCOVERY, DEFAULT_HOST as DEFAULT_HOST, DEFAULT_SSL as DEFAULT_SSL, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN, FRITZ_EXCEPTIONS as FRITZ_EXCEPTIONS, MeshRoles as MeshRoles
from _typeshed import Incomplete
from collections.abc import Callable as Callable, ValuesView
from dataclasses import dataclass, field
from datetime import datetime
from fritzconnection import FritzConnection
from fritzconnection.lib.fritzhosts import FritzHosts
from fritzconnection.lib.fritzstatus import FritzStatus
from fritzconnection.lib.fritzwlan import FritzGuestWLAN
from homeassistant.components.device_tracker import CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.hass_dict import HassKey as HassKey
from types import MappingProxyType
from typing import Any, TypedDict

_LOGGER: Incomplete
FRITZ_DATA_KEY: HassKey[FritzData]
type FritzConfigEntry = ConfigEntry[AvmWrapper]

def _is_tracked(mac: str, current_devices: ValuesView[set[str]]) -> bool: ...
def device_filter_out_from_trackers(mac: str, device: FritzDevice, current_devices: ValuesView[set[str]]) -> bool: ...
def _ha_is_stopping(activity: str) -> None: ...

class ClassSetupMissing(Exception):
    def __init__(self) -> None: ...

@dataclass
class Device:
    connected: bool
    connected_to: str
    connection_type: str
    ip_address: str
    name: str
    ssid: str | None
    wan_access: bool | None = ...

class Interface(TypedDict):
    device: str
    mac: str
    op_mode: str
    ssid: str | None
    type: str

HostAttributes = TypedDict('HostAttributes', {'Index': int, 'IPAddress': str, 'MACAddress': str, 'Active': bool, 'HostName': str, 'InterfaceType': str, 'X_AVM-DE_Port': int, 'X_AVM-DE_Speed': int, 'X_AVM-DE_UpdateAvailable': bool, 'X_AVM-DE_UpdateSuccessful': str, 'X_AVM-DE_InfoURL': str | None, 'X_AVM-DE_MACAddressList': str | None, 'X_AVM-DE_Model': str | None, 'X_AVM-DE_URL': str | None, 'X_AVM-DE_Guest': bool, 'X_AVM-DE_RequestClient': str, 'X_AVM-DE_VPN': bool, 'X_AVM-DE_WANAccess': str, 'X_AVM-DE_Disallow': bool, 'X_AVM-DE_IsMeshable': str, 'X_AVM-DE_Priority': str, 'X_AVM-DE_FriendlyName': str, 'X_AVM-DE_FriendlyNameIsWriteable': str})

class HostInfo(TypedDict):
    mac: str
    name: str
    ip: str
    status: bool

class UpdateCoordinatorDataType(TypedDict):
    call_deflections: dict[int, dict]
    entity_states: dict[str, StateType | bool]

class FritzBoxTools(DataUpdateCoordinator[UpdateCoordinatorDataType]):
    config_entry: FritzConfigEntry
    _devices: dict[str, FritzDevice]
    _options: MappingProxyType[str, Any] | None
    _unique_id: str | None
    connection: FritzConnection
    fritz_guest_wifi: FritzGuestWLAN
    fritz_hosts: FritzHosts
    fritz_status: FritzStatus
    hass: Incomplete
    host: Incomplete
    mesh_role: Incomplete
    device_conn_type: str | None
    device_is_router: bool
    password: Incomplete
    port: Incomplete
    username: Incomplete
    use_tls: Incomplete
    has_call_deflections: bool
    _model: str | None
    _current_firmware: str | None
    _latest_firmware: str | None
    _update_available: bool
    _release_url: str | None
    _entity_update_functions: dict[str, Callable[[FritzStatus, StateType], Any]]
    def __init__(self, hass: HomeAssistant, config_entry: FritzConfigEntry, password: str, port: int, username: str = ..., host: str = ..., use_tls: bool = ...) -> None: ...
    async def async_setup(self, options: MappingProxyType[str, Any] | None = None) -> None: ...
    def setup(self) -> None: ...
    async def async_register_entity_updates(self, key: str, update_fn: Callable[[FritzStatus, StateType], Any]) -> Callable[[], None]: ...
    def _entity_states_update(self) -> dict: ...
    async def _async_update_data(self) -> UpdateCoordinatorDataType: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def model(self) -> str: ...
    @property
    def current_firmware(self) -> str: ...
    @property
    def latest_firmware(self) -> str | None: ...
    @property
    def update_available(self) -> bool: ...
    @property
    def release_url(self) -> str | None: ...
    @property
    def mac(self) -> str: ...
    @property
    def devices(self) -> dict[str, FritzDevice]: ...
    @property
    def signal_device_new(self) -> str: ...
    @property
    def signal_device_update(self) -> str: ...
    async def _async_get_wan_access(self, ip_address: str) -> bool | None: ...
    async def _async_update_hosts_info(self) -> dict[str, Device]: ...
    def _update_device_info(self) -> tuple[bool, str | None, str | None]: ...
    async def _async_update_device_info(self) -> tuple[bool, str | None, str | None]: ...
    async def async_update_call_deflections(self) -> dict[int, dict[str, Any]]: ...
    def manage_device_info(self, dev_info: Device, dev_mac: str, consider_home: bool) -> bool: ...
    async def async_send_signal_device_update(self, new_device: bool) -> None: ...
    async def async_scan_devices(self, now: datetime | None = None) -> None: ...
    async def async_trigger_firmware_update(self) -> bool: ...
    async def async_trigger_reboot(self) -> None: ...
    async def async_trigger_reconnect(self) -> None: ...
    async def async_trigger_set_guest_password(self, password: str | None, length: int) -> None: ...
    async def async_trigger_cleanup(self) -> None: ...

class AvmWrapper(FritzBoxTools):
    async def _async_service_call(self, service_name: str, service_suffix: str, action_name: str, **kwargs: Any) -> dict: ...
    async def async_get_upnp_configuration(self) -> dict[str, Any]: ...
    async def async_get_wan_link_properties(self) -> dict[str, Any]: ...
    async def async_ipv6_active(self) -> bool: ...
    async def async_get_connection_info(self) -> ConnectionInfo: ...
    async def async_get_num_port_mapping(self, con_type: str) -> dict[str, Any]: ...
    async def async_get_port_mapping(self, con_type: str, index: int) -> dict[str, Any]: ...
    async def async_get_wlan_configuration(self, index: int) -> dict[str, Any]: ...
    async def async_set_wlan_configuration(self, index: int, turn_on: bool) -> dict[str, Any]: ...
    async def async_set_deflection_enable(self, index: int, turn_on: bool) -> dict[str, Any]: ...
    async def async_add_port_mapping(self, con_type: str, port_mapping: Any) -> dict[str, Any]: ...
    async def async_set_allow_wan_access(self, ip_address: str, turn_on: bool) -> dict[str, Any]: ...
    async def async_wake_on_lan(self, mac_address: str) -> dict[str, Any]: ...

@dataclass
class FritzData:
    tracked: dict[str, set[str]] = field(default_factory=dict)
    profile_switches: dict[str, set[str]] = field(default_factory=dict)
    wol_buttons: dict[str, set[str]] = field(default_factory=dict)

class FritzDevice:
    _connected: bool
    _connected_to: str | None
    _connection_type: str | None
    _ip_address: str | None
    _last_activity: datetime | None
    _mac: Incomplete
    _name: Incomplete
    _ssid: str | None
    _wan_access: bool | None
    def __init__(self, mac: str, name: str) -> None: ...
    def update(self, dev_info: Device, consider_home: float) -> None: ...
    @property
    def connected_to(self) -> str | None: ...
    @property
    def connection_type(self) -> str | None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def hostname(self) -> str: ...
    @property
    def ip_address(self) -> str | None: ...
    @property
    def last_activity(self) -> datetime | None: ...
    @property
    def ssid(self) -> str | None: ...
    @property
    def wan_access(self) -> bool | None: ...

class SwitchInfo(TypedDict):
    description: str
    friendly_name: str
    icon: str
    type: str
    callback_update: Callable
    callback_switch: Callable
    init_state: bool

@dataclass
class ConnectionInfo:
    connection: str
    mesh_role: MeshRoles
    wan_enabled: bool
    ipv6_active: bool
