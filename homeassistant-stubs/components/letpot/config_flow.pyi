from .const import CONF_ACCESS_TOKEN_EXPIRES as CONF_ACCESS_TOKEN_EXPIRES, CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN, CONF_REFRESH_TOKEN_EXPIRES as CONF_REFRESH_TOKEN_EXPIRES, CONF_USER_ID as CONF_USER_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
STEP_REAUTH_SCHEMA: Incomplete

class LetPotConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def _async_validate_credentials(self, email: str, password: str) -> tuple[dict[str, str], dict[str, Any] | None]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
