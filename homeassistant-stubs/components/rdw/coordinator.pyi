from .const import CONF_LICENSE_PLATE as CONF_LICENSE_PLATE, DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from vehicle import Vehicle

type RDWConfigEntry = ConfigEntry[RDWDataUpdateCoordinator]
class RDWDataUpdateCoordinator(DataUpdateCoordinator[Vehicle]):
    config_entry: RDWConfigEntry
    _rdw: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RDWConfigEntry) -> None: ...
    async def _async_update_data(self) -> Vehicle: ...
