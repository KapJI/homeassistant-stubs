from . import BringConfigEntry as BringConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from bring_api import BringAuthResponse as BringAuthResponse
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

class BringConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    reauth_entry: BringConfigEntry
    info: BringAuthResponse
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def validate_input(self, user_input: Mapping[str, Any]) -> dict[str, str]: ...
