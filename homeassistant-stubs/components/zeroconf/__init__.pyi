from .models import HaAsyncServiceBrowser as HaAsyncServiceBrowser, HaAsyncZeroconf as HaAsyncZeroconf, HaZeroconf as HaZeroconf
from .usage import install_multiple_zeroconf_catcher as install_multiple_zeroconf_catcher
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.components.network import async_get_source_ip as async_get_source_ip
from homeassistant.components.network.const import MDNS_TARGET_IP as MDNS_TARGET_IP
from homeassistant.components.network.models import Adapter as Adapter
from homeassistant.const import EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, __version__ as __version__
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.frame import report as report
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import Integration as Integration, async_get_homekit as async_get_homekit, async_get_integration as async_get_integration, async_get_zeroconf as async_get_zeroconf, bind_hass as bind_hass
from typing import Any, Final
from zeroconf import ServiceStateChange
from zeroconf.asyncio import AsyncServiceInfo

_LOGGER: Incomplete
DOMAIN: str
ZEROCONF_TYPE: str
HOMEKIT_TYPES: Incomplete
LOWER_MATCH_ATTRS: Incomplete
CONF_DEFAULT_INTERFACE: str
CONF_IPV6: str
DEFAULT_DEFAULT_INTERFACE: bool
DEFAULT_IPV6: bool
HOMEKIT_PAIRED_STATUS_FLAG: str
HOMEKIT_MODEL: str
MAX_PROPERTY_VALUE_LEN: int
MAX_NAME_LEN: int
ATTR_PROPERTIES: Final[str]
ATTR_PROPERTIES_ID: Final[str]
CONFIG_SCHEMA: Incomplete

class ZeroconfServiceInfo(BaseServiceInfo):
    host: str
    addresses: list[str]
    port: Union[int, None]
    hostname: str
    type: str
    name: str
    properties: dict[str, Any]
    def __getitem__(self, name: str) -> Any: ...
    def get(self, name: str, default: Any = ...) -> Any: ...
    def __init__(self, host, addresses, port, hostname, type, name, properties) -> None: ...

async def async_get_instance(hass: HomeAssistant) -> HaZeroconf: ...
async def async_get_async_instance(hass: HomeAssistant) -> HaAsyncZeroconf: ...
async def _async_get_instance(hass: HomeAssistant, **zcargs: Any) -> HaAsyncZeroconf: ...
def _async_zc_has_functional_dual_stack() -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _get_announced_addresses(adapters: list[Adapter], first_ip: Union[bytes, None] = ...) -> list[bytes]: ...
async def _async_register_hass_zc_service(hass: HomeAssistant, aio_zc: HaAsyncZeroconf, uuid: str) -> None: ...
def _match_against_data(matcher: dict[str, Union[str, dict[str, str]]], match_data: dict[str, str]) -> bool: ...
def _match_against_props(matcher: dict[str, str], props: dict[str, str]) -> bool: ...
def is_homekit_paired(props: dict[str, Any]) -> bool: ...

class ZeroconfDiscovery:
    hass: Incomplete
    zeroconf: Incomplete
    zeroconf_types: Incomplete
    homekit_models: Incomplete
    ipv6: Incomplete
    async_service_browser: Incomplete
    def __init__(self, hass: HomeAssistant, zeroconf: HaZeroconf, zeroconf_types: dict[str, list[dict[str, Union[str, dict[str, str]]]]], homekit_models: dict[str, str], ipv6: bool) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_stop(self) -> None: ...
    def async_service_update(self, zeroconf: HaZeroconf, service_type: str, name: str, state_change: ServiceStateChange) -> None: ...
    async def _process_service_update(self, zeroconf: HaZeroconf, service_type: str, name: str) -> None: ...

def async_get_homekit_discovery_domain(homekit_models: dict[str, str], props: dict[str, Any]) -> Union[str, None]: ...
def info_from_service(service: AsyncServiceInfo) -> Union[ZeroconfServiceInfo, None]: ...
def _first_non_link_local_address(addresses: Union[list[bytes], list[str]]) -> Union[str, None]: ...
def _suppress_invalid_properties(properties: dict) -> None: ...
def _truncate_location_name_to_valid(location_name: str) -> str: ...
