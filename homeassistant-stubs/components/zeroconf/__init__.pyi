from . import websocket_api as websocket_api
from .const import DOMAIN as DOMAIN, ZEROCONF_TYPE as ZEROCONF_TYPE
from .discovery import DATA_DISCOVERY as DATA_DISCOVERY, ZeroconfDiscovery as ZeroconfDiscovery, build_homekit_model_lookups as build_homekit_model_lookups, info_from_service as info_from_service
from .models import HaAsyncZeroconf as HaAsyncZeroconf, HaZeroconf as HaZeroconf
from .usage import install_multiple_zeroconf_catcher as install_multiple_zeroconf_catcher
from _typeshed import Incomplete
from homeassistant.components import network as network
from homeassistant.const import EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, __version__ as __version__
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import instance_id as instance_id
from homeassistant.helpers.deprecation import DeprecatedConstant as DeprecatedConstant, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_homekit as async_get_homekit, async_get_zeroconf as async_get_zeroconf, bind_hass as bind_hass
from homeassistant.setup import async_when_setup_or_start as async_when_setup_or_start
from typing import Any

_LOGGER: Incomplete
CONF_DEFAULT_INTERFACE: str
CONF_IPV6: str
DEFAULT_DEFAULT_INTERFACE: bool
DEFAULT_IPV6: bool
MAX_PROPERTY_VALUE_LEN: int
MAX_NAME_LEN: int
_DEPRECATED_ATTR_PROPERTIES_ID: Incomplete
CONFIG_SCHEMA: Incomplete
_DEPRECATED_ZeroconfServiceInfo: Incomplete

@bind_hass
async def async_get_instance(hass: HomeAssistant) -> HaZeroconf: ...
@bind_hass
async def async_get_async_instance(hass: HomeAssistant) -> HaAsyncZeroconf: ...
@callback
def async_get_async_zeroconf(hass: HomeAssistant) -> HaAsyncZeroconf: ...
def _async_get_instance(hass: HomeAssistant) -> HaAsyncZeroconf: ...
@callback
def _async_zc_has_functional_dual_stack() -> bool: ...
def _async_get_zc_args(hass: HomeAssistant) -> dict[str, Any]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _filter_disallowed_characters(name: str) -> str: ...
async def _async_register_hass_zc_service(hass: HomeAssistant, aio_zc: HaAsyncZeroconf, uuid: str) -> None: ...
def _suppress_invalid_properties(properties: dict) -> None: ...
def _truncate_location_name_to_valid(location_name: str) -> str: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
