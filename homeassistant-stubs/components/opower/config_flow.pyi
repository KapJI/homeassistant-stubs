from .const import CONF_LOGIN_DATA as CONF_LOGIN_DATA, CONF_TOTP_SECRET as CONF_TOTP_SECRET, CONF_UTILITY as CONF_UTILITY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.typing import VolDictType as VolDictType
from opower import MfaHandlerBase as MfaHandlerBase
from typing import Any

_LOGGER: Incomplete
CONF_MFA_CODE: str
CONF_MFA_METHOD: str

async def _validate_login(hass: HomeAssistant, data: Mapping[str, Any]) -> None: ...

class OpowerConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _data: dict[str, Any]
    mfa_handler: MfaHandlerBase | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_credentials(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_mfa_options(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_mfa_code(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @callback
    def _async_create_opower_entry(self, data: dict[str, Any], **kwargs: Any) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
