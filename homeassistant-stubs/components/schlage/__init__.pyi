from .const import DOMAIN as DOMAIN, SERVICE_ADD_CODE as SERVICE_ADD_CODE, SERVICE_DELETE_CODE as SERVICE_DELETE_CODE, SERVICE_GET_CODES as SERVICE_GET_CODES
from .coordinator import SchlageConfigEntry as SchlageConfigEntry, SchlageDataUpdateCoordinator as SchlageDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, SupportsResponse as SupportsResponse
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import service as service
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: SchlageConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SchlageConfigEntry) -> bool: ...
