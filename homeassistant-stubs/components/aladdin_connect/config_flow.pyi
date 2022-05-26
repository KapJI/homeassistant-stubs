from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
REAUTH_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> None: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    entry: Union[config_entries.ConfigEntry, None]
    async def async_step_reauth(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, import_data: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class InvalidAuth(HomeAssistantError): ...
