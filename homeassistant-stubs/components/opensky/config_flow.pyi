from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .sensor import CONF_ALTITUDE as CONF_ALTITUDE, DEFAULT_ALTITUDE as DEFAULT_ALTITUDE
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, CONF_RADIUS as CONF_RADIUS
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

class OpenSkyConfigFlowHandler(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_import(self, import_config: ConfigType) -> FlowResult: ...
