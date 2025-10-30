from .const import DOMAIN as DOMAIN
from .server import create_server as create_server
from .session import Session as Session
from .types import MCPServerConfigEntry as MCPServerConfigEntry
from _typeshed import Incomplete
from aiohttp import web
from anyio.streams.memory import MemoryObjectReceiveStream as MemoryObjectReceiveStream, MemoryObjectSendStream as MemoryObjectSendStream
from dataclasses import dataclass
from homeassistant.components import conversation as conversation
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.const import CONF_LLM_HASS_API as CONF_LLM_HASS_API
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import llm as llm
from mcp.server import InitializationOptions as InitializationOptions, Server as Server
from mcp.shared.message import SessionMessage

_LOGGER: Incomplete
STREAMABLE_API: str
TIMEOUT: int
CONTENT_TYPE_JSON: str
SSE_API: Incomplete
MESSAGES_API: Incomplete

@callback
def async_register(hass: HomeAssistant) -> None: ...
def async_get_config_entry(hass: HomeAssistant) -> MCPServerConfigEntry: ...

@dataclass
class Streams:
    read_stream: MemoryObjectReceiveStream[SessionMessage | Exception]
    read_stream_writer: MemoryObjectSendStream[SessionMessage | Exception]
    write_stream: MemoryObjectSendStream[SessionMessage]
    write_stream_reader: MemoryObjectReceiveStream[SessionMessage]

def create_streams() -> Streams: ...
async def create_mcp_server(hass: HomeAssistant, context: Context, entry: MCPServerConfigEntry) -> tuple[Server, InitializationOptions]: ...

class ModelContextProtocolSSEView(HomeAssistantView):
    name: Incomplete
    url = SSE_API
    async def get(self, request: web.Request) -> web.StreamResponse: ...

class ModelContextProtocolMessagesView(HomeAssistantView):
    name: Incomplete
    url = MESSAGES_API
    async def post(self, request: web.Request, session_id: str) -> web.StreamResponse: ...

class ModelContextProtocolStreamableView(HomeAssistantView):
    name: Incomplete
    url = STREAMABLE_API
    async def get(self, request: web.Request) -> web.StreamResponse: ...
    async def post(self, request: web.Request) -> web.StreamResponse: ...
