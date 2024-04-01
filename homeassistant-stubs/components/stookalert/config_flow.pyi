from .const import CONF_PROVINCE as CONF_PROVINCE, DOMAIN as DOMAIN, PROVINCES as PROVINCES
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from typing import Any

class StookalertFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
