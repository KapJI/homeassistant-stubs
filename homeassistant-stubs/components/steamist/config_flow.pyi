from .const import CONNECTION_EXCEPTIONS as CONNECTION_EXCEPTIONS, DISCOVER_SCAN_TIMEOUT as DISCOVER_SCAN_TIMEOUT, DOMAIN as DOMAIN
from .discovery import async_discover_device as async_discover_device, async_discover_devices as async_discover_devices, async_is_steamist_device as async_is_steamist_device, async_update_entry_from_discovery as async_update_entry_from_discovery
from _typeshed import Incomplete
from discovery30303 import Device30303
from homeassistant import config_entries as config_entries
from homeassistant.components import dhcp as dhcp
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered_devices: Incomplete
    _discovered_device: Incomplete
    def __init__(self) -> None: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> FlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def _async_handle_discovery(self) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    def _async_create_entry_from_device(self, device: Device30303) -> FlowResult: ...
    async def async_step_pick_device(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
