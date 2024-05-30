from .const import NOTIFICATIONS_SCAN_INTERVAL as NOTIFICATIONS_SCAN_INTERVAL, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from ring_doorbell import Ring as Ring, RingDevices

_LOGGER: Incomplete

async def _call_api(hass: HomeAssistant, target: Callable[[Unpack[_Ts]], _R], *args: Unpack[_Ts], msg_suffix: str = '') -> _R: ...

class RingDataCoordinator(DataUpdateCoordinator[RingDevices]):
    ring_api: Incomplete
    first_call: bool
    def __init__(self, hass: HomeAssistant, ring_api: Ring) -> None: ...
    async def _async_update_data(self) -> RingDevices: ...

class RingNotificationsCoordinator(DataUpdateCoordinator[None]):
    ring_api: Incomplete
    def __init__(self, hass: HomeAssistant, ring_api: Ring) -> None: ...
    async def _async_update_data(self) -> None: ...
