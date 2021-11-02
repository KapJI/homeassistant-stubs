from .const import CONF_USE_NEAREST as CONF_USE_NEAREST, DOMAIN as DOMAIN, NO_AIRLY_SENSORS as NO_AIRLY_SENSORS
from aiohttp import ClientSession as ClientSession
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, HTTP_NOT_FOUND as HTTP_NOT_FOUND, HTTP_UNAUTHORIZED as HTTP_UNAUTHORIZED
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class AirlyFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

async def test_location(client: ClientSession, api_key: str, latitude: float, longitude: float, use_nearest: bool = ...) -> bool: ...
