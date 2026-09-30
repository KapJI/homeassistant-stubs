from .const import DOMAIN as DOMAIN
from .timers import async_device_supports_timers as async_device_supports_timers
from _typeshed import Incomplete
from homeassistant.components.homeassistant import async_should_expose as async_should_expose
from homeassistant.components.llm import LLMTools as LLMTools
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import intent as intent
from homeassistant.helpers.llm import IntentTool as IntentTool, LLMContext as LLMContext, LLM_API_ASSIST as LLM_API_ASSIST, Tool as Tool, ToolAnnotations as ToolAnnotations

LLM_INTENTS: Incomplete
TIMER_INTENTS: Incomplete
INTENT_TITLES = LLM_INTENTS | TIMER_INTENTS
_CONTROL: Incomplete
_REPEATS: Incomplete
_ADDS: Incomplete
_READ_ONLY: Incomplete
INTENT_ANNOTATIONS: Incomplete
DEVICE_CONTROL_TOOL_USAGE_PROMPT: str

@callback
def async_get_tools(hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools | None: ...
