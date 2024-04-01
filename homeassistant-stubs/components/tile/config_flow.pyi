import voluptuous as vol
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

STEP_REAUTH_SCHEMA: Incomplete
STEP_USER_SCHEMA: Incomplete

class TileFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _password: Incomplete
    _username: Incomplete
    def __init__(self) -> None: ...
    async def _async_verify(self, step_id: str, schema: vol.Schema) -> ConfigFlowResult: ...
    async def async_step_import(self, import_config: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
