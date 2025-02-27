from .coordinator import FAAConfigEntry as FAAConfigEntry, FAADataUpdateCoordinator as FAADataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_ID as CONF_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: FAAConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FAAConfigEntry) -> bool: ...
