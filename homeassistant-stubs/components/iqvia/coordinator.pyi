from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

DEFAULT_SCAN_INTERVAL: Incomplete
type IqviaConfigEntry = ConfigEntry[dict[str, IqviaUpdateCoordinator]]

class IqviaUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: IqviaConfigEntry
    _update_method: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: IqviaConfigEntry, name: str, update_method: Callable[[], Coroutine[Any, Any, dict[str, Any]]]) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
