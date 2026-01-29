from . import LeilSaunaConfigEntry as LeilSaunaConfigEntry
from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysaunum import SaunumClient as SaunumClient, SaunumData

_LOGGER: Incomplete

class LeilSaunaCoordinator(DataUpdateCoordinator[SaunumData]):
    config_entry: LeilSaunaConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: SaunumClient, config_entry: LeilSaunaConfigEntry) -> None: ...
    async def _async_update_data(self) -> SaunumData: ...
