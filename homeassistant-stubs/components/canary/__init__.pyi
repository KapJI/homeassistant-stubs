from .const import CONF_FFMPEG_ARGUMENTS as CONF_FFMPEG_ARGUMENTS, DATA_COORDINATOR as DATA_COORDINATOR, DATA_UNDO_UPDATE_LISTENER as DATA_UNDO_UPDATE_LISTENER, DEFAULT_FFMPEG_ARGUMENTS as DEFAULT_FFMPEG_ARGUMENTS, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN
from .coordinator import CanaryDataUpdateCoordinator as CanaryDataUpdateCoordinator
from canary.api import Api
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final

_LOGGER: Final[Any]
MIN_TIME_BETWEEN_UPDATES: Final[Any]
CONFIG_SCHEMA: Final[Any]
PLATFORMS: Final[list[str]]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
def _get_canary_api_instance(entry: ConfigEntry) -> Api: ...
