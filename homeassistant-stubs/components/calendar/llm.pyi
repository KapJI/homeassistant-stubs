from .const import DOMAIN as DOMAIN, SERVICE_GET_EVENTS as SERVICE_GET_EVENTS
from _typeshed import Incomplete
from homeassistant.components.homeassistant import async_should_expose as async_should_expose
from homeassistant.components.llm import LLMTools as LLMTools
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import intent as intent
from homeassistant.helpers.llm import LLMContext as LLMContext, LLM_API_ASSIST as LLM_API_ASSIST, Tool as Tool, ToolAnnotations as ToolAnnotations, ToolInput as ToolInput, ToolResult as ToolResult
from typing import override

class CalendarGetEventsTool(Tool):
    name: str
    title: str
    description: str
    annotations: Incomplete
    integration = DOMAIN
    parameters: Incomplete
    def __init__(self, calendars: list[str]) -> None: ...
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> ToolResult: ...

@callback
def async_get_tools(hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools | None: ...
