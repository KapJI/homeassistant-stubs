from .const import CONF_FROM as CONF_FROM, CONF_TO as CONF_TO, PLATFORMS as PLATFORMS
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

TVTrainConfigEntry = ConfigEntry[TVDataUpdateCoordinator]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TVTrainConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TVTrainConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: TVTrainConfigEntry) -> bool: ...
