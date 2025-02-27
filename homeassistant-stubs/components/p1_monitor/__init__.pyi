from .const import LOGGER as LOGGER
from .coordinator import P1MonitorConfigEntry as P1MonitorConfigEntry, P1MonitorDataUpdateCoordinator as P1MonitorDataUpdateCoordinator
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: P1MonitorConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: P1MonitorConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: P1MonitorConfigEntry) -> bool: ...
