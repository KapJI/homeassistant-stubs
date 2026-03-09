from .const import DOMAIN as DOMAIN
from .coordinator import NtfyConfigEntry as NtfyConfigEntry, NtfyDataUpdateCoordinator as NtfyDataUpdateCoordinator, NtfyLatestReleaseUpdateCoordinator as NtfyLatestReleaseUpdateCoordinator, NtfyRuntimeData as NtfyRuntimeData, NtfyVersionDataUpdateCoordinator as NtfyVersionDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey

_LOGGER: Incomplete
PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete
NTFY_KEY: HassKey[NtfyLatestReleaseUpdateCoordinator]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: NtfyConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: NtfyConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: NtfyConfigEntry) -> bool: ...
