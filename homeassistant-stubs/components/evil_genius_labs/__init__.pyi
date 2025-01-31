from .coordinator import EvilGeniusConfigEntry as EvilGeniusConfigEntry, EvilGeniusUpdateCoordinator as EvilGeniusUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client

PLATFORMS: Incomplete
UPDATE_INTERVAL: int

async def async_setup_entry(hass: HomeAssistant, entry: EvilGeniusConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EvilGeniusConfigEntry) -> bool: ...
