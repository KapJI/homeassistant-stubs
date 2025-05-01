from . import websocket_api as websocket_api
from .const import DOMAIN as DOMAIN, SSDP_SCANNER as SSDP_SCANNER, UPNP_SERVER as UPNP_SERVER
from .scanner import IntegrationMatchers as IntegrationMatchers, Scanner as Scanner, SsdpChange as SsdpChange, SsdpHassJobCallback as SsdpHassJobCallback
from .server import Server as Server
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant
from homeassistant.helpers.deprecation import DeprecatedConstant as DeprecatedConstant, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.service_info.ssdp import SsdpServiceInfo as _SsdpServiceInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_ssdp as async_get_ssdp, bind_hass as bind_hass
from homeassistant.util.logging import catch_log_exception as catch_log_exception
from typing import Any

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
CONFIG_SCHEMA: Incomplete
_DEPRECATED_SsdpServiceInfo: Incomplete

def _format_err(name: str, *args: Any) -> str: ...
@bind_hass
async def async_register_callback(hass: HomeAssistant, callback: Callable[[_SsdpServiceInfo, SsdpChange], Coroutine[Any, Any, None] | None], match_dict: dict[str, str] | None = None) -> Callable[[], None]: ...
@bind_hass
async def async_get_discovery_info_by_udn_st(hass: HomeAssistant, udn: str, st: str) -> _SsdpServiceInfo | None: ...
@bind_hass
async def async_get_discovery_info_by_st(hass: HomeAssistant, st: str) -> list[_SsdpServiceInfo]: ...
@bind_hass
async def async_get_discovery_info_by_udn(hass: HomeAssistant, udn: str) -> list[_SsdpServiceInfo]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
