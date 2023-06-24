from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_FILE_PATH as CONF_FILE_PATH
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

DATA_SCHEMA: Incomplete
_LOGGER: Incomplete

def validate_path(hass: HomeAssistant, path: str) -> str: ...

class FilesizeConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class NotValidError(HomeAssistantError): ...
class NotAllowedError(HomeAssistantError): ...
