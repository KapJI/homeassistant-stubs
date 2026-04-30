from .const import PLATFORMS as PLATFORMS
from .coordinator import DucoConfigEntry as DucoConfigEntry, DucoCoordinator as DucoCoordinator
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

async def async_setup_entry(hass: HomeAssistant, entry: DucoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DucoConfigEntry) -> bool: ...
