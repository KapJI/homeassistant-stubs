from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from sfrbox_api.bridge import SFRBox as SFRBox
from typing import Any

_LOGGER: Incomplete
_SCAN_INTERVAL: Incomplete

class SFRDataUpdateCoordinator[_DataT](DataUpdateCoordinator[_DataT | None]):
    config_entry: ConfigEntry
    box: Incomplete
    _method: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, box: SFRBox, name: str, method: Callable[[SFRBox], Coroutine[Any, Any, _DataT | None]]) -> None: ...
    async def _async_update_data(self) -> _DataT | None: ...
