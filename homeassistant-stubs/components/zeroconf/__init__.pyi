from .models import HaServiceBrowser as HaServiceBrowser, HaZeroconf as HaZeroconf
from .usage import install_multiple_zeroconf_catcher as install_multiple_zeroconf_catcher
from homeassistant import util as util
from homeassistant.const import EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, __version__ as __version__
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.loader import async_get_homekit as async_get_homekit, async_get_zeroconf as async_get_zeroconf
from typing import Any, TypedDict
from zeroconf import ServiceInfo, Zeroconf as Zeroconf

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

async def async_get_instance(hass: HomeAssistant) -> HaZeroconf: ...
async def _async_get_instance(hass: HomeAssistant, **zcargs: Any) -> HaZeroconf: ...
async def async_setup(hass: HomeAssistant, config: dict) -> bool: ...
def _register_hass_zc_service(hass: HomeAssistant, zeroconf: HaZeroconf, uuid: str) -> None: ...
async def _async_start_zeroconf_browser(hass: HomeAssistant, zeroconf: HaZeroconf) -> None: ...
def handle_homekit(hass: HomeAssistant, homekit_models: dict[str, str], info: HaServiceInfo) -> bool: ...
def info_from_service(service: ServiceInfo) -> Union[HaServiceInfo, None]: ...
def _suppress_invalid_properties(properties: dict) -> None: ...
def _truncate_location_name_to_valid(location_name: str) -> str: ...
