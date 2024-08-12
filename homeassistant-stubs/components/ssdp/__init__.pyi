from _typeshed import Incomplete
from async_upnp_client.const import AddressTupleVXType as AddressTupleVXType, DeviceOrServiceType as DeviceOrServiceType, SsdpSource
from async_upnp_client.server import UpnpServerDevice, UpnpServerService as UpnpServerService
from async_upnp_client.ssdp_listener import SsdpDevice as SsdpDevice
from async_upnp_client.utils import CaseInsensitiveDict
from collections.abc import Callable as Callable, Coroutine, Mapping
from dataclasses import dataclass
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, MATCH_ALL as MATCH_ALL
from homeassistant.core import Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
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
ATTR_ST: str
ATTR_NT: str
ATTR_UPNP_DEVICE_TYPE: str
ATTR_UPNP_FRIENDLY_NAME: str
ATTR_UPNP_MANUFACTURER: str
ATTR_UPNP_MANUFACTURER_URL: str
ATTR_UPNP_MODEL_DESCRIPTION: str
ATTR_UPNP_MODEL_NAME: str
ATTR_UPNP_MODEL_NUMBER: str
ATTR_UPNP_MODEL_URL: str
ATTR_UPNP_SERIAL: str
ATTR_UPNP_SERVICE_LIST: str
ATTR_UPNP_UDN: str
ATTR_UPNP_UPC: str
ATTR_UPNP_PRESENTATION_URL: str
ATTR_HA_MATCHING_DOMAINS: str
PRIMARY_MATCH_KEYS: Incomplete
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

@dataclass(slots=True)
class SsdpServiceInfo(BaseServiceInfo):
    ssdp_usn: str
    ssdp_st: str
    upnp: Mapping[str, Any]
    ssdp_location: str | None = ...
    ssdp_nt: str | None = ...
    ssdp_udn: str | None = ...
    ssdp_ext: str | None = ...
    ssdp_server: str | None = ...
    ssdp_headers: Mapping[str, Any] = ...
    ssdp_all_locations: set[str] = ...
    x_homeassistant_matching_domains: set[str] = ...
    def __init__(self, ssdp_usn, ssdp_st, upnp, ssdp_location=..., ssdp_nt=..., ssdp_udn=..., ssdp_ext=..., ssdp_server=..., ssdp_headers=..., ssdp_all_locations=..., x_homeassistant_matching_domains=...) -> None: ...

SsdpChange: Incomplete
SsdpHassJobCallback: Incomplete
SSDP_SOURCE_SSDP_CHANGE_MAPPING: Mapping[SsdpSource, SsdpChange]

def _format_err(name: str, *args: Any) -> str: ...
async def async_register_callback(hass: HomeAssistant, callback: Callable[[SsdpServiceInfo, SsdpChange], Coroutine[Any, Any, None] | None], match_dict: dict[str, str] | None = None) -> Callable[[], None]: ...
async def async_get_discovery_info_by_udn_st(hass: HomeAssistant, udn: str, st: str) -> SsdpServiceInfo | None: ...
async def async_get_discovery_info_by_st(hass: HomeAssistant, st: str) -> list[SsdpServiceInfo]: ...
async def async_get_discovery_info_by_udn(hass: HomeAssistant, udn: str) -> list[SsdpServiceInfo]: ...
async def async_build_source_set(hass: HomeAssistant) -> set[IPv4Address | IPv6Address]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _async_process_callbacks(hass: HomeAssistant, callbacks: list[SsdpHassJobCallback], discovery_info: SsdpServiceInfo, ssdp_change: SsdpChange) -> None: ...
def _async_headers_match(headers: CaseInsensitiveDict, lower_match_dict: dict[str, str]) -> bool: ...

class IntegrationMatchers:
    _match_by_key: Incomplete
    def __init__(self) -> None: ...
    def async_setup(self, integration_matchers: dict[str, list[dict[str, str]]]) -> None: ...
    def async_matching_domains(self, info_with_desc: CaseInsensitiveDict) -> set[str]: ...

class Scanner:
    hass: Incomplete
    _cancel_scan: Incomplete
    _ssdp_listeners: Incomplete
    _device_tracker: Incomplete
    _callbacks: Incomplete
    _description_cache: Incomplete
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
    def _async_get_matching_callbacks(self, combined_headers: CaseInsensitiveDict) -> list[SsdpHassJobCallback]: ...
    def _ssdp_listener_callback(self, ssdp_device: SsdpDevice, dst: DeviceOrServiceType, source: SsdpSource) -> None: ...
    async def _ssdp_listener_process_callback_with_lookup(self, ssdp_device: SsdpDevice, dst: DeviceOrServiceType, source: SsdpSource) -> None: ...
    def _ssdp_listener_process_callback(self, ssdp_device: SsdpDevice, dst: DeviceOrServiceType, source: SsdpSource, info_desc: Mapping[str, Any]) -> None: ...
    def _async_dismiss_discoveries(self, byebye_discovery_info: SsdpServiceInfo) -> None: ...
    async def _async_get_description_dict(self, location: str | None) -> Mapping[str, str]: ...
    async def _async_headers_to_discovery_info(self, ssdp_device: SsdpDevice, headers: CaseInsensitiveDict) -> SsdpServiceInfo: ...
    async def async_get_discovery_info_by_udn_st(self, udn: str, st: str) -> SsdpServiceInfo | None: ...
    async def async_get_discovery_info_by_st(self, st: str) -> list[SsdpServiceInfo]: ...
    async def async_get_discovery_info_by_udn(self, udn: str) -> list[SsdpServiceInfo]: ...

def discovery_info_from_headers_and_description(ssdp_device: SsdpDevice, combined_headers: CaseInsensitiveDict, info_desc: Mapping[str, Any]) -> SsdpServiceInfo: ...
def _udn_from_usn(usn: str | None) -> str | None: ...

class HassUpnpServiceDevice(UpnpServerDevice):
    DEVICE_DEFINITION: Incomplete
    EMBEDDED_DEVICES: list[type[UpnpServerDevice]]
    SERVICES: list[type[UpnpServerService]]

async def _async_find_next_available_port(source: AddressTupleVXType) -> int: ...

class Server:
    hass: Incomplete
    _upnp_servers: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_start(self) -> None: ...
    async def _async_get_instance_udn(self) -> str: ...
    async def _async_start_upnp_servers(self, event: Event) -> None: ...
    async def async_stop(self, *_: Any) -> None: ...
    async def _async_stop_upnp_servers(self) -> None: ...
