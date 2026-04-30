from .const import DOMAIN as DOMAIN, SENSOR_UNIQUE_ID_MIGRATION as SENSOR_UNIQUE_ID_MIGRATION
from .coordinator import TwenteMilieuConfigEntry as TwenteMilieuConfigEntry, TwenteMilieuDataUpdateCoordinator as TwenteMilieuDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TwenteMilieuConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TwenteMilieuConfigEntry) -> bool: ...
