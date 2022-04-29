from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import ssdp as ssdp, zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

DATA_SCHEMA: Incomplete
ERROR_CANNOT_CONNECT: str
ERROR_UNKNOWN: str
_LOGGER: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]: ...

class RokuConfigFlow(ConfigFlow):
    VERSION: int
    discovery_info: dict[str, Any]
    def __init__(self) -> None: ...
    def _show_form(self, errors: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_homekit(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
