from .const import DOMAIN as DOMAIN
from .coordinator import CalendarUpdateCoordinator as CalendarUpdateCoordinator, DiskSpaceDataUpdateCoordinator as DiskSpaceDataUpdateCoordinator, HealthDataUpdateCoordinator as HealthDataUpdateCoordinator, MoviesDataUpdateCoordinator as MoviesDataUpdateCoordinator, QueueDataUpdateCoordinator as QueueDataUpdateCoordinator, RadarrConfigEntry as RadarrConfigEntry, RadarrData as RadarrData, RadarrDataUpdateCoordinator as RadarrDataUpdateCoordinator, StatusDataUpdateCoordinator as StatusDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: RadarrConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RadarrConfigEntry) -> bool: ...
