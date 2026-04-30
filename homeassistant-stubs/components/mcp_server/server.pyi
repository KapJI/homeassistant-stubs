from .const import STATELESS_LLM_API as STATELESS_LLM_API
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from mcp import types
from mcp.server import Server
from typing import Any

_LOGGER: Incomplete
SNAPSHOT_RESOURCE_URI: str
SNAPSHOT_RESOURCE_URL: Incomplete
SNAPSHOT_RESOURCE_MIME_TYPE: str
LIVE_CONTEXT_TOOL_NAME: str

def _has_live_context_tool(llm_api: llm.APIInstance) -> bool: ...
def _format_tool(tool: llm.Tool, custom_serializer: Callable[[Any], Any] | None) -> types.Tool: ...
async def create_server(hass: HomeAssistant, llm_api_id: str | list[str], llm_context: llm.LLMContext) -> Server: ...
