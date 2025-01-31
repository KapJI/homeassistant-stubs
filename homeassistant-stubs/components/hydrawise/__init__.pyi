from .const import APP_ID as APP_ID, DOMAIN as DOMAIN
from .coordinator import HydrawiseMainDataUpdateCoordinator as HydrawiseMainDataUpdateCoordinator, HydrawiseUpdateCoordinators as HydrawiseUpdateCoordinators, HydrawiseWaterUseDataUpdateCoordinator as HydrawiseWaterUseDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed

PLATFORMS: list[Platform]
_REQUIRED_AUTH_KEYS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
