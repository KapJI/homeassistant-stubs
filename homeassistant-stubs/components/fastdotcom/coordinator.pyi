from .const import DEFAULT_INTERVAL as DEFAULT_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

type FastdotcomConfigEntry = ConfigEntry[FastdotcomDataUpdateCoordinator]
class FastdotcomDataUpdateCoordinator(DataUpdateCoordinator[float]):
    def __init__(self, hass: HomeAssistant, entry: FastdotcomConfigEntry) -> None: ...
    async def _async_update_data(self) -> float: ...
