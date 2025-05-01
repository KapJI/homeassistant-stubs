from .const import CONNECTION_TYPE as CONNECTION_TYPE, LOCAL as LOCAL
from .coordinator import AdaxCloudCoordinator as AdaxCloudCoordinator, AdaxConfigEntry as AdaxConfigEntry, AdaxLocalCoordinator as AdaxLocalCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AdaxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AdaxConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: AdaxConfigEntry) -> bool: ...
