import abc
import asyncio
import voluptuous as vol
from .core import HomeAssistant as HomeAssistant, callback as callback
from .exceptions import HomeAssistantError as HomeAssistantError
from collections.abc import Mapping
from typing import Any, TypedDict

RESULT_TYPE_FORM: str
RESULT_TYPE_CREATE_ENTRY: str
RESULT_TYPE_ABORT: str
RESULT_TYPE_EXTERNAL_STEP: str
RESULT_TYPE_EXTERNAL_STEP_DONE: str
RESULT_TYPE_SHOW_PROGRESS: str
RESULT_TYPE_SHOW_PROGRESS_DONE: str
EVENT_DATA_ENTRY_FLOW_PROGRESSED: str

class FlowError(HomeAssistantError): ...
class UnknownHandler(FlowError): ...
class UnknownFlow(FlowError): ...
class UnknownStep(FlowError): ...

class AbortFlow(FlowError):
    reason: Any
    description_placeholders: Any
    def __init__(self, reason: str, description_placeholders: Union[dict, None] = ...) -> None: ...

class FlowResult(TypedDict):
    version: int
    type: str
    flow_id: str
    handler: str
    title: str
    data: Mapping[str, Any]
    step_id: str
    data_schema: vol.Schema
    extra: str
    required: bool
    errors: Union[dict[str, str], None]
    description: Union[str, None]
    description_placeholders: Union[dict[str, Any], None]
    progress_action: str
    url: str
    reason: str
    context: dict[str, Any]
    result: Any
    last_step: Union[bool, None]
    options: Mapping[str, Any]

class FlowManager(abc.ABC, metaclass=abc.ABCMeta):
    hass: Any
    _initializing: Any
    _initialize_tasks: Any
    _progress: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_wait_init_flow_finish(self, handler: str) -> None: ...
    @abc.abstractmethod
    async def async_create_flow(self, handler_key: Any, *, context: Union[dict[str, Any], None] = ..., data: Union[dict[str, Any], None] = ...) -> FlowHandler: ...
    @abc.abstractmethod
    async def async_finish_flow(self, flow: FlowHandler, result: FlowResult) -> FlowResult: ...
    async def async_post_init(self, flow: FlowHandler, result: FlowResult) -> None: ...
    def async_progress(self, include_uninitialized: bool = ...) -> list[FlowResult]: ...
    async def async_init(self, handler: str, *, context: Union[dict[str, Any], None] = ..., data: Any = ...) -> FlowResult: ...
    async def _async_init(self, init_done: asyncio.Future, handler: str, context: dict, data: Any) -> tuple[FlowHandler, FlowResult]: ...
    async def async_shutdown(self) -> None: ...
    async def async_configure(self, flow_id: str, user_input: Union[dict, None] = ...) -> FlowResult: ...
    def async_abort(self, flow_id: str) -> None: ...
    async def _async_handle_step(self, flow: Any, step_id: str, user_input: Union[dict, None], step_done: Union[asyncio.Future, None] = ...) -> FlowResult: ...

class FlowHandler:
    cur_step: Union[dict[str, str], None]
    flow_id: str
    hass: HomeAssistant
    handler: str
    context: dict[str, Any]
    init_step: str
    VERSION: int
    @property
    def source(self) -> Union[str, None]: ...
    @property
    def show_advanced_options(self) -> bool: ...
    def async_show_form(self, step_id: str, *, data_schema: vol.Schema = ..., errors: Union[dict[str, str], None] = ..., description_placeholders: Union[dict[str, Any], None] = ..., last_step: Union[bool, None] = ...) -> FlowResult: ...
    def async_create_entry(self, title: str, data: Mapping[str, Any], *, description: Union[str, None] = ..., description_placeholders: Union[dict, None] = ...) -> FlowResult: ...
    def async_abort(self, reason: str, *, description_placeholders: Union[dict, None] = ...) -> FlowResult: ...
    def async_external_step(self, step_id: str, url: str, *, description_placeholders: Union[dict, None] = ...) -> FlowResult: ...
    def async_external_step_done(self, next_step_id: str) -> FlowResult: ...
    def async_show_progress(self, step_id: str, progress_action: str, *, description_placeholders: Union[dict, None] = ...) -> FlowResult: ...
    def async_show_progress_done(self, next_step_id: str) -> FlowResult: ...

def _create_abort_data(flow_id: str, handler: str, reason: str, description_placeholders: Union[dict, None] = ...) -> FlowResult: ...
