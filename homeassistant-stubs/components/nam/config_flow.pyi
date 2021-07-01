from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import ATTR_NAME as ATTR_NAME, CONF_HOST as CONF_HOST
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Any

class NAMFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    host: Any
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def async_step_confirm_discovery(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_get_mac(self, host: str) -> str: ...
