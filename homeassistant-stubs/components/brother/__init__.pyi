from .const import DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, SNMP as SNMP
from .utils import get_snmp_engine as get_snmp_engine
from _typeshed import Incomplete
from brother import Brother, BrotherSensors
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

PLATFORMS: Incomplete
SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class BrotherDataUpdateCoordinator(DataUpdateCoordinator[BrotherSensors]):
    brother: Incomplete
    def __init__(self, hass: HomeAssistant, brother: Brother) -> None: ...
    async def _async_update_data(self) -> BrotherSensors: ...
