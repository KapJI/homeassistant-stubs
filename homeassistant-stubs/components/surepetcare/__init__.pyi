from .const import DOMAIN as DOMAIN
from .coordinator import SurePetcareConfigEntry as SurePetcareConfigEntry, SurePetcareDataCoordinator as SurePetcareDataCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
PLATFORMS: Incomplete
SCAN_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: SurePetcareConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SurePetcareConfigEntry) -> bool: ...
