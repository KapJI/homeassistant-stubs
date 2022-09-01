from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, str]) -> dict[str, str]: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class CannotConnect(HomeAssistantError): ...
class NotSupported(HomeAssistantError): ...
