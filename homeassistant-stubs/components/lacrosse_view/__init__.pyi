from .coordinator import LaCrosseConfigEntry as LaCrosseConfigEntry, LaCrosseUpdateCoordinator as LaCrosseUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LaCrosseConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LaCrosseConfigEntry) -> bool: ...
