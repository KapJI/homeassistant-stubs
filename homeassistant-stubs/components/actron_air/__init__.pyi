from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import ActronAirConfigEntry as ActronAirConfigEntry, ActronAirRuntimeData as ActronAirRuntimeData, ActronAirSystemCoordinator as ActronAirSystemCoordinator
from _typeshed import Incomplete
from actron_neo_api.models.system import ActronAirSystemInfo as ActronAirSystemInfo
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ActronAirConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ActronAirConfigEntry) -> bool: ...
