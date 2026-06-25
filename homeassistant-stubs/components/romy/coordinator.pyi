from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from romy import RomyRobot as RomyRobot
from typing import override

type RomyConfigEntry = ConfigEntry[RomyVacuumCoordinator]
class RomyVacuumCoordinator(DataUpdateCoordinator[None]):
    config_entry: RomyConfigEntry
    romy: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RomyConfigEntry, romy: RomyRobot) -> None: ...
    @override
    async def _async_update_data(self) -> None: ...
