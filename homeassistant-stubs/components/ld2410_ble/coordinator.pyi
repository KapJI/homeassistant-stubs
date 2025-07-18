from .const import DOMAIN as DOMAIN
from .models import LD2410BLEConfigEntry as LD2410BLEConfigEntry
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from ld2410_ble import LD2410BLE as LD2410BLE, LD2410BLEState as LD2410BLEState

_LOGGER: Incomplete
NEVER_TIME: float
DEBOUNCE_SECONDS: float

class LD2410BLECoordinator(DataUpdateCoordinator[None]):
    config_entry: LD2410BLEConfigEntry
    _ld2410_ble: Incomplete
    connected: bool
    _last_update_time: Incomplete
    _debounce_cancel: CALLBACK_TYPE | None
    _debounced_update_job: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: LD2410BLEConfigEntry, ld2410_ble: LD2410BLE) -> None: ...
    @callback
    def _async_handle_debounced_update(self, _now: datetime) -> None: ...
    @callback
    def _async_handle_update(self, state: LD2410BLEState) -> None: ...
    @callback
    def _async_handle_disconnect(self) -> None: ...
    async def async_shutdown(self) -> None: ...
