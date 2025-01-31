from .const import DOMAIN as DOMAIN
from .helpers import cookidoo_from_config_data as cookidoo_from_config_data
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_EMAIL as CONF_EMAIL, CONF_LANGUAGE as CONF_LANGUAGE, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.helpers.selector import CountrySelector as CountrySelector, CountrySelectorConfig as CountrySelectorConfig, LanguageSelector as LanguageSelector, LanguageSelectorConfig as LanguageSelectorConfig, TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

_LOGGER: Incomplete
AUTH_DATA_SCHEMA: Incomplete

class CookidooConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    COUNTRY_DATA_SCHEMA: dict
    LANGUAGE_DATA_SCHEMA: dict
    user_input: dict[str, Any]
    user_uuid: str
    async def async_step_reconfigure(self, user_input: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_language(self, language_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def generate_country_schema(self) -> None: ...
    async def generate_language_schema(self) -> None: ...
    async def validate_input(self, user_input: dict[str, Any], language_input: dict[str, Any] | None = None) -> dict[str, str]: ...
