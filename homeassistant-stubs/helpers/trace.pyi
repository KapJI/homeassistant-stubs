from .typing import TemplateVarsType as TemplateVarsType
from _typeshed import Incomplete
from collections import deque
from collections.abc import Callable as Callable, Generator
from contextvars import ContextVar
from homeassistant.core import ServiceResponse as ServiceResponse
from typing import Any

class TraceElement:
    __slots__: Incomplete
    _child_key: Incomplete
    _child_run_id: Incomplete
    _error: Incomplete
    path: Incomplete
    _result: Incomplete
    reuse_by_child: bool
    _timestamp: Incomplete
    _variables: Incomplete
    def __init__(self, variables: TemplateVarsType, path: str) -> None: ...
    def __repr__(self) -> str: ...
    def set_child_id(self, child_key: str, child_run_id: str) -> None: ...
    def set_error(self, ex: Exception) -> None: ...
    def set_result(self, **kwargs: Any) -> None: ...
    def update_result(self, **kwargs: Any) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...

trace_cv: ContextVar[dict[str, deque[TraceElement]] | None]
trace_stack_cv: ContextVar[list[TraceElement] | None]
trace_path_stack_cv: ContextVar[list[str] | None]
variables_cv: ContextVar[Any | None]
trace_id_cv: ContextVar[tuple[str, str] | None]
script_execution_cv: ContextVar[StopReason | None]

def trace_id_set(trace_id: tuple[str, str]) -> None: ...
def trace_id_get() -> tuple[str, str] | None: ...
def trace_stack_push(trace_stack_var: ContextVar, node: Any) -> None: ...
def trace_stack_pop(trace_stack_var: ContextVar) -> None: ...
def trace_stack_top(trace_stack_var: ContextVar) -> Any | None: ...
def trace_path_push(suffix: str | list[str]) -> int: ...
def trace_path_pop(count: int) -> None: ...
def trace_path_get() -> str: ...
def trace_append_element(trace_element: TraceElement, maxlen: int | None = ...) -> None: ...
def trace_get(clear: bool = ...) -> dict[str, deque[TraceElement]] | None: ...
def trace_clear() -> None: ...
def trace_set_child_id(child_key: str, child_run_id: str) -> None: ...
def trace_set_result(**kwargs: Any) -> None: ...
def trace_update_result(**kwargs: Any) -> None: ...

class StopReason:
    script_execution: str | None
    response: ServiceResponse

def script_execution_set(reason: str, response: ServiceResponse = ...) -> None: ...
def script_execution_get() -> str | None: ...
def trace_path(suffix: str | list[str]) -> Generator: ...
def async_trace_path(suffix: str | list[str]) -> Callable: ...
