from .const import DOMAIN as DOMAIN, SNMP_ENGINE as SNMP_ENGINE
from .coordinator import BrotherDataUpdateCoordinator as BrotherDataUpdateCoordinator
from .utils import get_snmp_engine as get_snmp_engine
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: Incomplete
BrotherConfigEntry = ConfigEntry[BrotherDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: BrotherConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BrotherConfigEntry) -> bool: ...
