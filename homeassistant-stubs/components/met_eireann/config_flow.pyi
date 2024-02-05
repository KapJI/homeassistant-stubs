from .const import DOMAIN as DOMAIN, HOME_LOCATION_NAME as HOME_LOCATION_NAME
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class MetEireannFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
