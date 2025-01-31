from .const import UPDATE_SECONDS as UPDATE_SECONDS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from py_dormakaba_dkey import DKEYLock as DKEYLock

_LOGGER: Incomplete
type DormakabaDkeyConfigEntry = ConfigEntry[DormakabaDkeyCoordinator]

class DormakabaDkeyCoordinator(DataUpdateCoordinator[None]):
    lock: Incomplete
    def __init__(self, hass: HomeAssistant, entry: DormakabaDkeyConfigEntry, lock: DKEYLock) -> None: ...
    async def _async_update_data(self) -> None: ...
