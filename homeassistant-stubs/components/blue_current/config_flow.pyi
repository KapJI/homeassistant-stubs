from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN
from typing import Any

DATA_SCHEMA: Incomplete

class BlueCurrentConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _reauth_entry: ConfigEntry | None
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
