from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete

class AsekoConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data_schema: Incomplete
    reauth_entry: ConfigEntry | None
    async def get_account_info(self, email: str, password: str) -> dict: ...
    async def async_step_user(self, user_input: Mapping[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_store_credentials(self, info: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth(self, user_input: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Mapping | None = None) -> ConfigFlowResult: ...
