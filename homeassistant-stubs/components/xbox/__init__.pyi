from .api import AsyncConfigEntryAuth as AsyncConfigEntryAuth
from .const import DOMAIN as DOMAIN
from .coordinator import XboxConfigEntry as XboxConfigEntry, XboxConsolesCoordinator as XboxConsolesCoordinator, XboxCoordinators as XboxCoordinators, XboxUpdateCoordinator as XboxUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: XboxConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: XboxConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: XboxConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: XboxConfigEntry) -> bool: ...
