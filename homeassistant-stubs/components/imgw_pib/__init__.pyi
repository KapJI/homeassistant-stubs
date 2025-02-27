from .const import CONF_STATION_ID as CONF_STATION_ID, DOMAIN as DOMAIN
from .coordinator import ImgwPibConfigEntry as ImgwPibConfigEntry, ImgwPibData as ImgwPibData, ImgwPibDataUpdateCoordinator as ImgwPibDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ImgwPibConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ImgwPibConfigEntry) -> bool: ...
