from .const import CONF_AZIMUTH as CONF_AZIMUTH, CONF_DAMPING as CONF_DAMPING, CONF_DECLINATION as CONF_DECLINATION, CONF_INVERTER_SIZE as CONF_INVERTER_SIZE, CONF_MODULES_POWER as CONF_MODULES_POWER, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from forecast_solar import Estimate
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

class ForecastSolarDataUpdateCoordinator(DataUpdateCoordinator[Estimate]):
    config_entry: ConfigEntry
    forecast: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> Estimate: ...
