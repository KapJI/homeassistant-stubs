from .api import AsyncConfigEntryAuth as AsyncConfigEntryAuth
from .const import DOMAIN as DOMAIN, OLD_NEW_UNIQUE_ID_SUFFIX_MAP as OLD_NEW_UNIQUE_ID_SUFFIX_MAP
from .coordinator import HomeConnectConfigEntry as HomeConnectConfigEntry, HomeConnectCoordinator as HomeConnectCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_migrate_entries as async_migrate_entries
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry) -> bool: ...
