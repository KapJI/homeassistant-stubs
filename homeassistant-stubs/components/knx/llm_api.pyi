import probatio
from .const import DOMAIN as DOMAIN
from .knx_module import KNXModule as KNXModule
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass, field as dc_field
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from homeassistant.util.json import JsonObjectType as JsonObjectType
from knx_telegram_store import TelegramStore as TelegramStore
from typing import Any, NamedTuple, override
from xknxproject.models import KNXProject as KNXProjectModel

LLM_API_ID = DOMAIN
LLM_API_NAME: str
API_PROMPT: str
type _ToolFunc = Callable[['KNXModule', Any], Awaitable[Any]]

class _ToolSpec(NamedTuple):
    name: str
    title: str
    description: str
    parameters: probatio.Schema
    func: _ToolFunc
    annotations: llm.ToolAnnotations

_READ_ONLY: Incomplete
_BUS_PROBE: Incomplete
_BUS_WRITE: Incomplete
_MAX_RESULT_ITEMS: int
_FIELD_BOUNDS: dict[str, Any]
_PAGINATION_MARKERS: dict[Any, Any]

def _field_description(input_type: type, name: str) -> str | None: ...
def _apply_field_descriptions(schema: probatio.Schema, input_type: type) -> None: ...
def _schema_from_dataclass(input_type: type) -> probatio.Schema: ...
def _paginate(items: list[Any], args: Mapping[str, Any], key: str) -> dict[str, Any]: ...
def _json_safe(value: Any) -> Any: ...
def _serialize(result: Any) -> JsonObjectType: ...

class KNXTool(llm.Tool):
    name: Incomplete
    title: Incomplete
    description: Incomplete
    parameters: Incomplete
    annotations: Incomplete
    integration: Incomplete
    _knx: Incomplete
    _func: Incomplete
    def __init__(self, knx: KNXModule, spec: _ToolSpec) -> None: ...
    @override
    async def async_call(self, hass: HomeAssistant, tool_input: llm.ToolInput, llm_context: llm.LLMContext) -> llm.ToolResult: ...

def _require_store(knx: KNXModule) -> TelegramStore: ...
async def _require_project(knx: KNXModule) -> KNXProjectModel: ...
def _store_func(lib_func: Callable, *, takes_input: bool = True) -> _ToolFunc: ...
def _project_func(lib_func: Callable, *, takes_input: bool = True, positional: tuple[str, ...] = ()) -> _ToolFunc: ...
def _dpt_func(lib_func: Callable, *, takes_input: bool = True, positional: tuple[str, ...] = ()) -> _ToolFunc: ...
def _address_order(address: str) -> tuple[int, ...] | tuple[()]: ...
def _last_values_func() -> _ToolFunc: ...
def _topology_func() -> _ToolFunc: ...
def _xknx_func(lib_func: Callable, *, takes_input: bool = True) -> _ToolFunc: ...
def _tool_specs() -> list[_ToolSpec]: ...
def _build_tools(knx: KNXModule) -> list[llm.Tool]: ...

@dataclass(kw_only=True)
class KNXLLMAPI(llm.API):
    knx: KNXModule
    _tools: list[llm.Tool] = dc_field(init=False)
    def __post_init__(self) -> None: ...
    @override
    async def async_get_api_instance(self, llm_context: llm.LLMContext) -> llm.APIInstance: ...

@callback
def async_register_llm_api(hass: HomeAssistant, knx: KNXModule) -> CALLBACK_TYPE: ...
