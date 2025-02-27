from .coordinator import SensoterraConfigEntry as SensoterraConfigEntry, SensoterraCoordinator as SensoterraCoordinator
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: SensoterraConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SensoterraConfigEntry) -> bool: ...
