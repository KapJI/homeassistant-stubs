from .const import CONF_ADMIN_API_KEY as CONF_ADMIN_API_KEY, CONF_API_URL as CONF_API_URL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete
GHOST_INTEGRATION_SETUP_URL: str
STEP_USER_DATA_SCHEMA: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete

class GhostConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _validate_credentials(self, api_url: str, admin_api_key: str) -> dict[str, Any]: ...
    async def _validate_and_create(self, api_url: str, admin_api_key: str, errors: dict[str, str]) -> ConfigFlowResult | None: ...
