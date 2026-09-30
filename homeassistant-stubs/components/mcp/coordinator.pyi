import httpx
import probatio
from .auth import AuthenticateHeader as AuthenticateHeader
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import AsyncGenerator, Awaitable, Callable
from contextlib import asynccontextmanager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, HomeAssistantError as HomeAssistantError, OAuth2TokenRequestReauthError as OAuth2TokenRequestReauthError
from homeassistant.helpers import llm as llm
from homeassistant.helpers.httpx_client import create_async_httpx_client as create_async_httpx_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.ssl import SSLCipherList as SSLCipherList, SSL_ALPN_HTTP11 as SSL_ALPN_HTTP11, client_context as client_context
from mcp.client.session import ClientSession
from mcp.types import InitializeResult as InitializeResult, ToolAnnotations
from typing import override

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
TIMEOUT: int
type TokenManager = Callable[[], Awaitable[str]]

def _create_sse_httpx_client(headers: dict[str, str] | None = None, timeout: httpx.Timeout | None = None, auth: httpx.Auth | None = None) -> httpx.AsyncClient: ...
@asynccontextmanager
async def mcp_client(hass: HomeAssistant, url: str, token_manager: TokenManager | None = None) -> AsyncGenerator[tuple[ClientSession, InitializeResult]]: ...
def _tool_annotations(remote: ToolAnnotations | None) -> llm.ToolAnnotations: ...

class ModelContextProtocolTool(llm.Tool):
    integration = DOMAIN
    name: Incomplete
    title: Incomplete
    description: Incomplete
    parameters: Incomplete
    annotations: Incomplete
    server_url: Incomplete
    config_entry: Incomplete
    token_manager: Incomplete
    def __init__(self, name: str, title: str | None, description: str | None, parameters: probatio.Schema, server_url: str, config_entry: ConfigEntry, token_manager: TokenManager | None = None, annotations: llm.ToolAnnotations = ...) -> None: ...
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: llm.ToolInput, llm_context: llm.LLMContext) -> llm.ToolResult: ...

class ModelContextProtocolCoordinator(DataUpdateCoordinator[list[llm.Tool]]):
    config_entry: ConfigEntry
    token_manager: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, token_manager: TokenManager | None = None) -> None: ...
    @override
    async def _async_update_data(self) -> list[llm.Tool]: ...
