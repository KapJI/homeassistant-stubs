from .const import CONF_USER_ID as CONF_USER_ID, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CODE as CONF_CODE, CONF_TOKEN as CONF_TOKEN, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any, NamedTuple

CONF_AUTH_CODE: str
CONF_DOCS_URL: str
AUTH_DOCS_URL: str
STEP_USER_SCHEMA: Any

class SimpliSafeOAuthValues(NamedTuple):
    code_verifier: str
    auth_url: str

def async_get_simplisafe_oauth_values() -> SimpliSafeOAuthValues: ...

class SimpliSafeFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _oauth_values: Any
    _reauth: bool
    _username: Any
    def __init__(self) -> None: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> SimpliSafeOptionsFlowHandler: ...
    def _async_show_form(self, *, errors: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, config: dict[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class SimpliSafeOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Any
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
