from .const import LOGGER as LOGGER
from .coordinator import WattTimeConfigEntry as WattTimeConfigEntry, WattTimeCoordinator as WattTimeCoordinator
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import aiohttp_client as aiohttp_client

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: WattTimeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WattTimeConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, config_entry: WattTimeConfigEntry) -> None: ...
