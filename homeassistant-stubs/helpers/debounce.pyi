from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from logging import Logger
from typing import Any, Awaitable, Callable

class Debouncer:
    hass: Any = ...
    logger: Any = ...
    cooldown: Any = ...
    immediate: Any = ...
    def __init__(self, hass: HomeAssistant, logger: Logger, cooldown: float, immediate: bool, *, function: Union[Callable[..., Awaitable[Any]], None]=...) -> None: ...
    @property
    def function(self) -> Union[Callable[..., Awaitable[Any]], None]: ...
    @function.setter
    def function(self, function: Callable[..., Awaitable[Any]]) -> None: ...
    async def async_call(self) -> None: ...
    def async_cancel(self) -> None: ...
