from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

_LOGGER: Any
USER_DATA_SCHEMA: Any

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, _: dict[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class InvalidAuth(HomeAssistantError): ...
