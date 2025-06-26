from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import PaperlessConfigEntry as PaperlessConfigEntry, PaperlessData as PaperlessData, PaperlessStatisticCoordinator as PaperlessStatisticCoordinator, PaperlessStatusCoordinator as PaperlessStatusCoordinator
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from pypaperless import Paperless

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: PaperlessConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PaperlessConfigEntry) -> bool: ...
async def _get_paperless_api(hass: HomeAssistant, entry: PaperlessConfigEntry) -> Paperless: ...
