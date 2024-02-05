import abc
from _typeshed import Incomplete
from collections import deque
from homeassistant.core import Context as Context
from homeassistant.helpers.trace import TraceElement as TraceElement, script_execution_get as script_execution_get, trace_id_get as trace_id_get, trace_id_set as trace_id_set, trace_set_child_id as trace_set_child_id
from typing import Any

class BaseTrace(abc.ABC, metaclass=abc.ABCMeta):
    context: Context
    key: str
    run_id: str
    def as_dict(self) -> dict[str, Any]: ...
    @abc.abstractmethod
    def as_extended_dict(self) -> dict[str, Any]: ...
    @abc.abstractmethod
    def as_short_dict(self) -> dict[str, Any]: ...

class ActionTrace(BaseTrace):
    _domain: str | None
    _trace: Incomplete
    _config: Incomplete
    _blueprint_inputs: Incomplete
    context: Incomplete
    _error: Incomplete
    _state: str
    _script_execution: Incomplete
    run_id: Incomplete
    _timestamp_finish: Incomplete
    _timestamp_start: Incomplete
    key: Incomplete
    _dict: Incomplete
    _short_dict: Incomplete
    def __init__(self, item_id: str | None, config: dict[str, Any] | None, blueprint_inputs: dict[str, Any] | None, context: Context) -> None: ...
    def set_trace(self, trace: dict[str, deque[TraceElement]] | None) -> None: ...
    def set_error(self, ex: Exception) -> None: ...
    def finished(self) -> None: ...
    def as_extended_dict(self) -> dict[str, Any]: ...
    def as_short_dict(self) -> dict[str, Any]: ...

class RestoredTrace(BaseTrace):
    context: Incomplete
    key: Incomplete
    run_id: Incomplete
    _dict: Incomplete
    _short_dict: Incomplete
    def __init__(self, data: dict[str, Any]) -> None: ...
    def as_extended_dict(self) -> dict[str, Any]: ...
    def as_short_dict(self) -> dict[str, Any]: ...
