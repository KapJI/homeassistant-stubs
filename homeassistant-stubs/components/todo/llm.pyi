from .const import DOMAIN as DOMAIN, TodoServices as TodoServices
from .intent import INTENT_LIST_ADD_ITEM as INTENT_LIST_ADD_ITEM, INTENT_LIST_COMPLETE_ITEM as INTENT_LIST_COMPLETE_ITEM, INTENT_LIST_REMOVE_ITEM as INTENT_LIST_REMOVE_ITEM
from _typeshed import Incomplete
from homeassistant.components.homeassistant import async_should_expose as async_should_expose
from homeassistant.components.llm import LLMTools as LLMTools
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import intent as intent
from homeassistant.helpers.llm import IntentTool as IntentTool, LLMContext as LLMContext, LLM_API_ASSIST as LLM_API_ASSIST, Tool as Tool, ToolInput as ToolInput
from homeassistant.util.json import JsonObjectType as JsonObjectType
from typing import override

LLM_INTENTS: Incomplete

class TodoGetItemsTool(Tool):
    name: str
    description: str
    parameters: Incomplete
    def __init__(self, todo_lists: list[str]) -> None: ...
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> JsonObjectType: ...

@callback
def async_get_tools(hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools | None: ...
