from .coordinator import SunsynkConfigEntry as SunsynkConfigEntry, SunsynkDataUpdateCoordinator as SunsynkDataUpdateCoordinator
from .entity import inverter_device_info as inverter_device_info
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: SunsynkConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SunsynkConfigEntry) -> bool: ...
