from .coordinator import BringConfigEntry as BringConfigEntry, BringDataUpdateCoordinator as BringDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BringConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BringConfigEntry) -> bool: ...
