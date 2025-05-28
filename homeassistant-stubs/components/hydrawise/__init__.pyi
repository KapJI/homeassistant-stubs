from .const import APP_ID as APP_ID
from .coordinator import HydrawiseConfigEntry as HydrawiseConfigEntry, HydrawiseMainDataUpdateCoordinator as HydrawiseMainDataUpdateCoordinator, HydrawiseUpdateCoordinators as HydrawiseUpdateCoordinators, HydrawiseWaterUseDataUpdateCoordinator as HydrawiseWaterUseDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed

PLATFORMS: list[Platform]
_REQUIRED_AUTH_KEYS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: HydrawiseConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HydrawiseConfigEntry) -> bool: ...
