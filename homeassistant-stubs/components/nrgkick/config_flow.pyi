from .api import NRGkickApiClientApiDisabledError as NRGkickApiClientApiDisabledError, NRGkickApiClientAuthenticationError as NRGkickApiClientAuthenticationError, NRGkickApiClientCommunicationError as NRGkickApiClientCommunicationError, NRGkickApiClientError as NRGkickApiClientError, NRGkickApiClientInvalidResponseError as NRGkickApiClientInvalidResponseError
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from typing import Any

_LOGGER: Incomplete

def _normalize_host(value: str) -> str: ...

STEP_USER_DATA_SCHEMA: Incomplete
STEP_AUTH_DATA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, host: str, username: str | None = None, password: str | None = None) -> dict[str, Any]: ...

class NRGkickConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered_host: str | None
    _discovered_name: str | None
    _pending_host: str | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user_auth(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_enable_json_api(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
