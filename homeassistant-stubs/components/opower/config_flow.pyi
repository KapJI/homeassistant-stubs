from .const import CONF_TOTP_SECRET as CONF_TOTP_SECRET, CONF_UTILITY as CONF_UTILITY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def _validate_login(hass: HomeAssistant, login_data: dict[str, str]) -> dict[str, str]: ...

class OpowerConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    utility_info: dict[str, Any] | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_mfa(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @callback
    def _async_create_opower_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
