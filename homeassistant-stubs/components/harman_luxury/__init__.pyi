from .coordinator import HarmanLuxuryConfigEntry as HarmanLuxuryConfigEntry, HarmanLuxuryCoordinator as HarmanLuxuryCoordinator
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: HarmanLuxuryConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HarmanLuxuryConfigEntry) -> bool: ...
