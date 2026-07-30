from . import api as api
from .const import DOMAIN as DOMAIN
from .coordinator import GoogleHealthActivityCoordinator as GoogleHealthActivityCoordinator, GoogleHealthBodyCoordinator as GoogleHealthBodyCoordinator, GoogleHealthDataUpdateCoordinator as GoogleHealthDataUpdateCoordinator, GoogleHealthDeviceCoordinator as GoogleHealthDeviceCoordinator, GoogleHealthNutritionCoordinator as GoogleHealthNutritionCoordinator, GoogleHealthSleepCoordinator as GoogleHealthSleepCoordinator
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation

_PLATFORMS: list[Platform]

@dataclass
class GoogleHealthData:
    activity_coordinator: GoogleHealthActivityCoordinator | None = ...
    body_coordinator: GoogleHealthBodyCoordinator | None = ...
    device_coordinator: GoogleHealthDeviceCoordinator | None = ...
    nutrition_coordinator: GoogleHealthNutritionCoordinator | None = ...
    sleep_coordinator: GoogleHealthSleepCoordinator | None = ...
type GoogleHealthConfigEntry = ConfigEntry[GoogleHealthData]

async def async_setup_entry(hass: HomeAssistant, entry: GoogleHealthConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GoogleHealthConfigEntry) -> bool: ...
