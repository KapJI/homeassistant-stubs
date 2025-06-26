from .const import CONF_SENSOR_ID as CONF_SENSOR_ID
from .coordinator import LuftdatenConfigEntry as LuftdatenConfigEntry, LuftdatenDataUpdateCoordinator as LuftdatenDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LuftdatenConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LuftdatenConfigEntry) -> bool: ...
