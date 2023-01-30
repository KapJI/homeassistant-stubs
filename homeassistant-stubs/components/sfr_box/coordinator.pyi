from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from sfrbox_api.bridge import SFRBox as SFRBox
from typing import Any, TypeVar

_LOGGER: Incomplete
_SCAN_INTERVAL: Incomplete
_T = TypeVar('_T')

class SFRDataUpdateCoordinator(DataUpdateCoordinator[_T]):
    box: Incomplete
    _method: Incomplete
    def __init__(self, hass: HomeAssistant, box: SFRBox, name: str, method: Callable[[SFRBox], Coroutine[Any, Any, _T]]) -> None: ...
    async def _async_update_data(self) -> _T: ...
