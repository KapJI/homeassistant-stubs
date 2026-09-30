from . import LLMTools as LLMTools
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.llm import LLMContext as LLMContext, Tool as Tool, ToolAnnotations as ToolAnnotations, ToolInput as ToolInput, ToolResult as ToolResult
from typing import override

class GetDateTimeTool(Tool):
    name: str
    title: str
    description: str
    annotations: Incomplete
    integration = DOMAIN
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> ToolResult: ...

@callback
def async_get_tools(hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools: ...
