from .const import CONF_SECRET as CONF_SECRET
from .coordinator import AirthingsConfigEntry as AirthingsConfigEntry, AirthingsDataUpdateCoordinator as AirthingsDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_ID as CONF_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: list[Platform]
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AirthingsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirthingsConfigEntry) -> bool: ...
