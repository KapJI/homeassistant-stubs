from .const import CONF_LINE as CONF_LINE, DEFAULT_LINES as DEFAULT_LINES, DOMAIN as DOMAIN, TUBE_LINES as TUBE_LINES
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithReload as OptionsFlowWithReload
from homeassistant.core import callback as callback
from homeassistant.helpers import selector as selector
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete

class LondonUndergroundConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(_: ConfigEntry) -> LondonUndergroundOptionsFlow: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, import_data: ConfigType) -> ConfigFlowResult: ...

class LondonUndergroundOptionsFlow(OptionsFlowWithReload):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
