from .const import CONF_CONTRIBUTING_USER as CONF_CONTRIBUTING_USER, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .sensor import CONF_ALTITUDE as CONF_ALTITUDE, DEFAULT_ALTITUDE as DEFAULT_ALTITUDE
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlowWithConfigEntry as OptionsFlowWithConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_RADIUS as CONF_RADIUS, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

class OpenSkyConfigFlowHandler(ConfigFlow, domain=DOMAIN):
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OpenSkyOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_import(self, import_config: ConfigType) -> FlowResult: ...

class OpenSkyOptionsFlowHandler(OptionsFlowWithConfigEntry):
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
