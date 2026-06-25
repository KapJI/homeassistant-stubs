from .coordinator import AqvifyAggrDataCoordinator as AqvifyAggrDataCoordinator, AqvifyConfigEntry as AqvifyConfigEntry, AqvifyCoordinator as AqvifyCoordinator, AqvifyRuntimeData as AqvifyRuntimeData
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: AqvifyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AqvifyConfigEntry) -> bool: ...
