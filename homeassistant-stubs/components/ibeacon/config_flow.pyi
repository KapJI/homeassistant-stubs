from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.components import bluetooth as bluetooth
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
