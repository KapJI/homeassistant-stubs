from .const import PLATFORMS as PLATFORMS
from .coordinator import UptimeRobotConfigEntry as UptimeRobotConfigEntry, UptimeRobotDataUpdateCoordinator as UptimeRobotDataUpdateCoordinator
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

async def async_setup_entry(hass: HomeAssistant, entry: UptimeRobotConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: UptimeRobotConfigEntry) -> bool: ...
