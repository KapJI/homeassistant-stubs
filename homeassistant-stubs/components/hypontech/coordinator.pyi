from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from hyponcloud import HyponCloud as HyponCloud, OverviewData as OverviewData, PlantData as PlantData

@dataclass
class HypontechCoordinatorData:
    overview: OverviewData
    plants: dict[str, PlantData]
type HypontechConfigEntry = ConfigEntry[HypontechDataCoordinator]

class HypontechDataCoordinator(DataUpdateCoordinator[HypontechCoordinatorData]):
    config_entry: HypontechConfigEntry
    api: Incomplete
    account_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HypontechConfigEntry, api: HyponCloud, account_id: str) -> None: ...
    async def _async_update_data(self) -> HypontechCoordinatorData: ...
