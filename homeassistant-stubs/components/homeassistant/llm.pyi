from .exposed_entities import async_should_expose as async_should_expose
from _typeshed import Incomplete
from homeassistant.components.llm import LLMTools as LLMTools
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, async_rounded_state as async_rounded_state
from homeassistant.const import EntityStateAttribute as EntityStateAttribute
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import intent as intent
from homeassistant.helpers.llm import LLMContext as LLMContext, LLM_API_ASSIST as LLM_API_ASSIST, Tool as Tool, ToolInput as ToolInput
from homeassistant.util.json import JsonObjectType as JsonObjectType
from typing import Any, override

CALENDAR_DOMAIN: str
SCRIPT_DOMAIN: str
NO_ENTITIES_PROMPT: str
DYNAMIC_CONTEXT_PROMPT: str

@callback
def async_get_exposed_entities(hass: HomeAssistant, assistant: str, include_state: bool = True) -> dict[str, dict[str, Any]]: ...
def _live_context_match_error(match_result: intent.MatchTargetsResult, name_filter: str | None, area_filter: str | None, domain_filter: list[str] | None) -> str: ...

class GetLiveContextTool(Tool):
    name: str
    description: str
    parameters: Incomplete
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> JsonObjectType: ...

@callback
def async_get_tools(hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools | None: ...
