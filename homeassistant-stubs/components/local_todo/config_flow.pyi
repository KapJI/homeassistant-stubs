from .const import CONF_STORAGE_KEY as CONF_STORAGE_KEY, CONF_TODO_LIST_NAME as CONF_TODO_LIST_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.util import slugify as slugify
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
