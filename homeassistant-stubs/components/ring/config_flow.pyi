from .const import CONF_2FA as CONF_2FA, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import APPLICATION_NAME as APPLICATION_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, str]) -> dict[str, Any]: ...

class RingConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    user_pass: dict[str, Any]
    reauth_entry: ConfigEntry | None
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_2fa(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class Require2FA(HomeAssistantError): ...
class InvalidAuth(HomeAssistantError): ...
