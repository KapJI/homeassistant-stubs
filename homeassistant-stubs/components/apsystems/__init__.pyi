from .coordinator import ApSystemsDataCoordinator as ApSystemsDataCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
ApsystemsConfigEntry = ConfigEntry[ApSystemsDataCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: ApsystemsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
