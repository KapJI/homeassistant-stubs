from .const import CONF_SERIAL as CONF_SERIAL, DEFAULT_ATTEMPTS as DEFAULT_ATTEMPTS, DOMAIN as DOMAIN, OVERALL_TIMEOUT as OVERALL_TIMEOUT, TARGET_ANY as TARGET_ANY, _LOGGER as _LOGGER
from .discovery import async_discover_devices as async_discover_devices
from .util import async_entry_is_legacy as async_entry_is_legacy, async_get_legacy_entry as async_get_legacy_entry, async_multi_execute_lifx_with_retries as async_multi_execute_lifx_with_retries, formatted_serial as formatted_serial, lifx_features as lifx_features, mac_matches_serial_number as mac_matches_serial_number
from aiolifx.aiolifx import Light as Light
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST
from homeassistant.core import callback as callback
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Self

class LifXConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    host: str | None
    _discovered_devices: dict[str, Light]
    _discovered_device: Light | None
    def __init__(self) -> None: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_homekit(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> ConfigFlowResult: ...
    async def _async_handle_discovery(self, host: str, serial: str | None = None) -> ConfigFlowResult: ...
    def is_matching(self, other_flow: Self) -> bool: ...
    @callback
    def _async_discovered_pending_migration(self) -> bool: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pick_device(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @callback
    def _async_create_entry_from_device(self, device: Light) -> ConfigFlowResult: ...
    async def _async_try_connect(self, host: str, serial: str | None = None, raise_on_progress: bool = True) -> Light | None: ...
