from .const import PLATFORMS as PLATFORMS
from .coordinator import AxleConfigEntry as AxleConfigEntry, AxleCoordinator as AxleCoordinator
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

async def async_setup_entry(hass: HomeAssistant, entry: AxleConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AxleConfigEntry) -> bool: ...
