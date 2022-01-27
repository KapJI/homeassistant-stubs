from .const import CONF_PROVINCE as CONF_PROVINCE, DOMAIN as DOMAIN, PROVINCES as PROVINCES
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class StookalertFlowHandler(ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
