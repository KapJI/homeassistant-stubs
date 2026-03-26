from .api import AuthenticatedMonzoAPI as AuthenticatedMonzoAPI
from .coordinator import MonzoConfigEntry as MonzoConfigEntry, MonzoCoordinator as MonzoCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_migrate_entry(hass: HomeAssistant, entry: MonzoConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: MonzoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MonzoConfigEntry) -> bool: ...
