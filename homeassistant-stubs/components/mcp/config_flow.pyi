from . import async_get_config_entry_implementation as async_get_config_entry_implementation
from .application_credentials import authorization_server_context as authorization_server_context
from .const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_AUTHORIZATION_URL as CONF_AUTHORIZATION_URL, CONF_TOKEN_URL as CONF_TOKEN_URL, DOMAIN as DOMAIN
from .coordinator import TokenManager as TokenManager, mcp_client as mcp_client
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.application_credentials import AuthorizationServer as AuthorizationServer
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.config_entry_oauth2_flow import AbstractOAuth2FlowHandler as AbstractOAuth2FlowHandler, async_get_implementations as async_get_implementations
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
OAUTH_DISCOVERY_ENDPOINT: str
MCP_DISCOVERY_HEADERS: Incomplete

async def async_discover_oauth_config(hass: HomeAssistant, mcp_server_url: str) -> AuthorizationServer: ...
async def validate_input(hass: HomeAssistant, data: dict[str, Any], token_manager: TokenManager | None = None) -> dict[str, Any]: ...

class ModelContextProtocolConfigFlow(AbstractOAuth2FlowHandler, domain=DOMAIN):
    VERSION: int
    DOMAIN = DOMAIN
    logger = _LOGGER
    data: dict[str, Any]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_auth_discovery(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def authorization_server(self) -> AuthorizationServer: ...
    async def async_step_credentials_choice(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_new_credentials(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pick_implementation(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_oauth_create_entry(self, data: dict) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    flow_impl: Incomplete
    async def async_step_reauth_confirm(self, user_input: Mapping[str, Any] | None = None) -> ConfigFlowResult: ...

class InvalidUrl(HomeAssistantError): ...
class CannotConnect(HomeAssistantError): ...
class TimeoutConnectError(HomeAssistantError): ...
class InvalidAuth(HomeAssistantError): ...
class MissingCapabilities(HomeAssistantError): ...
