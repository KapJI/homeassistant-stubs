from .models import HaAsyncServiceBrowser as HaAsyncServiceBrowser, HaAsyncZeroconf as HaAsyncZeroconf, HaZeroconf as HaZeroconf
from .usage import install_multiple_zeroconf_catcher as install_multiple_zeroconf_catcher
from collections.abc import Coroutine
from homeassistant import config_entries as config_entries, util as util
from homeassistant.components import network as network
from homeassistant.components.network.models import Adapter as Adapter
from homeassistant.const import EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, __version__ as __version__
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.loader import async_get_homekit as async_get_homekit, async_get_zeroconf as async_get_zeroconf, bind_hass as bind_hass
from typing import Any, TypedDict
from zeroconf import ServiceStateChange
from zeroconf.asyncio import AsyncServiceInfo

_LOGGER: Any
DOMAIN: str
ZEROCONF_TYPE: str
HOMEKIT_TYPES: Any
CONF_DEFAULT_INTERFACE: str
CONF_IPV6: str
DEFAULT_DEFAULT_INTERFACE: bool
DEFAULT_IPV6: bool
HOMEKIT_PAIRED_STATUS_FLAG: str
HOMEKIT_MODEL: str
MDNS_TARGET_IP: str
MAX_PROPERTY_VALUE_LEN: int
MAX_NAME_LEN: int
CONFIG_SCHEMA: Any

class HaServiceInfo(TypedDict):
    host: str
    port: Union[int, None]
    hostname: str
    type: str
    name: str
    properties: dict[str, Any]

class ZeroconfFlow(TypedDict):
    domain: str
    context: dict[str, Any]
    data: HaServiceInfo

async def async_get_instance(hass: HomeAssistant) -> HaZeroconf: ...
async def async_get_async_instance(hass: HomeAssistant) -> HaAsyncZeroconf: ...
async def _async_get_instance(hass: HomeAssistant, **zcargs: Any) -> HaAsyncZeroconf: ...
def _async_use_default_interface(adapters: list[Adapter]) -> bool: ...
async def async_setup(hass: HomeAssistant, config: dict) -> bool: ...
async def _async_register_hass_zc_service(hass: HomeAssistant, aio_zc: HaAsyncZeroconf, uuid: str) -> None: ...

class FlowDispatcher:
    hass: Any
    pending_flows: Any
    started: bool
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_start(self) -> None: ...
    def _async_process_pending_flows(self) -> None: ...
    def async_create(self, flow: ZeroconfFlow) -> None: ...
    def _init_flow(self, flow: ZeroconfFlow) -> Coroutine[None, None, FlowResult]: ...

class ZeroconfDiscovery:
    hass: Any
    zeroconf: Any
    zeroconf_types: Any
    homekit_models: Any
    ipv6: Any
    flow_dispatcher: Any
    async_service_browser: Any
    def __init__(self, hass: HomeAssistant, zeroconf: HaZeroconf, zeroconf_types: dict[str, list[dict[str, str]]], homekit_models: dict[str, str], ipv6: bool) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_stop(self) -> None: ...
    def async_start(self) -> None: ...
    def async_service_update(self, zeroconf: HaZeroconf, service_type: str, name: str, state_change: ServiceStateChange) -> None: ...
    async def _process_service_update(self, zeroconf: HaZeroconf, service_type: str, name: str) -> None: ...

def handle_homekit(hass: HomeAssistant, homekit_models: dict[str, str], info: HaServiceInfo) -> Union[ZeroconfFlow, None]: ...
def info_from_service(service: AsyncServiceInfo) -> Union[HaServiceInfo, None]: ...
def _suppress_invalid_properties(properties: dict) -> None: ...
def _truncate_location_name_to_valid(location_name: str) -> str: ...
