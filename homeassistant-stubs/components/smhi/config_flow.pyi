from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, HOME_LOCATION_NAME as HOME_LOCATION_NAME
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.selector import LocationSelector as LocationSelector
from typing import Any

async def async_check_location(hass: HomeAssistant, longitude: float, latitude: float) -> bool: ...

class SmhiFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
