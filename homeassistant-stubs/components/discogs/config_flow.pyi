from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers.aiohttp_client import SERVER_SOFTWARE as SERVER_SOFTWARE
from typing import Any, override

CONFIG_SCHEMA: Incomplete

class DiscogsConfigFlow(ConfigFlow, domain=DOMAIN):
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...

def _validate_token(token: str) -> tuple[int | None, str, dict[str, str]]: ...
