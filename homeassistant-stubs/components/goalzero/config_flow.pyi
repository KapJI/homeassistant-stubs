from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import dhcp as dhcp
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

_LOGGER: Incomplete

class GoalZeroFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    ip_address: Incomplete
    def __init__(self) -> None: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> FlowResult: ...
    async def async_step_confirm_discovery(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_try_connect(self, host: str) -> tuple[Union[str, None], Union[str, None]]: ...
