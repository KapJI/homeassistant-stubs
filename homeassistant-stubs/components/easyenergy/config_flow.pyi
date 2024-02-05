from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class EasyEnergyFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
