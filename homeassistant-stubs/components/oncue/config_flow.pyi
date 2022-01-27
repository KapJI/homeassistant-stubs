from .const import CONNECTION_EXCEPTIONS as CONNECTION_EXCEPTIONS, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Any

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
