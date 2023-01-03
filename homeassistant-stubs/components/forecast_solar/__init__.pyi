from .const import CONF_AZIMUTH as CONF_AZIMUTH, CONF_DAMPING as CONF_DAMPING, CONF_DECLINATION as CONF_DECLINATION, CONF_INVERTER_SIZE as CONF_INVERTER_SIZE, CONF_MODULES_POWER as CONF_MODULES_POWER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from forecast_solar import Estimate as Estimate
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
