from .const import DEFAULT_HOST as DEFAULT_HOST, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from typing import Any

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
REAUTH_SCHEMA: Incomplete

async def _validate_connection(user_input: dict[str, Any]) -> str: ...

class LibreHardwareMonitorConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _host: str | None
    _port: int | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
