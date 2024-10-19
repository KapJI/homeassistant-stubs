from .const import DOMAIN as DOMAIN, UPDATE_INTERVAL_DAILY_FORECAST as UPDATE_INTERVAL_DAILY_FORECAST, UPDATE_INTERVAL_OBSERVATION as UPDATE_INTERVAL_OBSERVATION
from .coordinator import AccuWeatherDailyForecastDataUpdateCoordinator as AccuWeatherDailyForecastDataUpdateCoordinator, AccuWeatherObservationDataUpdateCoordinator as AccuWeatherObservationDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: Incomplete

@dataclass
class AccuWeatherData:
    coordinator_observation: AccuWeatherObservationDataUpdateCoordinator
    coordinator_daily_forecast: AccuWeatherDailyForecastDataUpdateCoordinator
    def __init__(self, coordinator_observation, coordinator_daily_forecast) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: AccuWeatherConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AccuWeatherConfigEntry) -> bool: ...
