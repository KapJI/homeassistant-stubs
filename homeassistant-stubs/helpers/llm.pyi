import abc
import probatio
from . import frame as frame, intent as intent, selector as selector, service as service
from .deprecation import deprecated_function as deprecated_function
from .singleton import singleton as singleton
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable as Callable
from dataclasses import dataclass, field as dc_field
from homeassistant.const import ATTR_DOMAIN as ATTR_DOMAIN, ATTR_SERVICE as ATTR_SERVICE, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_SERVICE_REMOVED as EVENT_SERVICE_REMOVED
from homeassistant.core import Context as Context, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.json import JsonObjectType as JsonObjectType
from homeassistant.util.ulid import ulid_now as ulid_now
from typing import Any, override

ACTION_PARAMETERS_CACHE: HassKey[dict[str, dict[str, tuple[str | None, probatio.Schema]]]]
APIS_CACHE: HassKey[dict[str, API]]
LLM_API_ASSIST: str
TOOL_INTEGRATION_BREAKS_IN_HA_VERSION: str
DATE_TIME_PROMPT: str
DEFAULT_INSTRUCTIONS_PROMPT: str

@callback
def async_render_no_api_prompt(hass: HomeAssistant) -> str: ...
@callback
def _async_get_apis(hass: HomeAssistant) -> dict[str, API]: ...
@callback
def async_register_api(hass: HomeAssistant, api: API) -> Callable[[], None]: ...
async def async_get_api(hass: HomeAssistant, api_id: str | list[str], llm_context: LLMContext) -> APIInstance: ...
@callback
def async_get_apis(hass: HomeAssistant) -> list[API]: ...

@dataclass(slots=True)
class LLMContext:
    platform: str
    context: Context | None
    language: str | None
    assistant: str
    device_id: str | None

@dataclass(slots=True)
class ToolInput:
    tool_name: str
    tool_args: dict[str, Any]
    id: str = dc_field(default_factory=Incomplete)
    external: bool = ...

@dataclass(slots=True)
class ToolResult:
    data: JsonObjectType
    error: bool = ...

@dataclass(frozen=True, slots=True, kw_only=True)
class ToolAnnotations:
    read_only: bool = ...
    destructive: bool = ...
    idempotent: bool = ...
    open_world: bool = ...

class Tool(metaclass=abc.ABCMeta):
    name: str
    title: str | None
    description: str | None
    parameters: probatio.Schema
    annotations: ToolAnnotations
    integration: str | None
    @abstractmethod
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> ToolResult | JsonObjectType: ...
    @override
    def __repr__(self) -> str: ...

@dataclass
class APIInstance:
    api: API
    api_prompt: str
    llm_context: LLMContext
    tools: list[Tool]
    custom_serializer: Callable[[Any], Any] | None = ...
    def __post_init__(self) -> None: ...
    async def async_call_tool(self, tool_input: ToolInput) -> ToolResult: ...

@callback
def report_untagged_tool(tool: Tool, domain: str) -> None: ...
def _tool_integration_domain(tool: Tool) -> str | None: ...
def _integration_domain(module: str) -> str | None: ...

@dataclass(slots=True, kw_only=True)
class API(ABC, metaclass=abc.ABCMeta):
    hass: HomeAssistant
    id: str
    name: str
    @abstractmethod
    async def async_get_api_instance(self, llm_context: LLMContext) -> APIInstance: ...

@callback
def async_get_match_preferences(hass: HomeAssistant, llm_context: LLMContext) -> intent.MatchTargetsPreferences: ...

class IntentTool(Tool):
    name: Incomplete
    title: Incomplete
    integration: Incomplete
    annotations: Incomplete
    intent_type: Incomplete
    description: Incomplete
    extra_slots: Incomplete
    parameters: Incomplete
    def __init__(self, name: str, intent_handler: intent.IntentHandler, *, title: str | None = None, integration: str | None = None, annotations: ToolAnnotations = ...) -> None: ...
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> ToolResult: ...

class IntentResponseDict(dict):
    original: Incomplete
    def __init__(self, intent_response: Any) -> None: ...

class NamespacedTool(Tool):
    namespace: Incomplete
    name: Incomplete
    title: Incomplete
    description: Incomplete
    parameters: Incomplete
    annotations: Incomplete
    integration: Incomplete
    tool: Incomplete
    def __init__(self, namespace: str, tool: Tool) -> None: ...
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> ToolResult | JsonObjectType: ...

class MergedAPI(API):
    llm_apis: Incomplete
    def __init__(self, llm_apis: list[API]) -> None: ...
    @override
    async def async_get_api_instance(self, llm_context: LLMContext) -> APIInstance: ...
    def _custom_serializer(self, llm_apis: list[APIInstance]) -> Callable[[Any], Any] | None: ...

def selector_serializer(schema: Any) -> Any: ...
def _get_cached_action_parameters(hass: HomeAssistant, domain: str, action: str) -> tuple[str | None, probatio.Schema]: ...

class ActionTool(Tool):
    _domain: Incomplete
    _action: Incomplete
    name: Incomplete
    integration: Incomplete
    def __init__(self, hass: HomeAssistant, domain: str, action: str) -> None: ...
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: ToolInput, llm_context: LLMContext) -> ToolResult: ...
