import voluptuous as vol
from .const import DEFAULT_PORT as DEFAULT_PORT, DEVICE_TYPE_LIST as DEVICE_TYPE_LIST, DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .utils import async_client_session as async_client_session
from _typeshed import Incomplete
from aiocomelit.api import ComelitCommonApi as ComelitCommonApi
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PIN as CONF_PIN, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

DEFAULT_HOST: str
DEFAULT_PIN: int

def user_form_schema(user_input: dict[str, Any] | None) -> vol.Schema: ...

STEP_REAUTH_DATA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class ComelitConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class CannotConnect(HomeAssistantError): ...
class InvalidAuth(HomeAssistantError): ...
