from .const import DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioimmich.users.models import ImmichUser as ImmichUser
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

class InvalidUrl(HomeAssistantError): ...

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

def _parse_url(url: str) -> tuple[str, int, bool]: ...
async def check_user_info(hass: HomeAssistant, host: str, port: int, ssl: bool, verify_ssl: bool, api_key: str) -> ImmichUser: ...

class ImmichConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _name: str
    _current_data: Mapping[str, Any]
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
