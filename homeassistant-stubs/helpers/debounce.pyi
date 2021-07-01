from collections.abc import Awaitable
from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from logging import Logger
from typing import Any, Callable

class Debouncer:
    hass: Any
    logger: Any
    _function: Any
    cooldown: Any
    immediate: Any
    _timer_task: Any
    _execute_at_end_of_timer: bool
    _execute_lock: Any
    _job: Any
    def __init__(self, hass: HomeAssistant, logger: Logger, cooldown: float, immediate: bool, *, function: Union[Callable[..., Awaitable[Any]], None] = ...) -> None: ...
    @property
    def function(self) -> Union[Callable[..., Awaitable[Any]], None]: ...
    @function.setter
    def function(self, function: Callable[..., Awaitable[Any]]) -> None: ...
    async def async_call(self) -> None: ...
    async def _handle_timer_finish(self) -> None: ...
    def async_cancel(self) -> None: ...
    def _schedule_timer(self) -> None: ...
