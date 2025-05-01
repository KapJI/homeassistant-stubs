import voluptuous as vol
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import AsyncGenerator, Awaitable, Callable
from contextlib import asynccontextmanager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.json import JsonObjectType as JsonObjectType
from mcp.client.session import ClientSession

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
TIMEOUT: int
TokenManager = Callable[[], Awaitable[str]]

@asynccontextmanager
async def mcp_client(url: str, token_manager: TokenManager | None = None) -> AsyncGenerator[ClientSession]: ...

class ModelContextProtocolTool(llm.Tool):
    name: Incomplete
    description: Incomplete
    parameters: Incomplete
    server_url: Incomplete
    token_manager: Incomplete
    def __init__(self, name: str, description: str | None, parameters: vol.Schema, server_url: str, token_manager: TokenManager | None = None) -> None: ...
    async def async_call(self, hass: HomeAssistant, tool_input: llm.ToolInput, llm_context: llm.LLMContext) -> JsonObjectType: ...

class ModelContextProtocolCoordinator(DataUpdateCoordinator[list[llm.Tool]]):
    config_entry: ConfigEntry
    token_manager: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, token_manager: TokenManager | None = None) -> None: ...
    async def _async_update_data(self) -> list[llm.Tool]: ...
