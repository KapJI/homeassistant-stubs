import probatio
from .browse_media import SearchMedia as SearchMedia
from .const import ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, ATTR_MEDIA_SEARCH_QUERY as ATTR_MEDIA_SEARCH_QUERY, DOMAIN as DOMAIN, INTENT_MEDIA_NEXT as INTENT_MEDIA_NEXT, INTENT_MEDIA_PAUSE as INTENT_MEDIA_PAUSE, INTENT_MEDIA_PREVIOUS as INTENT_MEDIA_PREVIOUS, INTENT_MEDIA_UNPAUSE as INTENT_MEDIA_UNPAUSE, INTENT_PLAYER_MUTE as INTENT_PLAYER_MUTE, INTENT_PLAYER_UNMUTE as INTENT_PLAYER_UNMUTE, INTENT_SET_VOLUME as INTENT_SET_VOLUME, INTENT_SET_VOLUME_RELATIVE as INTENT_SET_VOLUME_RELATIVE, MediaPlayerEntityFeature as MediaPlayerEntityFeature, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA, SERVICE_SEARCH_MEDIA as SERVICE_SEARCH_MEDIA
from _typeshed import Incomplete
from homeassistant.components.homeassistant import async_should_expose as async_should_expose
from homeassistant.components.llm import LLMTools as LLMTools
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import intent as intent
from homeassistant.helpers.llm import IntentTool as IntentTool, LLMContext as LLMContext, LLM_API_ASSIST as LLM_API_ASSIST, Tool as Tool, ToolAnnotations as ToolAnnotations, ToolInput as ToolInput, ToolResult as ToolResult, async_get_match_preferences as async_get_match_preferences
from homeassistant.util.json import JsonValueType as JsonValueType
from typing import Any, override

LLM_INTENTS: Incomplete
_CONTROL: Incomplete
_CUMULATIVE: Incomplete
INTENT_ANNOTATIONS: Incomplete
SEARCH_PLAY_FEATURES: Incomplete
MAX_SEARCH_RESULTS: int
TARGET_SCHEMA: Incomplete

def _validate_args(schema: probatio.Schema, tool_args: dict[str, Any]) -> dict[str, Any]: ...
@callback
def _async_match_player(hass: HomeAssistant, llm_context: LLMContext, args: dict[str, Any]) -> State: ...

class MediaSearchTool(Tool):
    name: str
    title: str
    description: str
    parameters: Incomplete
    annotations: Incomplete
    integration = DOMAIN
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> ToolResult: ...

class MediaPlayTool(Tool):
    name: str
    title: str
    description: str
    parameters: Incomplete
    integration = DOMAIN
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> ToolResult: ...

@callback
def async_get_tools(hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools | None: ...
