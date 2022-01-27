from .const import DOMAIN as DOMAIN
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class ElgatoFlowHandler(ConfigFlow):
    VERSION: int
    host: str
    port: int
    serial_number: str
    mac: Union[str, None]
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_zeroconf_confirm(self, _: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    def _async_show_setup_form(self, errors: Union[dict[str, str], None] = ...) -> FlowResult: ...
    def _async_create_entry(self) -> FlowResult: ...
    async def _get_elgato_serial_number(self, raise_on_progress: bool = ...) -> None: ...
