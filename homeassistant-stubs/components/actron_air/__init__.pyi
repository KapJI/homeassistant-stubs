from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .coordinator import ActronAirConfigEntry as ActronAirConfigEntry, ActronAirRuntimeData as ActronAirRuntimeData, ActronAirSystemCoordinator as ActronAirSystemCoordinator
from _typeshed import Incomplete
from actron_neo_api.models.system import ActronAirSystemInfo as ActronAirSystemInfo
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ActronAirConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ActronAirConfigEntry) -> bool: ...
