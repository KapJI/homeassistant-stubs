import voluptuous as vol
from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

class OpenUvFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    @property
    def config_schema(self) -> vol.Schema: ...
    async def _show_form(self, errors: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, import_config: dict[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
