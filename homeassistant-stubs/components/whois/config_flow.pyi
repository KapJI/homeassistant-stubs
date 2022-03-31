from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class WhoisFlowHandler(ConfigFlow):
    VERSION: int
    imported_name: Union[str, None]
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
