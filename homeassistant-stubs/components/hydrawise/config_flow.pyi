from .const import APP_ID as APP_ID, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from typing import Any

STEP_USER_DATA_SCHEMA: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete

class HydrawiseConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _show_user_form(self, errors: dict[str, str]) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _show_reauth_form(self, errors: dict[str, str]) -> ConfigFlowResult: ...

async def _authenticate(username: str, password: str, api_key: str) -> tuple[str | None, dict[str, str]]: ...
