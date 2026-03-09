from .const import LOGGER as LOGGER
from .coordinator import IntelliClimaConfigEntry as IntelliClimaConfigEntry, IntelliClimaCoordinator as IntelliClimaCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IntelliClimaConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: IntelliClimaConfigEntry) -> bool: ...
