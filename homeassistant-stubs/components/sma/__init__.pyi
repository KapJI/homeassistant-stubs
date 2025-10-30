from .const import CONF_GROUP as CONF_GROUP
from .coordinator import SMADataUpdateCoordinator as SMADataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete
_LOGGER: Incomplete
type SMAConfigEntry = ConfigEntry[SMADataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: SMAConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SMAConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
