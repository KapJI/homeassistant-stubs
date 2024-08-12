import abc
import asyncio
import voluptuous as vol
from .core import HomeAssistant as HomeAssistant, callback as callback
from .exceptions import HomeAssistantError as HomeAssistantError
from .helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from .helpers.frame import report as report
from .loader import async_suggest_report_issue as async_suggest_report_issue
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Container, Hashable, Iterable, Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Generic, Required, TypedDict
from typing_extensions import TypeVar

_LOGGER: Incomplete

class FlowResultType(StrEnum):
    FORM = 'form'
    CREATE_ENTRY = 'create_entry'
    ABORT = 'abort'
    EXTERNAL_STEP = 'external'
    EXTERNAL_STEP_DONE = 'external_done'
    SHOW_PROGRESS = 'progress'
    SHOW_PROGRESS_DONE = 'progress_done'
    MENU = 'menu'

_DEPRECATED_RESULT_TYPE_FORM: Incomplete
_DEPRECATED_RESULT_TYPE_CREATE_ENTRY: Incomplete
_DEPRECATED_RESULT_TYPE_ABORT: Incomplete
_DEPRECATED_RESULT_TYPE_EXTERNAL_STEP: Incomplete
_DEPRECATED_RESULT_TYPE_EXTERNAL_STEP_DONE: Incomplete
_DEPRECATED_RESULT_TYPE_SHOW_PROGRESS: Incomplete
_DEPRECATED_RESULT_TYPE_SHOW_PROGRESS_DONE: Incomplete
_DEPRECATED_RESULT_TYPE_MENU: Incomplete
EVENT_DATA_ENTRY_FLOW_PROGRESSED: str
FLOW_NOT_COMPLETE_STEPS: Incomplete
STEP_ID_OPTIONAL_STEPS: Incomplete
_FlowResultT = TypeVar('_FlowResultT', bound='FlowResult[Any]', default='FlowResult')
_HandlerT = TypeVar('_HandlerT', default=str)

@dataclass(slots=True)
class BaseServiceInfo: ...
class FlowError(HomeAssistantError): ...
class UnknownHandler(FlowError): ...
class UnknownFlow(FlowError): ...
class UnknownStep(FlowError): ...

class InvalidData(vol.Invalid):
    schema_errors: Incomplete
    def __init__(self, message: str, path: list[Hashable] | None, error_message: str | None, schema_errors: dict[str, Any], **kwargs: Any) -> None: ...

class AbortFlow(FlowError):
    reason: Incomplete
    description_placeholders: Incomplete
    def __init__(self, reason: str, description_placeholders: Mapping[str, str] | None = None) -> None: ...

class FlowResult(TypedDict, Generic[_HandlerT], total=False):
    context: dict[str, Any]
    data_schema: vol.Schema | None
    data: Mapping[str, Any]
    description_placeholders: Mapping[str, str | None] | None
    description: str | None
    errors: dict[str, str] | None
    extra: str
    flow_id: Required[str]
    handler: Required[_HandlerT]
    last_step: bool | None
    menu_options: Container[str]
    preview: str | None
    progress_action: str
    progress_task: asyncio.Task[Any] | None
    reason: str
    required: bool
    result: Any
    step_id: str
    title: str
    translation_domain: str
    type: FlowResultType
    url: str

def _map_error_to_schema_errors(schema_errors: dict[str, Any], error: vol.Invalid, data_schema: vol.Schema) -> None: ...

class FlowManager(abc.ABC, Generic[_FlowResultT, _HandlerT], metaclass=abc.ABCMeta):
    _flow_result: type[_FlowResultT]
    hass: Incomplete
    _preview: Incomplete
    _progress: Incomplete
    _handler_progress_index: Incomplete
    _init_data_process_index: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @abc.abstractmethod
    async def async_create_flow(self, handler_key: _HandlerT, *, context: dict[str, Any] | None = None, data: dict[str, Any] | None = None) -> FlowHandler[_FlowResultT, _HandlerT]: ...
    @abc.abstractmethod
    async def async_finish_flow(self, flow: FlowHandler[_FlowResultT, _HandlerT], result: _FlowResultT) -> _FlowResultT: ...
    async def async_post_init(self, flow: FlowHandler[_FlowResultT, _HandlerT], result: _FlowResultT) -> None: ...
    def async_has_matching_flow(self, handler: _HandlerT, match_context: dict[str, Any], data: Any) -> bool: ...
    def async_get(self, flow_id: str) -> _FlowResultT: ...
    def async_progress(self, include_uninitialized: bool = False) -> list[_FlowResultT]: ...
    def async_progress_by_handler(self, handler: _HandlerT, include_uninitialized: bool = False, match_context: dict[str, Any] | None = None) -> list[_FlowResultT]: ...
    def async_progress_by_init_data_type(self, init_data_type: type, matcher: Callable[[Any], bool], include_uninitialized: bool = False) -> list[_FlowResultT]: ...
    def _async_progress_by_handler(self, handler: _HandlerT, match_context: dict[str, Any] | None) -> list[FlowHandler[_FlowResultT, _HandlerT]]: ...
    async def async_init(self, handler: _HandlerT, *, context: dict[str, Any] | None = None, data: Any = None) -> _FlowResultT: ...
    async def async_configure(self, flow_id: str, user_input: dict | None = None) -> _FlowResultT: ...
    async def _async_configure(self, flow_id: str, user_input: dict | None = None) -> _FlowResultT: ...
    def async_abort(self, flow_id: str) -> None: ...
    def _async_add_flow_progress(self, flow: FlowHandler[_FlowResultT, _HandlerT]) -> None: ...
    def _async_remove_flow_from_index(self, flow: FlowHandler[_FlowResultT, _HandlerT]) -> None: ...
    def _async_remove_flow_progress(self, flow_id: str) -> None: ...
    async def _async_handle_step(self, flow: FlowHandler[_FlowResultT, _HandlerT], step_id: str, user_input: dict | BaseServiceInfo | None) -> _FlowResultT: ...
    def _raise_if_step_does_not_exist(self, flow: FlowHandler[_FlowResultT, _HandlerT], step_id: str) -> None: ...
    async def _async_setup_preview(self, flow: FlowHandler[_FlowResultT, _HandlerT]) -> None: ...
    def _async_flow_handler_to_flow_result(self, flows: Iterable[FlowHandler[_FlowResultT, _HandlerT]], include_uninitialized: bool) -> list[_FlowResultT]: ...

class FlowHandler(Generic[_FlowResultT, _HandlerT]):
    _flow_result: type[_FlowResultT]
    cur_step: _FlowResultT | None
    flow_id: str
    hass: HomeAssistant
    handler: _HandlerT
    context: dict[str, Any]
    init_step: str
    init_data: Any
    VERSION: int
    MINOR_VERSION: int
    __progress_task: asyncio.Task[Any] | None
    __no_progress_task_reported: bool
    deprecated_show_progress: bool
    @property
    def source(self) -> str | None: ...
    @property
    def show_advanced_options(self) -> bool: ...
    def add_suggested_values_to_schema(self, data_schema: vol.Schema, suggested_values: Mapping[str, Any] | None) -> vol.Schema: ...
    def async_show_form(self, *, step_id: str | None = None, data_schema: vol.Schema | None = None, errors: dict[str, str] | None = None, description_placeholders: Mapping[str, str | None] | None = None, last_step: bool | None = None, preview: str | None = None) -> _FlowResultT: ...
    def async_create_entry(self, *, title: str | None = None, data: Mapping[str, Any], description: str | None = None, description_placeholders: Mapping[str, str] | None = None) -> _FlowResultT: ...
    def async_abort(self, *, reason: str, description_placeholders: Mapping[str, str] | None = None) -> _FlowResultT: ...
    def async_external_step(self, *, step_id: str | None = None, url: str, description_placeholders: Mapping[str, str] | None = None) -> _FlowResultT: ...
    def async_external_step_done(self, *, next_step_id: str) -> _FlowResultT: ...
    def async_show_progress(self, *, step_id: str | None = None, progress_action: str, description_placeholders: Mapping[str, str] | None = None, progress_task: asyncio.Task[Any] | None = None) -> _FlowResultT: ...
    def async_show_progress_done(self, *, next_step_id: str) -> _FlowResultT: ...
    def async_show_menu(self, *, step_id: str | None = None, menu_options: Container[str], description_placeholders: Mapping[str, str] | None = None) -> _FlowResultT: ...
    def async_remove(self) -> None: ...
    @staticmethod
    async def async_setup_preview(hass: HomeAssistant) -> None: ...
    def async_cancel_progress_task(self) -> None: ...
    def async_get_progress_task(self) -> asyncio.Task[Any] | None: ...
    def async_set_progress_task(self, progress_task: asyncio.Task[Any]) -> None: ...

class SectionConfig(TypedDict, total=False):
    collapsed: bool

class section:
    CONFIG_SCHEMA: Incomplete
    schema: Incomplete
    options: Incomplete
    def __init__(self, schema: vol.Schema, options: SectionConfig | None = None) -> None: ...
    def __call__(self, value: Any) -> Any: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
