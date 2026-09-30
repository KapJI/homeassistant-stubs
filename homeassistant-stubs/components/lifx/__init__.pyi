from .const import CONF_SERIAL as CONF_SERIAL, DATA_LIFX_MANAGER as DATA_LIFX_MANAGER, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import LIFXConfigEntry as LIFXConfigEntry, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .discovery import async_setup_discovery as async_setup_discovery
from .entity import async_repair_device_registry as async_repair_device_registry
from .manager import LIFXManager as LIFXManager
from .migration import async_migrate_serials as async_migrate_serials
from .services import async_setup_services as async_setup_services
from .util import async_resolve_host as async_resolve_host, normalize_serial as normalize_serial
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType

CONF_SERVER: str
CONF_BROADCAST: str
INTERFACE_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: LIFXConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: LIFXConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LIFXConfigEntry) -> bool: ...
