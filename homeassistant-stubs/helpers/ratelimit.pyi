from _typeshed import Incomplete
from collections.abc import Callable as Callable, Hashable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

_LOGGER: Incomplete

class KeyedRateLimit:
    hass: Incomplete
    _last_triggered: Incomplete
    _rate_limit_timers: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_has_timer(self, key: Hashable) -> bool: ...
    def async_triggered(self, key: Hashable, now: float | None = None) -> None: ...
    def async_cancel_timer(self, key: Hashable) -> None: ...
    def async_remove(self) -> None: ...
    def async_schedule_action[*_Ts](self, key: Hashable, rate_limit: float | None, now: float, action: Callable[[Unpack[_Ts]], None], *args: Unpack[_Ts]) -> float | None: ...
