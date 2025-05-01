from .const import CONF_INSTALLER_CODE as CONF_INSTALLER_CODE, CONF_USER_CODE as CONF_USER_CODE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_CODE as CONF_CODE, CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
STEP_AUTH_DATA_SCHEMA_SOLUTION: Incomplete
STEP_AUTH_DATA_SCHEMA_AMAX: Incomplete
STEP_AUTH_DATA_SCHEMA_BG: Incomplete
STEP_INIT_DATA_SCHEMA: Incomplete

async def try_connect(data: dict[str, Any], load_selector: int = 0) -> tuple[str, int | None]: ...

class BoschAlarmConfigFlow(ConfigFlow, domain=DOMAIN):
    _data: dict[str, Any]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_auth(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
