from .const import DOMAIN as DOMAIN
from .utils import hash_from_url as hash_from_url
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries, exceptions as exceptions
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

_LOGGER: Incomplete
DATA_SCHEMA: Incomplete

async def _validate_input(data: dict[str, Any]) -> dict[str, str]: ...

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...

class InputValidationError(exceptions.HomeAssistantError):
    base: Incomplete
    def __init__(self, base: str) -> None: ...
