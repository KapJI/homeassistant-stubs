from .const import DATA_DISCOVERY as DATA_DISCOVERY, DOMAIN as DOMAIN
from .utils import async_discover_devices as async_discover_devices
from homeassistant import config_entries as config_entries
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

class SwitcherFlowHandler(config_entries.ConfigFlow):
    async def async_step_import(self, import_config: ConfigType) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
