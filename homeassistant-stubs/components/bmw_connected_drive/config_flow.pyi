from . import DOMAIN as DOMAIN
from .const import CONF_ALLOWED_REGIONS as CONF_ALLOWED_REGIONS, CONF_READ_ONLY as CONF_READ_ONLY, CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries, core as core, exceptions as exceptions
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_REGION as CONF_REGION, CONF_SOURCE as CONF_SOURCE, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DATA_SCHEMA: Incomplete

async def validate_input(hass: core.HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class BMWConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> BMWOptionsFlow: ...

class BMWOptionsFlow(config_entries.OptionsFlowWithConfigEntry):
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_account_options(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class CannotConnect(exceptions.HomeAssistantError): ...
