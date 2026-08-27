from . import LLMTools as LLMTools
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.llm import LLMContext as LLMContext, Tool as Tool, ToolInput as ToolInput
from homeassistant.util.json import JsonObjectType as JsonObjectType
from typing import override

class GetDateTimeTool(Tool):
    name: str
    description: str
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> JsonObjectType: ...

@callback
def async_get_tools(hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools: ...
