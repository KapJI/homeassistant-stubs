from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

async def validate_input(hass: HomeAssistant, api_key: str) -> None: ...

class StreamlabsConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_import(self, user_input: dict[str, Any]) -> FlowResult: ...

class CannotConnect(HomeAssistantError): ...
