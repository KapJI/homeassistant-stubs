from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from kasa import SmartDevice as SmartDevice
from typing import Any

_LOGGER: Any
REQUEST_REFRESH_DELAY: float

class TPLinkDataUpdateCoordinator(DataUpdateCoordinator):
    device: Any
    update_children: bool
    def __init__(self, hass: HomeAssistant, device: SmartDevice) -> None: ...
    async def async_request_refresh_without_children(self) -> None: ...
    async def _async_update_data(self) -> None: ...
