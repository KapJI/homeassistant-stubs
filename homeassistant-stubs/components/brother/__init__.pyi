from .const import DOMAIN as DOMAIN
from .coordinator import BrotherConfigEntry as BrotherConfigEntry, BrotherDataUpdateCoordinator as BrotherDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.snmp import async_get_snmp_engine as async_get_snmp_engine
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BrotherConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BrotherConfigEntry) -> bool: ...
