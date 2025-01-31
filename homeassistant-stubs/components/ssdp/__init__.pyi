from _typeshed import Incomplete
from async_upnp_client.const import AddressTupleVXType as AddressTupleVXType, DeviceOrServiceType as DeviceOrServiceType, SsdpSource
from async_upnp_client.description_cache import DescriptionCache
from async_upnp_client.server import UpnpServer, UpnpServerDevice, UpnpServerService as UpnpServerService
from async_upnp_client.ssdp_listener import SsdpDevice as SsdpDevice, SsdpListener
from async_upnp_client.utils import CaseInsensitiveDict
from collections.abc import Callable as Callable, Coroutine, Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, MATCH_ALL as MATCH_ALL
from homeassistant.core import Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as core_callback
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.deprecation import DeprecatedConstant as DeprecatedConstant, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.service_info.ssdp import SsdpServiceInfo as _SsdpServiceInfo
from homeassistant.helpers.system_info import async_get_system_info as async_get_system_info
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_ssdp as async_get_ssdp, bind_hass as bind_hass
from homeassistant.util.async_ import create_eager_task as create_eager_task
from homeassistant.util.logging import catch_log_exception as catch_log_exception
from ipaddress import IPv4Address, IPv6Address
from typing import Any

DOMAIN: str
SSDP_SCANNER: str
UPNP_SERVER: str
UPNP_SERVER_MIN_PORT: int
UPNP_SERVER_MAX_PORT: int
SCAN_INTERVAL: Incomplete
IPV4_BROADCAST: Incomplete
ATTR_SSDP_LOCATION: str
ATTR_SSDP_ST: str
ATTR_SSDP_NT: str
ATTR_SSDP_UDN: str
ATTR_SSDP_USN: str
ATTR_SSDP_EXT: str
ATTR_SSDP_SERVER: str
ATTR_SSDP_BOOTID: str
ATTR_SSDP_NEXTBOOTID: str
_DEPRECATED_ATTR_ST: Incomplete
_DEPRECATED_ATTR_NT: Incomplete
_DEPRECATED_ATTR_UPNP_DEVICE_TYPE: Incomplete
_DEPRECATED_ATTR_UPNP_FRIENDLY_NAME: Incomplete
_DEPRECATED_ATTR_UPNP_MANUFACTURER: Incomplete
_DEPRECATED_ATTR_UPNP_MANUFACTURER_URL: Incomplete
_DEPRECATED_ATTR_UPNP_MODEL_DESCRIPTION: Incomplete
_DEPRECATED_ATTR_UPNP_MODEL_NAME: Incomplete
_DEPRECATED_ATTR_UPNP_MODEL_NUMBER: Incomplete
_DEPRECATED_ATTR_UPNP_MODEL_URL: Incomplete
_DEPRECATED_ATTR_UPNP_SERIAL: Incomplete
_DEPRECATED_ATTR_UPNP_SERVICE_LIST: Incomplete
_DEPRECATED_ATTR_UPNP_UDN: Incomplete
_DEPRECATED_ATTR_UPNP_UPC: Incomplete
_DEPRECATED_ATTR_UPNP_PRESENTATION_URL: Incomplete
ATTR_HA_MATCHING_DOMAINS: str
PRIMARY_MATCH_KEYS: Incomplete
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
_DEPRECATED_SsdpServiceInfo: Incomplete
SsdpChange: Incomplete
type SsdpHassJobCallback = HassJob[[_SsdpServiceInfo, SsdpChange], Coroutine[Any, Any, None] | None]
SSDP_SOURCE_SSDP_CHANGE_MAPPING: Mapping[SsdpSource, SsdpChange]

def _format_err(name: str, *args: Any) -> str: ...
@bind_hass
async def async_register_callback(hass: HomeAssistant, callback: Callable[[_SsdpServiceInfo, SsdpChange], Coroutine[Any, Any, None] | None], match_dict: dict[str, str] | None = None) -> Callable[[], None]: ...
@bind_hass
async def async_get_discovery_info_by_udn_st(hass: HomeAssistant, udn: str, st: str) -> _SsdpServiceInfo | None: ...
@bind_hass
async def async_get_discovery_info_by_st(hass: HomeAssistant, st: str) -> list[_SsdpServiceInfo]: ...
@bind_hass
async def async_get_discovery_info_by_udn(hass: HomeAssistant, udn: str) -> list[_SsdpServiceInfo]: ...
async def async_build_source_set(hass: HomeAssistant) -> set[IPv4Address | IPv6Address]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@core_callback
def _async_process_callbacks(hass: HomeAssistant, callbacks: list[SsdpHassJobCallback], discovery_info: _SsdpServiceInfo, ssdp_change: SsdpChange) -> None: ...
@core_callback
def _async_headers_match(headers: CaseInsensitiveDict, lower_match_dict: dict[str, str]) -> bool: ...

class IntegrationMatchers:
    _match_by_key: dict[str, dict[str, list[tuple[str, dict[str, str]]]]] | None
    def __init__(self) -> None: ...
    @core_callback
    def async_setup(self, integration_matchers: dict[str, list[dict[str, str]]]) -> None: ...
    @core_callback
    def async_matching_domains(self, info_with_desc: CaseInsensitiveDict) -> set[str]: ...

class Scanner:
    hass: Incomplete
    _cancel_scan: Callable[[], None] | None
    _ssdp_listeners: list[SsdpListener]
    _device_tracker: Incomplete
    _callbacks: list[tuple[SsdpHassJobCallback, dict[str, str]]]
    _description_cache: DescriptionCache | None
    integration_matchers: Incomplete
    def __init__(self, hass: HomeAssistant, integration_matchers: IntegrationMatchers) -> None: ...
    @property
    def _ssdp_devices(self) -> list[SsdpDevice]: ...
    async def async_register_callback(self, callback: SsdpHassJobCallback, match_dict: dict[str, str] | None = None) -> Callable[[], None]: ...
    async def async_stop(self, *_: Any) -> None: ...
    async def _async_stop_ssdp_listeners(self) -> None: ...
    async def async_scan(self, *_: Any) -> None: ...
    async def async_scan_multicast(self, *_: Any) -> None: ...
    async def async_scan_broadcast(self, *_: Any) -> None: ...
    async def async_start(self) -> None: ...
    async def _async_start_ssdp_listeners(self) -> None: ...
    @core_callback
    def _async_get_matching_callbacks(self, combined_headers: CaseInsensitiveDict) -> list[SsdpHassJobCallback]: ...
    def _ssdp_listener_callback(self, ssdp_device: SsdpDevice, dst: DeviceOrServiceType, source: SsdpSource) -> None: ...
    async def _ssdp_listener_process_callback_with_lookup(self, ssdp_device: SsdpDevice, dst: DeviceOrServiceType, source: SsdpSource) -> None: ...
    def _ssdp_listener_process_callback(self, ssdp_device: SsdpDevice, dst: DeviceOrServiceType, source: SsdpSource, info_desc: Mapping[str, Any], skip_callbacks: bool = False) -> None: ...
    def _async_dismiss_discoveries(self, byebye_discovery_info: _SsdpServiceInfo) -> None: ...
    async def _async_get_description_dict(self, location: str | None) -> Mapping[str, str]: ...
    async def _async_headers_to_discovery_info(self, ssdp_device: SsdpDevice, headers: CaseInsensitiveDict) -> _SsdpServiceInfo: ...
    async def async_get_discovery_info_by_udn_st(self, udn: str, st: str) -> _SsdpServiceInfo | None: ...
    async def async_get_discovery_info_by_st(self, st: str) -> list[_SsdpServiceInfo]: ...
    async def async_get_discovery_info_by_udn(self, udn: str) -> list[_SsdpServiceInfo]: ...
    @core_callback
    def _handle_config_entry_removed(self, entry: config_entries.ConfigEntry) -> None: ...

def discovery_info_from_headers_and_description(ssdp_device: SsdpDevice, combined_headers: CaseInsensitiveDict, info_desc: Mapping[str, Any]) -> _SsdpServiceInfo: ...
def _udn_from_usn(usn: str | None) -> str | None: ...

class HassUpnpServiceDevice(UpnpServerDevice):
    DEVICE_DEFINITION: Incomplete
    EMBEDDED_DEVICES: list[type[UpnpServerDevice]]
    SERVICES: list[type[UpnpServerService]]

async def _async_find_next_available_port(source: AddressTupleVXType) -> int: ...

class Server:
    hass: Incomplete
    _upnp_servers: list[UpnpServer]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_start(self) -> None: ...
    async def _async_get_instance_udn(self) -> str: ...
    async def _async_start_upnp_servers(self, event: Event) -> None: ...
    async def async_stop(self, *_: Any) -> None: ...
    async def _async_stop_upnp_servers(self) -> None: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
