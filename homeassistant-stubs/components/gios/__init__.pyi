from .const import CONF_STATION_ID as CONF_STATION_ID, DOMAIN as DOMAIN
from .coordinator import GiosConfigEntry as GiosConfigEntry, GiosData as GiosData, GiosDataUpdateCoordinator as GiosDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: GiosConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GiosConfigEntry) -> bool: ...
