from .const import CONF_LINE as CONF_LINE, CONF_STATION_ID as CONF_STATION_ID, CONF_STOP_ID as CONF_STOP_ID, DOMAIN as DOMAIN, LOGGER as LOGGER, SUBENTRY_TYPE_STOP as SUBENTRY_TYPE_STOP, SUBENTRY_TYPE_VELOV_STATION as SUBENTRY_TYPE_VELOV_STATION
from _typeshed import Incomplete
from data_grand_lyon_ha import DataGrandLyonClient as DataGrandLyonClient, TclPassage, VelovStation
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

@dataclass
class DataGrandLyonData:
    tcl_coordinator: DataGrandLyonTclCoordinator
    velov_coordinator: DataGrandLyonVelovCoordinator
type DataGrandLyonConfigEntry = ConfigEntry[DataGrandLyonData]

class DataGrandLyonTclCoordinator(DataUpdateCoordinator[dict[str, list[TclPassage]]]):
    config_entry: DataGrandLyonConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: DataGrandLyonConfigEntry, client: DataGrandLyonClient) -> None: ...
    async def _async_update_data(self) -> dict[str, list[TclPassage]]: ...

class DataGrandLyonVelovCoordinator(DataUpdateCoordinator[dict[str, VelovStation]]):
    config_entry: DataGrandLyonConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: DataGrandLyonConfigEntry, client: DataGrandLyonClient) -> None: ...
    async def _async_update_data(self) -> dict[str, VelovStation]: ...
