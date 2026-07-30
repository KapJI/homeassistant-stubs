from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.homeassistant import async_should_expose as async_should_expose
from homeassistant.components.llm import LLMTools as LLMTools
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers.llm import ActionTool as ActionTool, LLMContext as LLMContext, LLM_API_ASSIST as LLM_API_ASSIST, Tool as Tool

class ScriptTool(ActionTool):
    name: Incomplete
    description: Incomplete
    def __init__(self, hass: HomeAssistant, script_entity_id: str) -> None: ...

@callback
def async_get_tools(hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools | None: ...
