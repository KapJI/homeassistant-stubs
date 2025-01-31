from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_ZONE as CONF_ZONE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from open_meteo import Forecast

type OpenMeteoConfigEntry = ConfigEntry[OpenMeteoDataUpdateCoordinator]
class OpenMeteoDataUpdateCoordinator(DataUpdateCoordinator[Forecast]):
    config_entry: OpenMeteoConfigEntry
    open_meteo: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OpenMeteoConfigEntry) -> None: ...
    async def _async_update_data(self) -> Forecast: ...
