from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, DOMAIN as DOMAIN
from .errors import CannotConnect as CannotConnect, LoginError as LoginError
from .hub import MikrotikDataUpdateCoordinator as MikrotikDataUpdateCoordinator, get_api as get_api
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
