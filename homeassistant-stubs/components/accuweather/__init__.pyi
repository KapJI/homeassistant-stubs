from .const import DOMAIN as DOMAIN
from .coordinator import AccuWeatherConfigEntry as AccuWeatherConfigEntry, AccuWeatherDailyForecastDataUpdateCoordinator as AccuWeatherDailyForecastDataUpdateCoordinator, AccuWeatherData as AccuWeatherData, AccuWeatherHourlyForecastDataUpdateCoordinator as AccuWeatherHourlyForecastDataUpdateCoordinator, AccuWeatherObservationDataUpdateCoordinator as AccuWeatherObservationDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AccuWeatherConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AccuWeatherConfigEntry) -> bool: ...
