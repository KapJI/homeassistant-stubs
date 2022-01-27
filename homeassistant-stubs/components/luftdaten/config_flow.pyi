from .const import CONF_SENSOR_ID as CONF_SENSOR_ID, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class SensorCommunityFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    def _show_form(self, errors: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
