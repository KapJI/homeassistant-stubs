from . import PyNUTData as PyNUTData
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

@dataclass
class NutRuntimeData:
    coordinator: NutCoordinator
    data: PyNUTData
    unique_id: str
    user_available_commands: set[str]
type NutConfigEntry = ConfigEntry[NutRuntimeData]

class NutCoordinator(DataUpdateCoordinator[dict[str, str]]):
    config_entry: NutConfigEntry
    _data: Incomplete
    def __init__(self, hass: HomeAssistant, data: PyNUTData, config_entry: NutConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, str]: ...
