from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class CPUSpeedFlowHandler(ConfigFlow):
    VERSION: int
    _imported_name: Union[str, None]
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, config: dict[str, Any]) -> FlowResult: ...
