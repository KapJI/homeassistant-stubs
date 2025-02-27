from .coordinator import CO2SignalConfigEntry as CO2SignalConfigEntry, CO2SignalCoordinator as CO2SignalCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: CO2SignalConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: CO2SignalConfigEntry) -> bool: ...
