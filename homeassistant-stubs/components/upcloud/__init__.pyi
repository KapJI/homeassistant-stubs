from .coordinator import UpCloudConfigEntry as UpCloudConfigEntry, UpCloudDataUpdateCoordinator as UpCloudDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: UpCloudConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: UpCloudConfigEntry) -> bool: ...
