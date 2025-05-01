from .const import CONF_STATION as CONF_STATION
from .coordinator import PegelOnlineConfigEntry as PegelOnlineConfigEntry, PegelOnlineDataUpdateCoordinator as PegelOnlineDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PegelOnlineConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PegelOnlineConfigEntry) -> bool: ...
