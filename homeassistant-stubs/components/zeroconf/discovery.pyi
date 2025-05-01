import re
from .const import DOMAIN as DOMAIN, REQUEST_TIMEOUT as REQUEST_TIMEOUT
from .models import HaZeroconf as HaZeroconf
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.discovery_flow import DiscoveryKey as DiscoveryKey
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as _ZeroconfServiceInfo
from homeassistant.loader import HomeKitDiscoveredIntegration as HomeKitDiscoveredIntegration, ZeroconfMatcher as ZeroconfMatcher
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Final
from zeroconf import ServiceStateChange
from zeroconf.asyncio import AsyncServiceBrowser, AsyncServiceInfo

_LOGGER: Incomplete
ZEROCONF_TYPE: str
HOMEKIT_TYPES: Incomplete
_HOMEKIT_MODEL_SPLITS: Incomplete
HOMEKIT_PAIRED_STATUS_FLAG: str
HOMEKIT_MODEL_LOWER: str
HOMEKIT_MODEL_UPPER: str
ATTR_DOMAIN: Final[str]
ATTR_NAME: Final[str]
ATTR_PROPERTIES: Final[str]
DATA_DISCOVERY: HassKey[ZeroconfDiscovery]

def build_homekit_model_lookups(homekit_models: dict[str, HomeKitDiscoveredIntegration]) -> tuple[dict[str, HomeKitDiscoveredIntegration], dict[re.Pattern, HomeKitDiscoveredIntegration]]: ...
def _compile_fnmatch(pattern: str) -> re.Pattern: ...
def _memorized_fnmatch(name: str, pattern: str) -> bool: ...
def _match_against_props(matcher: dict[str, str], props: dict[str, str | None]) -> bool: ...
def is_homekit_paired(props: dict[str, Any]) -> bool: ...
def async_get_homekit_discovery(homekit_model_lookups: dict[str, HomeKitDiscoveredIntegration], homekit_model_matchers: dict[re.Pattern, HomeKitDiscoveredIntegration], props: dict[str, Any]) -> HomeKitDiscoveredIntegration | None: ...
def info_from_service(service: AsyncServiceInfo) -> _ZeroconfServiceInfo | None: ...

class ZeroconfDiscovery:
    hass: Incomplete
    zeroconf: Incomplete
    zeroconf_types: Incomplete
    homekit_model_lookups: Incomplete
    homekit_model_matchers: Incomplete
    async_service_browser: AsyncServiceBrowser | None
    _service_update_listeners: set[Callable[[AsyncServiceInfo], None]]
    _service_removed_listeners: set[Callable[[str], None]]
    def __init__(self, hass: HomeAssistant, zeroconf: HaZeroconf, zeroconf_types: dict[str, list[ZeroconfMatcher]], homekit_model_lookups: dict[str, HomeKitDiscoveredIntegration], homekit_model_matchers: dict[re.Pattern, HomeKitDiscoveredIntegration]) -> None: ...
    @callback
    def async_register_service_update_listener(self, listener: Callable[[AsyncServiceInfo], None]) -> Callable[[], None]: ...
    @callback
    def async_register_service_removed_listener(self, listener: Callable[[str], None]) -> Callable[[], None]: ...
    async def async_setup(self) -> None: ...
    async def async_stop(self) -> None: ...
    @callback
    def _handle_config_entry_removed(self, entry: config_entries.ConfigEntry) -> None: ...
    def _async_dismiss_discoveries(self, name: str) -> None: ...
    @callback
    def async_service_update(self, zeroconf: HaZeroconf, service_type: str, name: str, state_change: ServiceStateChange) -> None: ...
    @callback
    def _async_service_update(self, zeroconf: HaZeroconf, service_type: str, name: str) -> None: ...
    async def _async_lookup_and_process_service_update(self, zeroconf: HaZeroconf, async_service_info: AsyncServiceInfo, service_type: str, name: str) -> None: ...
    @callback
    def _async_process_service_update(self, async_service_info: AsyncServiceInfo, service_type: str, name: str) -> None: ...
