from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from typing import Any

_LOGGER: Incomplete

class ToloSaunaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered_host: str
    @staticmethod
    def _check_device_availability(host: str) -> bool: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
