from .const import API_TIMEOUT as API_TIMEOUT, CONF_EUROPE as CONF_EUROPE, REGION_DEFAULT as REGION_DEFAULT, REGION_EU as REGION_EU
from .coordinator import FGLairConfigEntry as FGLairConfigEntry, FGLairCoordinator as FGLairCoordinator
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_REGION as CONF_REGION, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: FGLairConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FGLairConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: FGLairConfigEntry) -> bool: ...
