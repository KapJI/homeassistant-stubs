import abc
import voluptuous as vol
from . import intent as intent, selector as selector, service as service
from .singleton import singleton as singleton
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.calendar import SERVICE_GET_EVENTS as SERVICE_GET_EVENTS
from homeassistant.components.climate import INTENT_GET_TEMPERATURE as INTENT_GET_TEMPERATURE
from homeassistant.components.cover import INTENT_CLOSE_COVER as INTENT_CLOSE_COVER, INTENT_OPEN_COVER as INTENT_OPEN_COVER
from homeassistant.components.homeassistant import async_should_expose as async_should_expose
from homeassistant.components.intent import async_device_supports_timers as async_device_supports_timers
from homeassistant.components.weather import INTENT_GET_WEATHER as INTENT_GET_WEATHER
from homeassistant.const import ATTR_DOMAIN as ATTR_DOMAIN, ATTR_SERVICE as ATTR_SERVICE, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_SERVICE_REMOVED as EVENT_SERVICE_REMOVED
from homeassistant.core import Context as Context, Event as Event, HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.json import JsonObjectType as JsonObjectType
from typing import Any

ACTION_PARAMETERS_CACHE: HassKey[dict[str, dict[str, tuple[str | None, vol.Schema]]]]
LLM_API_ASSIST: str
BASE_PROMPT: str
DEFAULT_INSTRUCTIONS_PROMPT: str

@callback
def async_render_no_api_prompt(hass: HomeAssistant) -> str: ...
@callback
def _async_get_apis(hass: HomeAssistant) -> dict[str, API]: ...
@callback
def async_register_api(hass: HomeAssistant, api: API) -> Callable[[], None]: ...
async def async_get_api(hass: HomeAssistant, api_id: str, llm_context: LLMContext) -> APIInstance: ...
@callback
def async_get_apis(hass: HomeAssistant) -> list[API]: ...

@dataclass(slots=True)
class LLMContext:
    platform: str
    context: Context | None
    user_prompt: str | None
    language: str | None
    assistant: str | None
    device_id: str | None

@dataclass(slots=True)
class ToolInput:
    tool_name: str
    tool_args: dict[str, Any]

class Tool(metaclass=abc.ABCMeta):
    name: str
    description: str | None
    parameters: vol.Schema
    @abstractmethod
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> JsonObjectType: ...
    def __repr__(self) -> str: ...

@dataclass
class APIInstance:
    api: API
    api_prompt: str
    llm_context: LLMContext
    tools: list[Tool]
    custom_serializer: Callable[[Any], Any] | None = ...
    async def async_call_tool(self, tool_input: ToolInput) -> JsonObjectType: ...

@dataclass(slots=True, kw_only=True)
class API(ABC, metaclass=abc.ABCMeta):
    hass: HomeAssistant
    id: str
    name: str
    @abstractmethod
    async def async_get_api_instance(self, llm_context: LLMContext) -> APIInstance: ...

class IntentTool(Tool):
    name: Incomplete
    description: Incomplete
    extra_slots: Incomplete
    parameters: Incomplete
    def __init__(self, name: str, intent_handler: intent.IntentHandler) -> None: ...
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> JsonObjectType: ...

class AssistAPI(API):
    IGNORE_INTENTS: Incomplete
    cached_slugify: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_get_api_instance(self, llm_context: LLMContext) -> APIInstance: ...
    @callback
    def _async_get_api_prompt(self, llm_context: LLMContext, exposed_entities: dict | None) -> str: ...
    @callback
    def _async_get_tools(self, llm_context: LLMContext, exposed_entities: dict | None) -> list[Tool]: ...

def _get_exposed_entities(hass: HomeAssistant, assistant: str) -> dict[str, dict[str, Any]]: ...
def _selector_serializer(schema: Any) -> Any: ...
def _get_cached_action_parameters(hass: HomeAssistant, domain: str, action: str) -> tuple[str | None, vol.Schema]: ...

class ActionTool(Tool):
    _domain: Incomplete
    _action: Incomplete
    name: Incomplete
    def __init__(self, hass: HomeAssistant, domain: str, action: str) -> None: ...
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> JsonObjectType: ...

class ScriptTool(ActionTool):
    name: Incomplete
    def __init__(self, hass: HomeAssistant, script_entity_id: str) -> None: ...

class CalendarGetEventsTool(Tool):
    name: str
    description: str
    parameters: Incomplete
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> JsonObjectType: ...
