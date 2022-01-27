from collections.abc import Awaitable, Callable as Callable
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Any
NEVER_TIME: Any
ACTIVE_UPDATES_INTERVAL: int

class LookinPushCoordinator:
    last_update: Any
    name: Any
    def __init__(self, name: str) -> None: ...
    def update(self) -> None: ...
    def active(self, interval: timedelta) -> bool: ...

class LookinDataUpdateCoordinator(DataUpdateCoordinator):
    push_coordinator: Any
    def __init__(self, hass: HomeAssistant, push_coordinator: LookinPushCoordinator, name: str, update_interval: Union[timedelta, None] = ..., update_method: Union[Callable[[], Awaitable[dict]], None] = ...) -> None: ...
    def async_set_updated_data(self, data: dict) -> None: ...
    async def _async_update_data(self) -> dict: ...
