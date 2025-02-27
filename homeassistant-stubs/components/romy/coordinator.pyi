from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from romy import RomyRobot as RomyRobot

class RomyVacuumCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    hass: Incomplete
    romy: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, romy: RomyRobot) -> None: ...
    async def _async_update_data(self) -> None: ...
