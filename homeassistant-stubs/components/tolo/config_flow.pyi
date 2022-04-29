from .const import DEFAULT_NAME as DEFAULT_NAME, DEFAULT_RETRY_COUNT as DEFAULT_RETRY_COUNT, DEFAULT_RETRY_TIMEOUT as DEFAULT_RETRY_TIMEOUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import dhcp as dhcp
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

_LOGGER: Incomplete

class ToloSaunaConfigFlow(ConfigFlow):
    VERSION: int
    _discovered_host: Union[str, None]
    @staticmethod
    def _check_device_availability(host: str) -> bool: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> FlowResult: ...
    async def async_step_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
