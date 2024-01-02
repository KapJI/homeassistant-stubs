from .const import CONF_COUNTER_ID as CONF_COUNTER_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

def validate_input(data: dict[str, Any]) -> None: ...

class SuezWaterConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_import(self, user_input: dict[str, Any]) -> FlowResult: ...

class CannotConnect(HomeAssistantError): ...
class InvalidAuth(HomeAssistantError): ...
