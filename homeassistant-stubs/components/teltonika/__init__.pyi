from .coordinator import TeltonikaDataUpdateCoordinator as TeltonikaDataUpdateCoordinator
from .util import normalize_url as normalize_url
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: Incomplete
type TeltonikaConfigEntry = ConfigEntry[TeltonikaDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: TeltonikaConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TeltonikaConfigEntry) -> bool: ...
