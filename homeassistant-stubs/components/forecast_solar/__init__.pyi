from .const import CONF_AZIMUTH as CONF_AZIMUTH, CONF_DAMPING as CONF_DAMPING, CONF_DAMPING_EVENING as CONF_DAMPING_EVENING, CONF_DAMPING_MORNING as CONF_DAMPING_MORNING, CONF_DECLINATION as CONF_DECLINATION, CONF_MODULES_POWER as CONF_MODULES_POWER, DEFAULT_AZIMUTH as DEFAULT_AZIMUTH, DEFAULT_DAMPING as DEFAULT_DAMPING, DEFAULT_DECLINATION as DEFAULT_DECLINATION, DEFAULT_MODULES_POWER as DEFAULT_MODULES_POWER, DOMAIN as DOMAIN, SUBENTRY_TYPE_PLANE as SUBENTRY_TYPE_PLANE
from .coordinator import ForecastSolarConfigEntry as ForecastSolarConfigEntry, ForecastSolarDataUpdateCoordinator as ForecastSolarDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError

PLATFORMS: Incomplete

async def async_migrate_entry(hass: HomeAssistant, entry: ForecastSolarConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ForecastSolarConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ForecastSolarConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ForecastSolarConfigEntry) -> bool: ...
