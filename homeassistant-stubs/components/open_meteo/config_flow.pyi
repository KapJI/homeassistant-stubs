from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_ZONE as CONF_ZONE
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.selector import selector as selector
from typing import Any

class OpenMeteoFlowHandler(ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
