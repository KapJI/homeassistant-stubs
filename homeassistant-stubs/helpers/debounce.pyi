from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from logging import Logger
from typing import TypeVar

_R_co = TypeVar('_R_co', covariant=True)

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
    def __init__(self, hass: HomeAssistant, logger: Logger, *, cooldown: float, immediate: bool, function: Union[Callable[[], _R_co], None] = ...) -> None: ...
    @property
    def function(self) -> Union[Callable[[], _R_co], None]: ...
    @function.setter
    def function(self, function: Callable[[], _R_co]) -> None: ...
    async def async_call(self) -> None: ...
    async def _handle_timer_finish(self) -> None: ...
    def async_cancel(self) -> None: ...
    def _schedule_timer(self) -> None: ...
