import logging
from collections.abc import Awaitable
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, Callable, TypeVar

T = TypeVar('T')

class RenaultDataUpdateCoordinator(DataUpdateCoordinator[T]):
    access_denied: bool
    not_supported: bool
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, name: str, update_interval: timedelta, update_method: Callable[[], Awaitable[T]]) -> None: ...
    update_interval: Any
    async def _async_update_data(self) -> T: ...
    async def async_config_entry_first_refresh(self) -> None: ...
