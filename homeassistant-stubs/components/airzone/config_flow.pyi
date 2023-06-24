from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import dhcp as dhcp
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID, CONF_PORT as CONF_PORT
from homeassistant.data_entry_flow import AbortFlow as AbortFlow, FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
SYSTEM_ID_SCHEMA: Incomplete

def short_mac(addr: str) -> str: ...

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    _discovered_ip: str | None
    _discovered_mac: str | None
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> FlowResult: ...
    async def async_step_discovered_connection(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
