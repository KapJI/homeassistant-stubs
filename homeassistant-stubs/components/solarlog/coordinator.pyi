from . import SolarlogConfigEntry as SolarlogConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from solarlog_cli.solarlog_models import SolarlogData

_LOGGER: Incomplete

class SolarLogCoordinator(DataUpdateCoordinator[SolarlogData]):
    unique_id: Incomplete
    name: Incomplete
    host: Incomplete
    solarlog: Incomplete
    def __init__(self, hass: HomeAssistant, entry: SolarlogConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> SolarlogData: ...
    async def renew_authentication(self) -> bool: ...
