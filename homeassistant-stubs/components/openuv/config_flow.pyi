import voluptuous as vol
from .const import CONF_FROM_WINDOW as CONF_FROM_WINDOW, CONF_TO_WINDOW as CONF_TO_WINDOW, DEFAULT_FROM_WINDOW as DEFAULT_FROM_WINDOW, DEFAULT_TO_WINDOW as DEFAULT_TO_WINDOW, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

class OpenUvFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    @property
    def config_schema(self) -> vol.Schema: ...
    async def _show_form(self, errors: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OpenUvOptionsFlowHandler: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class OpenUvOptionsFlowHandler(config_entries.OptionsFlow):
    entry: Incomplete
    def __init__(self, entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
