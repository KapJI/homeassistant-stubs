from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

_LOGGER: Any

class NFAndroidTVFlowHandler(config_entries.ConfigFlow):
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, import_config: dict[str, Any]) -> FlowResult: ...
    async def _async_try_connect(self, host: str) -> Union[str, None]: ...
