import asyncio
import voluptuous as vol
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.json import JsonObjectType as JsonObjectType
from mcp.client.session import ClientSession

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
TIMEOUT: int

@asynccontextmanager
async def mcp_client(url: str) -> AsyncGenerator[ClientSession]: ...

class ModelContextProtocolTool(llm.Tool):
    name: Incomplete
    description: Incomplete
    parameters: Incomplete
    session: Incomplete
    def __init__(self, name: str, description: str | None, parameters: vol.Schema, session: ClientSession) -> None: ...
    async def async_call(self, hass: HomeAssistant, tool_input: llm.ToolInput, llm_context: llm.LLMContext) -> JsonObjectType: ...

class ModelContextProtocolCoordinator(DataUpdateCoordinator[list[llm.Tool]]):
    config_entry: ConfigEntry
    _session: ClientSession | None
    _setup_error: Exception | None
    _stop: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _connect(self, connected: asyncio.Event, stop: asyncio.Event) -> None: ...
    async def close(self) -> None: ...
    async def _async_update_data(self) -> list[llm.Tool]: ...
