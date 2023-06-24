from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CODE as CONF_CODE, CONF_TOKEN as CONF_TOKEN, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any, NamedTuple

CONF_AUTH_CODE: str
STEP_USER_SCHEMA: Incomplete

class SimpliSafeOAuthValues(NamedTuple):
    auth_url: str
    code_verifier: str

def async_get_simplisafe_oauth_values() -> SimpliSafeOAuthValues: ...

class SimpliSafeFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _oauth_values: Incomplete
    _reauth: bool
    def __init__(self) -> None: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> SimpliSafeOptionsFlowHandler: ...
    async def async_step_reauth(self, config: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class SimpliSafeOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
