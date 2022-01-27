from .const import CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

DATA_SCHEMA: Any

class TVWeatherConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    entry: config_entries.ConfigEntry
    async def validate_input(self, sensor_api: str, station: str) -> str: ...
    async def async_step_import(self, config: dict[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
