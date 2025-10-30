from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, PLATFORMS_WITH_AUTH as PLATFORMS_WITH_AUTH
from .coordinator import SFRConfigEntry as SFRConfigEntry, SFRDataUpdateCoordinator as SFRDataUpdateCoordinator, SFRRuntimeData as SFRRuntimeData
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

async def async_setup_entry(hass: HomeAssistant, entry: SFRConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SFRConfigEntry) -> bool: ...
