from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import async_get_integration as async_get_integration
from homeassistant.util.network import is_ip_address as is_ip_address
from typing import Any

_LOGGER: Any
STEP_USER_DATA_SCHEMA: Any
VALLOX_CONNECTION_EXCEPTIONS: Any

async def validate_host(hass: HomeAssistant, host: str) -> None: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_import(self, data: dict[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class InvalidHost(HomeAssistantError): ...
