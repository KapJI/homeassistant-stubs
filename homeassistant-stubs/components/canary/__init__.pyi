from .const import CONF_FFMPEG_ARGUMENTS as CONF_FFMPEG_ARGUMENTS, DEFAULT_FFMPEG_ARGUMENTS as DEFAULT_FFMPEG_ARGUMENTS, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN
from .coordinator import CanaryConfigEntry as CanaryConfigEntry, CanaryDataUpdateCoordinator as CanaryDataUpdateCoordinator
from _typeshed import Incomplete
from canary.api import Api
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

_LOGGER: Final[Incomplete]
MIN_TIME_BETWEEN_UPDATES: Final[Incomplete]
CONFIG_SCHEMA: Final[Incomplete]
PLATFORMS: Final[list[Platform]]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: CanaryConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: CanaryConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: CanaryConfigEntry) -> None: ...
def _get_canary_api_instance(entry: CanaryConfigEntry) -> Api: ...
