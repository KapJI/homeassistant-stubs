from .const import ATTR_ENCRYPTED as ATTR_ENCRYPTED, CONF_DEVICE_KEY as CONF_DEVICE_KEY, CONF_SALT as CONF_SALT, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

def validate_input(entry: dict[str, str]) -> Union[dict[str, str], None]: ...

class SimplePushFlowHandler(config_entries.ConfigFlow):
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
