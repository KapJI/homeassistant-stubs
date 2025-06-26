from .const import DOMAIN as DOMAIN
from .coordinator import NtfyConfigEntry as NtfyConfigEntry, NtfyDataUpdateCoordinator as NtfyDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: NtfyConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: NtfyConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: NtfyConfigEntry) -> bool: ...
