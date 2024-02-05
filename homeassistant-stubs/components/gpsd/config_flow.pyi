from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

STEP_USER_DATA_SCHEMA: Incomplete

class GPSDConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_import(self, import_data: dict[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
