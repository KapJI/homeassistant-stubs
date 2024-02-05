from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from kasa import SmartDevice as SmartDevice

_LOGGER: Incomplete
REQUEST_REFRESH_DELAY: float

class TPLinkDataUpdateCoordinator(DataUpdateCoordinator[None]):
    device: Incomplete
    def __init__(self, hass: HomeAssistant, device: SmartDevice, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> None: ...
