from .coordinator import SensorPushCloudConfigEntry as SensorPushCloudConfigEntry, SensorPushCloudCoordinator as SensorPushCloudCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: SensorPushCloudConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SensorPushCloudConfigEntry) -> bool: ...
