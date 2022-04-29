from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from logging import Logger
from typing import Any

class Debouncer:
    hass: Incomplete
    logger: Incomplete
    _function: Incomplete
    cooldown: Incomplete
    immediate: Incomplete
    _timer_task: Incomplete
    _execute_at_end_of_timer: bool
    _execute_lock: Incomplete
    _job: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, cooldown: float, immediate: bool, function: Union[Callable[..., Awaitable[Any]], None] = ...) -> None: ...
    @property
    def function(self) -> Union[Callable[..., Awaitable[Any]], None]: ...
    @function.setter
    def function(self, function: Callable[..., Awaitable[Any]]) -> None: ...
    async def async_call(self) -> None: ...
    async def _handle_timer_finish(self) -> None: ...
    def async_cancel(self) -> None: ...
    def _schedule_timer(self) -> None: ...
