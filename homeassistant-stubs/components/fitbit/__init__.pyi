from . import api as api
from .const import FitbitScope as FitbitScope
from .coordinator import FitbitConfigEntry as FitbitConfigEntry, FitbitData as FitbitData, FitbitDeviceCoordinator as FitbitDeviceCoordinator
from .exceptions import FitbitApiException as FitbitApiException, FitbitAuthException as FitbitAuthException
from .model import config_from_entry_data as config_from_entry_data
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: FitbitConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FitbitConfigEntry) -> bool: ...
