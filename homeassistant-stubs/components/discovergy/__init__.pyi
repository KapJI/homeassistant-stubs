from .coordinator import DiscovergyConfigEntry as DiscovergyConfigEntry, DiscovergyUpdateCoordinator as DiscovergyUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.httpx_client import create_async_httpx_client as create_async_httpx_client

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: DiscovergyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DiscovergyConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: DiscovergyConfigEntry) -> None: ...
