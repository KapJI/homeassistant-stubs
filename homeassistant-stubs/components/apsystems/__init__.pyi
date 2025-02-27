from .const import DEFAULT_PORT as DEFAULT_PORT
from .coordinator import ApSystemsConfigEntry as ApSystemsConfigEntry, ApSystemsData as ApSystemsData, ApSystemsDataCoordinator as ApSystemsDataCoordinator
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ApSystemsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ApSystemsConfigEntry) -> bool: ...
