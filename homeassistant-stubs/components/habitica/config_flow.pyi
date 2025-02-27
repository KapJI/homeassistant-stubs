from .const import CONF_API_USER as CONF_API_USER, DEFAULT_URL as DEFAULT_URL, DOMAIN as DOMAIN, FORGOT_PASSWORD_URL as FORGOT_PASSWORD_URL, HABITICANS_URL as HABITICANS_URL, SECTION_DANGER_ZONE as SECTION_DANGER_ZONE, SECTION_REAUTH_API_KEY as SECTION_REAUTH_API_KEY, SECTION_REAUTH_LOGIN as SECTION_REAUTH_LOGIN, SIGN_UP_URL as SIGN_UP_URL, SITE_DATA_URL as SITE_DATA_URL, X_CLIENT as X_CLIENT
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry
from _typeshed import Incomplete
from collections.abc import Mapping
from habiticalib import LoginData as LoginData, UserData as UserData
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

STEP_ADVANCED_DATA_SCHEMA: Incomplete
STEP_LOGIN_DATA_SCHEMA: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete
STEP_RECONF_DATA_SCHEMA: Incomplete
_LOGGER: Incomplete

class HabiticaConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_login(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_advanced(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def validate_login(self, user_input: Mapping[str, Any]) -> tuple[dict[str, str], LoginData | None, UserData | None]: ...
    async def validate_api_key(self, user_input: Mapping[str, Any]) -> tuple[dict[str, str], UserData | None]: ...
