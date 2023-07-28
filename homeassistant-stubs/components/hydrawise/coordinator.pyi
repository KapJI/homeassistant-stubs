from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pydrawise.legacy import LegacyHydrawise as LegacyHydrawise

class HydrawiseDataUpdateCoordinator(DataUpdateCoordinator[None]):
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: LegacyHydrawise, scan_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> None: ...
