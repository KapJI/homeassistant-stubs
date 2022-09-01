from .const import DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant import config_entries as config_entries
from homeassistant.components.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> FlowResult: ...
