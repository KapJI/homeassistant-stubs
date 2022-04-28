import voluptuous as vol
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CODE as CONF_CODE, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

DEFAULT_EMAIL_2FA_SLEEP: int
DEFAULT_EMAIL_2FA_TIMEOUT: int
STEP_REAUTH_SCHEMA: Any
STEP_SMS_2FA_SCHEMA: Any
STEP_USER_SCHEMA: Any

class SimpliSafeFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _password: Any
    _reauth: bool
    _simplisafe: Any
    _username: Any
    def __init__(self) -> None: ...
    async def _async_authenticate(self, error_step_id: str, error_schema: vol.Schema) -> FlowResult: ...
    async def _async_finish_setup(self) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> SimpliSafeOptionsFlowHandler: ...
    async def async_step_reauth(self, config: dict[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_sms_2fa(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class SimpliSafeOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Any
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
