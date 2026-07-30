from .const import CURRENT_VERSION as CURRENT_VERSION, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_UNIT_ID as DEFAULT_UNIT_ID, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from typing import Any, override

async def _async_probe(user_input: dict[str, Any]) -> tuple[str | None, str | None]: ...

class NeoPoolConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = CURRENT_VERSION
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
