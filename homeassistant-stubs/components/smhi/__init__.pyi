from .coordinator import SMHIConfigEntry as SMHIConfigEntry, SMHIDataUpdateCoordinator as SMHIDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SMHIConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SMHIConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: SMHIConfigEntry) -> bool: ...
