from .const import CONF_UNIT_ID as CONF_UNIT_ID
from .coordinator import KacoConfigEntry as KacoConfigEntry, KacoDataUpdateCoordinator as KacoDataUpdateCoordinator
from homeassistant.components.modbus import async_get_unit as async_get_unit
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: KacoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: KacoConfigEntry) -> bool: ...
