from .const import CONF_REFERRER as CONF_REFERRER
from .coordinator import GoogleWeatherConfigEntry as GoogleWeatherConfigEntry, GoogleWeatherCurrentConditionsCoordinator as GoogleWeatherCurrentConditionsCoordinator, GoogleWeatherDailyForecastCoordinator as GoogleWeatherDailyForecastCoordinator, GoogleWeatherHourlyForecastCoordinator as GoogleWeatherHourlyForecastCoordinator, GoogleWeatherRuntimeData as GoogleWeatherRuntimeData, GoogleWeatherSubEntryRuntimeData as GoogleWeatherSubEntryRuntimeData
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: GoogleWeatherConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GoogleWeatherConfigEntry) -> bool: ...
async def async_update_options(hass: HomeAssistant, entry: GoogleWeatherConfigEntry) -> None: ...
