from .const import CONF_SECRET as CONF_SECRET
from .coordinator import AirthingsDataUpdateCoordinator as AirthingsDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: list[Platform]
SCAN_INTERVAL: Incomplete
type AirthingsConfigEntry = ConfigEntry[AirthingsDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: AirthingsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirthingsConfigEntry) -> bool: ...
