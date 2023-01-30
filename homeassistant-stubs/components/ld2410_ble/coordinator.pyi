from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from ld2410_ble import LD2410BLE as LD2410BLE, LD2410BLEState as LD2410BLEState

_LOGGER: Incomplete

class LD2410BLECoordinator(DataUpdateCoordinator[None]):
    _ld2410_ble: Incomplete
    connected: bool
    def __init__(self, hass: HomeAssistant, ld2410_ble: LD2410BLE) -> None: ...
    def _async_handle_update(self, state: LD2410BLEState) -> None: ...
    def _async_handle_disconnect(self) -> None: ...
