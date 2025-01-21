from . import DOMAIN as DOMAIN
from .const import CONF_ALLOWED_REGIONS as CONF_ALLOWED_REGIONS, CONF_CAPTCHA_REGIONS as CONF_CAPTCHA_REGIONS, CONF_CAPTCHA_TOKEN as CONF_CAPTCHA_TOKEN, CONF_CAPTCHA_URL as CONF_CAPTCHA_URL, CONF_GCID as CONF_GCID, CONF_READ_ONLY as CONF_READ_ONLY, CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN
from .coordinator import BMWConfigEntry as BMWConfigEntry
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_REGION as CONF_REGION, CONF_SOURCE as CONF_SOURCE, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from homeassistant.util.ssl import get_default_context as get_default_context
from typing import Any

DATA_SCHEMA: Incomplete
RECONFIGURE_SCHEMA: Incomplete
CAPTCHA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class BMWConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data: dict[str, Any]
    _existing_entry_data: dict[str, Any]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_change_password(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_captcha(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: BMWConfigEntry) -> BMWOptionsFlow: ...

class BMWOptionsFlow(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_account_options(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class CannotConnect(HomeAssistantError): ...
class InvalidAuth(HomeAssistantError): ...
class MissingCaptcha(HomeAssistantError): ...
