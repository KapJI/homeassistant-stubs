from .client import ThreemaAPIClient as ThreemaAPIClient, ThreemaAuthError as ThreemaAuthError, ThreemaConnectionError as ThreemaConnectionError
from .const import CONF_API_SECRET as CONF_API_SECRET, CONF_GATEWAY_ID as CONF_GATEWAY_ID, CONF_PRIVATE_KEY as CONF_PRIVATE_KEY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete
PLATFORMS: list[Platform]
type ThreemaConfigEntry = ConfigEntry[ThreemaAPIClient]

async def async_setup_entry(hass: HomeAssistant, entry: ThreemaConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ThreemaConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ThreemaConfigEntry) -> bool: ...
