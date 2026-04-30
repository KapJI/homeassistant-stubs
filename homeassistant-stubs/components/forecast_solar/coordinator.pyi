from .const import CONF_AZIMUTH as CONF_AZIMUTH, CONF_DAMPING_EVENING as CONF_DAMPING_EVENING, CONF_DAMPING_MORNING as CONF_DAMPING_MORNING, CONF_DECLINATION as CONF_DECLINATION, CONF_INVERTER_SIZE as CONF_INVERTER_SIZE, CONF_MODULES_POWER as CONF_MODULES_POWER, DEFAULT_DAMPING as DEFAULT_DAMPING, DOMAIN as DOMAIN, LOGGER as LOGGER, SUBENTRY_TYPE_PLANE as SUBENTRY_TYPE_PLANE
from forecast_solar import Estimate, ForecastSolar
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

type ForecastSolarConfigEntry = ConfigEntry[ForecastSolarDataUpdateCoordinator]
class ForecastSolarDataUpdateCoordinator(DataUpdateCoordinator[Estimate]):
    config_entry: ForecastSolarConfigEntry
    forecast: ForecastSolar
    def __init__(self, hass: HomeAssistant, entry: ForecastSolarConfigEntry) -> None: ...
    async def _async_update_data(self) -> Estimate: ...
