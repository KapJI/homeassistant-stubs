from .const import CONF_UTILITY as CONF_UTILITY, DOMAIN as DOMAIN
from .coordinator import OpowerConfigEntry as OpowerConfigEntry, OpowerCoordinator as OpowerCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: OpowerConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OpowerConfigEntry) -> bool: ...
