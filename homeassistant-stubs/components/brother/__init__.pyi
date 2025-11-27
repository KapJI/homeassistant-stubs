from .const import CONF_COMMUNITY as CONF_COMMUNITY, DEFAULT_COMMUNITY as DEFAULT_COMMUNITY, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, SECTION_ADVANCED_SETTINGS as SECTION_ADVANCED_SETTINGS
from .coordinator import BrotherConfigEntry as BrotherConfigEntry, BrotherDataUpdateCoordinator as BrotherDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.snmp import async_get_snmp_engine as async_get_snmp_engine
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BrotherConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BrotherConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: BrotherConfigEntry) -> bool: ...
