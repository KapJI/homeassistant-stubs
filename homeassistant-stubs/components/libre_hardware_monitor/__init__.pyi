from .const import DOMAIN as DOMAIN
from .coordinator import LibreHardwareMonitorConfigEntry as LibreHardwareMonitorConfigEntry, LibreHardwareMonitorCoordinator as LibreHardwareMonitorCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_migrate_entry(hass: HomeAssistant, config_entry: LibreHardwareMonitorConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: LibreHardwareMonitorConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: LibreHardwareMonitorConfigEntry) -> bool: ...
