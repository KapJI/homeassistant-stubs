from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, MIN_REQUIRED_MEALIE_VERSION as MIN_REQUIRED_MEALIE_VERSION
from .utils import create_version as create_version
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.hassio import HassioServiceInfo as HassioServiceInfo
from typing import Any

USER_SCHEMA: Incomplete
REAUTH_SCHEMA: Incomplete
DISCOVERY_SCHEMA: Incomplete
EXAMPLE_URL: str

class MealieConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    host: str | None
    verify_ssl: bool
    _hassio_discovery: dict[str, Any] | None
    async def check_connection(self, api_token: str) -> tuple[dict[str, str], str | None]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> ConfigFlowResult: ...
    async def async_step_hassio_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _show_hassio_form(self, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
